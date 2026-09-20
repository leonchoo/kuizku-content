/**
 * KuizKu Question Report Backend — Apps Script Web App
 * Phase 10.5R-C — Part C
 *
 * Receives question reports from the KuizKu Android app via HTTPS POST,
 * validates the payload, writes a row to the bound Google Sheet, and returns
 * a JSON response indicating success or error.
 *
 * Per Phase 10.5R-B spec:
 *  - 10 required fields
 *  - reason enum validation (4 values)
 *  - field length / regex validation
 *  - timestamp ±7 days validation
 *  - IP-based rate limit (100 reports / IP / hour)
 *  - No PII collected (no name, email, phone, account ID, advertising ID, device ID)
 *  - No Google Login required
 *  - No shared secret (intentional per 638 §四)
 *
 * Sheet columns (Row 1 = header, Row 2+ = data):
 *   timestamp | questionId | reason | bankId | bankVersion |
 *   schoolTrack | gradeLevel | subjectCode | language | appVersion
 */

const SHEET_ID = '17KXHOUebjla4E1nyyBfjMNpcsHrKAVigASmG259tNZY';

const HEADER_ROW = [
  'timestamp', 'questionId', 'reason', 'bankId', 'bankVersion',
  'schoolTrack', 'gradeLevel', 'subjectCode', 'language', 'appVersion'
];

const VALID_REASONS = ['WRONG_ANSWER', 'UNCLEAR_QUESTION', 'TYPO_SPELLING', 'OTHER'];
const VALID_TRACKS = ['SK', 'SJKC', 'INTERNATIONAL'];
const VALID_LANGS = ['ms', 'zh', 'en'];
const VALID_CODES = ['bm', 'bc', 'en', 'math', 'science', 'moral', 'islam', 'art', 'music'];
const VALID_GRADE_REGEX = /^Tahun[1-6]$|^Tingkatan[1-5]$/;
const RATE_LIMIT_PER_HOUR = 100;
const RATE_LIMIT_TTL_SEC = 3600;
const TIMESTAMP_WINDOW_MS = 7 * 24 * 60 * 60 * 1000; // ±7 days

/**
 * doPost: Receives a JSON payload via HTTPS POST.
 *
 * Apps Script Web Apps ALWAYS return HTTP 200 — the success/failure
 * distinction is encoded in the JSON body's `status` field.
 * Per Phase 10.5R-C Part A fix: Android must check body.status === 'ok'.
 */
function doPost(e) {
  // 1. Parse JSON
  let payload;
  try {
    if (!e || !e.postData || !e.postData.contents) {
      return jsonResponse({ status: 'error', message: 'Empty request body' });
    }
    payload = JSON.parse(e.postData.contents);
  } catch (err) {
    return jsonResponse({ status: 'error', message: 'Invalid JSON' });
  }
  if (!payload || typeof payload !== 'object' || Array.isArray(payload)) {
    return jsonResponse({ status: 'error', message: 'Body must be a JSON object' });
  }

  // 2. Validate 10 required fields
  for (const field of HEADER_ROW) {
    if (!(field in payload)) {
      return jsonResponse({ status: 'error', message: 'Missing field: ' + field });
    }
  }

  // 3. Type + enum validation
  if (typeof payload.bankVersion !== 'number' || payload.bankVersion < 0 || payload.bankVersion > 10000) {
    return jsonResponse({ status: 'error', message: 'Invalid bankVersion' });
  }
  if (typeof payload.timestamp !== 'number' || payload.timestamp <= 0) {
    return jsonResponse({ status: 'error', message: 'Invalid timestamp (must be positive number)' });
  }
  if (VALID_REASONS.indexOf(payload.reason) === -1) {
    return jsonResponse({ status: 'error', message: 'Invalid reason' });
  }
  if (VALID_TRACKS.indexOf(payload.schoolTrack) === -1) {
    return jsonResponse({ status: 'error', message: 'Invalid schoolTrack' });
  }
  if (VALID_LANGS.indexOf(payload.language) === -1) {
    return jsonResponse({ status: 'error', message: 'Invalid language' });
  }
  if (VALID_CODES.indexOf(payload.subjectCode) === -1) {
    return jsonResponse({ status: 'error', message: 'Invalid subjectCode' });
  }
  if (!VALID_GRADE_REGEX.test(payload.gradeLevel)) {
    return jsonResponse({ status: 'error', message: 'Invalid gradeLevel (must be Tahun<n> or Tingkatan<n>)' });
  }

  // 4. Length / regex checks
  if (typeof payload.questionId !== 'string' || payload.questionId.length === 0 || payload.questionId.length > 128 ||
      !/^[A-Za-z0-9_-]+$/.test(payload.questionId)) {
    return jsonResponse({ status: 'error', message: 'Invalid questionId (max 128, regex [A-Za-z0-9_-]+)' });
  }
  if (typeof payload.bankId !== 'string' || payload.bankId.length === 0 || payload.bankId.length > 128 ||
      !/^[a-z][a-z0-9_]+$/.test(payload.bankId)) {
    return jsonResponse({ status: 'error', message: 'Invalid bankId (max 128, regex [a-z][a-z0-9_]+)' });
  }
  if (typeof payload.appVersion !== 'string' || payload.appVersion.length === 0 || payload.appVersion.length > 32 ||
      !/^\d+\.\d+\.\d+$/.test(payload.appVersion)) {
    return jsonResponse({ status: 'error', message: 'Invalid appVersion (max 32, regex N+.N+.N+)' });
  }

  // 5. Timestamp range: reject ancient / future (>7 days off)
  const now = Date.now();
  if (Math.abs(now - payload.timestamp) > TIMESTAMP_WINDOW_MS) {
    return jsonResponse({ status: 'error', message: 'Timestamp out of range (>7 days from now)' });
  }

  // 6. IP-based rate limit (CacheService, TTL 3600s)
  // Apps Script exposes the request IP via e.parameter['x-forwarded-for']
  // (when behind a load balancer) or e.parameter['userIp'] (legacy).
  // We use a stable key from whichever is available.
  const cache = CacheService.getScriptCache();
  const ip = (e && e.parameter && (e.parameter['x-forwarded-for'] || e.parameter['userIp'])) || 'unknown';
  const rateKey = 'rate:' + ip;
  const currentCount = Number(cache.get(rateKey) || '0');
  if (currentCount >= RATE_LIMIT_PER_HOUR) {
    return jsonResponse({ status: 'rate_limited', message: 'Too many reports from this source' });
  }
  cache.put(rateKey, String(currentCount + 1), RATE_LIMIT_TTL_SEC);

  // 7. Open the bound Google Sheet by ID directly
  //    No DriveApp, no Script Properties, no name-based fallback.
  //    Sheet ID is hardcoded per 638 instruction (Phase 10.5R-C Part C).
  let sheet;
  try {
    sheet = SpreadsheetApp.openById(SHEET_ID);
  } catch (err) {
    return jsonResponse({ status: 'error', message: 'Sheet not found: ' + SHEET_ID });
  }
  if (!sheet) {
    return jsonResponse({ status: 'error', message: 'Sheet is null after openById' });
  }

  // 8. Ensure header row exists (first sheet in the workbook)
  const logSheet = sheet.getSheets()[0];
  const headerRange = logSheet.getRange(1, 1, 1, HEADER_ROW.length);
  const header = headerRange.getValues()[0];
  let headerMatches = HEADER_ROW.length === header.length;
  if (headerMatches) {
    for (let i = 0; i < HEADER_ROW.length; i++) {
      if (header[i] !== HEADER_ROW[i]) {
        headerMatches = false;
        break;
      }
    }
  }
  if (!headerMatches) {
    headerRange.setValues([HEADER_ROW]);
  }

  // 9. Append the row
  const row = HEADER_ROW.map(field => payload[field]);
  logSheet.appendRow(row);

  // 10. Return success
  return jsonResponse({
    status: 'ok',
    rowIndex: logSheet.getLastRow(),
  });
}

/**
 * doGet: Health check endpoint (per Phase 10.5R-B §C).
 * Returns 200 with { status: 'ok', version: '1' }.
 */
function doGet() {
  return jsonResponse({ status: 'ok', version: '1' });
}

/**
 * Helper: produce a ContentService TextOutput with JSON content type.
 * Note: Apps Script always returns HTTP 200 — error/success distinction
 * is in the JSON body.
 */
function jsonResponse(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
