"""Part F: 10 backend test scenarios for KuizKu Question Report backend V7."""
import urllib.request
import urllib.error
import json
import re
import time
import sys

EXEC_URL = "https://script.google.com/macros/s/AKfycbxNerG3Tt_dfpAyOlUuhNvvDescaHEguIvkB5V-aVbmuabZfHsd4Mlh6uxfKs3FryuL/exec"


def post(payload, label=""):
    """POST payload to /exec, return (status_code, response_dict)."""
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(EXEC_URL, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode('utf-8', errors='replace')
            matches = re.findall(r'\{[^{}]*"status"[^{}]*\}', body)
            parsed = json.loads(matches[0]) if matches else {'raw': body[:200]}
            return resp.status, parsed
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        matches = re.findall(r'\{[^{}]*"status"[^{}]*\}', body)
        parsed = json.loads(matches[0]) if matches else {'error': f'HTTP {e.code}'}
        return e.code, parsed
    except Exception as e:
        return 0, {'error': str(e)}


def post_raw(data, label=""):
    """POST raw bytes to /exec."""
    req = urllib.request.Request(EXEC_URL, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode('utf-8', errors='replace')
            matches = re.findall(r'\{[^{}]*"status"[^{}]*\}', body)
            parsed = json.loads(matches[0]) if matches else {'raw': body[:200]}
            return resp.status, parsed
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        matches = re.findall(r'\{[^{}]*"status"[^{}]*\}', body)
        parsed = json.loads(matches[0]) if matches else {'error': f'HTTP {e.code}'}
        return e.code, parsed
    except Exception as e:
        return 0, {'error': str(e)}


def get():
    with urllib.request.urlopen(EXEC_URL, timeout=15) as resp:
        body = resp.read().decode('utf-8', errors='replace')
        matches = re.findall(r'\{[^{}]*"status"[^{}]*\}', body)
        parsed = json.loads(matches[0]) if matches else {'raw': body[:200]}
        return resp.status, parsed


def main():
    now_ms = int(time.time() * 1000)
    results = {}

    # === F.1 doGet health check ===
    code, body = get()
    results['F.1 doGet'] = (code, body)
    print(f"F.1 doGet: HTTP {code} | body={body}")

    # === F.2a Valid WRONG_ANSWER ===
    code, body = post({
        'questionId': 'p10_v7_t01', 'reason': 'WRONG_ANSWER',
        'bankId': 'llcai_test', 'bankVersion': 1,
        'schoolTrack': 'SK', 'gradeLevel': 'Tahun1',
        'subjectCode': 'bm', 'language': 'ms',
        'appVersion': '1.0.0', 'timestamp': now_ms,
    })
    results['F.2a WRONG_ANSWER'] = (code, body)
    print(f"F.2a WRONG_ANSWER: HTTP {code} | body={body}")

    # === F.2b Valid UNCLEAR_QUESTION ===
    code, body = post({
        'questionId': 'p10_v7_t02', 'reason': 'UNCLEAR_QUESTION',
        'bankId': 'llcai_test', 'bankVersion': 1,
        'schoolTrack': 'SK', 'gradeLevel': 'Tahun2',
        'subjectCode': 'bc', 'language': 'zh',
        'appVersion': '1.0.0', 'timestamp': now_ms,
    })
    results['F.2b UNCLEAR_QUESTION'] = (code, body)
    print(f"F.2b UNCLEAR_QUESTION: HTTP {code} | body={body}")

    # === F.2c Valid TYPO_SPELLING ===
    code, body = post({
        'questionId': 'p10_v7_t03', 'reason': 'TYPO_SPELLING',
        'bankId': 'llcai_test', 'bankVersion': 1,
        'schoolTrack': 'INTERNATIONAL', 'gradeLevel': 'Tingkatan3',
        'subjectCode': 'math', 'language': 'en',
        'appVersion': '1.0.0', 'timestamp': now_ms,
    })
    results['F.2c TYPO_SPELLING'] = (code, body)
    print(f"F.2c TYPO_SPELLING: HTTP {code} | body={body}")

    # === F.2d Valid OTHER ===
    code, body = post({
        'questionId': 'p10_v7_t04', 'reason': 'OTHER',
        'bankId': 'llcai_test', 'bankVersion': 1,
        'schoolTrack': 'SJKC', 'gradeLevel': 'Tahun4',
        'subjectCode': 'science', 'language': 'ms',
        'appVersion': '1.0.0', 'timestamp': now_ms,
    })
    results['F.2d OTHER'] = (code, body)
    print(f"F.2d OTHER: HTTP {code} | body={body}")

    # === F.3 Malformed JSON ===
    code, body = post_raw(b'{not valid json')
    results['F.3 malformed JSON'] = (code, body)
    print(f"F.3 malformed JSON: HTTP {code} | body={body}")

    # === F.4 Missing required field ===
    code, body = post({
        'questionId': 'p10_v7_t05', 'reason': 'WRONG_ANSWER',
        'bankId': 'llcai_test', 'bankVersion': 1,
        # missing schoolTrack, gradeLevel, subjectCode, language, appVersion, timestamp
    })
    results['F.4 missing field'] = (code, body)
    print(f"F.4 missing field: HTTP {code} | body={body}")

    # === F.5 Invalid reason ===
    code, body = post({
        'questionId': 'p10_v7_t06', 'reason': 'INVALID_REASON_XYZ',
        'bankId': 'llcai_test', 'bankVersion': 1,
        'schoolTrack': 'SK', 'gradeLevel': 'Tahun1',
        'subjectCode': 'bm', 'language': 'ms',
        'appVersion': '1.0.0', 'timestamp': now_ms,
    })
    results['F.5 invalid reason'] = (code, body)
    print(f"F.5 invalid reason: HTTP {code} | body={body}")

    # === F.6 Invalid field/regex (questionId with invalid chars) ===
    code, body = post({
        'questionId': 'invalid@chars!', 'reason': 'WRONG_ANSWER',
        'bankId': 'llcai_test', 'bankVersion': 1,
        'schoolTrack': 'SK', 'gradeLevel': 'Tahun1',
        'subjectCode': 'bm', 'language': 'ms',
        'appVersion': '1.0.0', 'timestamp': now_ms,
    })
    results['F.6 invalid questionId regex'] = (code, body)
    print(f"F.6 invalid questionId regex: HTTP {code} | body={body}")

    # === F.7 Invalid timestamp (too old, >7 days) ===
    old_ms = now_ms - (10 * 24 * 60 * 60 * 1000)  # 10 days ago
    code, body = post({
        'questionId': 'p10_v7_t08', 'reason': 'WRONG_ANSWER',
        'bankId': 'llcai_test', 'bankVersion': 1,
        'schoolTrack': 'SK', 'gradeLevel': 'Tahun1',
        'subjectCode': 'bm', 'language': 'ms',
        'appVersion': '1.0.0', 'timestamp': old_ms,
    })
    results['F.7 invalid timestamp'] = (code, body)
    print(f"F.7 invalid timestamp: HTTP {code} | body={body}")

    # === F.8 Duplicate (server allows duplicate; Android-side dedupe is separate) ===
    code, body = post({
        'questionId': 'p10_v7_t01', 'reason': 'WRONG_ANSWER',
        'bankId': 'llcai_test', 'bankVersion': 1,
        'schoolTrack': 'SK', 'gradeLevel': 'Tahun1',
        'subjectCode': 'bm', 'language': 'ms',
        'appVersion': '1.0.0', 'timestamp': now_ms,
    })
    results['F.8 duplicate submission (server allows)'] = (code, body)
    print(f"F.8 duplicate submission: HTTP {code} | body={body}")

    print()
    print("=== SUMMARY ===")
    for label, (code, body) in results.items():
        status_str = body.get('status', '?') if isinstance(body, dict) else '?'
        msg_str = body.get('message', '') if isinstance(body, dict) else ''
        row_str = f"rowIndex={body.get('rowIndex')}" if isinstance(body, dict) and 'rowIndex' in body else ''
        print(f"  {label:42s} | HTTP {code} | status={status_str:10s} | {msg_str} {row_str}")

    # Save
    with open('D:/tmp/part_f_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print()
    print("Saved to D:/tmp/part_f_results.json")

    return results


if __name__ == "__main__":
    main()
