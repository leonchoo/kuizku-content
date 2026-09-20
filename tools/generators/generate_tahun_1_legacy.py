"""Phase 10.1.1 — Generate 100 ORIGINAL Tahun 1 questions.

Per 638 §:
  - 30 BM + 28 Math + 22 Science + 20 BI = 100 Q
  - Easy 60 / Medium 30 / Hard 10
  - All questions: contentOrigin=ORIGINAL, licenseStatus=self_authored,
    commercialReuseAllowed=allowed, examYear=null,
    gradeLevel="Tahun1", questionType=SINGLE_CHOICE
  - 4 options, exactly 1 correct, correctAnswer=A/B/C/D
  - explanation must justify correct answer
  - age-appropriate (Tahun 1 = 7-year-olds in Malaysia)
  - BRAND NEW wording/options/distractors (no copy/para/synonym/numbers-only/names-only/context-only)

Reference DB used for:
  - syllabus scope
  - topic identification
  - difficulty calibration
  - question-style reference
NOT for direct content reuse.

This is a SINGLE self-contained Python file. It defines questions as data
and validates them in-memory. No external API. No LLM.
"""

import hashlib
import json
import re
from pathlib import Path
from collections import Counter, defaultdict

OUT_PATH = Path(r"D:\Users\bajub\kuizku_p10\tahun_1_pilot.json")

# =====================================================================
# QUESTION BUILDERS (one helper per subject for readability)
# =====================================================================

def q_bm(idx, topic, skill, difficulty, qtext, opts, correct_letter, explanation):
    """Bahasa Melayu question. difficulty 1=easy/2=medium/3=hard."""
    return {
        "questionId": f"v5-t1-bm-{idx:03d}",
        "subject": "Bahasa Melayu",
        "gradeLevel": "Tahun1",
        "language": "ms",
        "questionType": "SINGLE_CHOICE",
        "topic": topic,
        "subtopic": topic,
        "learningFocus": topic,
        "skillType": skill,
        "difficultyDistribution": _diff_for(difficulty),
        "contentOrigin": "ORIGINAL",
        "licenseStatus": "self_authored",
        "commercialReuseAllowed": True,
        "examYear": None,
        "gradeLevel_year": "Tahun1",
        "questionText": qtext,
        "options": {
            "a": opts[0],
            "b": opts[1],
            "c": opts[2],
            "d": opts[3],
        },
        "correctAnswer": correct_letter.lower(),
        "correctAnswerLabel": correct_letter,
        "explanation": explanation,
        "versionId": 1,
        "createdAtMillis": 1700000000000,
        "updatedAtMillis": 1700000000000,
        "sourceReference": "KuizKu ORIGINAL authoring",
        "paperCode": None,
        "examStage": None,
    }


def q_math(idx, topic, skill, difficulty, qtext, opts, correct_letter, explanation):
    return {
        "questionId": f"v5-t1-math-{idx:03d}",
        "subject": "Mathematics",
        "gradeLevel": "Tahun1",
        "language": "ms",
        "questionType": "SINGLE_CHOICE",
        "topic": topic,
        "subtopic": topic,
        "learningFocus": topic,
        "skillType": skill,
        "difficultyDistribution": _diff_for(difficulty),
        "contentOrigin": "ORIGINAL",
        "licenseStatus": "self_authored",
        "commercialReuseAllowed": True,
        "examYear": None,
        "gradeLevel_year": "Tahun1",
        "questionText": qtext,
        "options": {
            "a": opts[0],
            "b": opts[1],
            "c": opts[2],
            "d": opts[3],
        },
        "correctAnswer": correct_letter.lower(),
        "correctAnswerLabel": correct_letter,
        "explanation": explanation,
        "versionId": 1,
        "createdAtMillis": 1700000000000,
        "updatedAtMillis": 1700000000000,
        "sourceReference": "KuizKu ORIGINAL authoring",
        "paperCode": None,
        "examStage": None,
    }


def q_sci(idx, topic, skill, difficulty, qtext, opts, correct_letter, explanation):
    return {
        "questionId": f"v5-t1-sci-{idx:03d}",
        "subject": "Science",
        "gradeLevel": "Tahun1",
        "language": "ms",
        "questionType": "SINGLE_CHOICE",
        "topic": topic,
        "subtopic": topic,
        "learningFocus": topic,
        "skillType": skill,
        "difficultyDistribution": _diff_for(difficulty),
        "contentOrigin": "ORIGINAL",
        "licenseStatus": "self_authored",
        "commercialReuseAllowed": True,
        "examYear": None,
        "gradeLevel_year": "Tahun1",
        "questionText": qtext,
        "options": {
            "a": opts[0],
            "b": opts[1],
            "c": opts[2],
            "d": opts[3],
        },
        "correctAnswer": correct_letter.lower(),
        "correctAnswerLabel": correct_letter,
        "explanation": explanation,
        "versionId": 1,
        "createdAtMillis": 1700000000000,
        "updatedAtMillis": 1700000000000,
        "sourceReference": "KuizKu ORIGINAL authoring",
        "paperCode": None,
        "examStage": None,
    }


def q_bi(idx, topic, skill, difficulty, qtext, opts, correct_letter, explanation):
    return {
        "questionId": f"v5-t1-bi-{idx:03d}",
        "subject": "Bahasa Inggeris",
        "gradeLevel": "Tahun1",
        "language": "en",
        "questionType": "SINGLE_CHOICE",
        "topic": topic,
        "subtopic": topic,
        "learningFocus": topic,
        "skillType": skill,
        "difficultyDistribution": _diff_for(difficulty),
        "contentOrigin": "ORIGINAL",
        "licenseStatus": "self_authored",
        "commercialReuseAllowed": True,
        "examYear": None,
        "gradeLevel_year": "Tahun1",
        "questionText": qtext,
        "options": {
            "a": opts[0],
            "b": opts[1],
            "c": opts[2],
            "d": opts[3],
        },
        "correctAnswer": correct_letter.lower(),
        "correctAnswerLabel": correct_letter,
        "explanation": explanation,
        "versionId": 1,
        "createdAtMillis": 1700000000000,
        "updatedAtMillis": 1700000000000,
        "sourceReference": "KuizKu ORIGINAL authoring",
        "paperCode": None,
        "examStage": None,
    }


def _diff_for(d):
    if d == 1:
        return {"easy": 100, "medium": 0, "hard": 0}
    elif d == 2:
        return {"easy": 0, "medium": 100, "hard": 0}
    else:
        return {"easy": 0, "medium": 0, "hard": 100}


# =====================================================================
# BAHASA MELAYU — 30 Q (12 easy, 12 medium, 6 hard = 30)
# Topics: Mendengar & Bertutur(5), Membaca(8), Penulisan(6),
#         Tatabahasa(5), Perbendaharaan Kata(3), Pemahaman(3)
# =====================================================================

BM = [
    # === Mendengar & Bertutur (5 Q: 3 easy + 2 medium) ===
    q_bm(1, "Mendengar & Bertutur", "RECOGNITION", 1,
        "Apabila cikgu berkata 'Selamat pagi', kita harus jawab ...",
        ["Selamat tengah hari", "Selamat pagi, cikgu", "Terima kasih, cikgu", "Selamat malam"],
        "B",
        "Sopan santun: membalas ucapan dengan sebutan yang sama adalah adab yang baik."),
    q_bm(2, "Mendengar & Bertutur", "RECOGNITION", 1,
        "Aiman memperkenalkan diri: 'Nama saya Aiman. Saya murid Tahun Satu.' Maklumat ini dikenali sebagai ...",
        ["Tempat tinggal", "Nama dan kelas", "Nama ibu bapa", "Makanan kegemaran"],
        "B",
        "Nama sendiri dan kelas adalah maklumat peribadi yang biasa diperkenalkan."),
    q_bm(3, "Mendengar & Bertutur", "RECOGNITION", 1,
        "Ibu menyuruh Ali membersihkan bilik. Apakah cara paling sopan untuk menolak?",
        ["Tidak, saya malas", "Maaf, saya tidak suka", "Maaf ibu, saya mahu belajar dulu", "Saya tidak mahu"],
        "C",
        "Cara menolak yang sopan ialah memberi alasan yang baik, bukannya menolak secara kasar."),
    q_bm(4, "Mendengar & Bertutur", "COMPREHENSION", 2,
        "Cikgu memberi arahan: 'Buka buku muka surat 12.' Apakah yang perlu dilakukan?",
        ["Menutup buku", "Membuka buku di muka surat 12", "Menulis di buku", "Meletakkan buku di atas meja"],
        "B",
        "Arahan 'buka buku muka surat 12' bermaksud membuka halaman 12 dalam buku."),
    q_bm(5, "Mendengar & Bertutur", "COMPREHENSION", 2,
        "Apabila rakan bertanya 'Apa khabar?', jawapan yang sesuai ialah ...",
        ["Terima kasih", "Khabar baik, terima kasih", "Saya lapar", "Selamat tinggal"],
        "B",
        "'Khabar baik' adalah jawapan standard untuk menanyakan khabar."),

    # === Membaca (Suku Kata / Perkataan Mudah) (8 Q: 5 easy + 2 medium + 1 hard) ===
    q_bm(6, "Membaca", "RECOGNITION", 1,
        "Perkataan yang bermula dengan huruf 'M' ialah ...",
        ["rumah", "meja", "bola", "awan"],
        "B",
        "'Meja' bermula dengan huruf 'M'."),
    q_bm(7, "Membaca", "RECOGNITION", 1,
        "Antara perkataan berikut, yang manakah paling panjang?",
        ["bola", "rumah", "sekolah", "kucing"],
        "C",
        "'Sekolah' mempunyai 7 huruf, lebih panjang daripada yang lain."),
    q_bm(8, "Membaca", "RECOGNITION", 1,
        "Suku kata 'ba' + 'ka' = ...",
        ["buku", "baka", "bila", "bola"],
        "B",
        "Menggabungkan 'ba' dan 'ka' menghasilkan perkataan 'baka'."),
    q_bm(9, "Membaca", "RECOGNITION", 1,
        "Apakah bunyi akhir perkataan 'buku'?",
        ["/b/", "/u/", "/k/", "/bu/"],
        "B",
        "Suku kata akhir 'buku' ialah 'ku', bunyi utamanya /u/."),
    q_bm(10, "Membaca", "RECOGNITION", 1,
        "Perkataan yang betul ejaannya ialah ...",
        ["sekolah", "sekoalh", "sekola", "sekoalh"],
        "A",
        "'Sekolah' dieja dengan betul: s-e-k-o-l-a-h."),
    q_bm(11, "Membaca", "RECOGNITION", 2,
        "Perkataan 'membaca' dibahagikan kepada suku kata seperti ...",
        ["mem-ba-ca", "mem-bac-a", "me-mba-ca", "mem-baca"],
        "A",
        "'Membaca' dibahagikan kepada tiga suku kata: mem-ba-ca."),
    q_bm(12, "Membaca", "COMPREHENSION", 2,
        "Bacaan: 'Ali bermain bola di halaman.' Siapakah yang bermain bola?",
        ["Halaman", "Ali", "Bola", "Sekolah"],
        "B",
        "Subjek dalam ayat adalah 'Ali', jadi Ali yang bermain bola."),
    q_bm(13, "Membaca", "COMPREHENSION", 3,
        "Ayat: 'Siti membaca buku di perpustakaan dengan teliti.' Apakah 'dengan teliti' memberi maklumat tentang?",
        ["Buku Siti", "Cara Siti membaca", "Perpustakaan", "Siti"],
        "B",
        "'Dengan teliti' adalah frasa yang menjelaskan cara melakukan sesuatu — cara Siti membaca."),

    # === Penulisan (Huruf / Perkataan / Ayat Mudah) (6 Q: 4 easy + 2 medium) ===
    q_bm(14, "Penulisan", "APPLICATION", 1,
        "Apakah huruf pertama dalam perkataan 'awan'?",
        ["a", "w", "n", "i"],
        "A",
        "Perkataan 'awan' bermula dengan huruf 'a'."),
    q_bm(15, "Penulisan", "APPLICATION", 1,
        "Susun huruf-huruf ini menjadi perkataan: 'a - n - i - n - g'",
        ["aning", "nangai", "naing", "ingna"],
        "C",
        "Susunan 'a-n-i-n-g' menghasilkan perkataan 'naing', tetapi lebih sesuai ialah 'anjing'. Jawapan 'naing' bukan perkataan standard; jawapan tepat ialah 'anjing'. [Catatan: soalan ini menggunakan 'anjing' sebagai jawapan.]"),
        # FIX: use proper word
        # Replacing with cleaner question
        ),
]

# Re-do BM section more carefully — the above has a placeholder; redo BM from scratch.

BM = []

# Helper macro to keep code compact
def add_bm(idx, topic, skill, diff, qtext, opts, correct, expl):
    BM.append({
        "questionId": f"v5-t1-bm-{idx:03d}",
        "subject": "Bahasa Melayu",
        "gradeLevel": "Tahun1",
        "language": "ms",
        "questionType": "SINGLE_CHOICE",
        "topic": topic,
        "subtopic": topic,
        "learningFocus": topic,
        "skillType": skill,
        "difficultyDistribution": _diff_for(diff),
        "contentOrigin": "ORIGINAL",
        "licenseStatus": "self_authored",
        "commercialReuseAllowed": True,
        "examYear": None,
        "gradeLevel_year": "Tahun1",
        "questionText": qtext,
        "options": {"a": opts[0], "b": opts[1], "c": opts[2], "d": opts[3]},
        "correctAnswer": correct.lower(),
        "correctAnswerLabel": correct,
        "explanation": expl,
        "versionId": 1,
        "createdAtMillis": 1700000000000,
        "updatedAtMillis": 1700000000000,
        "sourceReference": "KuizKu ORIGINAL authoring",
        "paperCode": None,
        "examStage": None,
    })


def add_math(idx, topic, skill, diff, qtext, opts, correct, expl):
    BM.append({
        "questionId": f"v5-t1-math-{idx:03d}",
        "subject": "Mathematics",
        "gradeLevel": "Tahun1",
        "language": "ms",
        "questionType": "SINGLE_CHOICE",
        "topic": topic,
        "subtopic": topic,
        "learningFocus": topic,
        "skillType": skill,
        "difficultyDistribution": _diff_for(diff),
        "contentOrigin": "ORIGINAL",
        "licenseStatus": "self_authored",
        "commercialReuseAllowed": True,
        "examYear": None,
        "gradeLevel_year": "Tahun1",
        "questionText": qtext,
        "options": {"a": opts[0], "b": opts[1], "c": opts[2], "d": opts[3]},
        "correctAnswer": correct.lower(),
        "correctAnswerLabel": correct,
        "explanation": expl,
        "versionId": 1,
        "createdAtMillis": 1700000000000,
        "updatedAtMillis": 1700000000000,
        "sourceReference": "KuizKu ORIGINAL authoring",
        "paperCode": None,
        "examStage": None,
    })


def add_sci(idx, topic, skill, diff, qtext, opts, correct, expl):
    BM.append({
        "questionId": f"v5-t1-sci-{idx:03d}",
        "subject": "Science",
        "gradeLevel": "Tahun1",
        "language": "ms",
        "questionType": "SINGLE_CHOICE",
        "topic": topic,
        "subtopic": topic,
        "learningFocus": topic,
        "skillType": skill,
        "difficultyDistribution": _diff_for(diff),
        "contentOrigin": "ORIGINAL",
        "licenseStatus": "self_authored",
        "commercialReuseAllowed": True,
        "examYear": None,
        "gradeLevel_year": "Tahun1",
        "questionText": qtext,
        "options": {"a": opts[0], "b": opts[1], "c": opts[2], "d": opts[3]},
        "correctAnswer": correct.lower(),
        "correctAnswerLabel": correct,
        "explanation": expl,
        "versionId": 1,
        "createdAtMillis": 1700000000000,
        "updatedAtMillis": 1700000000000,
        "sourceReference": "KuizKu ORIGINAL authoring",
        "paperCode": None,
        "examStage": None,
    })


def add_bi(idx, topic, skill, diff, qtext, opts, correct, expl):
    BM.append({
        "questionId": f"v5-t1-bi-{idx:03d}",
        "subject": "Bahasa Inggeris",
        "gradeLevel": "Tahun1",
        "language": "en",
        "questionType": "SINGLE_CHOICE",
        "topic": topic,
        "subtopic": topic,
        "learningFocus": topic,
        "skillType": skill,
        "difficultyDistribution": _diff_for(diff),
        "contentOrigin": "ORIGINAL",
        "licenseStatus": "self_authored",
        "commercialReuseAllowed": True,
        "examYear": None,
        "gradeLevel_year": "Tahun1",
        "questionText": qtext,
        "options": {"a": opts[0], "b": opts[1], "c": opts[2], "d": opts[3]},
        "correctAnswer": correct.lower(),
        "correctAnswerLabel": correct,
        "explanation": expl,
        "versionId": 1,
        "createdAtMillis": 1700000000000,
        "updatedAtMillis": 1700000000000,
        "sourceReference": "KuizKu ORIGINAL authoring",
        "paperCode": None,
        "examStage": None,
    })


# =====================================================================
# All 100 questions (BM 30 + Math 28 + Science 22 + BI 20)
# =====================================================================

# ---------------- BAHASA MELAYU (30) ----------------
# Mendengar & Bertutur (5)
add_bm(1, "Mendengar & Bertutur", "RECOGNITION", 1,
    "Apabila guru berkata 'Selamat pagi', kita membalas dengan ...",
    ["Selamat tengah hari", "Selamat pagi, cikgu", "Terima kasih, cikgu", "Selamat malam"],
    "B",
    "Membalas ucapan guru dengan sebutan yang sama menunjukkan adab sopan yang baik.")
add_bm(2, "Mendengar & Bertutur", "RECOGNITION", 1,
    "Mira memperkenalkan diri: 'Nama saya Mira. Saya murid Tahun Satu.' Maklumat yang dibayangkan ialah ...",
    ["Alamat rumah", "Nama dan kelas", "Nama ibu bapa", "Warna kegemaran"],
    "B",
    "Nama sendiri dan kelas adalah maklumat asas yang lazim diperkenalkan dalam perkenalan.")
add_bm(3, "Mendengar & Bertutur", "RECOGNITION", 1,
    "Ibu menyuruh Danial membereskan bilik. Cara paling sopan untuk menjawab ialah ...",
    ["Tidak, saya malas", "Saya tak mahu", "Baik ibu, saya akan membereskan sekarang", "Nanti sajalah"],
    "C",
    "Menjawab dengan 'Baik, saya akan ...' menunjukkan kerelaan dan adab yang baik terhadap ibu.")
add_bm(4, "Mendengar & Bertutur", "COMPREHENSION", 2,
    "Guru memberi arahan: 'Buka buku di halaman dua belas.' Apakah tindakan kamu?",
    ["Menutup buku", "Membuka buku di halaman 12", "Menulis di buku", "Meletakkan buku di atas lantai"],
    "B",
    "Arahan 'buka buku di halaman dua belas' bermaksud membuka halaman bernombor 12 dalam buku.")
add_bm(5, "Mendengar & Bertutur", "COMPREHENSION", 2,
    "Rakan bertanya 'Apa khabar?' Balasan yang sesuai ialah ...",
    ["Terima kasih", "Khabar baik, terima kasih", "Saya lapar", "Selamat tinggal"],
    "B",
    "'Khabar baik' adalah jawapan standard apabila seseorang bertanya khabar.")

# Membaca (8)
add_bm(6, "Membaca", "RECOGNITION", 1,
    "Antara perkataan berikut, yang manakah bermula dengan huruf 'M'?",
    ["rumah", "bola", "awan", "kucing"],
    "A",
    "Perkataan 'rumah' bermula dengan huruf 'M'.")
add_bm(7, "Membaca", "RECOGNITION", 1,
    "Antara perkataan berikut, yang manakah paling panjang?",
    ["bola", "rumah", "sekolah", "buku"],
    "C",
    "'Sekolah' mempunyai 7 huruf, lebih panjang daripada 'rumah' (5), 'bola' (4), atau 'buku' (4).")
add_bm(8, "Membaca", "RECOGNITION", 1,
    "Gabungkan suku kata 'ba' + 'ka' untuk menghasilkan perkataan ...",
    ["buku", "baka", "bola", "batu"],
    "B",
    "Menggabungkan 'ba' dan 'ka' menghasilkan perkataan 'baka'.")
add_bm(9, "Membaca", "RECOGNITION", 1,
    "Apakah bunyi vokal akhir dalam perkataan 'buku'?",
    ["/b/", "/k/", "/u/", "/bu/"],
    "C",
    "Vokal akhir 'buku' ialah /u/; konsonan /b/ dan /k/ masing-masing di awal dan tengah.")
add_bm(10, "Membaca", "RECOGNITION", 1,
    "Perkataan yang dieja dengan betul ialah ...",
    ["sekolah", "sekoalh", "sekola", "sekolaah"],
    "A",
    "'Sekolah' dieja s-e-k-o-l-a-h dengan tepat.")
add_bm(11, "Membaca", "RECOGNITION", 2,
    "Perkataan 'membaca' dibahagikan kepada suku kata berikut ...",
    ["mem-ba-ca", "mem-bac-a", "me-mba-ca", "memm-baca"],
    "A",
    "'Membaca' terdiri daripada tiga suku kata: mem-ba-ca.")
add_bm(12, "Membaca", "COMPREHENSION", 2,
    "Ayat: 'Aiman bermain bola di padang.' Siapakah yang bermain bola?",
    ["Padang", "Aiman", "Bola", "Sekolah"],
    "B",
    "Subjek dalam ayat ialah 'Aiman', jadi Aiman yang bermain bola.")
add_bm(13, "Membaca", "COMPREHENSION", 3,
    "Ayat: 'Siti membaca buku di perpustakaan dengan tekun.' Apakah 'dengan tekun' menjelaskan?",
    ["Buku Siti", "Tempat Siti membaca", "Cara Siti membaca", "Perpustakaan"],
    "C",
    "'Dengan tekun' adalah frasa yang menjelaskan cara seseorang melakukan sesuatu — cara Siti membaca.")

# Penulisan (6)
add_bm(14, "Penulisan", "APPLICATION", 1,
    "Apakah huruf pertama dalam perkataan 'awan'?",
    ["a", "w", "n", "i"],
    "A",
    "Perkataan 'awan' bermula dengan huruf 'a'.")
add_bm(15, "Penulisan", "APPLICATION", 1,
    "Susun huruf 'i - n - a - y - a' untuk menjadi perkataan ...",
    ["iyanan", "ainya", "niyana", "yainan"],
    "B",
    "Susunan 'i-n-a-y-a' dibaca 'ainya' — bukan perkataan standard. Jawapan yang sah: 'niat' (i-n-i-a-t). [Pembetulan: soalan ini perlu direka dengan perkataan standard.]\""),
]

# Reset BM — the helper function approach above mixed data and helpers. Let me
# redo cleanly with a proper structure that allows all 100 questions.
