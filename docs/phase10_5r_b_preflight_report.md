# Phase 10.5R-B — Question Report Backend Preflight Report

> **READ-ONLY PREFLIGHT.** No Android source modified. No Google Apps Script deployed. No Google Sheet created. No code committed. No push.
>
> Built on Phase 10.5R commit `5de8a30` (verified locally). `ReportRemoteConfig.endpointUrl = null` (verified).

---

## A. Backend Architecture

```
[Android device]
     │
     │ HTTPS POST (application/json)
     │ Payload: { questionId, reason, bankId, bankVersion,
     │           schoolTrack, gradeLevel, subjectCode, language,
     │           appVersion, timestamp }
     │
     ▼
[Google Apps Script Web App]
   doPost(e) handler
     │
     ├─ Validate JSON structure
     ├─ Validate 10 required fields
     ├─ Validate `reason` enum
     ├─ Validate field lengths / regex
     ├─ Rate-limit check (per IP / per questionId window)
     ├─ Duplicate check (questionId + bankVersion + reason window)
     └─ appendRow → Google Sheet
     │
     ▼
[Google Sheet: kuizku-question-reports]

[Backend returns]
   HTTP 200 + { status: "ok", rowIndex: 42 }            — success
   HTTP 200 + { status: "duplicate", message: "..." }  — counted as success (Android already dedupes)
   HTTP 400 + { status: "error", message: "..." }      — invalid payload
   HTTP 429 + { status: "rate_limited", message: "..." } — too many requests
   HTTP 500 + { status: "error", message: "..." }      — backend failure
```

**Key design decisions**:
1. **Single endpoint**, single method (`doPost`). No REST conventions beyond the implicit POST.
2. **All 5xx are transient → Android shows "Couldn't send report"**. All 4xx are permanent (invalid payload) → Android still shows "Couldn't send report" (no UI differentiation in v1).
3. **No authentication / no Google login**. The endpoint is publicly POSTable; abuse protection is by rate limit + payload validation only (per 638 §3 "不依赖用户账号").
4. **Backend logs the same 10 fields Android sends**. No question text, no options, no correct answer, no PII.

---

## B. Google Sheet Schema

### Recommended Sheet name
`kuizku-question-reports` (one sheet per deployment). Row 1 is the header.

### Columns (left to right)

| # | Column | Type | Required | Source | Validation |
|---|---|---|:---:|---|---|
| A | `timestamp` | DateTime (ISO 8601 UTC, ms epoch) | ✅ | Android | Range: now ± 7 days (reject future / ancient) |
| B | `questionId` | String | ✅ | Android | Non-empty, ≤128 chars, regex: `^[A-Za-z0-9_\-]+$` |
| C | `reason` | String (enum) | ✅ | Android | One of: `WRONG_ANSWER`, `UNCLEAR_QUESTION`, `TYPO_SPELLING`, `OTHER` |
| D | `bankId` | String | ✅ | Android | Non-empty, ≤128 chars, regex: `^[a-z][a-z0-9_]+$` |
| E | `bankVersion` | Integer | ✅ | Android | Range: 0..10000 |
| F | `schoolTrack` | String (enum) | ✅ | Android | One of: `SK`, `SJKC`, `INTERNATIONAL` |
| G | `gradeLevel` | String | ✅ | Android | One of: `Tahun1`..`Tahun6` (Primary) or `Tingkatan1`..`Tingkatan5` (Secondary) — Apps Script checks first char matches stage |
| H | `subjectCode` | String | ✅ | Android | One of: `bm`, `bc`, `en`, `math`, `science`, `moral`, `islam`, `art`, `music` |
| I | `language` | String | ✅ | Android | One of: `ms`, `zh`, `en` |
| J | `appVersion` | String | ✅ | Android | Non-empty, ≤32 chars, regex: `^\d+\.\d+\.\d+$` |

### Header row (Row 1, frozen)

```
A1: timestamp
B1: questionId
C1: reason
D1: bankId
E1: bankVersion
F1: schoolTrack
G1: gradeLevel
H1: subjectCode
I1: language
J1: appVersion
```

### Data rows (Row 2+)

Each report = 1 row. Order: timestamp ascending (auto-sorted by Sheet).

### Sheet access
- **Editor**: Apps Script service account (or "user running the web app")
- **Viewer**: 638 + collaborators only
- **Public read**: NO
- **Sheet URL**: stored in 1Password / local config, NOT in Git, NOT in code

---

## C. Apps Script API Specification

### Endpoints

- **POST** `/` (the Web App's public URL) — receives reports.
- **GET** `/` — health check: returns 200 with `{ status: "ok", version: "1" }` (so 638 can verify deployment without sending real reports).

### `doPost(e)` pseudocode

```javascript
function doPost(e) {
  const logSheet = SpreadsheetApp.openById(SCRIPT_PROP.getProperty('SHEET_ID'))
                                .getSheetByName('kuizku-question-reports');

  // 1. Parse JSON
  let payload;
  try {
    payload = JSON.parse(e.postData.contents);
  } catch (err) {
    return jsonResponse(400, { status: 'error', message: 'Invalid JSON' });
  }
  if (!payload || typeof payload !== 'object') {
    return jsonResponse(400, { status: 'error', message: 'Body must be a JSON object' });
  }

  // 2. Validate 10 required fields
  const REQUIRED = ['timestamp','questionId','reason','bankId','bankVersion',
                    'schoolTrack','gradeLevel','subjectCode','language','appVersion'];
  for (const k of REQUIRED) {
    if (!(k in payload)) {
      return jsonResponse(400, { status: 'error', message: 'Missing field: ' + k });
    }
  }

  // 3. Type + enum validation
  const VALID_REASON = ['WRONG_ANSWER','UNCLEAR_QUESTION','TYPO_SPELLING','OTHER'];
  const VALID_TRACK  = ['SK','SJKC','INTERNATIONAL'];
  const VALID_LANG   = ['ms','zh','en'];
  const VALID_CODE   = ['bm','bc','en','math','science','moral','islam','art','music'];
  const VALID_GRADE  = /^Tahun[1-6]$|^Tingkatan[1-5]$/;

  if (!VALID_REASON.includes(payload.reason))
    return jsonResponse(400, { status:'error', message:'Invalid reason' });
  if (!VALID_TRACK.includes(payload.schoolTrack))
    return jsonResponse(400, { status:'error', message:'Invalid schoolTrack' });
  if (!VALID_LANG.includes(payload.language))
    return jsonResponse(400, { status:'error', message:'Invalid language' });
  if (!VALID_CODE.includes(payload.subjectCode))
    return jsonResponse(400, { status:'error', message:'Invalid subjectCode' });
  if (!VALID_GRADE.test(payload.gradeLevel))
    return jsonResponse(400, { status:'error', message:'Invalid gradeLevel' });
  if (typeof payload.bankVersion !== 'number' || payload.bankVersion < 0)
    return jsonResponse(400, { status:'error', message:'Invalid bankVersion' });

  // 4. Length / regex checks
  if (payload.questionId.length > 128 || !/^[A-Za-z0-9_-]+$/.test(payload.questionId))
    return jsonResponse(400, { status:'error', message:'Invalid questionId' });
  if (payload.bankId.length > 128 || !/^[a-z][a-z0-9_]+$/.test(payload.bankId))
    return jsonResponse(400, { status:'error', message:'Invalid bankId' });
  if (payload.appVersion.length > 32 || !/^\d+\.\d+\.\d+$/.test(payload.appVersion))
    return jsonResponse(400, { status:'error', message:'Invalid appVersion' });
  if (typeof payload.timestamp !== 'number' || payload.timestamp < Date.now() - 7*24*3600*1000)
    return jsonResponse(400, { status:'error', message:'Invalid timestamp' });

  // 5. Rate limit (per-IP)
  const cache = CacheService.getScriptCache();
  const ip = e.parameter ? (e.parameter['x-forwarded-for'] || 'unknown') : 'unknown';
  const rateKey = 'rate:' + ip;
  const current = Number(cache.get(rateKey) || '0');
  if (current > 100) {  // 100 reports / hour / IP
    return jsonResponse(429, { status:'rate_limited', message:'Too many reports' });
  }
  cache.put(rateKey, String(current + 1), 3600);  // 1-hour TTL

  // 6. Append row (Sheet row 2+)
  const row = [
    new Date(payload.timestamp),
    payload.questionId,
    payload.reason,
    payload.bankId,
    payload.bankVersion,
    payload.schoolTrack,
    payload.gradeLevel,
    payload.subjectCode,
    payload.language,
    payload.appVersion,
  ];
  const appended = logSheet.appendRow(row);
  const rowIndex = appended.getRange().getRow();

  return jsonResponse(200, { status:'ok', rowIndex: rowIndex });
}

function doGet() {
  return jsonResponse(200, { status: 'ok', version: '1' });
}

function jsonResponse(code, body) {
  return ContentService
    .createTextOutput(JSON.stringify(body))
    .setMimeType(ContentService.MimeType.JSON);
}
```

### Important Apps Script HTTP status code limitation (per 638 §2)

**Apps Script Web Apps return HTTP 200 for EVERY response** by default. The `ContentService` does NOT support setting arbitrary HTTP status codes (e.g., 400, 429, 500) — the underlying platform always returns 200 to the client.

**Workaround**: encode the HTTP status into the JSON body's `status` field. The JSON body becomes the source of truth.

### OkHttp compatibility check (per 638 §2)

The Android `OkHttpReportRemoteDataSource.postReport` returns `resp.isSuccessful` — **this is HTTP status code 200..299**.

For Apps Script, the HTTP status will ALWAYS be 200, so `resp.isSuccessful` will ALWAYS be true (even for "error" responses). This means:

**PROBLEM**: Android's current "success = HTTP 2xx" check is insufficient for Apps Script. Every Apps Script response will be considered "Success", even if the JSON body says `{"status":"error","message":"Invalid reason"}`.

**PROPOSED FIX (Android side, next implementation phase)**: Parse the JSON response body. If `body.status === "ok"` → success; otherwise → `FailedTransient`.

This is a **mandatory** change to `OkHttpReportRemoteDataSource` in the next phase. The current `postReport` returning `resp.isSuccessful` is INSUFFICIENT for Apps Script.

### Response examples

**Success**:
```json
HTTP 200
{ "status": "ok", "rowIndex": 42 }
```

**Duplicate (logged as success in v1 — Android already dedupes, so this is just for backend observability)**:
```json
HTTP 200
{ "status": "ok", "rowIndex": 42, "note": "duplicate" }
```

**Validation error**:
```json
HTTP 200
{ "status": "error", "message": "Invalid reason" }
```

**Rate limited**:
```json
HTTP 200
{ "status": "rate_limited", "message": "Too many reports" }
```

**Backend failure (Sheet unreachable)**:
```json
HTTP 200  (Apps Script returns 200 even on internal failure)
{ "status": "error", "message": "Sheet access denied" }
```

**IMPORTANT**: Apps Script catches all internal errors and returns 200 with an error body. The HTTP status is **never** 5xx from the client's perspective.

---

## D. Security / Abuse Protection

### Per 638 §4: no user login, no Google account, no PII

### Where protection lives

| Layer | Protects | Mechanism |
|---|---|---|
| **Android** | Dedupe within device | DataStore key `questionId|bankVersion|reason` (already implemented in 5de8a30) |
| **Apps Script** | Dedupe across devices + rate limiting + payload validation | (1) Append-only Sheet acts as cross-device dedupe (acceptable to have dupes in Sheet; Android's dedupe is per-device which is the primary defense). (2) CacheService IP-based rate limit: 100 reports/IP/hour. (3) Field validation per §C. |
| **Google Sheet** | Read access | Editor = service account; viewer = 638 only |
| **HTTP** | Transport encryption | HTTPS-only via Apps Script Web App default URL (`https://script.google.com/...`) |

### Web App URL secret status

Per 638 §4: "Web App URL 是否应该视为 secret".

**Answer**: **No, but with caveats**. The Apps Script Web App URL is:
- **Not a cryptographic secret** — anyone who knows it can POST garbage (rate-limited at 100/hour/IP).
- **Not trivially guessable** — the URL contains a long random `/exec` token specific to your deployment.
- **Should NOT be committed to public Git** — the URL identifies the deployment; if leaked, an attacker can spam your Sheet (until rate-limited).

**Decision**: Treat the Web App URL as a **deployment identifier, not a cryptographic secret**. Store in `local.properties` (gitignored) like `quiz_bank_base_url`. **Never** commit a real URL.

### Token / shared secret?

**Recommendation: NO shared secret in v1**.

**Reasoning**:
- Adding a shared secret means the secret must live in (a) Android client (extractable, can be leaked via APK decompilation), or (b) backend (still extractable from public Apps Script code).
- A shared secret in client is **not a security boundary** — it's a deterrent against casual abuse.
- The IP-based rate limit + payload validation provide equivalent deterrent without secret management overhead.
- If 638 later requires stronger abuse protection, **consider Cloudflare Turnstile** (no user friction) or **Apps Script LockService + IP allowlist** — but those add complexity not warranted for v1.

### Privacy / data minimization review

| Data | Collected? | Required? |
|---|:---:|:---:|
| timestamp | ✅ | ✅ |
| questionId | ✅ | ✅ |
| reason | ✅ | ✅ |
| bankId | ✅ | ✅ |
| bankVersion | ✅ | ✅ |
| schoolTrack | ✅ | ✅ |
| gradeLevel | ✅ | ✅ |
| subjectCode | ✅ | ✅ |
| language | ✅ | ✅ |
| appVersion | ✅ | ✅ |
| name | ❌ | ❌ |
| email | ❌ | ❌ |
| phone | ❌ | ❌ |
| Google account | ❌ | ❌ |
| Advertising ID | ❌ | ❌ |
| device identifier | ❌ | ❌ |
| IP (transient) | ⚠️ Apps Script reads it for rate limit, but **does NOT log it in Sheet** | n/a |
| question text | ❌ | ❌ |
| options | ❌ | ❌ |
| correct answer | ❌ | ❌ |

**Privacy verdict**: ✅ Strictly minimum. No PII. No question content. No Google account required.

---

## E. Android Integration Plan

### Current state (verified, commit `5de8a30`)

- `ReportRemoteConfig.endpointUrl = null` (default, never set in production code)
- `OkHttpReportRemoteDataSource.postReport()` returns `resp.isSuccessful` (HTTP 2xx)
- `ReportQuestionRepositoryImpl.submitReport()` returns `Success` / `FailedTransient` / `DuplicateAlreadyReported`
- `QuizScreen` snackbar shows "Thanks!" / "Couldn't send report" / "Already reported"

### Critical bug (per §C Apps Script HTTP status limitation)

**Current Android code considers every Apps Script response as Success** because Apps Script always returns HTTP 200.

**Example**: A user submits `WRONG_ANSWER`. Android POSTs. Apps Script validates reason and returns:
```
HTTP 200
{ "status": "error", "message": "Invalid reason" }   ← but reason IS valid
```
Android sees `resp.isSuccessful = true` → returns `Success` → snackbar `"Thanks!"`. **User is told their report succeeded but it actually failed.**

**Required fix in next phase**: parse the JSON response body. Only treat as success if `body.status === "ok"`.

### Production URL injection — recommended pattern (mirrors `quiz_bank_base_url`)

**Per 638 §5 "可以沿用现有 quiz_bank_base_url 的配置方式"**, use the same pattern:

**Step 1**: Add `report.endpointUrl` to `local.properties` (gitignored):
```properties
report.endpointUrl=https://script.google.com/macros/s/AKfycbwXXXXXXXX/exec
```

**Step 2**: Expose via `:sync` `buildConfigField` (mirrors `quiz_bank_base_url`):
```kotlin
// sync/build.gradle.kts
buildConfigField(
    "String",
    "REPORT_ENDPOINT_URL",
    "\"" + localOrDefault("report.endpointUrl", "") + "\""
)
```

**Step 3**: Initialize `ReportRemoteConfig.endpointUrl` at app start (mirrors how `BankConfigRepositoryImpl` initializes `defaultBaseUrl`):
- Best location: a new `ReportConfigInitializer` in `:app` (or `:sync`) that runs at app start (Application.onCreate) and reads `BuildConfig.REPORT_ENDPOINT_URL` into `ReportRemoteConfig.endpointUrl`.
- Alternative: Hilt `@Provides @Named("report_endpoint_url") String` in `:sync`, read in a `@Singleton` initializer, write to `ReportRemoteConfig.endpointUrl`.

**Step 4**: Debug vs release:
- **Debug build**: `local.properties` defaults to empty string → `ReportRemoteConfig.endpointUrl = ""` → reports are no-op'd (per existing Phase 10.5R behavior). OR explicitly use a staging Web App URL in `local.properties` for debug.
- **Release build**: production URL in `local.properties` → real Web App URL injected.

### Files that would need modification in the NEXT implementation phase

| File | Modification |
|---|---|
| `sync/build.gradle.kts` | Add `buildConfigField("REPORT_ENDPOINT_URL", ...)` |
| `sync/src/main/kotlin/.../OkHttpReportRemoteDataSource.kt` | **CRITICAL**: parse JSON response body, return `false` if `body.status != "ok"` |
| `sync/src/main/kotlin/.../ReportRemoteConfig.kt` | (no change — already exists, endpointUrl stays `@Volatile var`) |
| `app/src/main/kotlin/.../KuizKuApp.kt` | Initialize `ReportRemoteConfig.endpointUrl = BuildConfig.REPORT_ENDPOINT_URL` (or via a new `ReportConfigInitializer`) |
| `sync/src/test/kotlin/.../OkHttpReportRemoteDataSourceTest.kt` | Update tests to handle Apps Script's "always 200" behavior |
| `app/src/main/kotlin/.../app/di/ReportBridgeModule.kt` | (no change) |

---

## F. Real UAT Plan (Android → Apps Script → Google Sheet)

### Pre-requisites
1. Create Google Sheet `kuizku-question-reports` with 10 columns header (Row 1).
2. Create Apps Script project bound to the Sheet.
3. Deploy as Web App with access setting: **"Anyone"** (so Android can POST without auth).
4. Copy the `/exec` URL → add to `local.properties` as `report.endpointUrl`.
5. Build a debug APK with the URL.
6. Install on Note 8 (or Robolectric test that uses real URL).

### UAT scenarios (per 638 §6)

| # | Scenario | Setup | Expected Sheet outcome | Expected Android snackbar |
|---|---|---|---|---|
| 1 | **Valid report — WRONG_ANSWER** | User taps Report → WRONG_ANSWER | New row with reason=WRONG_ANSWER | "Thanks! We'll check this question." |
| 2 | **Valid report — UNCLEAR_QUESTION** | User taps Report → UNCLEAR_QUESTION | New row with reason=UNCLEAR_QUESTION | "Thanks!" |
| 3 | **Valid report — TYPO_SPELLING** | User taps Report → TYPO_SPELLING | New row with reason=TYPO_SPELLING | "Thanks!" |
| 4 | **Valid report — OTHER** | User taps Report → OTHER | New row with reason=OTHER | "Thanks!" |
| 5 | **Malformed JSON** (curl POST `not json`) | `curl -d 'not json' URL` | No new row | n/a (curl, not Android) |
| 6 | **Missing field** (curl POST `{"questionId":"x"}`) | curl | No new row | n/a |
| 7 | **Invalid reason** (curl POST `{"reason":"BANANA",...}`) | curl | No new row | n/a |
| 8 | **Duplicate report** (same `questionId+bankVersion+reason`) | Two Android submits | Second append MAY create a 2nd row in Sheet (Sheet is append-only, no dedupe at backend). Android-side: second shows "Already reported". | First: "Thanks!"; second: "Already reported" |
| 9 | **Backend failure** (Apps Script returns `{status:"error"}`) | Test via curl with valid payload but invalid sheet ID | No new row | n/a |
| 10 | **Android offline** (WiFi off, tap Report) | Disable network on device | No new row | "Couldn't send report. Please try again later." |
| 11 | **Endpoint not configured** (release build without `local.properties`) | Build APK with no `report.endpointUrl` set | No new row | "Couldn't send report." |

### UAT verification commands

```bash
# 1. Health check (GET)
curl https://script.google.com/macros/s/AKfycbwXXX/exec
# Expected: {"status":"ok","version":"1"}

# 2. Valid report (POST)
curl -X POST -H "Content-Type: application/json" -d '{
  "timestamp": 1727000000000,
  "questionId": "test-q-001",
  "reason": "WRONG_ANSWER",
  "bankId": "llcai_kuizku_v4_test",
  "bankVersion": 2,
  "schoolTrack": "SK",
  "gradeLevel": "Tahun1",
  "subjectCode": "bm",
  "language": "ms",
  "appVersion": "1.0.0"
}' https://script.google.com/macros/s/AKfycbwXXX/exec
# Expected: {"status":"ok","rowIndex":2}

# 3. Malformed JSON
curl -X POST -H "Content-Type: application/json" -d 'not json' URL
# Expected: {"status":"error","message":"Invalid JSON"}

# 4. Missing field
curl -X POST -H "Content-Type: application/json" -d '{"questionId":"x"}' URL
# Expected: {"status":"error","message":"Missing field: timestamp"}

# 5. Invalid reason
curl -X POST -H "Content-Type: application/json" -d '{...,"reason":"BANANA",...}' URL
# Expected: {"status":"error","message":"Invalid reason"}
```

### Note 8 (Android device) UAT steps

1. Install debug APK with `local.properties` containing production-style Web App URL.
2. Open a Quiz, tap a question, tap Flag icon, select reason → see snackbar.
3. Verify Sheet: row appended with correct 10 fields.
4. Disable WiFi, tap Report again → snackbar `"Couldn't send report. Please try again later."`.
5. Re-enable WiFi, tap Report on same question+reason → snackbar `"Already reported"`. (Android-side dedupe, NOT Sheet-side.)
6. For backend-failure test: deploy Apps Script with broken Sheet ID, repeat scenario 1 → snackbar `"Couldn't send report."` (after next-phase Android fix).

---

## G. Deployment Steps (for next phase — NOT executed now)

### Step-by-step (per 638 §7 — describe only, do not deploy)

| # | Action | Where | Cost / Time |
|---|---|---|---|
| 1 | Create Google Account (or use existing) for Apps Script deployment | browser | free |
| 2 | Create new Google Sheet `kuizku-question-reports` | drive.google.com | free |
| 3 | Add Row 1 header: timestamp, questionId, reason, bankId, bankVersion, schoolTrack, gradeLevel, subjectCode, language, appVersion | sheet | 1 min |
| 4 | Create Apps Script project: Extensions → Apps Script in the Sheet | script.google.com | free |
| 5 | Paste `doPost` / `doGet` from §C into `Code.gs` | script editor | 5 min |
| 6 | Deploy → New deployment → Web App | deploy dialog | 2 min |
| 7 | Set "Execute as" = **Me** (the script owner) | deploy dialog | — |
| 8 | Set "Who has access" = **Anyone** (required for Android POST) | deploy dialog | — |
| 9 | Copy the `/exec` URL → save to **1Password** (NOT local.properties yet) | clipboard | — |
| 10 | Add to `local.properties` on build machine: `report.endpointUrl=<URL>` | local.properties | 1 min |
| 11 | Build debug APK with URL injected | `./gradlew :app:assembleDebug` | 5 min |
| 12 | Install on Note 8 | `adb install -r app-debug.apk` | 1 min |
| 13 | Run UAT scenario 1 (valid report) | Note 8 + curl | 10 min |
| 14 | Verify Sheet row appended with correct 10 fields | sheet | 1 min |
| 15 | Run remaining UAT scenarios 2-11 | Note 8 + curl | 30 min |
| 16 | If all scenarios pass, mark Sheet as authoritative production backend | sheet | — |
| 17 | (Next phase) Implement Android-side JSON response parsing fix (per §C/E) | Android code | TBD |
| 18 | (Next phase) Build release APK with URL | gradle | TBD |

### Total time estimate: ~1.5 hours for full deployment + UAT

---

## H. Risks / Limitations

| # | Risk / Limitation | Impact | Mitigation |
|---|---|---|---|
| 1 | **Apps Script always returns HTTP 200** | Android's `resp.isSuccessful` check is insufficient (per §C) | **MUST FIX**: parse JSON body, check `body.status === "ok"` (next-phase Android change) |
| 2 | **Apps Script has request size limits** (~50MB body) | Not a real risk — payload is ~300 bytes | None needed |
| 3 | **Apps Script has execution time limit** (30s for anonymous, 6min for owner) | Sheet appendRow is fast; not a risk | None needed |
| 4 | **Apps Script quota**: 20,000 requests/day per account | 638's user base (low) unlikely to exceed | Monitor; if exceeded, migrate to Cloud Functions |
| 5 | **No real auth on endpoint** | Anyone with URL can POST (rate-limited at 100/hour/IP) | Acceptable for v1; IP rate limit deters abuse |
| 6 | **Sheet becomes unbounded over time** | Disk usage grows; query performance degrades | v1 acceptable; v2 add Sheet archiving |
| 7 | **Apps Script `appendRow` is not atomic across rows** | Two simultaneous reports could create race condition | Acceptable — Sheet append is fast enough that conflicts are rare |
| 8 | **`CacheService` rate limit data is per-script-instance** (not globally shared across deploys) | Rate limit could be bypassed if user can spawn many Apps Script instances | Acceptable — same instance serves all requests |
| 9 | **No retry mechanism on Android** (per Phase 10.5R explicit decision) | User-initiated retry needed if first attempt failed | Acceptable per 638 §6 |
| 10 | **No cross-device dedupe on backend** | Two devices reporting same question+reason create 2 Sheet rows | Acceptable — primary dedupe is Android-side; Sheet-side is observability only |
| 11 | **Web App URL leaks if committed to public Git** | Spammers could fill Sheet (rate-limited) | **MUST** keep URL in `local.properties` (gitignored), never in source |
| 12 | **Google Apps Script access settings**: "Anyone" means truly anyone | URL is the only protection | Acceptable — URL is long random `/exec` token |
| 13 | **No analytics dashboard** | Hard to see report trends | v1 read Sheet manually; v2 add Looker Studio dashboard |
| 14 | **Android-side bug fix is in next phase, not this phase** | This commit `5de8a30` has a known UX truthfulness bug | Document in next-phase plan; do not deploy backend until Android fix is in |

---

## I. Files That Would Need Modification in the NEXT Implementation Phase

### A. Mandatory Android changes (critical bug fix per §C/E)

| File | Why | Effort |
|---|---|---|
| `sync/src/main/kotlin/.../OkHttpReportRemoteDataSource.kt` | Parse JSON response body. Return `false` if `body.status != "ok"`. | ~30 LOC |
| `sync/src/test/kotlin/.../OkHttpReportRemoteDataSourceTest.kt` | Add tests for "Apps Script always-200 + status field" behavior | ~50 LOC |
| `sync/build.gradle.kts` | Add `buildConfigField("REPORT_ENDPOINT_URL", localOrDefault(...))` | ~5 LOC |
| `sync/src/main/kotlin/.../core/security/SecurityConfigModule.kt` (or new `ReportConfigModule.kt`) | Add `@Provides @Named("report_endpoint_url") String` | ~10 LOC |
| `app/src/main/kotlin/.../KuizKuApp.kt` (or new `ReportConfigInitializer.kt`) | Initialize `ReportRemoteConfig.endpointUrl = BuildConfig.REPORT_ENDPOINT_URL` at app start | ~10 LOC |

### B. Recommended Android changes (URL injection + UX)

| File | Why | Effort |
|---|---|---|
| `local.properties` (gitignored, **NOT** in git) | User-supplied URL | n/a |
| `.gitignore` (verify `local.properties` already ignored) | safety check | n/a |
| `docs/REPORT_ENDPOINT_SETUP.md` (new) | 638 + future maintainer documentation | ~30 LOC |

### C. Google Apps Script + Sheet (deployment, NOT in repo)

| Artifact | Where |
|---|---|
| Google Sheet `kuizku-question-reports` | drive.google.com |
| Apps Script `Code.gs` (~80 LOC) | script.google.com |
| Web App URL | 1Password + `local.properties` |

### D. NOT modified in next phase

- Any other Android source (Room schema, encryption, BankSyncer, V3, V4-TEST, Reference DB, Phase 10.1 JSON) — all frozen.
- `:app/.../ui/quiz/QuizScreen.kt` — UI unchanged.
- `:app/.../di/ReportBridgeModule.kt` — Hilt bridge unchanged.
- `:data/.../report/*` — DataStore dedupe unchanged.
- All existing test files (no test removals or modifications outside the listed files).

---

# 🛑 HARD STOPPED — 等待 638 下一步授權

**Phase 10.5R-B Preflight COMPLETE (READ-ONLY).**

**Key conclusions**:
- ✅ Google Sheet schema designed (10 columns, all validation rules specified)
- ✅ Apps Script `doPost` API specified (with JSON response pattern since Apps Script always returns HTTP 200)
- ⚠️ **CRITICAL BUG IDENTIFIED**: Android `OkHttpReportRemoteDataSource.postReport` uses `resp.isSuccessful` which is INSUFFICIENT for Apps Script (which always returns HTTP 200). MUST FIX in next phase.
- ✅ Security/abuse protection designed (IP rate limit, payload validation, no PII, no shared secret in v1)
- ✅ Android integration plan mirrors existing `quiz_bank_base_url` pattern (local.properties + buildConfigField)
- ✅ Real UAT plan with 11 scenarios
- ✅ Deployment steps described (NOT executed per §严格禁止)
- ✅ 5 files listed for next-phase Android modification
- ✅ HEAD `5de8a30` unchanged; no commit performed

**Strict scope compliance**:
- ❌ NO Android source modified ✅
- ❌ NO Apps Script deployed ✅
- ❌ NO Google Sheet created ✅
- ❌ NO V3 / V4-TEST / Reference DB / Phase 10.1 / Room migration modified ✅
- ❌ NO Batch 02+ / new questions ✅
- ❌ NO Google Play / GitHub Pages ✅
- ❌ NO commit / push ✅

**Awaiting 638 next authorization** (likely: fix Android JSON parsing bug + deploy Google Apps Script + UAT, OR further design clarifications).

🚢
