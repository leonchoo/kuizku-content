# -*- coding: utf-8 -*-
"""Apply audit fixes to batch_secondary_01_sk_bm_t1.json.

Fixes:
1. subjectId bug: '***' -> 'sk_sec_bm_ms_T1' (all 25 items)
2. Skill reclassification (5 items): 011, 012, 013, 014, 018 -> RECOGNITION
3. Item 016 content: change question to genuine inference
4. Item 020 difficulty: demote from Hard (3) to Medium (2)
"""
import json
import hashlib

PATH = r'D:\Users\bajub\kuizku_p10\batch_secondary_01_sk_bm_t1.json'
with open(PATH) as f:
    batch = json.load(f)

questions = batch['questions']

# Fix 1: subjectId for ALL items
SUBJECT_ID = "sk_sec_bm_ms_T1"
for q in questions:
    q['subjectId'] = SUBJECT_ID
print(f'Fix 1: All 25 items subjectId -> {SUBJECT_ID}')

# Fix 2: Skill reclassification (verbatim lookup)
SKILL_RECLASS = {
    'v5-t1-bm-sec-011': 'RECOGNITION',
    'v5-t1-bm-sec-012': 'RECOGNITION',
    'v5-t1-bm-sec-013': 'RECOGNITION',
    'v5-t1-bm-sec-014': 'RECOGNITION',
    'v5-t1-bm-sec-018': 'RECOGNITION',
}
for q in questions:
    if q['questionId'] in SKILL_RECLASS:
        old = q['skillType']
        new = SKILL_RECLASS[q['questionId']]
        q['skillType'] = new
        # Update difficultyDistribution if skill change implies rebalancing
        if old == 'COMP' and new == 'REC':
            # Update distribution accordingly
            if q['difficulty'] == 1:
                q['difficultyDistribution'] = {"easy": 100, "medium": 0, "hard": 0}
            elif q['difficulty'] == 2:
                q['difficultyDistribution'] = {"easy": 0, "medium": 100, "hard": 0}
            elif q['difficulty'] == 3:
                q['difficultyDistribution'] = {"easy": 0, "medium": 0, "hard": 100}
        print(f'Fix 2: {q["questionId"]} skill: {old} -> {new}')

# Fix 3: Item 016 — change question to genuine inference
# Original: "Apakah perasaan Aiman pada hari itu?" -> verbatim answer "Gembira"
# New: "Apakah sebab Aiman gembira pada hari itu?"
#       Answer: "Kerana hari itu berjalan dengan lancar" (requires inference)
item016 = next(q for q in questions if q['questionId'] == 'v5-t1-bm-sec-016')
item016['questionText'] = (
    'Baca petikan:\n\n'
    '"Setiap pagi, Aiman bangun awal. Dia membantu ibunya di dapur. '
    'Ibu selalu tersenyum apabila melihat Aiman rajin. Selepas sarapan, '
    'Aiman berjalan ke sekolah bersama adiknya. Di sekolah, dia belajar '
    'dengan tekun. Guru-gurunya suka akan sikapnya yang baik. Pada petang, '
    'Aiman bermain bola di padang berdekatan rumahnya. Dia gembira kerana '
    'hari itu berjalan dengan lancar."\n\n'
    'Mengapakah Aiman gembira pada hari itu?'
)
item016['options'] = {
    "a": "Kerana dia bermain bola pada petang.",
    "b": "Kerana hari itu berjalan dengan lancar.",
    "c": "Kerana gurunya sayang akan dia.",
    "d": "Kerana adiknya berjalan bersamanya."
}
item016['correctAnswer'] = 'b'
item016['correctAnswerLabel'] = 'B'
item016['explanation'] = (
    'Petikan menyatakan "Dia gembira kerana hari itu berjalan dengan lancar" - '
    'sebab Aiman gembira ialah kerana hari itu berjalan dengan lancar. '
    'Pilihan a/c/d mengandungi maklumat benar tetapi BUNCA SEBAB yang SALAH. '
    'Mengapakah = memerlukan sebab, bukan peristiwa.'
)
print(f'Fix 3: 016 question rewritten for genuine inference')

# Fix 4: Item 020 difficulty 3 -> 2 (too obviously correct for Hard)
item020 = next(q for q in questions if q['questionId'] == 'v5-t1-bm-sec-020')
item020['difficulty'] = 2
item020['difficultyDistribution'] = {"easy": 0, "medium": 100, "hard": 0}
print(f'Fix 4: 020 difficulty 3 -> 2 (distractors too obvious for Hard)')

# Write back
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

# Compute hashes
with open(PATH, 'rb') as f:
    file_data = f.read()
file_sha256 = hashlib.sha256(file_data).hexdigest()
q_only = json.dumps(batch['questions'], ensure_ascii=False, indent=2, sort_keys=False)
q_sha256 = hashlib.sha256(q_only.encode('utf-8')).hexdigest()

print(f'\nNew file SHA-256: {file_sha256}')
print(f'New questions-only SHA-256: {q_sha256}')
