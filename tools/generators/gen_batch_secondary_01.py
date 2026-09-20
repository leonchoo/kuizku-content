# -*- coding: utf-8 -*-
"""Generate batch_secondary_01_sk_bm_t1.json — 25 original T1 BM items."""
import json
import hashlib
import os
from collections import Counter

INT32_MAX = 2**31 - 1
BASE_MILLIS = 1727000000000


def make_item(qid, topic, subtopic, learning_focus, skill, diff, diff_pct,
              question_text, options, correct_key, explanation,
              source_tag, confidence):
    return {
        "questionId": qid,
        "subjectId": "sk_sec_bm_ms_T1",
        "subjectCode": "bm",
        "topic": topic,
        "subtopic": subtopic,
        "learningFocus": learning_focus,
        "skillType": skill,
        "difficulty": diff,
        "difficultyDistribution": diff_pct,
        "language": "ms",
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
        "curriculum": "KSSM",
        "gradeLevel_year": "Tingkatan1",
        "gradeLevel": "Tingkatan1",
        "source_tag": source_tag,
        "blueprint_confidence": confidence,
        "sourceReference": "KuizKu ORIGINAL authoring (Phase 10.5 Batch secondary_01_sk_bm_t1); Reference DB has no T1 BM source (only T2/T3/T5 secondary BM as difficulty anchor)"
    }


items = []

# ============================================================
# Passage 1 — Narrative for items 11, 12, 15, 16, 17
# ============================================================
passage_1 = (
    "Setiap pagi, Aiman bangun awal. Dia membantu ibunya di dapur. "
    "Ibu selalu tersenyum apabila melihat Aiman rajin. Selepas sarapan, "
    "Aiman berjalan ke sekolah bersama adiknya. Di sekolah, dia belajar "
    "dengan tekun. Guru-gurunya suka akan sikapnya yang baik. Pada petang, "
    "Aiman bermain bola di padang berdekatan rumahnya. Dia gembira kerana "
    "hari itu berjalan dengan lancar."
)

# Item 11
items.append(make_item(
    "v5-t1-bm-sec-011",
    "Pemahaman", "Petikan naratif - literal (siapa)",
    "Mengenal pasti watak utama",
    "COMPREHENSION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Baca petikan:\n\n"' + passage_1 + '"\n\nSiapakah watak utama dalam petikan di atas?',
    {"a": "Ibu Aiman", "b": "Adik Aiman", "c": "Guru Aiman", "d": "Aiman"},
    "d",
    "Aiman disebut sebagai watak yang melakukan pelbagai aktiviti dalam petikan - bangun awal, membantu ibu, berjalan ke sekolah, belajar, bermain bola.",
    "CURRICULUM_DERIVED", "A"
))

# Item 12
items.append(make_item(
    "v5-t1-bm-sec-012",
    "Pemahaman", "Petikan naratif - literal (di mana)",
    "Mengenal pasti tempat",
    "COMPREHENSION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Baca petikan:\n\n"' + passage_1 + '"\n\nDi manakah Aiman bermain bola pada petang?',
    {"a": "Di dapur", "b": "Di sekolah", "c": "Di padang berdekatan rumahnya", "d": "Di dalam rumah"},
    "c",
    "Petikan menyatakan 'Aiman bermain bola di padang berdekatan rumahnya' - padang berdekatan rumah.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# Passage 2 — Descriptive for items 13, 14
# ============================================================
passage_2 = (
    "Kampung Tanjung Selamat terletak di tepi laut. Rumah-rumah penduduknya "
    "berwarna-warni dan tersusun rapi. Pantai kampung ini sangat bersih. "
    "Air lautnya jernih dan biru. Pokok-pokok kelapa tumbuh tinggi di tepi "
    "pantai. Pada waktu pagi, nelayan turun ke laut untuk menangkap ikan. "
    "Suasana kampung ini tenang dan damai. Ramai pelawat datang pada hujung "
    "minggu untuk menikmati keindahan kampung."
)

# Item 13
items.append(make_item(
    "v5-t1-bm-sec-013",
    "Pemahaman", "Petikan deskriptif - ciri fizikal",
    "Mengenal pasti ciri fizikal tempat",
    "COMPREHENSION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Baca petikan:\n\n"' + passage_2 + '"\n\nApakah warna air laut di Kampung Tanjung Selamat?',
    {"a": "Putih", "b": "Hitam", "c": "Biru dan jernih", "d": "Merah"},
    "c",
    "Petikan menyatakan 'Air lautnya jernih dan biru' - biru dan jernih.",
    "CURRICULUM_DERIVED", "A"
))

# Item 14
items.append(make_item(
    "v5-t1-bm-sec-014",
    "Pemahaman", "Petikan deskriptif - suasana",
    "Mengenal pasti suasana tempat",
    "COMPREHENSION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Baca petikan:\n\n"' + passage_2 + '"\n\nBagaimanakah suasana di Kampung Tanjung Selamat?',
    {"a": "Bising dan huru-hara", "b": "Tenang dan damai", "c": "Gelap dan sunyi", "d": "Penuh dengan kenderaan"},
    "b",
    "Petikan menyatakan 'Suasana kampung ini tenang dan damai'.",
    "CURRICULUM_DERIVED", "A"
))

# Item 15
items.append(make_item(
    "v5-t1-bm-sec-015",
    "Pemahaman", "Maksud ungkapan dalam petikan",
    "Memahami ungkapan harian",
    "COMPREHENSION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Baca petikan:\n\n"' + passage_1 + '"\n\nApakah maksud ungkapan "hari itu berjalan dengan lancar"?',
    {"a": "Hari itu hujan lebat", "b": "Hari itu berjalan tanpa masalah", "c": "Hari itu sangat membosankan", "d": "Hari itu penuh dengan masalah"},
    "b",
    "'Berjalan dengan lancar' bermaksud berjalan tanpa masalah atau tanpa halangan.",
    "CURRICULUM_DERIVED", "A"
))

# Item 16
items.append(make_item(
    "v5-t1-bm-sec-016",
    "Pemahaman", "Petikan naratif - inferens",
    "Membuat inferens mudah",
    "APPLICATION", 3, {"easy": 0, "medium": 0, "hard": 100},
    'Baca petikan:\n\n"' + passage_1 + '"\n\nApakah perasaan Aiman pada hari itu?',
    {"a": "Sedih", "b": "Marah", "c": "Gembira", "d": "Takut"},
    "c",
    "Petikan menyatakan 'Dia gembira kerana hari itu berjalan dengan lancar' - perasaan Aiman ialah gembira.",
    "CURRICULUM_DERIVED", "B"
))

# Item 17
items.append(make_item(
    "v5-t1-bm-sec-017",
    "Pemahaman", "Nilai murni dalam petikan",
    "Mengenal pasti nilai murni",
    "APPLICATION", 3, {"easy": 0, "medium": 0, "hard": 100},
    'Baca petikan:\n\n"' + passage_1 + '"\n\nApakah nilai murni yang terdapat dalam petikan di atas?',
    {"a": "Malas", "b": "Rajin dan sayang ibu", "c": "Tamak", "d": "Pemberontak"},
    "b",
    "Aiman bangun awal, membantu ibunya di dapur, dan belajar dengan tekun. Nilai murni yang jelas ialah rajin dan sayang ibu.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 1 - T1BM-TA-01 Kata nama am vs khas
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-001",
    "Tatabahasa", "Kata nama am vs kata nama khas",
    "Membezakan kata nama am dan khas",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Antara perkataan berikut, yang manakah merupakan kata nama khas?',
    {"a": "rumah", "b": "sekolah", "c": "Sekolah Kebangsaan Tanjung", "d": "kereta"},
    "c",
    "Kata nama khas menamakan sesuatu yang khusus dan biasanya ditulis dengan huruf besar. 'Sekolah Kebangsaan Tanjung' ialah nama khusus.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 2 - T1BM-TA-02 Kata ganti nama pertama/kedua
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-002",
    "Tatabahasa", "Kata ganti nama diri pertama / kedua",
    "Mengenal pasti kata ganti nama",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Antara perkataan berikut, yang manakah merupakan kata ganti nama diri pertama?',
    {"a": "awak", "b": "saya", "c": "dia", "d": "mereka"},
    "b",
    "'Saya' ialah kata ganti nama diri pertama (orang yang bercakap). 'Awak' = kedua, 'dia/mereka' = ketiga.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 3 - T1BM-TA-03 Kata ganti nama ketiga formal
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-003",
    "Tatabahasa", "Kata ganti nama diri ketiga (formal vs tak formal)",
    "Memilih kata ganti nama mengikut konteks",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Kamu menulis surat rasmi kepada guru besar. Perkataan yang manakah paling sesuai digunakan untuk merujuk guru besar?',
    {"a": "dia", "b": "beliau", "c": "awak", "d": "kamu"},
    "b",
    "Dalam surat rasmi, 'beliau' digunakan untuk merujuk orang yang dihormati seperti guru besar. 'Dia' kurang formal; 'awak/kamu' untuk orang kedua.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 4 - T1BM-TA-05 Imbuhan awalan meN-
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-004",
    "Tatabahasa", "Imbuhan awalan meN-",
    "Membentuk kata kerja daripada kata nama",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Kata nama "minum" boleh menjadi kata kerja jika ditambah imbuhan awalan. Yang manakah betul?',
    {"a": "meN-minum", "b": "pem-minum", "c": "minum-an", "d": "per-minum"},
    "a",
    "Awalan 'meN-' bergabung dengan kata nama yang bermula dengan huruf 'm', 'n', 'ny', 'ng', 'p', 'b', 'f', 'v' menjadi 'meN-'. 'Minum' -> 'meminum'.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 5 - T1BM-TA-08 Kata hubung
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-005",
    "Tatabahasa", "Kata hubung",
    "Menggabungkan ayat dengan kata hubung",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Pilih kata hubung yang sesuai untuk menggabungkan dua ayat berikut: "Ahmad belajar bersungguh-sungguh. __________ dia mendapat keputusan cemerlang dalam peperiksaan."',
    {"a": "atau", "b": "tetapi", "c": "kerana", "d": "walaupun"},
    "c",
    "'Kerana' menunjukkan sebab. 'Ahmad belajar bersungguh-sungguh' sebab 'dia mendapat keputusan cemerlang'.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 6 - T1BM-TA-09 Kata sendi
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-006",
    "Tatabahasa", "Kata sendi",
    "Memilih kata sendi yang sesuai",
    "APPLICATION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Pilih kata sendi yang betul untuk melengkapkan ayat: "Buku itu berada __________ atas meja."',
    {"a": "dari", "b": "pada", "c": "ke", "d": "kepada"},
    "b",
    "'Pada' digunakan untuk menunjukkan lokasi atau tempat. 'Buku itu berada pada atas meja' = lokasi tepat.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 7 - T1BM-TA-10 Penjodoh bilangan
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-007",
    "Tatabahasa", "Penjodoh bilangan",
    "Memilih penjodoh bilangan yang sesuai",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Pilih penjodoh bilangan yang sesuai: "Saya melihat seekor __________ di tepi jalan."',
    {"a": "kerusi", "b": "kucing", "c": "rumah", "d": "buku"},
    "b",
    "'Seekor' digunakan untuk haiwan. 'Seekor kucing' = betul.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 8 - T1BM-TA-13 Peribahasa asas
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-008",
    "Tatabahasa", "Peribahasa asas",
    "Memahami maksud peribahasa",
    "COMPREHENSION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Apakah maksud peribahasa "berat sama dipikul, ringan sama dijinjing"?',
    {"a": "Bekerja bersendirian", "b": "Tolong-menolong dalam melakukan sesuatu kerja", "c": "Membahagikan barang dengan adil", "d": "Bekerja keras sendirian"},
    "b",
    "Peribahasa ini bermaksud tolong-menolong dalam melakukan sesuatu kerja bersama-sama.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 9 - T1BM-TA-14 Kata tugas dalam ayat majmuk
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-009",
    "Tatabahasa", "Kata tugas dalam ayat majmuk",
    "Mencantum dua ayat dengan kata hubung",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Ayat manakah yang betul menggunakan kata hubung "tetapi"?',
    {"a": "Saya suka makan nasi tetapi saya tidak suka minum teh.", "b": "Saya suka makan nasi dan saya tidak suka minum teh.", "c": "Saya suka makan nasi atau saya tidak suka minum teh.", "d": "Saya suka makan nasi kerana saya tidak suka minum teh."},
    "a",
    "'Tetapi' menunjukkan pertentangan. 'Suka nasi' dan 'tidak suka minum teh' = pertentangan.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 10 - T1BM-TA-06 Imbuhan akhiran -kan (B)
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-010",
    "Tatabahasa", "Imbuhan akhiran -kan",
    "Membentuk kata kerja transitif",
    "APPLICATION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Kata kerja "membersih" boleh ditambah imbuhan akhiran untuk membentuk kata kerja transitif. Yang manakah betul?',
    {"a": "membersih", "b": "membersihkan", "c": "membersihi", "d": "membersihan"},
    "b",
    "Akhiran '-kan' membentuk kata kerja transitif. 'Membersih' -> 'membersihkan' (membuat sesuatu menjadi bersih).",
    "CURRICULUM_DERIVED", "B"
))

# ============================================================
# ITEM 18 - T1BM-PN-01 Format karangan
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-018",
    "Penulisan", "Format karangan",
    "Susunan perenggan karangan",
    "APPLICATION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Apakah perenggan yang terdapat dalam sebuah karangan jenis naratif?',
    {"a": "Hanya pendahuluan", "b": "Pendahuluan, isi, dan penutup", "c": "Hanya isi dan penutup", "d": "Hanya penutup"},
    "b",
    "Karangan naratif standard mempunyai tiga perenggan: pendahuluan, isi, dan penutup.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 19 - T1BM-PN-02 Betulkan ayat songsang
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-019",
    "Penulisan", "Betulkan ayat songsang",
    "Membetulkan susunan ayat",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Antara ayat berikut, yang manakah betul susunannya?',
    {"a": "Semalam ke pasar ibu saya pergi.", "b": "Semalam ibu saya pergi ke pasar.", "c": "Pergi ke pasar ibu saya semalam.", "d": "Ibu saya semalam pergi ke pasar."},
    "b",
    "Susunan ayat yang betul mengikut struktur S-P-K: 'Ibu saya pergi ke pasar' + 'Semalam' (keterangan masa).",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 20 - T1BM-PN-02 Betulkan ayat (pilihan terbaik)
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-020",
    "Penulisan", "Betulkan struktur ayat",
    "Membetulkan struktur ayat gramatis",
    "APPLICATION", 3, {"easy": 0, "medium": 0, "hard": 100},
    'Antara ayat berikut, yang manakah paling gramatis (betul struktur)?',
    {"a": "Dia pergi sekolah dengan basikal.", "b": "Dengan basikal dia pergi sekolah.", "c": "Sekolah dia pergi dengan basikal.", "d": "Pergi sekolah dengan basikal dia."},
    "a",
    "'Dia pergi sekolah dengan basikal' mengikut struktur S-P-K + Keterangan Cara.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 21 - T1BM-KK-01 Sinonim (B)
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-021",
    "Kosa Kata", "Sinonim",
    "Mencari persamaan makna",
    "RECOGNITION", 1, {"easy": 100, "medium": 0, "hard": 0},
    'Apakah sinonim bagi perkataan "rumah"?',
    {"a": "kereta", "b": "kediaman", "c": "sekolah", "d": "kedai"},
    "b",
    "Sinonim 'rumah' = 'kediaman'.",
    "INFERRED", "B"
))

# ============================================================
# ITEM 22 - T1BM-KK-02 Antonim (B)
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-022",
    "Kosa Kata", "Antonim",
    "Mencari lawan makna",
    "RECOGNITION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Apakah antonim bagi perkataan "besar"?',
    {"a": "tinggi", "b": "kecil", "c": "panjang", "d": "lebar"},
    "b",
    "Antonim 'besar' = 'kecil'.",
    "INFERRED", "B"
))

# ============================================================
# ITEM 23 - T1BM-KK-04 Ungkapan sesuai konteks
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-023",
    "Kosa Kata", "Ungkapan sesuai konteks",
    "Memilih ungkapan yang sesuai mengikut konteks",
    "APPLICATION", 3, {"easy": 0, "medium": 0, "hard": 100},
    'Rakan kamu kelihatan sedih kerana gagal dalam peperiksaan. Ungkapan manakah yang paling sesuai untuk kamu gunakan?',
    {"a": "Tabik spring!", "b": "Saya simpati dengan kamu.", "c": "Syabas!", "d": "Teruskan sahaja!"},
    "b",
    "'Saya simpati dengan kamu' untuk menyatakan rasa sedih bersama seseorang.",
    "CURRICULUM_DERIVED", "A"
))

# ============================================================
# ITEM 24 - T1BM-KB-01 Pilih ayat sesuai场合 (B)
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-024",
    "Kemahiran Berbahasa", "Ayat sesuai场合 (rasmi / tak rasmi)",
    "Memilih ayat sesuai场合",
    "APPLICATION", 3, {"easy": 0, "medium": 0, "hard": 100},
    'Kamu ingin menjemput kawan kamu bermain badminton pada hujung minggu. Ayat yang manakah paling sesuai?',
    {"a": "Dengan hormatnya, saya ingin menjemput Tuan untuk bermain badminton.", "b": "Hei, jom main badminton petang ni!", "c": "Saya berharap agar Tuan sudi bermain badminton dengan saya.", "d": "Untuk perhatian Tuan, bermain badminton akan saya cadangkan."},
    "b",
    "Antara kawan sebaya, bahasa tak rasmi sesuai: 'Hei, jom main badminton petang ni!'.",
    "INFERRED", "B"
))

# ============================================================
# ITEM 25 - T1BM-TA-04 Kata kerja transitif vs tak transitif (B)
# ============================================================
items.append(make_item(
    "v5-t1-bm-sec-025",
    "Tatabahasa", "Kata kerja transitif vs tak transitif",
    "Membezakan kata kerja transitif",
    "APPLICATION", 2, {"easy": 0, "medium": 100, "hard": 0},
    'Antara ayat berikut, yang manakah menggunakan kata kerja transitif?',
    {"a": "Ahmad tidur.", "b": "Siti membaca buku.", "c": "Kanak-kanak itu berlari.", "d": "Bayi itu menangis."},
    "b",
    "Kata kerja transitif memerlukan objek. 'Siti membaca buku' - 'buku' ialah objek.",
    "CURRICULUM_DERIVED", "B"
))

# Sort by ID
items.sort(key=lambda x: x['questionId'])

# Build full batch
batch = {
    "metadata": {
        "batch_id": "batch_secondary_01_sk_bm_t1",
        "phase": "10.5",
        "schoolTrack": "SK",
        "language": "ms",
        "grade": "Tingkatan1",
        "subject": "Bahasa Melayu",
        "subjectCode": "bm",
        "subjectId": "sk_sec_bm_ms_T1",
        "curriculum": "KSSM",
        "questionType": "SINGLE_CHOICE",
        "totalQuestions": 25,
        "difficultyDistribution": {
            "easy": 10,
            "medium": 10,
            "hard": 5
        },
        "note": "Phase 10.5 Batch secondary_01_sk_bm_t1 - T1 BM original authoring. Reference DB does NOT contain T1 BM source questions. T2/T3 used only as style/difficulty anchor. Primary T5/T6 NOT used as T1 source. See secondary_t1_bm_blueprint.md and secondary_t1_bm_scope_review.md for full source audit.",
        "reference_db_status": "NO_T1_BM_FILES",
        "reference_db_anchors_used": [
            "references/BM/T2/mid-year-styleanchor.docx",
            "references/BM/T2/exam-format.docx",
            "references/BM/T3/difficulty-ceiling.docx",
            "references/BM/T3/sample-format.docx.docx",
            "references/BM/T5/difficulty-reference.docx",
            "references/BM/T2/penjodoh-styleref.pdf (style anchor only)"
        ]
    },
    "questions": items
}

# Write JSON
OUTPUT = r'D:\Users\bajub\kuizku_p10\batch_secondary_01_sk_bm_t1.json'
with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

# Compute hashes
with open(OUTPUT, 'rb') as f:
    file_data = f.read()
file_sha256 = hashlib.sha256(file_data).hexdigest()

# Questions-only hash
questions_only = json.dumps(batch['questions'], ensure_ascii=False, indent=2, sort_keys=False)
q_sha256 = hashlib.sha256(questions_only.encode('utf-8')).hexdigest()

print(f'JSON written: {OUTPUT}')
print(f'File SHA-256: {file_sha256}')
print(f'Questions-only SHA-256: {q_sha256}')
print(f'Total questions: {len(items)}')

# Difficulty breakdown
print()
print('Difficulty breakdown:')
diff_count = Counter()
skill_count = Counter()
conf_count = Counter()
source_tag_count = Counter()
for it in items:
    diff_count[it['difficulty']] += 1
    skill_count[it['skillType']] += 1
    conf_count[it['blueprint_confidence']] += 1
    source_tag_count[it['source_tag']] += 1

for d in sorted(diff_count.keys()):
    label = {1: 'Easy', 2: 'Medium', 3: 'Hard'}[d]
    print(f'  {label}: {diff_count[d]}')

print()
print('Skill breakdown:')
for s, c in skill_count.items():
    print(f'  {s}: {c}')

print()
print('Confidence breakdown:')
for cf, c in conf_count.items():
    print(f'  {cf}: {c}')

print()
print('Source tag breakdown:')
for st, c in source_tag_count.items():
    print(f'  {st}: {c}')

# Topic breakdown
print()
print('Topic breakdown:')
topic_count = Counter()
for it in items:
    topic_count[it['topic']] += 1
for t, c in topic_count.items():
    print(f'  {t}: {c}')

# List question IDs in order
print()
print('Question IDs in order:')
for it in items:
    print(f'  {it["questionId"]} | {it["topic"]} | {it["subtopic"]} | diff={it["difficulty"]} | skill={it["skillType"]} | conf={it["blueprint_confidence"]}')
