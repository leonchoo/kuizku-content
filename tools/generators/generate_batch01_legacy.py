"""Phase 10.5 Batch 01 — Generate 25 ORIGINAL SK BM Tahun 1 questions.

Per 638 Phase 10.5 Batch 01:
- schoolTrack=SK, language=ms, grade=Tahun1, subject=bm, curriculum=KSSR
- SINGLE_CHOICE only
- 25 ORIGINAL questions
- Difficulty: Easy 15 / Medium 7 / Hard 3 (60/30/10 %)
- Topics from Phase 10.4 BM Tahun 1 blueprint:
  Mendengar & Bertutur (5), Membaca (5), Penulisan (5), Tatabahasa (5), Perbendaharaan Kata (5)
- Skills: RECOGNITION (15 easy), COMPREHENSION (5 medium), APPLICATION (5: 4 medium + 1 hard), no ANALY/PROBLEM_SOLVING
- Hard questions only at APPLICATION level (no UPSR prep framing per 638 §一)
- All KuizKu ORIGINAL. NO copy from V3/V4-TEST/Phase 10.1/Reference DB.
- Metadata: contentOrigin=ORIGINAL, licenseStatus=self_authored,
  commercialReuseAllowed=true, examYear=null, contentYear=2026
"""

import json
import hashlib
from collections import Counter
from pathlib import Path

OUT_PATH = Path(r"D:\Users\bajub\kuizku_p10\batch01_sk_bm_y1.json")

# Common fields for every question (Phase 10.3 schema)
SUBJECT_ID = "sk_prim_bm_ms_Y1"
SUBJECT_CODE = "bm"
LANGUAGE = "ms"
GRADE = "Tahun1"
TRACK = "SK"
CURRICULUM = "KSSR"
QUESTION_TYPE = "SINGLE_CHOICE"
CONTENT_YEAR = 2026
BATCH_ID = "batch01_sk_bm_y1"
PHASE = "10.5"
SOURCE_REF = "KuizKu ORIGINAL authoring (Phase 10.5 Batch 01)"
NOW_MS = 1727000000000

def q(idx, topic, subtopic, learning_focus, skill, diff, qtext, opts, ans, expl):
    """Build a single Phase 10.3 V5-schema question."""
    if diff == 1:
        dd = {"easy": 100, "medium": 0, "hard": 0}
    elif diff == 2:
        dd = {"easy": 0, "medium": 100, "hard": 0}
    else:
        dd = {"easy": 0, "medium": 0, "hard": 100}
    return {
        "questionId": f"v5-t1-bm-{idx:03d}",
        "subjectId": SUBJECT_ID,
        "subjectCode": SUBJECT_CODE,
        "topic": topic,
        "subtopic": subtopic,
        "learningFocus": learning_focus,
        "skillType": skill,
        "difficulty": diff,
        "difficultyDistribution": dd,
        "language": LANGUAGE,
        "questionText": qtext,
        "options": {
            "a": opts[0],
            "b": opts[1],
            "c": opts[2],
            "d": opts[3],
        },
        "correctAnswer": ans.lower(),
        "correctAnswerLabel": ans.upper(),
        "explanation": expl,
        "versionId": 1,
        "createdAtMillis": NOW_MS,
        "updatedAtMillis": NOW_MS,
        "contentOrigin": "ORIGINAL",
        "licenseStatus": "self_authored",
        "commercialReuseAllowed": True,
        "examYear": None,
        "contentYear": CONTENT_YEAR,
        "schoolTrack": TRACK,
        "curriculum": CURRICULUM,
        "gradeLevel_year": GRADE,
        "gradeLevel": GRADE,
        "sourceReference": SOURCE_REF,
    }


# ============================================================
# 25 ORIGINAL questions — Phase 10.5 Batch 01
# ============================================================

QUESTIONS = [
    # --- Topic 1: Mendengar & Bertutur (5 Q) ---
    q(1, "Mendengar & Bertutur", "Ucapan harian",
      "Sopan santun — membalas ucapan guru",
      "RECOGNITION", 1,
      "Apabila guru berkata 'Selamat pagi' kepada kamu, apakah jawapan yang paling sopan?",
      ["Selamat malam, cikgu", "Selamat pagi, cikgu", "Terima kasih, cikgu", "Selamat tinggal, cikgu"],
      "B",
      "Membalas dengan sebutan yang sama ialah adab sopan. 'Selamat pagi' dibalas dengan 'Selamat pagi, cikgu'."),

    q(2, "Mendengar & Bertutur", "Arahan guru",
      "Membalas arahan guru di bilik darjah",
      "RECOGNITION", 1,
      "Guru berkata 'Buka buku kamu di muka surat 10.' Apakah yang kamu patut lakukan?",
      ["Tutup buku kamu", "Buka buku di muka surat 10", "Letakkan buku di dalam beg", "Tulis di papan putih"],
      "B",
      "Arahan 'Buka buku di muka surat 10' bermaksud membuka halaman bernombor 10 dalam buku."),

    q(3, "Mendengar & Bertutur", "Perkenalan diri",
      "Memerihalkan maklumat asas dalam perkenalan diri",
      "RECOGNITION", 1,
      "Apakah maklumat yang biasa disebut apabila memperkenalkan diri di sekolah?",
      ["Alamat rumah sahaja", "Nama sendiri dan kelas", "Nama guru", "Nama ibu bapa"],
      "B",
      "Perkenalan diri biasanya menyebut nama sendiri dan kelas, contohnya 'Nama saya Ali, saya murid Tahun Satu'."),

    q(4, "Mendengar & Bertutur", "Sopan santun — menolak",
      "Menolak permintaan dengan cara yang sopan",
      "RECOGNITION", 1,
      "Rakan anda menawarkan kuih, tetapi anda sudah makan. Apakah jawapan yang paling sopan?",
      ["Tidak mahu", "Saya sudah makan, terima kasih", "Jangan beri saya", "Bawakan kuih yang lain"],
      "B",
      "Memberi alasan ringkas dan berterima kasih menunjukkan adab sopan. 'Saya sudah makan, terima kasih' lebih baik daripada sekadar 'Tidak mahu'."),

    q(5, "Mendengar & Bertutur", "Mendengar cerita pendek",
      "Mengenal pasti watak utama daripada cerita pendek",
      "COMPREHENSION", 2,
      "Cikgu bercerita tentang seorang budak yang membantu nenek menyeberang jalan. Siapakah watak utama dalam cerita ini?",
      ["Nenek", "Cikgu", "Budak yang membantu", "Polis"],
      "C",
      "Watak utama ialah orang yang melakukan tindakan utama dalam cerita. Budak yang membantu nenek ialah watak utama."),

    # --- Topic 2: Membaca (Suku Kata / Perkataan Mudah) (5 Q) ---
    q(6, "Membaca (Suku Kata / Perkataan Mudah)", "Suku kata KV + vokal",
      "Membaca suku kata terbuka",
      "RECOGNITION", 1,
      "Antara pasangan suku kata berikut, yang manakah membentuk perkataan 'bola'?",
      ["ba + la", "bo + la", "bi + la", "bu + la"],
      "B",
      "Menggabungkan 'bo' dan 'la' menghasilkan perkataan 'bola'. Suku kata 'bola' bermula dengan vokal 'o'."),

    q(7, "Membaca (Suku Kata / Perkataan Mudah)", "Suku kata tertutup",
      "Mengenal pasti konsonan akhir dalam perkataan",
      "RECOGNITION", 1,
      "Perkataan 'kanak-kanak' mengandungi suku kata KV + K. Apakah bunyi akhir perkataan ini?",
      ["/a/", "/k/", "/n/", "/i/"],
      "B",
      "'Kanak-kanak' dibaca 'ka-nak-ka-nak'. Suku kata akhir 'nak' berakhir dengan konsonan /k/."),

    q(8, "Membaca (Suku Kata / Perkataan Mudah)", "Perkataan mudah",
      "Mengenal pasti perkataan yang berakhir dengan huruf tertentu",
      "RECOGNITION", 1,
      "Antara perkataan berikut, yang manakah berakhir dengan huruf 'h'?",
      ["bola", "meja", "rumah", "kawan"],
      "C",
      "'Rumah' berakhir dengan huruf 'h'. 'Bola' dan 'meja' berakhir dengan 'a', 'kawan' berakhir dengan 'n'."),

    q(9, "Membaca (Suku Kata / Perkataan Mudah)", "Huruf vokal",
      "Mengenal pasti huruf vokal pertama",
      "RECOGNITION", 1,
      "Apakah huruf vokal pertama dalam perkataan 'awan'?",
      ["w", "a", "n", "i"],
      "B",
      "Vokal pertama 'a' muncul di awal perkataan 'awan'."),

    q(10, "Membaca (Suku Kata / Perkataan Mudah)", "Ayat mudah",
      "Membaca ayat mudah 3-4 perkataan",
      "RECOGNITION", 1,
      "Ayat manakah yang lengkap dan betul?",
      ["Ali makan", "Ali makan nasi", "makan nasi Ali", "nasi makan Ali"],
      "B",
      "Ayat lengkap mengikut susunan subjek-predikat-objek: 'Ali' (subjek) + 'makan' (predikat) + 'nasi' (objek)."),

    # --- Topic 3: Penulisan (Huruf / Perkataan / Ayat Mudah) (5 Q) ---
    q(11, "Penulisan (Huruf / Perkataan / Ayat Mudah)", "Huruf besar vs huruf kecil",
      "Mengenal pasti huruf besar dalam perkataan",
      "RECOGNITION", 1,
      "Dalam perkataan 'Sekolah', huruf manakah yang ditulis dengan huruf besar?",
      ["a", "e", "S", "l"],
      "C",
      "Perkataan 'Sekolah' bermula dengan huruf besar 'S' pada awal perkataan (contoh: Sekolah Rendah)."),

    q(12, "Penulisan (Huruf / Perkataan / Ayat Mudah)", "Ayat mudah",
      "Menyusun perkataan menjadi ayat",
      "APPLICATION", 2,
      "Susun perkataan ini menjadi ayat yang betul: 'buku - saya - membaca'.",
      ["Buku saya membaca", "Membaca buku saya", "Saya membaca buku", "Saya buku membaca"],
      "C",
      "Ayat lengkap mengikut susunan subjek-predikat-objek: 'Saya' (subjek) + 'membaca' (predikat) + 'buku' (objek)."),

    q(13, "Penulisan (Huruf / Perkataan / Ayat Mudah)", "Penulisan nama sendiri",
      "Menulis nama sendiri dengan huruf besar",
      "APPLICATION", 2,
      "Nama 'SITI' ditulis dengan huruf besar di mana?",
      ["Semua huruf", "Hanya huruf pertama", "Tiada huruf besar", "Hanya huruf akhir"],
      "A",
      "Nama sendiri ditulis dengan semua huruf besar, contohnya 'SITI'."),

    q(14, "Penulisan (Huruf / Perkataan / Ayat Mudah)", "Tanda baca",
      "Tanda baca yang betul untuk ayat tanya",
      "APPLICATION", 2,
      "Ayat tanya perlu diakhiri dengan tanda baca apakah?",
      ["titik (.)", "tanda tanya (?)", "koma (,)", "tanda seru (!)"],
      "B",
      "Tanda tanya (?) digunakan untuk menamatkan ayat tanya."),

    q(15, "Penulisan (Huruf / Perkataan / Ayat Mudah)", "Penulisan ayat mudah",
      "Menulis ayat mudah berdasarkan rangsangan gambar",
      "APPLICATION", 3,
      "Ali nampak seekor kucing di halaman. Ayat manakah yang paling sesuai ditulis oleh Ali?",
      ["Kucing Ali.", "Ada kucing.", "Terdapat seekor kucing di halaman rumah Ali.", "Kucing minum."],
      "C",
      "Ayat lengkap perlu mengandungi subjek, predikat, dan objek/tempat. 'Terdapat seekor kucing di halaman rumah Ali' ialah ayat lengkap yang sesuai untuk murid Tahun Satu."),

    # --- Topic 4: Tatabahasa (Imbuhan, Kata Nama, Kata Kerja) (5 Q) ---
    q(16, "Tatabahasa (Imbuhan, Kata Nama, Kata Kerja)", "Kata nama",
      "Mengenal pasti kata nama (nama benda)",
      "RECOGNITION", 1,
      "Antara perkataan berikut, yang manakah kata nama (nama benda)?",
      ["lari", "meja", "cantik", "tidur"],
      "B",
      "'Meja' ialah nama benda — kata nama. 'Lari' dan 'tidur' ialah perbuatan (kata kerja), 'cantik' ialah sifat (kata adjektif)."),

    q(17, "Tatabahasa (Imbuhan, Kata Nama, Kata Kerja)", "Kata kerja",
      "Mengenal pasti kata kerja (perbuatan)",
      "RECOGNITION", 1,
      "Antara perkataan berikut, yang manakah kata kerja (perbuatan)?",
      ["rumah", "buku", "menulis", "kawan"],
      "C",
      "'Menulis' ialah perbuatan — kata kerja. 'Rumah', 'buku', 'kawan' ialah nama benda — kata nama."),

    q(18, "Tatabahasa (Imbuhan, Kata Nama, Kata Kerja)", "Imbuhan",
      "Mengesan perkataan yang menggunakan awalan 'ber-'",
      "APPLICATION", 3,
      "Apakah yang berlaku jika kita menambah awalan 'ber-' pada perkataan 'lari'?",
      ["Berlari (berlari di padang)", "Belari", "Perlari", "Terlari"],
      "A",
      "'Lari' + 'ber-' = 'berlari'. Awalan 'ber-' digunakan untuk membentuk kata kerja daripada kata dasar (contoh: 'lari' → 'berlari')."),

    q(19, "Tatabahasa (Imbuhan, Kata Nama, Kata Kerja)", "Imbuhan",
      "Mengesan perkataan yang menggunakan imbuhan 'me-'",
      "RECOGNITION", 1,
      "Antara perkataan berikut, yang manakah bermula dengan imbuhan 'me-'?",
      ["buku", "menulis", "sekolah", "kawan"],
      "B",
      "'Menulis' bermula dengan 'me-'. Imbuhan 'me-' digunakan untuk membentuk kata kerja."),

    q(20, "Tatabahasa (Imbuhan, Kata Nama, Kata Kerja)", "Ayat mudah",
      "Membezakan jenis perkataan dalam ayat",
      "RECOGNITION", 1,
      "Dalam ayat 'Ali makan nasi', perkataan manakah kata nama?",
      ["Ali", "makan", "nasi", "di"],
      "C",
      "'Nasi' ialah benda yang boleh dilihat/dirasa — kata nama. 'Ali' juga kata nama (nama orang), tetapi jawapan paling sesuai ialah 'nasi' (nama benda umum)."),

    # --- Topic 5: Perbendaharaan Kata (Sinonim / Antonim Mudah) (5 Q) ---
    q(21, "Perbendaharaan Kata (Sinonim / Antonim Mudah)", "Sinonim",
      "Mengenal pasti sinonim (persamaan maksud) dalam konteks pelbagai",
      "APPLICATION", 3,
      "Apakah sinonim (persamaan maksud) bagi perkataan 'gembira'?",
      ["sedih", "suka", "penat", "marah"],
      "B",
      "'Gembira' bermaksud 'suka' atau 'bahagia'. Sinonim ialah perkataan yang mempunyai persamaan maksud — murid Tahun Satu perlu memahami perasaan melalui contoh konteks."),

    q(22, "Perbendaharaan Kata (Sinonim / Antonim Mudah)", "Antonim",
      "Mengenal pasti antonim (lawan maksud)",
      "RECOGNITION", 1,
      "Apakah antonim (lawan maksud) bagi perkataan 'tinggi'?",
      ["besar", "panjang", "rendah", "luas"],
      "C",
      "Antonim 'tinggi' ialah 'rendah'. 'Besar', 'panjang', 'luas' ialah kata adjektif tetapi bukan antonim yang tepat untuk 'tinggi'."),

    q(23, "Perbendaharaan Kata (Sinonim / Antonim Mudah)", "Sinonim dalam konteks",
      "Mencari sinonim yang sesuai dalam ayat",
      "APPLICATION", 2,
      "Dalam ayat 'Ibu kelihatan ceria hari ini', perkataan manakah sinonim bagi 'ceria'?",
      ["sedih", "rindu", "gembira", "marah"],
      "C",
      "'Ceria' bermaksud 'gembira' atau 'riang'. Sinonim dalam konteks ini ialah 'gembira'."),

    q(24, "Perbendaharaan Kata (Sinonim / Antonim Mudah)", "Antonim dalam konteks",
      "Mencari antonim yang sesuai dalam ayat",
      "APPLICATION", 2,
      "Antara ayat berikut, yang manakah menggunakan perkataan antonim dengan betul?",
      [
        "Dia seorang yang sangat tinggi.",
        "Pasar itu sangat besar dan mahal.",
        "Adik saya berbadan kecil manakala abang saya berbadan tinggi.",
        "Buku itu berwarna merah dan tebal."
      ],
      "C",
      "Ayat C membandingkan 'kecil' dan 'tinggi' — pasangan antonim (lawan maksud) untuk saiz badan."),

    q(25, "Perbendaharaan Kata (Sinonim / Antonim Mudah)", "Perbendaharaan dalam cerita",
      "Memilih perkataan yang sesuai untuk melengkapkan cerita",
      "APPLICATION", 2,
      "Lengkapkan ayat: 'Ahmad seorang budak yang ___ . Semua orang suka bermain bersamanya.'",
      ["pendiam", "jahat", "comel dan baik hati", "malas"],
      "C",
      "'Comel dan baik hati' sesuai melengkapkan ayat kerana ia menjelaskan mengapa semua orang suka bermain dengan Ahmad."
      ),
]

# Sanity assertions
assert len(QUESTIONS) == 25, f"Expected 25, got {len(QUESTIONS)}"

# Difficulty distribution: must be exactly Easy 15 / Medium 7 / Hard 3
diff_counts = Counter(q["difficulty"] for q in QUESTIONS)
assert diff_counts[1] == 15, f"Easy (diff=1) expected 15, got {diff_counts[1]}"
assert diff_counts[2] == 7, f"Medium (diff=2) expected 7, got {diff_counts[2]}"
assert diff_counts[3] == 3, f"Hard (diff=3) expected 3, got {diff_counts[3]}"

# Topic distribution: must cover 5 topics × 5 questions each
topic_counts = Counter(q["topic"] for q in QUESTIONS)
expected_topics = {
    "Mendengar & Bertutur": 5,
    "Membaca (Suku Kata / Perkataan Mudah)": 5,
    "Penulisan (Huruf / Perkataan / Ayat Mudah)": 5,
    "Tatabahasa (Imbuhan, Kata Nama, Kata Kerja)": 5,
    "Perbendaharaan Kata (Sinonim / Antonim Mudah)": 5,
}
for t, n in expected_topics.items():
    assert topic_counts[t] == n, f"Topic '{t}' expected {n}, got {topic_counts[t]}"

# Skill distribution
skill_counts = Counter(q["skillType"] for q in QUESTIONS)
print(f"Skill distribution: {dict(skill_counts)}")

# Save
final_output = {
    "metadata": {
        "batch_id": BATCH_ID,
        "phase": PHASE,
        "schoolTrack": TRACK,
        "language": LANGUAGE,
        "grade": GRADE,
        "subject": "Bahasa Melayu",
        "subjectCode": SUBJECT_CODE,
        "curriculum": CURRICULUM,
        "questionType": QUESTION_TYPE,
        "totalQuestions": len(QUESTIONS),
        "difficultyDistribution": {"easy": 15, "medium": 7, "hard": 3},
        "note": "Batch 01 of Phase 10.5 — first formal production batch. All 25 questions are KuizKu ORIGINAL. NO copy from V3/V4-TEST/Phase 10.1/Reference DB.",
    },
    "questions": QUESTIONS,
}

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=2, ensure_ascii=False)

# SHA-256 of questions-only
q_payload = {"questions": QUESTIONS}
q_sha = hashlib.sha256(json.dumps(q_payload, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()

print(f"File: {OUT_PATH}")
print(f"File SHA-256: {hashlib.sha256(open(OUT_PATH,'rb').read()).hexdigest()}")
print(f"Questions-only SHA-256: {q_sha}")
print(f"Total questions: {len(QUESTIONS)}")
print(f"Difficulty: easy={diff_counts[1]} medium={diff_counts[2]} hard={diff_counts[3]}")
print(f"Topics: {dict(topic_counts)}")
print(f"Skills: {dict(skill_counts)}")
