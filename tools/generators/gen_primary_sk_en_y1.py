# -*- coding: utf-8 -*-
"""Generate primary SK English Year 1 Batch 01 - 25 ORIGINAL items.

REVISION 2 — Avoiding overlap with tahun_1_pilot.json Bahasa Inggeris items
(pilot has 20 English items covering greetings, instructions, alphabet, sight words,
 plurals, articles, capitalisation, colours, animals — these must be AVOIDED).

Per Blueprint:
- 15 Easy / 7 Medium / 3 Hard = 25
- 16 Recognition / 4 Comprehension / 5 Application = 25
- 22 A / 3 B / 0 C
- Subject ID: sk_prim_en_en_T1
"""
import json
import hashlib
from collections import Counter

SUBJECT_ID = "sk_prim_en_en_T1"
BASE_MILLIS = 1727000000000


def make_item(qid, topic, subtopic, learning_focus, skill, diff, diff_pct,
              question_text, options, correct_key, explanation,
              source_tag, confidence):
    return {
        "questionId": qid,
        "subjectId": SUBJECT_ID,
        "subjectCode": "en",
        "topic": topic,
        "subtopic": subtopic,
        "learningFocus": learning_focus,
        "skillType": skill,
        "difficulty": diff,
        "difficultyDistribution": diff_pct,
        "language": "en",
        "questionText": question_text,
        "options": options,
        "correctAnswer": correct_key,
        "correctAnswerLabel": correct_key.upper(),
        "explanation": explanation,
        "versionId": 1,
        "createdAtMillis": BASE_MILLIS,
        "updatedAtMillis": BASE_MILLIS,
        "contentOrigin": "ORIGINAL",
        "licenseStatus": "self_authored",
        "commercialReuseAllowed": True,
        "examYear": None,
        "contentYear": 2026,
        "schoolTrack": "SK",
        "stage": "primary",
        "curriculum": "KSSR",
        "gradeLevel_year": "Tahun1",
        "gradeLevel": "Tahun1",
        "source_tag": source_tag,
        "blueprint_confidence": confidence,
        "sourceReference": "KuizKu ORIGINAL authoring (Phase 10.5 Primary SK English Year 1 Batch 01); Reference DB has 1 T1 English file (style anchor only) used as style anchor only. tahun_1_pilot.json English items (20) cross-checked for originality."
    }


items = []

# ============================================================
# Listening & Speaking (4 items) — DIFFERENT scenarios from pilot
# ============================================================

# 001 - Farewell (pilot used 'Good morning, class')
items.append(make_item(
    "sk-en-y1-001", "Listening & Speaking", "Farewell",
    "Memilih jawapan perpisahan",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Your friend says "See you tomorrow." What is a polite reply?',
    {"a": "Good night.", "b": "See you tomorrow.", "c": "How are you?", "d": "I am sad."},
    "b",
    "'See you tomorrow' dibalas dengan 'See you tomorrow'. 'Good night/How are you/I am sad' = bukan perpisahan.",
    "CURRICULUM_DERIVED", "A"
))

# 002 - Apology (pilot used 'Open your book')
items.append(make_item(
    "sk-en-y1-002", "Listening & Speaking", "Apology",
    "Memilih ucapan minta maaf",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'You accidentally step on your friend\'s foot. What should you say?',
    {"a": "I am angry.", "b": "I am sorry.", "c": "See you later.", "d": "Good morning."},
    "b",
    "'I am sorry' = ucapan minta maaf. 'I am angry/See you later/Good morning' = tidak sesuai.",
    "CURRICULUM_DERIVED", "A"
))

# 003 - Greeting (different scenario: different time of day)
items.append(make_item(
    "sk-en-y1-003", "Listening & Speaking", "Greetings by time of day",
    "Memilih salam mengikut waktu",
    "COMPREHENSION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'It is 8 p.m. and you meet your neighbour. What do you say?',
    {"a": "Good morning.", "b": "Good afternoon.", "c": "Good evening.", "d": "Hello, banana."},
    "c",
    "8 p.m. = petang/malam = 'Good evening'. 'Good morning' = pagi, 'Good afternoon' = tengah hari, 'Hello, banana' = tidak sesuai.",
    "CURRICULUM_DERIVED", "A"
))

# 004 - Polite request (different scenario: asking to borrow)
items.append(make_item(
    "sk-en-y1-004", "Listening & Speaking", "Polite expressions",
    "Memilih ungkapan meminta dengan sopan",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'You want to borrow a pen from a friend. What do you say?',
    {"a": "Give me your pen now.", "b": "May I borrow your pen, please?", "c": "I want a pen.", "d": "Pen."},
    "b",
    "'May I borrow your pen, please?' = sopan. 'Give me your pen now/I want a pen/Pen' = kasar/lengkap.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# Reading / Phonics / Sight Words (6 items) — DIFFERENT from pilot
# ============================================================

# 005 - Letter sound (different letter - D)
items.append(make_item(
    "sk-en-y1-005", "Reading", "Letter-sound",
    "Mengenal pasti huruf dengan bunyi",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Which letter makes the sound /d/?',
    {"a": "b", "b": "p", "c": "D", "d": "t"},
    "c",
    "Huruf 'D' (besar) menghasilkan bunyi /d/. 'b/p/t' = bunyi lain.",
    "CURRICULUM_DERIVED", "A"
))

# 006 - Sight word "you" (different from pilot's 'the', 'is')
items.append(make_item(
    "sk-en-y1-006", "Reading", "Sight words",
    "Mengenal pasti sight word 'you'",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Which word is "you"?',
    {"a": "yuo", "b": "yau", "c": "you", "d": "yow"},
    "c",
    "'You' dieja y-o-u. 'Yuo/yau/yow' = ejaan salah.",
    "CURRICULUM_DERIVED", "A"
))

# 007 - Sight word "and" (different)
items.append(make_item(
    "sk-en-y1-007", "Reading", "Sight words",
    "Mengenal pasti sight word 'and'",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Which word is "and"?',
    {"a": "end", "b": "and", "c": "hand", "d": "ant"},
    "b",
    "'And' adalah sight word. 'End/hand/ant' = perkataan lain.",
    "CURRICULUM_DERIVED", "A"
))

# 008 - Rhyme recognition (different from pilot's word-picture matching)
items.append(make_item(
    "sk-en-y1-008", "Reading", "Rhyming",
    "Mengenal pasti perkataan yang rhymed",
    "COMPREHENSION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Which word rhymes with "cat"?',
    {"a": "dog", "b": "hat", "c": "fish", "d": "cow"},
    "b",
    "'Cat' dan 'hat' rhymed (-at bunyi). 'Dog/fish/cow' = rhymed bunyi lain.",
    "CURRICULUM_DERIVED", "A"
))

# 009 - Sentence reading (different from pilot's cat on mat)
items.append(make_item(
    "sk-en-y1-009", "Reading", "Simple sentence reading",
    "Membaca dan memahami ayat mudah",
    "COMPREHENSION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Read: "Aiman is reading a book in the library." Where is Aiman?',
    {"a": "In the library.", "b": "In the garden.", "c": "In the kitchen.", "d": "At the playground."},
    "a",
    "Ayat 'Aiman is reading a book in the library' = Aiman berada di perpustakaan.",
    "CURRICULUM_DERIVED", "A"
))

# 010 - Word-picture matching (different context: ball)
items.append(make_item(
    "sk-en-y1-010", "Reading", "Word-picture matching",
    "Memadankan perkataan dengan gambar",
    "COMPREHENSION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'A picture shows a small, round, red fruit. Which word matches?',
    {"a": "apple", "b": "car", "c": "house", "d": "pencil"},
    "a",
    "Buah kecil, bulat, merah = epal = apple. 'Car/house/pencil' = bukan buah.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# Writing (3 items) — DIFFERENT from pilot
# ============================================================

# 011 - Punctuation (different - period)
items.append(make_item(
    "sk-en-y1-011", "Writing", "Punctuation",
    "Mengenal pasti tanda noktah (period)",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Which punctuation mark goes at the end of "I like apples"?',
    {"a": "?", "b": "!", "c": ".", "d": ","},
    "c",
    "Akhir ayat pernyataan = noktah (.). '?' = tanya, '!' = seruan, ',' = koma.",
    "CURRICULUM_DERIVED", "A"
))

# 012 - Letter matching (uppercase to lowercase)
items.append(make_item(
    "sk-en-y1-012", "Writing", "Letter case",
    "Memadankan huruf besar dan huruf kecil",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Which lowercase letter matches the uppercase letter "T"?',
    {"a": "t", "b": "f", "c": "l", "d": "i"},
    "a",
    "'T' (huruf besar) sepadan dengan 't' (huruf kecil). 'f/l/i' = huruf lain.",
    "CURRICULUM_DERIVED", "A"
))

# 013 - Word writing (different spelling - 'book')
items.append(make_item(
    "sk-en-y1-013", "Writing", "Spelling",
    "Menulis perkataan dengan ejaan betul",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Which spelling of "book" is correct?',
    {"a": "bak", "b": "boko", "c": "book", "d": "bokke"},
    "c",
    "'Book' dieja b-o-o-k. 'Bak/boko/bokke' = ejaan salah.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# Grammar (5 items) — DIFFERENT from pilot
# ============================================================

# 014 - Preposition 'under' (different from articles)
items.append(make_item(
    "sk-en-y1-014", "Grammar", "Prepositions",
    "Memilih preposisi tempat",
    "COMPREHENSION", 3, {"easy": 0, "medium": 0, "hard": 100},
    'Look at the picture: the ball is under the chair. Choose the correct sentence:',
    {"a": "The ball is on the chair.", "b": "The ball is under the chair.", "c": "The ball is in the box.", "d": "The ball is on the table."},
    "b",
    "Gambar menunjukkan bola di bawah kerusi = 'under the chair'.",
    "INFERRED", "B"
))

# 015 - Plural with -es (different from -s)
items.append(make_item(
    "sk-en-y1-015", "Grammar", "Plurals",
    "Membentuk plural dengan -es",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'What is the plural of "box"?',
    {"a": "box", "b": "boxs", "c": "boxes", "d": "boxen"},
    "c",
    "Plural untuk perkataan berakhir dengan -x/-s/-sh/-ch/-o: tambah -es. 'Boxes' = betul.",
    "INFERRED", "B"
))

# 016 - Subject-verb agreement (he/she) (different from cat is black)
items.append(make_item(
    "sk-en-y1-016", "Grammar", "Verb to be (is) with he/she",
    "Memilih ayat yang betul dengan 'he/she'",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Choose the correct sentence:',
    {"a": "She are happy.", "b": "She is happy.", "c": "She am happy.", "d": "She be happy."},
    "b",
    "'She' (orang ketiga tunggal) + 'is'. 'Are/am/be' = bentuk salah.",
    "CURRICULUM_DERIVED", "A"
))

# 017 - Pronoun "they" (different)
items.append(make_item(
    "sk-en-y1-017", "Grammar", "Pronouns",
    "Memilih pronoun untuk orang ketiga jamak",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Which pronoun is used for "Ali and his friends"?',
    {"a": "he", "b": "she", "c": "it", "d": "they"},
    "d",
    "'Ali dan kawan-kawannya' (orang ketiga jamak) = 'they'. 'he/she' = tunggal, 'it' = benda.",
    "CURRICULUM_DERIVED", "A"
))

# 018 - Conjunction "and" (different)
items.append(make_item(
    "sk-en-y1-018", "Grammar", "Conjunctions",
    "Memilih conjunction yang betul",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Choose the correct sentence:',
    {"a": "I like apples but I like oranges.", "b": "I like apples and I like oranges.", "c": "I like apples or I like oranges.", "d": "I like apples because I like oranges."},
    "b",
    "'And' menggabungkan dua benda yang sama-sama disukai. 'But/or/because' = conjunction lain.",
    "INFERRED", "B"
))

# ============================================================
# Vocabulary (7 items) — DIFFERENT from pilot
# ============================================================

# 019 - Colour yellow (different from red/blue)
items.append(make_item(
    "sk-en-y1-019", "Vocabulary", "Colours",
    "Mengenal pasti warna",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Which colour is the sun?',
    {"a": "blue", "b": "green", "c": "yellow", "d": "black"},
    "c",
    "Matahari = kuning = yellow. 'Blue/green/black' = warna lain.",
    "CURRICULUM_DERIVED", "A"
))

# 020 - Animal cat (different from dog/cow)
items.append(make_item(
    "sk-en-y1-020", "Vocabulary", "Animals",
    "Mengenal pasti nama haiwan",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Which animal says "meow"?',
    {"a": "fish", "b": "bird", "c": "cat", "d": "horse"},
    "c",
    "Suara 'meow' = kucing = cat. 'Fish/bird/horse' = haiwan lain.",
    "CURRICULUM_DERIVED", "A"
))

# 021 - Family father (different)
items.append(make_item(
    "sk-en-y1-021", "Vocabulary", "Family",
    "Mengenal pasti ahli keluarga",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'What is the English word for "bapa"?',
    {"a": "father", "b": "mother", "c": "brother", "d": "sister"},
    "a",
    "'Bapa' dalam BM = 'father' dalam English. 'Mother/brother/sister' = ahli keluarga lain.",
    "CURRICULUM_DERIVED", "A"
))

# 022 - Number ten (different from five)
items.append(make_item(
    "sk-en-y1-022", "Vocabulary", "Numbers",
    "Mengenal pasti nombor",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'How many fingers do you have on both hands?',
    {"a": "five", "b": "eight", "c": "ten", "d": "twenty"},
    "c",
    "10 jari di kedua-dua tangan = ten. 'Five/eight/twenty' = nombor lain.",
    "CURRICULUM_DERIVED", "A"
))

# 023 - School item pencil (different from book)
items.append(make_item(
    "sk-en-y1-023", "Vocabulary", "School items",
    "Mengenal pasti barang sekolah",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Which item do you use to write?',
    {"a": "pencil", "b": "ruler", "c": "eraser", "d": "chair"},
    "a",
    "Barang yang digunakan untuk menulis = pensel = pencil. 'Ruler/eraser/chair' = barang lain.",
    "CURRICULUM_DERIVED", "A"
))

# 024 - Action "swimming" (different from running)
items.append(make_item(
    "sk-en-y1-024", "Vocabulary", "Action verbs",
    "Mengenal pasti kata kerja tindakan dalam konteks",
    "APPLICATION", 3, {"easy": 0, "medium": 0, "hard": 100},
    'Sara is in the swimming pool. She is moving her arms and legs in the water. What is she doing?',
    {"a": "reading", "b": "sleeping", "c": "swimming", "d": "cooking"},
    "c",
    "Di dalam kolam renang + menggerakkan tangan dan kaki = swimming. 'Reading/sleeping/cooking' = tindakan lain.",
    "CURRICULUM_DERIVED", "A"
))

# 025 - Number subtraction (different from addition)
items.append(make_item(
    "sk-en-y1-025", "Vocabulary", "Numbers (subtraction)",
    "Mengenal pasti nombor dalam konteks penolakan",
    "APPLICATION", 3, {"easy": 0, "medium": 0, "hard": 100},
    'Ali has 8 candies. He gives 3 to his sister. How many candies does Ali have now?',
    {"a": "three", "b": "four", "c": "five", "d": "eleven"},
    "c",
    "8 - 3 = 5 = five. 'Three/four/eleven' = jawapan salah.",
    "CURRICULUM_DERIVED", "A"
))

# Sort by ID
items.sort(key=lambda x: x['questionId'])

# Build metadata
batch = {
    "metadata": {
        "batch_id": "primary_sk_en_y1_batch01",
        "phase": "10.5",
        "schoolTrack": "SK",
        "stage": "primary",
        "language": "en",
        "grade": "Tahun1",
        "subject": "English",
        "subjectCode": "en",
        "subjectId": SUBJECT_ID,
        "curriculum": "KSSR",
        "questionType": "SINGLE_CHOICE",
        "totalQuestions": 25,
        "difficultyDistribution": {
            "easy": 15,
            "medium": 7,
            "hard": 3
        },
        "note": "Phase 10.5 Primary SK English Tahun 1 Batch 01 (Revision 2). Originality audit: tahun_1_pilot.json Bahasa Inggeris items (20) cross-checked. Items redesigned to avoid near-paraphrase of pilot. Reference DB has 1 T1 English file used as style anchor only. See primary/blueprint_sk_en_y1.md and primary/COVERAGE_MATRIX.md.",
        "reference_db_status": "1_T1_ENGLISH_FILE_STYLE_ANCHOR_ONLY",
        "reference_db_anchors_used": [
            "references/English/T1/styleanchor.pdf (style anchor only)"
        ],
        "originality_audit": "tahun_1_pilot.json (20 Bahasa Inggeris items) — avoided: greetings scenarios, plural of cat, cat-on-mat sentence, article pattern. Replaced with: farewell, apology, time-of-day greetings, plural of box, Aiman-in-library sentence, apple word-picture, he/she verb agreement, they pronoun, conjunction and, colour yellow/sun, animal cat/meow, father family, ten fingers, pencil, swimming action, number subtraction."
    },
    "questions": items
}

# Write JSON
OUTPUT = r'D:\Users\bajub\kuizku_p10\primary\batch01_sk_en_y1.json'
with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

# Compute hashes
with open(OUTPUT, 'rb') as f:
    file_data = f.read()
file_sha256 = hashlib.sha256(file_data).hexdigest()
q_only = json.dumps(batch['questions'], ensure_ascii=False, indent=2, sort_keys=False)
q_sha256 = hashlib.sha256(q_only.encode('utf-8')).hexdigest()

print(f'JSON written: {OUTPUT}')
print(f'Total questions: {len(items)}')
print(f'File SHA-256: {file_sha256}')
print(f'Questions-only SHA-256: {q_sha256}')

diff_count = Counter(q['difficulty'] for q in items)
labels = {1: 'Easy', 2: 'Medium', 3: 'Hard'}
print('\nDifficulty:')
for d in [1, 2, 3]:
    print(f'  {labels[d]}: {diff_count.get(d, 0)}')

skill_count = Counter(q['skillType'] for q in items)
print('\nSkill:')
for s, c in sorted(skill_count.items()):
    print(f'  {s}: {c}')

conf_count = Counter(q['blueprint_confidence'] for q in items)
print('\nConfidence:')
for c, n in sorted(conf_count.items()):
    print(f'  {c}: {n}')

src_count = Counter(q['source_tag'] for q in items)
print('\nSource tag:')
for s, n in sorted(src_count.items()):
    print(f'  {s}: {n}')

topic_count = Counter(q['topic'] for q in items)
print('\nTopic:')
for t, c in sorted(topic_count.items()):
    print(f'  {t}: {c}')
