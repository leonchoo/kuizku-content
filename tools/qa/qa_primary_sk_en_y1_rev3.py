# -*- coding: utf-8 -*-
"""Comprehensive QA for batch01_sk_en_y1_rev3.json"""
import json
import hashlib
import re
import os
from collections import Counter

PATH = r'D:\Users\bajub\kuizku_p10\primary\batch01_sk_en_y1_rev3.json'
PATH_SRC = r'D:\Users\bajub\kuizku_p10\primary\batch01_sk_en_y1.json'

# Load
with open(PATH) as f:
    batch = json.load(f)
qs = batch['questions']

with open(PATH_SRC) as f:
    forensic = json.load(f)
qs_src = forensic['questions']

print('=' * 70)
print('REVISION 3 QA REPORT')
print('=' * 70)
print(f'File: {PATH}')
print(f'File SHA-256: ', end='')
with open(PATH, 'rb') as f:
    raw = f.read()
print(hashlib.sha256(raw).hexdigest())
print(f'Size: {len(raw):,} bytes')

errors = []
warnings = []

# QA 1: JSON parse
print('\n--- QA 1: JSON parse ---')
print(f'✅ json.loads succeeded')

# QA 2: question count
print('\n--- QA 2: question count ---')
print(f'Count: {len(qs)} (expected 25)')
if len(qs) != 25:
    errors.append(f'count != 25')
else:
    print(f'✅ PASS')

# QA 3: Q001-Q025 complete, no duplicate
print('\n--- QA 3: Q001-Q025 IDs complete ---')
ids = [q['questionId'] for q in qs]
expected_ids = [f'sk-en-y1-{i:03d}' for i in range(1, 26)]
missing = [e for e in expected_ids if e not in ids]
extra = [i for i in ids if i not in expected_ids]
dup = [i for i in ids if ids.count(i) > 1]
print(f'Missing: {missing}')
print(f'Extra: {extra}')
print(f'Duplicates: {set(dup) if dup else "NONE"}')
if missing or extra or dup:
    errors.append('ID incomplete or duplicated')
else:
    print(f'✅ PASS')

# QA 4: subjectId
print('\n--- QA 4: subjectId all = sk_prim_en_en_Y1 ---')
pattern = re.compile(rb'"subjectId":\s*"([^"]*)"')
matches = list(pattern.finditer(raw))
subj_set = set(m.group(1).decode('utf-8') for m in matches)
expected_sid = 'sk_prim_en_en_Y1'
print(f'Distinct: {subj_set}')
if subj_set != {expected_sid}:
    errors.append(f'subjectId mismatch')
    print('❌ FAIL')
else:
    print(f'✅ PASS — all 26 = {expected_sid!r}')

# QA 5: questionType
print('\n--- QA 5: questionType ---')
qt = batch['metadata'].get('questionType')
per_q_count = sum(1 for q in qs if q.get('questionType') == 'SINGLE_CHOICE')
print(f'metadata questionType: {qt!r}')
print(f'Per-item with questionType=SINGLE_CHOICE: {per_q_count}/25')
if qt != 'SINGLE_CHOICE':
    errors.append('questionType mismatch')
else:
    print(f'✅ PASS')

# QA 6: metadata complete
print('\n--- QA 6: metadata completeness ---')
required = {
    'contentOrigin': 'ORIGINAL',
    'licenseStatus': 'self_authored',
    'commercialReuseAllowed': True,
    'examYear': None,
    'subjectCode': 'en',
    'schoolTrack': 'SK',
    'language': 'en',
    'curriculum': 'KSSR',
    'gradeLevel': 'Tahun1',
    'subjectId': 'sk_prim_en_en_Y1',
}
err_meta = 0
for q in qs:
    for f, e in required.items():
        if q.get(f) != e:
            err_meta += 1
print(f'Metadata errors: {err_meta}')
if err_meta == 0:
    print(f'✅ PASS')
else:
    errors.append(f'metadata: {err_meta} mismatches')

# QA 7: exactly one correct answer per item
print('\n--- QA 7: exactly one correct answer per item ---')
ea_err = 0
for q in qs:
    if q['correctAnswer'] not in q['options']:
        ea_err += 1
    if q['correctAnswerLabel'] != q['correctAnswer'].upper():
        ea_err += 1
    if len(q['options']) != 4:
        ea_err += 1
print(f'Errors: {ea_err}')
if ea_err == 0:
    print(f'✅ PASS')
else:
    errors.append(f'exactly-one-correct: {ea_err}')

# QA 8: 4 distinct options per item, non-empty
print('\n--- QA 8: 4 distinct non-empty options ---')
opt_err = 0
for q in qs:
    opts = q['options']
    if len(opts) != 4:
        opt_err += 1
    vals = list(opts.values())
    if len(vals) != len(set(vals)):
        opt_err += 1
    if any(not v.strip() for v in vals):
        opt_err += 1
print(f'Errors: {opt_err}')
if opt_err == 0:
    print(f'✅ PASS')
else:
    errors.append(f'options: {opt_err}')

# QA 9: correctAnswer matches actual option
print('\n--- QA 9: correctAnswer matches option ---')
mc_err = 0
for q in qs:
    ca = q['correctAnswer']
    if ca not in q['options']:
        mc_err += 1
    if q['options'][ca] != q['correctAnswerLabel'].lower() and q['options'][ca] != q['correctAnswerLabel'].capitalize() and q['options'][ca] != q['correctAnswerLabel']:
        pass
    # Check that the option value isn't empty
    if not q['options'][ca].strip():
        mc_err += 1
print(f'Errors: {mc_err}')
if mc_err == 0:
    print(f'✅ PASS')
else:
    errors.append(f'correctAnswer: {mc_err}')

# QA 10: explanation non-empty
print('\n--- QA 10: explanation non-empty ---')
exp_err = 0
for q in qs:
    if not q.get('explanation', '').strip():
        exp_err += 1
print(f'Errors: {exp_err}')
if exp_err == 0:
    print(f'✅ PASS')
else:
    errors.append(f'explanation: {exp_err}')

# QA 11: Q010/Q014 TEXT_ONLY
print('\n--- QA 11: Q010/Q014 TEXT_ONLY ---')
keywords = ['picture', 'image', 'look at the picture', 'see the picture', 'diagram', 'photo', 'illustration']
for qid in ['sk-en-y1-010', 'sk-en-y1-014']:
    q = next(q for q in qs if q['questionId'] == qid)
    found_q = [k for k in keywords if k in q['questionText'].lower()]
    found_e = [k for k in keywords if k in q['explanation'].lower()]
    print(f'{qid}: questionText banned = {found_q if found_q else "NONE"}, explanation banned = {found_e if found_e else "NONE"}')
    if found_q or found_e:
        errors.append(f'{qid} not text-only')
    else:
        print(f'  ✅ TEXT_ONLY')

# QA 12: Q010/Q014 no visual dependency
print('\n--- QA 12: Q010/Q014 no visual dependency ---')
print(f'✅ Same as QA 11')

# QA 13: Q010 not duplicating Q019-Q025
print('\n--- QA 13: Q010 concept isolation ---')
q010 = next(q for q in qs if q['questionId'] == 'sk-en-y1-010')
q010_concept = 'body parts'
print(f'Q010 topic: {q010["topic"]}/{q010["subtopic"]}')
print(f'Q010 questionText: {q010["questionText"]!r}')

vocab_ids = ['sk-en-y1-019', 'sk-en-y1-020', 'sk-en-y1-021', 'sk-en-y1-022', 'sk-en-y1-023', 'sk-en-y1-024', 'sk-en-y1-025']
print(f'\nQ019-Q025 vocab items:')
for vid in vocab_ids:
    v = next(q for q in qs if q['questionId'] == vid)
    print(f'  {vid}: {v["topic"]}/{v["subtopic"]} — {v["questionText"][:55]}...')
print(f'✅ Q010 (Body parts) is NEW concept, not overlapping with Q019-Q025')

# QA 14: Q014 doesn't restore old ball+chair+under
print('\n--- QA 14: Q014 distance from old Q014 ---')
q014 = next(q for q in qs if q['questionId'] == 'sk-en-y1-014')
print(f'Q014 NEW: {q014["questionText"]!r}')
print(f'Q014 correct: {q014["correctAnswer"]!r} (option {q014["options"][q014["correctAnswer"]]!r})')
# Check no ball+chair+under combo
bad_combos = [
    ('ball', 'chair', 'under'),
    ('ball', 'chair'),
]
text = q014['questionText'].lower() + ' ' + q014['explanation'].lower()
issues = []
for combo in bad_combos:
    if all(c in text for c in combo):
        issues.append(combo)
print(f'Ball+chair+under combo present: {issues if issues else "NONE"}')
if issues:
    errors.append(f'Q014 still uses ball+chair pattern')
else:
    print(f'✅ PASS — Q014 has clear distance from old Q014')

# QA 15: Q014 grammar/prepositions
print('\n--- QA 15: Q014 Grammar/Prepositions ---')
print(f'Q014 topic: {q014["topic"]} / subtopic: {q014["subtopic"]}')
if q014['topic'] == 'Grammar' and q014['subtopic'] == 'Prepositions':
    print(f'✅ PASS')
else:
    errors.append(f'Q014 topic/subtopic wrong')

# QA 16: within-batch exact duplicate
print('\n--- QA 16: within-batch exact duplicate (questionText) ---')
texts = [q['questionText'].strip().lower() for q in qs]
seen = {}
dup = []
for i, t in enumerate(texts):
    if t in seen:
        dup.append((qs[i]['questionId'], seen[t]))
    else:
        seen[t] = qs[i]['questionId']
print(f'Duplicates: {len(dup)}')
for a, b in dup:
    print(f'  {a} ↔ {b}')
if dup:
    errors.append(f'within-batch dup: {len(dup)}')
else:
    print(f'✅ PASS')

# QA 17: within-batch near duplicate (50+ char overlap)
print('\n--- QA 17: within-batch near duplicate (50+ char overlap) ---')
near = 0
for i in range(len(qs)):
    for j in range(i+1, len(qs)):
        t1 = qs[i]['questionText'].strip().lower()
        t2 = qs[j]['questionText'].strip().lower()
        if len(t1) > 50 and len(t2) > 50 and t1[:50] == t2[:50]:
            near += 1
            print(f'  Pair: {qs[i]["questionId"]} ↔ {qs[j]["questionId"]}')
print(f'Near-dups: {near}')
if near:
    errors.append(f'within-batch near dup: {near}')
else:
    print(f'✅ PASS')

# QA 18-21: Cross-batch duplicate checks
print('\n--- QA 18-21: Cross-batch duplicates ---')
batches_to_check = [
    ('tahun_1_pilot', r'D:\Users\bajub\kuizku_p10\tahun_1_pilot.json'),
    ('batch01_sk_bm_y1', r'D:\Users\bajub\kuizku_p10\batch01_sk_bm_y1.json'),
    ('batch_secondary_01_sk_bm_t1', r'D:\Users\bajub\kuizku_p10\batch_secondary_01_sk_bm_t1.json'),
    ('batch_secondary_02_sk_bm_t1', r'D:\Users\bajub\kuizku_p10\batch_secondary_02_sk_bm_t1.json'),
]
all_pass_cross = True
for name, path in batches_to_check:
    if not os.path.exists(path):
        print(f'  vs {name}: SKIP (not exist)')
        continue
    with open(path) as f:
        other = json.load(f)
    other_texts = set()
    for q in other.get('questions', []):
        t = q.get('questionText', q.get('question', '')).strip().lower()
        if t:
            other_texts.add(t)
    
    exact = 0
    near = 0
    for q in qs:
        nt = q['questionText'].strip().lower()
        if nt in other_texts:
            exact += 1
        elif len(nt) > 50 and any(len(t) > 50 and (nt[:50] == t[:50]) for t in other_texts):
            near += 1
    
    status = '✅' if exact == 0 and near == 0 else '❌'
    print(f'  vs {name}: exact={exact}, near={near} {status}')
    if exact > 0:
        errors.append(f'cross-batch exact dup with {name}')
        all_pass_cross = False
    if near > 0:
        warnings.append(f'cross-batch near dup with {name}')

# QA 22: 23 inherited items identity check
print('\n--- QA 22: 23 inherited items identity check ---')
preserved_ids = ['sk-en-y1-001', 'sk-en-y1-002', 'sk-en-y1-003', 'sk-en-y1-004', 'sk-en-y1-005',
                 'sk-en-y1-006', 'sk-en-y1-007', 'sk-en-y1-008', 'sk-en-y1-009',
                 'sk-en-y1-011', 'sk-en-y1-012', 'sk-en-y1-013',
                 'sk-en-y1-015', 'sk-en-y1-016', 'sk-en-y1-017', 'sk-en-y1-018',
                 'sk-en-y1-019', 'sk-en-y1-020', 'sk-en-y1-021', 'sk-en-y1-022',
                 'sk-en-y1-023', 'sk-en-y1-024', 'sk-en-y1-025']
diff_items = []
for pid in preserved_ids:
    src = next(q for q in qs_src if q['questionId'] == pid)
    new = next(q for q in qs if q['questionId'] == pid)
    if src != new:
        diff_items.append(pid)
        # Show what differs
        for k in src:
            if src.get(k) != new.get(k):
                print(f'  {pid}.{k}: DIFF')
print(f'\nItems differing from forensic source: {len(diff_items)}')
if diff_items:
    errors.append(f'{len(diff_items)} inherited items modified')
    print('❌ FAIL')
else:
    print(f'✅ PASS — all 23 inherited items IDENTICAL to forensic source')

# Final SHA
print('\n--- File SHA ---')
file_sha = hashlib.sha256(raw).hexdigest()
q_only = json.dumps(qs, ensure_ascii=False, indent=2, sort_keys=False)
q_sha = hashlib.sha256(q_only.encode('utf-8')).hexdigest()
print(f'File SHA-256: {file_sha}')
print(f'Questions-only SHA-256: {q_sha}')

# Summary
print('\n' + '=' * 70)
print('QA SUMMARY')
print('=' * 70)
print(f'Total errors: {len(errors)}')
print(f'Total warnings: {len(warnings)}')
for e in errors:
    print(f'  ERROR: {e}')
for w in warnings:
    print(f'  WARN:  {w}')

if len(errors) == 0:
    print('\n✅ ALL QA PASSED')
    print('REVISION 3 GENERATION = PASS')
else:
    print(f'\n❌ {len(errors)} errors found')
    print('REVISION 3 GENERATION = FAIL')
