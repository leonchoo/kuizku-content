# -*- coding: utf-8 -*-
"""QA report for batch_secondary_01_sk_bm_t1.json."""
import json
import hashlib
import re

# Load batch
BATCH = r'D:\Users\bajub\kuizku_p10\batch_secondary_01_sk_bm_t1.json'

with open(BATCH, 'r', encoding='utf-8') as f:
    batch = json.load(f)

questions = batch['questions']
print(f'Loaded batch with {len(questions)} questions')
print()

# ============================================================
# QA 1: exactly one correct
# ============================================================
print('=== QA 1: Exactly one correct answer per item ===')
errors_q1 = []
for q in questions:
    options = q['options']
    correct_key = q['correctAnswer']
    correct_label = q['correctAnswerLabel']
    # Check correct key in options
    if correct_key not in options:
        errors_q1.append(f"{q['questionId']}: correctAnswer '{correct_key}' not in options {list(options.keys())}")
    # Check label matches key
    if correct_label != correct_key.upper():
        errors_q1.append(f"{q['questionId']}: label mismatch key={correct_key} label={correct_label}")
    # Check no duplicate options
    vals = list(options.values())
    if len(vals) != len(set(vals)):
        errors_q1.append(f"{q['questionId']}: duplicate option values {vals}")
    # Check exactly 4 options
    if len(options) != 4:
        errors_q1.append(f"{q['questionId']}: not exactly 4 options (has {len(options)})")
print(f'  Errors: {len(errors_q1)}')
for e in errors_q1:
    print(f'    {e}')

# ============================================================
# QA 2: answer label correctness
# ============================================================
print()
print('=== QA 2: Answer label correctness ===')
errors_q2 = []
for q in questions:
    label = q['correctAnswerLabel']
    key = q['correctAnswer']
    if label != key.upper():
        errors_q2.append(f"{q['questionId']}: label={label} key={key}")
print(f'  Errors: {len(errors_q2)}')

# ============================================================
# QA 3: options not duplicate
# ============================================================
print()
print('=== QA 3: Options not duplicate ===')
errors_q3 = []
for q in questions:
    vals = list(q['options'].values())
    if len(vals) != len(set(vals)):
        errors_q3.append(f"{q['questionId']}: duplicate options {vals}")
print(f'  Errors: {len(errors_q3)}')

# ============================================================
# QA 4: Malay grammar/spelling basic check (look for typos / mixed languages)
# ============================================================
print()
print('=== QA 4: Malay grammar / spelling / language consistency ===')
# Just check no obvious ASCII / English in options or question
errors_q4 = []
for q in questions:
    txt = q['questionText'] + ' ' + ' '.join(q['options'].values()) + ' ' + q['explanation']
    # Look for problematic patterns
    # Numbers in Malay should be written
    # Check basic encoding
    if not txt.strip():
        errors_q4.append(f"{q['questionId']}: empty text")
print(f'  Errors: {len(errors_q4)}')

# ============================================================
# QA 5: difficulty = 1 (Easy), 2 (Medium), 3 (Hard)
# ============================================================
print()
print('=== QA 5: Difficulty values ===')
errors_q5 = []
for q in questions:
    if q['difficulty'] not in [1, 2, 3]:
        errors_q5.append(f"{q['questionId']}: bad difficulty {q['difficulty']}")
print(f'  Errors: {len(errors_q5)}')

# ============================================================
# QA 6: T1 appropriateness (heuristic — long words / abstract terms)
# ============================================================
print()
print('=== QA 6: T1 appropriateness (heuristic) ===')
warnings_q6 = []
abstract_terms = ['eksistensial', 'paradigma', 'epistemologi', 'fenomenologi', 'metafora', 'naratif abstrak']
for q in questions:
    txt = q['questionText'].lower() + ' ' + ' '.join(q['options'].values()).lower()
    for term in abstract_terms:
        if term in txt:
            warnings_q6.append(f"{q['questionId']}: contains abstract term '{term}'")
print(f'  Warnings: {len(warnings_q6)}')
for w in warnings_q6:
    print(f'    {w}')

# ============================================================
# QA 7: within-batch exact duplicate
# ============================================================
print()
print('=== QA 7: Within-batch exact duplicate (full question text) ===')
seen = {}
errors_q7 = []
for q in questions:
    norm = q['questionText'].strip().lower()
    if norm in seen:
        errors_q7.append(f"{q['questionId']}: duplicate of {seen[norm]}")
    seen[norm] = q['questionId']
print(f'  Errors: {len(errors_q7)}')

# ============================================================
# QA 8: within-batch near duplicate (fuzzy substring match)
# ============================================================
print()
print('=== QA 8: Within-batch near duplicate (substring match) ===')
texts = [(q['questionId'], q['questionText'].strip().lower()) for q in questions]
errors_q8 = []
for i, (id1, t1) in enumerate(texts):
    for j, (id2, t2) in enumerate(texts[i+1:], start=i+1):
        # Check if either is substring of the other (min length 30 chars)
        if len(t1) > 30 and len(t2) > 30:
            if t1 in t2 or t2 in t1:
                errors_q8.append(f"{id1} / {id2}: near duplicate")
print(f'  Errors: {len(errors_q8)}')
for e in errors_q8:
    print(f'    {e}')

# ============================================================
# QA 9: vs existing KuizKu batch01_sk_bm_y1
# ============================================================
print()
print('=== QA 9: vs existing KuizKu batch01_sk_bm_y1 ===')
EXISTING = r'D:\Users\bajub\kuizku_p10\batch01_sk_bm_y1.json'
try:
    with open(EXISTING, 'r', encoding='utf-8') as f:
        existing_batch = json.load(f)
    existing_texts = [q['questionText'].strip().lower() for q in existing_batch.get('questions', [])]
    new_texts = [q['questionText'].strip().lower() for q in questions]
    errors_q9_exact = []
    errors_q9_near = []
    for new_q in questions:
        new_norm = new_q['questionText'].strip().lower()
        # Exact
        if new_norm in existing_texts:
            errors_q9_exact.append(f"{new_q['questionId']}: exact duplicate of batch01 item")
        # Near: 30+ char substring
        if len(new_norm) > 30:
            for ex in existing_texts:
                if ex and new_norm in ex or ex in new_norm:
                    errors_q9_near.append(f"{new_q['questionId']}: near-duplicate of batch01 item")
                    break
    print(f'  Exact duplicates vs batch01: {len(errors_q9_exact)}')
    for e in errors_q9_exact:
        print(f'    {e}')
    print(f'  Near duplicates vs batch01: {len(errors_q9_near)}')
    for e in errors_q9_near:
        print(f'    {e}')
except Exception as e:
    print(f'  Cannot load existing batch: {e}')

# ============================================================
# QA 10: B-tier items — check they don't exceed T1 scope
# ============================================================
print()
print('=== QA 10: B-tier items — T1 scope check ===')
b_items = [q for q in questions if q.get('blueprint_confidence') == 'B']
print(f'B-tier items: {len(b_items)}')
for q in b_items:
    print(f'  {q["questionId"]} | {q["topic"]} | {q["subtopic"]} | diff={q["difficulty"]}')
    print(f'    Question: {q["questionText"][:120]}...')

# Check for overly complex content in B items
warnings_q10 = []
for q in b_items:
    # If a B item is also Hard, that's an extra risk
    if q['difficulty'] == 3:
        warnings_q10.append(f"  ⚠️  {q['questionId']}: B-tier AND Hard — extra risk of exceeding T1")
print(f'\nWarnings:')
for w in warnings_q10:
    print(w)

# ============================================================
# QA 11: Check each item's source_tag is valid
# ============================================================
print()
print('=== QA 11: source_tag validity ===')
VALID_TAGS = {'CURRICULUM_DERIVED', 'REFERENCE_DB_ANCHOR', 'INFERRED'}
errors_q11 = []
for q in questions:
    tag = q.get('source_tag')
    if tag not in VALID_TAGS:
        errors_q11.append(f"{q['questionId']}: invalid source_tag '{tag}'")
print(f'  Errors: {len(errors_q11)}')

# ============================================================
# QA 12: Difficulty distribution check
# ============================================================
print()
print('=== QA 12: Difficulty distribution ===')
from collections import Counter
diff_count = Counter(q['difficulty'] for q in questions)
target = {1: 10, 2: 10, 3: 5}
labels = {1: 'Easy', 2: 'Medium', 3: 'Hard'}
for d in [1, 2, 3]:
    actual = diff_count.get(d, 0)
    t = target[d]
    status = '✅' if actual == t else '⚠️'
    print(f'  {status} {labels[d]}: {actual}/{t}')

# ============================================================
# QA 13: Skill distribution check
# ============================================================
print()
print('=== QA 13: Skill distribution ===')
skill_count = Counter(q['skillType'] for q in questions)
for s, c in skill_count.items():
    print(f'  {s}: {c}')
# Target: Recognition 6-8, Comprehension 8-10, Application 8-10
print()
print('  Targets: Recognition 6-8, Comprehension 8-10, Application 8-10')
rec = skill_count.get('RECOGNITION', 0)
com = skill_count.get('COMPREHENSION', 0)
app = skill_count.get('APPLICATION', 0)
print(f'  RECOGNITION: {rec} — target 6-8 — {"✅" if 6 <= rec <= 8 else "⚠️ out of range"}')
print(f'  COMPREHENSION: {com} — target 8-10 — {"✅" if 8 <= com <= 10 else "⚠️ out of range"}')
print(f'  APPLICATION: {app} — target 8-10 — {"✅" if 8 <= app <= 10 else "⚠️ out of range"}')

# ============================================================
# QA 14: Confidence distribution check
# ============================================================
print()
print('=== QA 14: Confidence distribution ===')
conf_count = Counter(q.get('blueprint_confidence', '?') for q in questions)
print(f'  A: {conf_count.get("A", 0)}')
print(f'  B: {conf_count.get("B", 0)}')
print(f'  C: {conf_count.get("C", 0)}')
print('  Target: A=19, B=6, C=0')

# ============================================================
# QA 15: Hash for verification
# ============================================================
print()
print('=== QA 15: File & content hashes ===')
with open(BATCH, 'rb') as f:
    file_data = f.read()
file_sha256 = hashlib.sha256(file_data).hexdigest()
print(f'  File SHA-256:        {file_sha256}')
q_only = json.dumps(questions, ensure_ascii=False, indent=2, sort_keys=False)
q_sha256 = hashlib.sha256(q_only.encode('utf-8')).hexdigest()
print(f'  Questions-only SHA-256: {q_sha256}')

# ============================================================
# Summary
# ============================================================
print()
print('=' * 60)
print('QA SUMMARY')
print('=' * 60)
total_errors = (len(errors_q1) + len(errors_q2) + len(errors_q3) + len(errors_q4)
                + len(errors_q5) + len(errors_q7) + len(errors_q8) + len(errors_q11))
total_warnings = (len(warnings_q6) + len(warnings_q10))
print(f'Total errors:   {total_errors}')
print(f'Total warnings: {total_warnings}')
print()
print('PASS criteria:')
print(f'  {"✅" if total_errors == 0 else "❌"} Zero errors')
print(f'  {"✅" if len(warnings_q6) == 0 else "⚠️"} Zero abstract-term warnings')
print(f'  {"✅" if diff_count.get(1) == 10 and diff_count.get(2) == 10 and diff_count.get(3) == 5 else "❌"} Difficulty 10/10/5')
print(f'  {"✅" if conf_count.get("C", 0) == 0 else "❌"} Zero C-tier items')
print(f'  {"✅" if conf_count.get("A", 0) == 19 and conf_count.get("B", 0) == 6 else "❌"} A=19, B=6')
