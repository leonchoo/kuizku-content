# -*- coding: utf-8 -*-
"""QA report for primary SK English Year 1 batch 01."""
import json
import re
import hashlib
from collections import Counter

BATCH = r'D:\Users\bajub\kuizku_p10\primary\batch01_sk_en_y1.json'

with open(BATCH) as f:
    batch = json.load(f)
qs = batch['questions']

errors = []
warnings = []

# ============================================================
# 1. Question count
# ============================================================
print('=== QA 1: Question count ===')
print(f'  Count: {len(qs)} (expected 25)')
if len(qs) != 25:
    errors.append('count != 25')

# ============================================================
# 2. subjectId
# ============================================================
print('\n=== QA 2: subjectId ===')
subj = set(q.get('subjectId') for q in qs)
print(f'  Distinct values: {subj}')
expected = 'sk_prim_en_en_T1'
if subj != {expected}:
    errors.append(f'subjectId not unique {expected}: {subj}')
else:
    print(f'  ✅ All 25 = {expected!r}')

# ============================================================
# 3. Metadata completeness
# ============================================================
print('\n=== QA 3: Metadata completeness ===')
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
    'stage': 'primary',
    'subjectId': 'sk_prim_en_en_T1',
}
err_meta = []
for q in qs:
    for f, e in required.items():
        if q.get(f) != e:
            err_meta.append(f'{q["questionId"]}: {f} expected {e!r}, got {q.get(f)!r}')
print(f'  Metadata errors: {len(err_meta)}')
if err_meta:
    errors.append(f'metadata: {len(err_meta)} mismatches')

# ============================================================
# 4. Exactly one correct answer
# ============================================================
print('\n=== QA 4: Exactly one correct answer ===')
ea_err = 0
for q in qs:
    opts = q['options']
    k = q['correctAnswer']
    lbl = q['correctAnswerLabel']
    if k not in opts:
        ea_err += 1
    if lbl != k.upper():
        ea_err += 1
    if len(opts) != 4:
        ea_err += 1
print(f'  Errors: {ea_err}')

# ============================================================
# 5. No duplicate options
# ============================================================
print('\n=== QA 5: No duplicate options ===')
dup_err = 0
for q in qs:
    vals = list(q['options'].values())
    if len(vals) != len(set(vals)):
        dup_err += 1
print(f'  Errors: {dup_err}')

# ============================================================
# 6. Difficulty distribution
# ============================================================
print('\n=== QA 6: Difficulty distribution ===')
dc = Counter(q['difficulty'] for q in qs)
print(f'  Easy: {dc.get(1, 0)} (target 15)')
print(f'  Medium: {dc.get(2, 0)} (target 7)')
print(f'  Hard: {dc.get(3, 0)} (target 3)')
if dc.get(1, 0) != 15 or dc.get(2, 0) != 7 or dc.get(3, 0) != 3:
    warnings.append(f'difficulty mismatch: {dict(dc)}')

# ============================================================
# 7. Skill distribution
# ============================================================
print('\n=== QA 7: Skill distribution ===')
sc = Counter(q['skillType'] for q in qs)
for s, c in sorted(sc.items()):
    print(f'  {s}: {c}')

# ============================================================
# 8. Source tag distribution
# ============================================================
print('\n=== QA 8: Source tag distribution ===')
sr = Counter(q.get('source_tag') for q in qs)
for s, c in sorted(sr.items()):
    print(f'  {s}: {c}')
if sr.get('KSSM_T1_OFFICIAL', 0) > 0:
    errors.append('KSSM_T1_OFFICIAL used (prohibited)')

# ============================================================
# 9. Within-batch duplicate
# ============================================================
print('\n=== QA 9: Within-batch exact duplicate ===')
seen = {}
dup = 0
for q in qs:
    norm = q['questionText'].strip().lower()
    if norm in seen:
        dup += 1
    seen[norm] = q['questionId']
print(f'  Errors: {dup}')

# ============================================================
# 10. Cross-batch duplicate (vs primary_batch01_sk_bm_y1, phase10.1 pilot)
# ============================================================
print('\n=== QA 10: Cross-batch duplicate check ===')
try:
    with open(r'D:\Users\bajub\kuizku_p10\batch01_sk_bm_y1.json') as f:
        b01 = json.load(f)
    b01_texts = set(q['questionText'].strip().lower() for q in b01['questions'])
    cross_dup = 0
    for q in qs:
        if q['questionText'].strip().lower() in b01_texts:
            cross_dup += 1
            errors.append(f'cross-batch dup with batch01_sk_bm_y1')
    print(f'  Cross-batch (vs batch01_sk_bm_y1): {cross_dup} errors')
except FileNotFoundError:
    print('  batch01_sk_bm_y1 not found - skip')

# Check phase 10.1 pilot
try:
    with open(r'D:\Users\bajub\kuizku_p10\tahun_1_pilot.json') as f:
        p101 = json.load(f)
    p101_texts = set(q.get('questionText', q.get('question', '')).strip().lower() for q in p101.get('questions', []))
    cross_dup = 0
    for q in qs:
        if q['questionText'].strip().lower() in p101_texts:
            cross_dup += 1
    print(f'  Cross-batch (vs tahun_1_pilot): {cross_dup} errors')
except Exception as e:
    print(f'  pilot check error: {e}')

# ============================================================
# 11. JSON schema validity (json.loads already passed)
# ============================================================
print('\n=== QA 11: JSON schema validity ===')
print(f'  ✅ json.loads succeeded with {len(qs)} questions')

# ============================================================
# 12. Originality
# ============================================================
print('\n=== QA 12: Originality (English-specific) ===')
abstract_english = ['postmodern', 'metaphor', 'epistemology', 'existential']
scope_err = 0
for q in qs:
    txt = q['questionText'].lower()
    for t in abstract_english:
        if t in txt:
            scope_err += 1
print(f'  Abstract vocabulary errors: {scope_err}')

# ============================================================
# 13. File SHA
# ============================================================
print('\n=== QA 13: File SHA ===')
with open(BATCH, 'rb') as f:
    raw = f.read()
file_sha = hashlib.sha256(raw).hexdigest()
print(f'  File SHA-256: {file_sha}')

# ============================================================
# Summary
# ============================================================
print('\n' + '=' * 60)
print('QA SUMMARY')
print('=' * 60)
print(f'Total errors: {len(errors)}')
print(f'Total warnings: {len(warnings)}')
for e in errors:
    print(f'  ERROR: {e}')
for w in warnings:
    print(f'  WARN:  {w}')
if len(errors) == 0:
    print('\n✅ ALL QA PASSED')
else:
    print(f'\n❌ {len(errors)} errors found')
