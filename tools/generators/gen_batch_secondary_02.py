# -*- coding: utf-8 -*-
"""Generate batch_secondary_02_sk_bm_t1.json - 25 ORIGINAL T1 BM items.

Per Batch 02 Blueprint v2 (revision PASS):
- 8 Easy / 12 Medium / 5 Hard
- 9 Recognition / 8 Comprehension / 8 Application
- 21 A / 4 B / 0 C
- 8 Tatabahasa / 10 Pemahaman / 3 Penulisan / 3 Kosa Kata / 1 KB
- All NEW passages (no Batch 01 Aiman / Kampung Tanjung Selamat)
- All NEW peribahasa (Batch 01 used "berat sama dipikul, ringan sama dijinjing")
- subjectId = "sk_sec_bm_ms_T1" (exact)
"""
import json
import hashlib
from collections import Counter

SUBJECT_ID = "sk_sec_bm_ms_T1"
BASE_MILLIS = 1727000000000


def make_item(qid, topic, subtopic, learning_focus, skill, diff, diff_pct,
              question_text, options, correct_key, explanation,
              source_tag, confidence, scope_note=None, passage=None):
    """Build a single question dict with required metadata."""
    item = {
        "questionId": qid,
        "subjectId": SUBJECT_ID,
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
        "stage": "secondary",
        "curriculum": "KSSM",
        "gradeLevel_year": "Tingkatan1",
        "gradeLevel": "Tingkatan1",
        "source_tag": source_tag,
        "blueprint_confidence": confidence,
        "sourceReference": "KuizKu ORIGINAL authoring (Phase 10.5 Batch secondary_02_sk_bm_t1); Reference DB has no T1 BM source (T2/T3/T5 secondary BM used only as style/difficulty anchor)"
    }
    if passage:
        item["passage"] = passage
    if scope_note:
        item["scope_note"] = scope_note
    return item


items = []

# ============================================================
# PASSAGES (all NEW, no overlap with Batch 01)
# ============================================================

# Passage P1 (for PM-01 literal "apa") - naratif about a boy named Danial doing a science project
passage_p1 = (
    "Setiap petang, Danial duduk di meja belajar sambil menulis idea. "
    "Idea itu dicatatkan di atas kertas putih, kemudian dilukis dengan pensel warna. "
    "Selepas lukisan siap, Danial menampal kertas itu di dinding biliknya. "
    "Dinding bilik Danial penuh dengan idea-idea baru. Ibu Danial sering melihat "
    "idea-idea itu apabila masuk ke bilik Danial. Danial gembira kerana ibunya "
    "menghargai idea-idea yang diciptakannya."
)

# Passage P2 (for PM-02 literal "bila") - naratif about a girl named Lina learning to ride a bicycle
passage_p2 = (
    "Pada hari Sabtu yang lalu, Lina belajar menunggang basikal di padang kampung. "
    "Awalnya Lina jatuh beberapa kali. Selepas setengah jam, Lina sudah boleh "
    "menunggang basikal dengan seimbang. Ayah Lina sangat bangga dengan pencapaian "
    "Lina. Pada petang itu juga, Lina berjaya menunggang basikal sehingga ke "
    "hujung padang. Lina berasa sangat gembira pada hari itu."
)

# Passage P3 (for PM-03, PM-04 procedural) - how to make a glass of iced tea
passage_p3 = (
    "Cara Membuat Teh Ais\n\n"
    "Bahan: Satu uncang teh, satu sudu besar gula, air panas, dan ais.\n\n"
    "Langkah-langkah:\n"
    "1. Masukkan satu uncang teh ke dalam cawan.\n"
    "2. Tuangkan air panas ke dalam cawan sehingga separuh penuh.\n"
    "3. Tambah satu sudu besar gula ke dalam cawan.\n"
    "4. Kacau sehingga gula larut.\n"
    "5. Masukkan ais ke dalam cawan sehingga penuh.\n"
    "6. Teh ais sedia untuk dihidangkan."
)

# Passage P4 (for PM-05, PM-06 dialog) - short conversation between two students
passage_p4 = (
    "Sara : Hai, Lin. Awak nampak buku Bahasa Melayu aku tak?\n"
    "Linda : Saya nampak tadi dekat meja guru. Cuba awak tanya cikgu.\n"
    "Sara : Baiklah, saya pergi tanya cikgu sekarang.\n"
    "Linda : Hati-hati, ya. Nanti saya tolong awak mencarinya jika guru kata tidak ada.\n"
    "Sara : Terima kasih, Lin. Awak kawan yang baik."
)

# Passage P5 (for PM-07 descriptive - perasaan) - about a student's first day at a new school
passage_p5 = (
    "Pada hari pertama persekolahan, Lina berjalan perlahan ke pintu sekolah baharu. "
    "Jantungnya berdegup kencang apabila melihat ramai pelajar yang lalu-lalang. "
    "Wajah Lina kelihatan serius apabila dia tidak mengenali siapa pun di "
    "sekolah itu. Selepas sejam, Lina tersenyum apabila seorang pelajar datang "
    "menyapanya. Lina kini berasa lebih tenang dan yakin."
)

# Passage P6 (for PM-08 peribahasa without petikan) - sentence-level example (this item is COMPREHENSION with ayat context, no petikan needed)

# Passage P7 (for PM-10 banding dua petikan) - two short paragraphs comparing rural and urban life
passage_p7a = (
    "Petikan A\n\n"
    "Kampung Tanjung Damai terletak di kawasan pergunungan. Rumah-rumah penduduknya "
    "terbuat daripada kayu dan beratapkan nipah. Pada waktu pagi, penduduk kampung "
    "bangun awal untuk bekerja di sawah. Aktiviti gotong-royong sering dijalankan "
    "pada hujung minggu."
)
passage_p7b = (
    "Petikan B\n\n"
    "Bandar Raya Sentosa dipenuhi dengan bangunan pencakar langit. Lalu lintas "
    "sangat sibuk pada waktu pagi dan petang. Penduduk bandar bergantung kepada "
    "pengangkutan awam seperti bas dan teksi untuk bergerak. Aktiviti bersukan "
    "lebih banyak dilakukan di gimnasium tertutup."
)

# ============================================================
# ITEMS
# ============================================================

# ============== TATABAHASA (8 items) ==============

# T2BM-TA-01: Kata adjektif - APPLICATION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-001",
    "Tatabahasa", "Kata adjektif",
    "Mengenal pasti dan memilih kata adjektif yang sesuai",
    "APPLICATION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Pilih kata adjektif yang sesuai untuk melengkapkan ayat: "Bunga itu sangat __________ di tepi jalan."',
    {"a": "berlari", "b": "cantik", "c": "membaca", "d": "tidur"},
    "b",
    "'Cantik' ialah kata adjektif yang sesuai untuk menggambarkan bunga. 'Berlari/membaca/tidur' ialah kata kerja, bukan kata adjektif.",
    "CURRICULUM_DERIVED", "A"
))

# T2BM-TA-02: Kata adjektif darjah - APPLICATION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-002",
    "Tatabahasa", "Kata adjektif darjah",
    "Membandingkan kata adjektif darjah (positif / komparatif / superlatif)",
    "APPLICATION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Antara ayat berikut, yang manakah menggunakan kata adjektif pada darjah komparatif (bandingan)?',
    {"a": "Rumah ini besar.", "b": "Rumah ini lebih besar daripada rumah itu.", "c": "Rumah ini terbesar di kampung.", "d": "Rumah ini sebuah rumah besar."},
    "b",
    "'Lebih besar daripada' adalah darjah komparatif. 'Besar' = positif; 'terbesar' = superlatif; 'sebuah rumah besar' = frasa adjektif (bukan darjah).",
    "CURRICULUM_DERIVED", "A"
))

# T2BM-TA-03: Bentuk kata ganda - RECOGNITION Easy B
items.append(make_item(
    "v5-t1-bm-sec2-003",
    "Tatabahasa", "Bentuk kata",
    "Mengenal pasti kata ganda",
    "RECOGNITION", 1,
    {"easy": 100, "medium": 0, "hard": 0},
    'Antara perkataan berikut, yang manakah merupakan kata ganda?',
    {"a": "rumah-rumah", "b": "berlari", "c": "cantik", "d": "makan"},
    "a",
    "'Rumah-rumah' ialah kata ganda (berulang). 'Berlari/cantik/makan' ialah kata dasar (bukan ganda).",
    "INFERRED", "B"
))

# T2BM-TA-04: Bentuk kata dasar vs terbitan - RECOGNITION Easy A
items.append(make_item(
    "v5-t1-bm-sec2-004",
    "Tatabahasa", "Bentuk kata",
    "Membezakan kata dasar vs kata terbitan",
    "RECOGNITION", 1,
    {"easy": 100, "medium": 0, "hard": 0},
    'Antara perkataan berikut, yang manakah merupakan kata terbitan (mengandungi imbuhan)?',
    {"a": "makan", "b": "tidur", "c": "pelajar", "d": "minum"},
    "c",
    "'Pelajar' = kata terbitan (imbuhan 'pe-' + 'ajar'). 'Makan/tidur/minum' = kata dasar (tiada imbuhan).",
    "CURRICULUM_DERIVED", "A"
))

# T2BM-TA-05: Kata ganti nama milik - RECOGNITION Easy A
items.append(make_item(
    "v5-t1-bm-sec2-005",
    "Tatabahasa", "Kata ganti nama",
    "Mengenal pasti kata ganti nama milik (saya/kita/kami/kamu)",
    "RECOGNITION", 1,
    {"easy": 100, "medium": 0, "hard": 0},
    'Pilih kata ganti nama milik yang betul untuk melengkapkan ayat: "Ali dan saya pergi ke sekolah. __________ bersekolah di Bandar Seri Begawan."',
    {"a": "Saya", "b": "Dia", "c": "Kami", "d": "Mereka"},
    "c",
    "'Ali dan saya' = dua orang (pertama + pertama jamak). Kata ganti nama milik yang betul = 'kami'. 'Saya' untuk diri sendiri; 'dia/mereka' untuk orang ketiga.",
    "CURRICULUM_DERIVED", "A"
))

# T2BM-TA-06: Kata hubung pancangan - APPLICATION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-006",
    "Tatabahasa", "Kata hubung",
    "Mengenal pasti kata hubung pancangan (supaya/untuk)",
    "APPLICATION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Pilih kata hubung yang betul untuk melengkapkan ayat: "Ahmad belajar dengan tekun __________ dia memperoleh keputusan yang cemerlang."',
    {"a": "atau", "b": "supaya", "c": "tetapi", "d": "walaupun"},
    "b",
    "'Supaya' menunjukkan tujuan/hasrat. 'Ahmad belajar... supaya memperoleh' = bertujuan. 'Untuk' juga boleh digunakan tetapi 'supaya' lebih standard untuk matlamat. 'Atau/tetapi/walaupun' tidak sesuai.",
    "CURRICULUM_DERIVED", "A"
))

# T2BM-TA-07: Kata hubung syarat - APPLICATION Medium B
items.append(make_item(
    "v5-t1-bm-sec2-007",
    "Tatabahasa", "Kata hubung",
    "Mengisi tempat kosong dengan kata hubung syarat (jika)",
    "APPLICATION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Pilih kata hubung syarat yang betul: "__________ hujan turun, kita tidak akan pergi ke sekolah."',
    {"a": "atau", "b": "tetapi", "c": "jika", "d": "supaya"},
    "c",
    "'Jika' adalah kata hubung syarat. 'Jika hujan turun' = kalau hujan turun. 'Atau/tetapi/supaya' bukan untuk menunjukkan syarat/keadaan.",
    "INFERRED", "B"
))

# T2BM-TA-08: Bentuk kata pinjaman - RECOGNITION Easy A
items.append(make_item(
    "v5-t1-bm-sec2-008",
    "Tatabahasa", "Bentuk kata",
    "Mengenal pasti kata pinjaman dalam ayat BM",
    "RECOGNITION", 1,
    {"easy": 100, "medium": 0, "hard": 0},
    'Antara perkataan berikut, yang manakah merupakan kata pinjaman (dipinjam dari bahasa lain)?',
    {"a": "rumah", "b": "buku", "c": "sekolah", "d": "comel"},
    "d",
    "'Comel' dipinjam daripada bahasa Inggeris 'cute'. 'Rumah/buku/sekolah' ialah kata asas Melayu (walaupun asalnya daripada Sanskrit, ia sudah diterima sepenuhnya dalam BM).",
    "CURRICULUM_DERIVED", "A"
))

# ============== PEMAHAMAN (10 items) ==============

# T2BM-PM-01: Naratif literal "apa" - RECOGNITION Easy A
items.append(make_item(
    "v5-t1-bm-sec2-009",
    "Pemahaman", "Petikan naratif",
    "Literal 'apa' dalam petikan naratif",
    "RECOGNITION", 1,
    {"easy": 100, "medium": 0, "hard": 0},
    'Baca petikan:\n\n"' + passage_p1 + '"\n\nApakah yang dicatatkan Danial di atas kertas putih?',
    {"a": "Lukisan pemandangan", "b": "Idea", "c": "Surat", "d": "Senarai nama"},
    "b",
    "Petikan menyatakan 'Idea itu dicatatkan di atas kertas putih' — Danial menulis idea di atas kertas.",
    "CURRICULUM_DERIVED", "A",
    passage=passage_p1
))

# T2BM-PM-02: Naratif literal "bila" - RECOGNITION Easy A
items.append(make_item(
    "v5-t1-bm-sec2-010",
    "Pemahaman", "Petikan naratif",
    "Literal 'bila' dalam petikan naratif",
    "RECOGNITION", 1,
    {"easy": 100, "medium": 0, "hard": 0},
    'Baca petikan:\n\n"' + passage_p2 + '"\n\nBilakah Lina belajar menunggang basikal?',
    {"a": "Pada hari Ahad", "b": "Pada hari Sabtu", "c": "Pada hari Jumaat", "d": "Pada hari Isnin"},
    "b",
    "Petikan menyatakan 'Pada hari Sabtu yang lalu, Lina belajar menunggang basikal' — Sabtu.",
    "CURRICULUM_DERIVED", "A",
    passage=passage_p2
))

# T2BM-PM-03: Prosedural pemahaman langkah - COMPREHENSION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-011",
    "Pemahaman", "Petikan prosedural",
    "Memahami langkah dalam teks prosedural",
    "COMPREHENSION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Baca petikan:\n\n"' + passage_p3 + '"\n\nMengapakah uncang teh dimasukkan ke dalam cawan terlebih dahulu?',
    {"a": "Supaya teh tidak tumpah.", "b": "Supaya teh dapat direndam di dalam air panas untuk mengeluarkan rasanya.", "c": "Supaya gula boleh larut.", "d": "Supaya ais boleh sejukkan teh."},
    "b",
    "Langkah prosedural memasukkan uncang teh dahulu supaya teh dapat direndam di dalam air panas untuk mengeluarkan rasanya — logik prosedur memerlukan teh direndam sebelum ditambah bahan lain.",
    "CURRICULUM_DERIVED", "A",
    passage=passage_p3
))

# T2BM-PM-04: Prosedural susun langkah - APPLICATION Hard A
items.append(make_item(
    "v5-t1-bm-sec2-012",
    "Pemahaman", "Petikan prosedural",
    "Menyusun langkah mengikut urutan yang betul",
    "APPLICATION", 3,
    {"easy": 0, "medium": 0, "hard": 100},
    'Baca petikan:\n\n"' + passage_p3 + '"\n\nYang manakah susunan langkah yang betul untuk membuat teh ais?',
    {"a": "Masukkan uncang teh -> masukkan ais -> tambah gula -> tuang air panas",
 "b": "Tuang air panas -> masukkan uncang teh -> tambah gula -> masukkan ais",
    "c": "Masukkan uncang teh -> tuang air panas -> tambah gula -> kacau -> masukkan ais",
    "d": "Tambah gula -> masukkan ais -> tuang air panas -> masukkan uncang teh"},
    "c",
    "Urutan betul mengikut prosedur: uncang teh (1) -> air panas (2) -> gula (3) -> kacau (4) -> ais (5). Pilihan C mengikut urutan prosedur dalam petikan.",
    "CURRICULUM_DERIVED", "A",
    passage=passage_p3
))

# T2BM-PM-05: Dialog respons watak - COMPREHENSION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-013",
    "Pemahaman", "Petikan dialog",
    "Memahami respons watak dalam dialog",
    "COMPREHENSION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Baca dialog:\n\n"' + passage_p4 + '"\n\nApakah respons Linda terhadap Sara?',
    {"a": "Linda menasihati Sara supaya tidak mencari buku.", "b": "Linda bersetuju untuk membantu Sara mencarikan buku jika cikgu kata tidak ada.", "c": "Linda tidak kisah tentang masalah Sara.", "d": "Linda menyuruh Sara pulang ke rumah."},
    "b",
    "Linda berkata 'Nanti saya tolong awak mencarinya jika guru kata tidak ada' — Linda menawarkan bantuan jika diperlukan.",
    "CURRICULUM_DERIVED", "A",
    passage=passage_p4
))

# T2BM-PM-06: Dialog mesej/tujuan - COMPREHENSION Hard A
items.append(make_item(
    "v5-t1-bm-sec2-014",
    "Pemahaman", "Petikan dialog",
    "Memahami mesej / tujuan dialog",
    "COMPREHENSION", 3,
    {"easy": 0, "medium": 0, "hard": 100},
    'Baca dialog:\n\n"' + passage_p4 + '"\n\nApakah tujuan utama dialog antara Sara dan Linda?',
    {"a": "Untuk bercanda", "b": "Untuk menunjukkan persahabatan dan saling membantu mencari buku yang hilang", "c": "Untuk berbincang tentang guru", "d": "Untuk membuat kerja sekolah"},
    "b",
    "Dialog menunjukkan Sara meminta pertolongan Linda untuk mencari buku yang hilang, dan Linda dengan sukarela membantu. Mesej dialog = persahabatan dan saling membantu.",
    "CURRICULUM_DERIVED", "A",
    passage=passage_p4
))

# T2BM-PM-07: Deskriptif perasaan - RECOGNITION Easy A
items.append(make_item(
    "v5-t1-bm-sec2-015",
    "Pemahaman", "Petikan deskriptif",
    "Mengenal pasti perasaan dalam petikan",
    "RECOGNITION", 1,
    {"easy": 100, "medium": 0, "hard": 0},
    'Baca petikan:\n\n"' + passage_p5 + '"\n\nApakah perasaan Lina selepas seorang pelajar menyapanya?',
    {"a": "Sedih", "b": "Takut", "c": "Lebih tenang dan yakin", "d": "Marah"},
    "c",
    "Petikan menyatakan 'Lina kini berasa lebih tenang dan yakin' — perasaan Lina selepas disapa ialah lebih tenang dan yakin.",
    "CURRICULUM_DERIVED", "A",
    passage=passage_p5
))

# T2BM-PM-08: Peribahasa dalam ayat - COMPREHENSION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-016",
    "Pemahaman", "Peribahasa",
    "Memahami maksud peribahasa dalam konteks ayat (tanpa petikan)",
    "COMPREHENSION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Apakah maksud peribahasa "kera di hutan disusukan, anak di rumah mati kelaparan"?',
    {"a": "Orang yang menjaga haiwan liar akan kelaparan.", "b": "Orang yang sibuk menguruskan hal orang lain sehingga mengabaikan keluarga sendiri.", "c": "Haiwan di hutan lebih penting daripada manusia.", "d": "Makanan di hutan lebih berkhasiat daripada di rumah."},
    "b",
    "'Kera di hutan disusukan, anak di rumah mati kelaparan' bermaksud seseorang yang sibuk menjaga/memberi perhatian kepada hal orang lain sehingga mengabaikan keperluan sendiri atau keluarga sendiri.",
    "CURRICULUM_DERIVED", "A"
))

# T2BM-PM-09: Peribahasa sesuai situasi - APPLICATION Hard A
items.append(make_item(
    "v5-t1-bm-sec2-017",
    "Pemahaman", "Peribahasa",
    "Memilih peribahasa yang sesuai dengan situasi",
    "APPLICATION", 3,
    {"easy": 0, "medium": 0, "hard": 100},
    'Kawan kamu selalu ketinggalan beg di merata tempat. Peribahasa manakah yang paling sesuai untuk menggambarkan sikapnya?',
    {"a": "Berat sama dipikul, ringan sama dijinjing.", "b": "Hendak seribu daya, tak hendak seribu daya juga.", "c": "Hendak berkawan jangan berkawan dengan yang liar.", "d": "Malang tidak berbau."},
    "b",
    "'Hendak seribu daya, tak hendak seribu daya juga' bermaksud jika ada kemahuan, banyak cara akan dicari; jika tiada kemahuan, banyak alasan pula. Sesuai untuk kawan yang selalu lupa/ketinggalan (tiada usaha).",
    "CURRICULUM_DERIVED", "A"
))

# T2BM-PM-10: Banding dua petikan - COMPREHENSION Hard B
items.append(make_item(
    "v5-t1-bm-sec2-018",
    "Pemahaman", "Banding dua petikan",
    "Membandingkan dua petikan pendek (persamaan / perbezaan)",
    "COMPREHENSION", 3,
    {"easy": 0, "medium": 0, "hard": 100},
    'Baca kedua-dua petikan:\n\n"' + passage_p7a + '\n\n' + passage_p7b + '"\n\nApakah satu perbezaan utama antara kehidupan di kampung dan di bandar?',
    {"a": "Penduduk kampung dan bandar sama-sama pergi ke sawah.", "b": "Kampung menggunakan kayu sebagai bahan rumah, manakala bandar dipenuhi bangunan pencakar langit.", "c": "Penduduk bandar suka bersukan, manakala penduduk kampung tidak suka bersukan.", "d": "Kampung dan bandar tidak mempunyai penduduk."},
    "b",
    "Petikan A menyebut rumah penduduk kampung 'terbuat daripada kayu dan beratapkan nipah'. Petikan B menyebut 'Bandar Raya Sentosa dipenuhi dengan bangunan pencakar langit'. Perbezaan utama = bahan rumah.",
    "INFERRED", "B",
    passage=f"{passage_p7a}\n\n{passage_p7b}"
))

# ============== PENULISAN (3 items) ==============

# T2BM-PN-01: Jenis karangan - COMPREHENSION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-019",
    "Penulisan", "Jenis karangan",
    "Membezakan naratif vs deskriptif",
    "COMPREHENSION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Karangan jenis "Saya menceritakan peristiwa lawatan ke zoo" menggunakan perenggan pendahuluan, isi yang mengikut urutan masa, dan perenggan penutup. Apakah jenis karangan ini?',
    {"a": "Karangan deskriptif", "b": "Karangan naratif", "c": "Karangan ekspositori", "d": "Karangan argumentatif"},
    "b",
    "Ciri-ciri karangan naratif: menceritakan peristiwa/peristiwa secara kronologi (urutan masa). 'Saya menceritakan peristiwa lawatan' menunjukkan naratif (peristiwa + urutan masa).",
    "CURRICULUM_DERIVED", "A"
))

# T2BM-PN-02: Tanda baca - RECOGNITION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-020",
    "Penulisan", "Tanda baca",
    "Memilih ayat dengan tanda baca betul",
    "RECOGNITION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Antara ayat berikut, yang manakah menggunakan tanda baca dengan betul?',
    {"a": "Kamu pergi ke sekolah.",
    "b": "Kamu pergi, ke sekolah.",
    "c": "Kamu pergi ke sekolah?",
    "d": "Kamu pergi ke sekolah!"},
    "c",
    "Tanda soal (?) digunakan pada akhir ayat tanya. (a) tamat dengan noktah (pernyataan). (b) salah — koma antara subjek dan predikat. (d) tidak sesuai —seruan boleh tetapi tidak sesuai konteks. (c) betul ayat tanya.",
    "CURRICULUM_DERIVED", "A"
))

# T2BM-PN-03: Jenis ayat tunggal vs majmuk - COMPREHENSION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-021",
    "Penulisan", "Ayat",
    "Membezakan ayat tunggal vs ayat majmuk",
    "COMPREHENSION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Antara ayat berikut, yang manakah merupakan ayat majmuk?',
    {"a": "Ali tidur.", "b": "Ali membaca buku.", "c": "Ali membaca buku sedangkan adiknya bermain.", "d": "Adiknya bermain."},
    "c",
    "Ayat majmuk mengandungi dua klausa atau lebih yang digabungkan dengan kata hubung. 'Ali membaca buku sedangkan adiknya bermain' mempunyai dua klausa (Ali membaca buku + adiknya bermain) digabungkan dengan 'sedangkan'.",
    "CURRICULUM_DERIVED", "A"
))

# ============== KOSA KATA (3 items) ==============

# T2BM-KK-01: Istilah teknikal - APPLICATION Hard B
items.append(make_item(
    "v5-t1-bm-sec2-022",
    "Kosa Kata", "Istilah",
    "Memilih perkataan sesuai untuk konteks teknikal",
    "APPLICATION", 3,
    {"easy": 0, "medium": 0, "hard": 100},
    'Dalam kelas sains, guru berkata: "Sebelum menjalankan eksperimen, pelajar perlu memahami __________ eksperimen terlebih dahulu." Apakah perkataan yang sesuai untuk mengisi tempat kosong?',
    {"a": "kaedah", "b": "cerita", "c": "nyanyian", "d": "lukisan"},
    "a",
    "'Kaedah' adalah istilah saintifik/teknikal yang sesuai bermaksud cara melakukan sesuatu. 'Cerita/nyanyian/lukisan' bukan istilah saintifik.",
    "INFERRED", "B"
))

# T2BM-KK-02: Simpulan bahasa sesuai konteks - APPLICATION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-023",
    "Kosa Kata", "Simpulan bahasa",
    "Memilih simpulan bahasa yang sesuai konteks",
    "APPLICATION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Sahabat kamu kehilangan dompet di suatu tempat. Kamu ingin menyatakan bahawa kehilangan itu pasti akan ditemukan. Simpulan bahasa manakah yang paling sesuai?',
    {"a": "Hendak seribu daya, tak hendak seribu daya juga.", "b": "Sepandai-pandai tupai melompat, akhirnya jatuh ke tanah juga.", "c": "Bulat air kerana pembetung.", "d": "Hendak berkawan jangan berkawan dengan yang liar."},
    "b",
    "'Sepandai-pandai tupai melompat, akhirnya jatuh ke tanah juga' bermaksud walau pandai atau licik, akhirnya akan terbongkar juga. Sesuai untuk mengatakan kehilangan pasti ditemukan.",
    "CURRICULUM_DERIVED", "A"
))

# T2BM-KK-03: Ejaan - RECOGNITION Easy A
items.append(make_item(
    "v5-t1-bm-sec2-024",
    "Kosa Kata", "Ejaan",
    "Mengeja perkataan BM dengan tepat",
    "RECOGNITION", 1,
    {"easy": 100, "medium": 0, "hard": 0},
    'Antara pilihan berikut, ejaan yang manakah betul?',
    {"a": "sekolah", "b": "sekola", "c": "sekollah", "d": "sekolaah"},
    "a",
    "'Sekolah' dieja dengan satu 'h' di akhir. (b) tiada 'h'. (c) dua 'l'. (d) dua 'a'.",
    "CURRICULUM_DERIVED", "A"
))

# ============== KEMAHIRAN BERBAHASA (1 item) ==============

# T2BM-KB-01: Tujuan teks - COMPREHENSION Medium A
items.append(make_item(
    "v5-t1-bm-sec2-025",
    "Kemahiran Berbahasa", "Tujuan teks",
    "Mengenal pasti tujuan teks (instruksi / naratif / deskripsi)",
    "COMPREHENSION", 2,
    {"easy": 0, "medium": 100, "hard": 0},
    'Teks "Cara Membuat Teh Ais" mengandungi senarai bahan dan langkah-langkah yang perlu diikuti. Apakah tujuan utama teks ini?',
    {"a": "Untuk menceritakan kisah", "b": "Untuk menggambarkan tempat", "c": "Untuk memberi panduan / instruksi", "d": "Untuk membincangkan isu"},
    "c",
    "Teks yang mengandungi 'senarai bahan + langkah-langkah' = teks instruksi/ prosedur. Tujuannya memberi panduan cara melakukan sesuatu.",
    "CURRICULUM_DERIVED", "A"
))

# Sort by ID
items.sort(key=lambda x: x['questionId'])

# Build metadata
batch = {
    "metadata": {
        "batch_id": "batch_secondary_02_sk_bm_t1",
        "phase": "10.5",
        "schoolTrack": "SK",
        "stage": "secondary",
        "language": "ms",
        "grade": "Tingkatan1",
        "subject": "Bahasa Melayu",
        "subjectCode": "bm",
        "subjectId": SUBJECT_ID,
        "curriculum": "KSSM",
        "questionType": "SINGLE_CHOICE",
        "totalQuestions": 25,
        "difficultyDistribution": {
            "easy": 8,
            "medium": 12,
            "hard": 5
        },
        "note": "Phase 10.5 Batch secondary_02_sk_bm_t1 - T1 BM original authoring. Coverage-extension of Batch 01 (different peribahasa, different passages, different question intents). Reference DB does NOT contain T1 BM source questions. T2/T3 used only as style/difficulty anchor. Primary T5/T6 NOT used as T1 source. See secondary_t1_bm_batch02_blueprint.md for full source audit and scope review.",
        "reference_db_status": "NO_T1_BM_FILES",
        "reference_db_anchors_used": [
            "references/BM/T2/mid-year-styleanchor.docx (style anchor)",
            "references/BM/T3/difficulty-ceiling.docx (difficulty ceiling)",
            "references/BM/T5/difficulty-reference.docx (difficulty ceiling)",
            "references/BM/T2/penjodoh-styleref.pdf (style anchor)"
        ],
        "batch_01_compatibility": "Coverage-extension only. No duplicate topics, no duplicate peribahasa, no duplicate passages."
    },
    "questions": items
}

# Write JSON
OUTPUT = r'D:\Users\bajub\kuizku_p10\batch_secondary_02_sk_bm_t1.json'
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

# Distributions
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

strand_count = Counter(q['topic'] for q in items)
print('\nTopic:')
for t, c in sorted(strand_count.items()):
    print(f'  {t}: {c}')

# List all question IDs
print('\nQuestion IDs:')
for q in items:
    print(f'  {q["questionId"]} | {q["topic"]} | {q["subtopic"]} | skill={q["skillType"]} | diff={q["difficulty"]} | conf={q["blueprint_confidence"]} | source={q["source_tag"]}')
