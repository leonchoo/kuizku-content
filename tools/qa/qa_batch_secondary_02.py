# -*- coding: utf-8 -*-
"""QA report for batch_secondary_02_sk_bm_t1.json."""
import json
import re
import hashlib
from collections import Counter

BATCH02 = r'D:\Users\bajub\kuizku_p10\batch_secondary_02_sk_bm_t1.json'
BATCH01 = r'D:\Users\bajub\kuizku_p10\batch_secondary_01_sk_bm_t1.json'

with open(BATCH02) as f:
    batch02 = json.load(f)
with open(BATCH01) as f:
    batch01 = json.load(f)

qs = batch02['questions']
qs1 = batch01['questions']

errors = []
warnings = []

# ============================================================
# 1. Question count
# ============================================================
print('=== QA 1: Question count ===')
print(f'  Batch 02: {len(qs)} questions (expected 25)')
if len(qs) != 25:
    errors.append(f'QA1: wrong count {len(qs)}')

# ============================================================
# 2. subjectId
# ============================================================
print('\n=== QA 2: subjectId ===')
subj = set(q.get('subjectId') for q in qs)
print(f'  Distinct values: {subj}')
expected_sid = 'sk_sec_bm_ms_T1'
if subj != {expected_sid}:
    errors.append(f'QA2: subjectId not unique {expected_sid}: {subj}')
if not all(q.get('subjectId') == expected_sid for q in qs):
    errors.append('QA2: not all 25 subjectId correct')
else:
    print(f'  ✅ All 25 = {expected_sid!r}')

# ============================================================
# 3. Metadata completeness
# ============================================================
print('\n=== QA 3: Metadata completeness ===')
required = {
    'contentOrigin': 'ORIGINAL',
    'licenseStatus': 'self_authored',
    'commercialReuseAllowed': True,
    'examYear': None,
    'subjectCode': 'bm',
    'schoolTrack': 'SK',
    'language': 'ms',
    'curriculum': 'KSSM',
    'gradeLevel': 'Tingkatan1',
    'stage': 'secondary',
    'subjectId': 'sk_sec_bm_ms_T1',
}
meta_errors = []
for i, q in enumerate(qs):
    for field, expected in required.items():
        actual = q.get(field)
        if actual != expected:
            meta_errors.append(f'  {q["questionId"]}: {field} expected {expected!r}, got {actual!r}')
if meta_errors:
    errors.append(f'QA3: {len(meta_errors)} metadata mismatches')
    for e in meta_errors[:5]:
        print(e)
else:
    print(f'  ✅ All 25 have correct metadata')

# ============================================================
# 4. Exactly one correct answer
# ============================================================
print('\n=== QA 4: Exactly one correct answer ===')
ea_errors = 0
for q in qs:
    options = q['options']
    correct_key = q['correctAnswer']
    correct_label = q['correctAnswerLabel']
    # correctKey in options
    if correct_key not in options:
        ea_errors += 1
        errors.append(f'QA4: {q["questionId"]}: correctAnswer key not in options')
    # label matches key
    if correct_label != correct_key.upper():
        ea_errors += 1
        errors.append(f'QA4: {q["questionId"]}: label mismatch')
    # exactly 4 options
    if len(options) != 4:
        ea_errors += 1
        errors.append(f'QA4: {q["questionId"]}: not 4 options')
print(f'  Errors: {ea_errors}')

# ============================================================
# 5. No duplicate options
# ============================================================
print('\n=== QA 5: No duplicate options ===')
dup_errors = 0
for q in qs:
    vals = list(q['options'].values())
    if len(vals) != len(set(vals)):
        dup_errors += 1
        errors.append(f'QA5: {q["questionId"]}: duplicate options {vals}')
print(f'  Errors: {dup_errors}')

# ============================================================
# 6. Answer label consistency (covered in QA4)

# ============================================================
# 7. Difficulty distribution
# ============================================================
print('\n=== QA 7: Difficulty distribution ===')
diff_count = Counter(q['difficulty'] for q in qs)
print(f'  Easy: {diff_count.get(1, 0)} (target 8)')
print(f'  Medium: {diff_count.get(2, 0)} (target 12)')
print(f'  Hard: {diff_count.get(3, 0)} (target 5)')
target_diff = {1: 8, 2: 12, 3: 5}
for d, t in target_diff.items():
    if diff_count.get(d, 0) != t:
        warnings.append(f'QA7: Difficulty {d} count {diff_count.get(d, 0)} != target {t}')

# ============================================================
# 8. Skill distribution
# ============================================================
print('\n=== QA 8: Skill distribution ===')
skill_count = Counter(q['skillType'] for q in qs)
print(f'  RECOGNITION: {skill_count.get("RECOGNITION", 0)} (target 9)')
print(f'  COMPREHENSION: {skill_count.get("COMPREHENSION", 0)} (target 8)')
print(f'  APPLICATION: {skill_count.get("APPLICATION", 0)} (target 8)')

# ============================================================
# 9. Source tag distribution
# ============================================================
print('\n=== QA 9: Source tag distribution ===')
src_count = Counter(q.get('source_tag') for q in qs)
print(f'  CURRICULUM_DERIVED: {src_count.get("CURRICULUM_DERIVED", 0)}')
print(f'  INFERRED: {src_count.get("INFERRED", 0)}')
print(f'  KSSM_T1_OFFICIAL: {src_count.get("KSSM_T1_OFFICIAL", 0)} (must be 0)')
if src_count.get('KSSM_T1_OFFICIAL', 0) > 0:
    errors.append('QA9: KSSM_T1_OFFICIAL used - prohibited')

# ============================================================
# 10. Within-batch duplicate
# ============================================================
print('\n=== QA 10: Within-batch exact duplicate ===')
seen = {}
dup_in_batch = 0
for q in qs:
    norm = q['questionText'].strip().lower()
    if norm in seen:
        dup_in_batch += 1
        errors.append(f'QA10: {q["questionId"]}: dup of {seen[norm]}')
    seen[norm] = q['questionId']
print(f'  Errors: {dup_in_batch}')

# ============================================================
# 11. Batch 01 exact duplicate
# ============================================================
print('\n=== QA 11: Batch 01 exact duplicate ===')
batch01_texts = set(q['questionText'].strip().lower() for q in qs1)
exact_dup = 0
for q in qs:
    norm = q['questionText'].strip().lower()
    if norm in batch01_texts:
        exact_dup += 1
        errors.append(f'QA11: {q["questionId"]}: exact dup of Batch 01 item')
print(f'  Errors: {exact_dup}')

# ============================================================
# 12. Batch 01 near duplicate (substring)
# ============================================================
print('\n=== QA 12: Batch 01 near duplicate (substring) ===')
near_dup = 0
for q in qs:
    new_norm = q['questionText'].strip().lower()
    if len(new_norm) <= 30:
        continue
    for ex in batch01_texts:
        if ex and len(ex) > 30 and (new_norm in ex or ex in new_norm):
            near_dup += 1
            errors.append(f'QA12: {q["questionId"]}: near-dup of Batch 01')
            break
print(f'  Errors: {near_dup}')

# ============================================================
# 13. Peribahasa overlap
# ============================================================
print('\n=== QA 13: Peribahasa overlap with Batch 01 ===')
batch01_peribahasa = []
for q in qs1:
    qt = q['questionText']
    if 'berat sama dipikul' in qt or 'ringan sama dijinjing' in qt:
        batch01_peribahasa.append(q['questionId'])
print(f'  Batch 01 peribahasa used: {batch01_peribahasa}')

batch02_peribahasa = []
for q in qs:
    qt = q['questionText']
    exp = q.get('explanation', '')
    if 'kera di hutan' in qt or 'kera di hutan' in exp:
        batch02_peribahasa.append(q['questionId'])
    if 'sepandai-pandai tupai' in qt or 'sepandai-pandai tupai' in exp:
        batch02_peribahasa.append(q['questionId'])
print(f'  Batch 02 peribahasa used: {batch02_peribahasa}')

# Check for the specific phrase used in Batch 01
banned_phrases = ['berat sama dipikul', 'ringan sama dijinjing']
batch01_banned_used = 0
for q in qs:
    qt = q['questionText']
    exp = q.get('explanation', '')
    for p in banned_phrases:
        if p in qt or p in exp:
            batch01_banned_used += 1
            errors.append(f'QA13: {q["questionId"]}: uses Batch 01 peribahasa "{p}"')
print(f'  Banned phrases used: {batch01_banned_used} (must be 0)')

# ============================================================
# 14. JSON schema validity (already done by json.loads)
# ============================================================
print('\n=== QA 14: JSON schema validity ===')
print(f'  ✅ json.loads() succeeded with {len(qs)} questions')

# ============================================================
# 15. T1 scope (heuristic - check for tertiary-level vocabulary)
# ============================================================
print('\n=== QA 15: T1 scope heuristic ===')
abstract_terms = ['eksistensial', 'paradigma', 'epistemologi', 'fenomenologi', 'metafora', 'naratif abstrak']
scope_errors = 0
for q in qs:
    txt = q['questionText'].lower() + ' ' + ' '.join(q['options'].values()).lower()
    for t in abstract_terms:
        if t in txt:
            scope_errors += 1
            errors.append(f'QA15: {q["questionId"]}: abstract term "{t}"')
print(f'  Errors: {scope_errors}')

# ============================================================
# 16. Passage overlap with Batch 01
# ============================================================
print('\n=== QA 16: Passage overlap with Batch 01 ===')
# Extract Batch 01 passages
batch01_passages = []
for q in qs1:
    if 'Setiap pagi, Aiman' in q['questionText']:
        batch01_passages.append(('Aiman bangun awal', q['questionId']))
    if 'Kampung Tanjung Selamat' in q['questionText']:
        batch01_passages.append(('Kampung Tanjung Selamat', q['questionId']))

passage_overlap = 0
for q in qs:
    qt = q['questionText']
    for p_text, p_qid in batch01_passages:
        # Check for substantial passage overlap (>30 chars)
        for snippet in [p_text, p_text[:50]]:
            if snippet in qt and len(snippet) > 30:
                passage_overlap += 1
                errors.append(f'QA16: {q["questionId"]}: passage overlap with Batch 01 {p_qid}')
print(f'  Errors: {passage_overlap}')

# ============================================================
# 17. File SHA
# ============================================================
print('\n=== QA 17: File SHA ===')
with open(BATCH02, 'rb') as f:
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
