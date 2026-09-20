# Phase 10.4 — KuizKu Primary Content Master Blueprint

> **READ-ONLY BLUEPRINT. NO questions generated. NO Android code modified. NO V3/V4-TEST/Reference DB touched. NO commit. NO push. NO Play upload.**
>
> Built on Phase 10.3 multi-track schema (`2f790b1`). Phase 10.1 JSON SHA preserved (`72ca4e4586...`).

---

## 1. Current Baseline

| Source | Total Q | Subjects | Grades | Track | Language | Subject mix |
|---|---:|---:|---|---|---|---|
| **V3 production** (`/v3/`) | 30 | 27 | T1–T6 | SK (implicit) | ms only | 100% Bahasa Melayu |
| **V4-TEST pilot** (`/v4-test/`) | 92 | 12 | T1–T5 | SK (implicit) | ms only | 100% Bahasa Melayu |
| **Phase 10.1 pilot** (local, not deployed) | 100 | 4 | T1 only | SK (implicit) | 80 ms + 20 en | BM 30 + Math 28 + Science 22 + English 20 |
| **Reference DB primary** | 140 source files | BM 18 + Math 77 + Science 28 + English 17 | T1–T6 | mixed (Malaysian UASA/UPSA + Chinese workbooks for T2/T3) | mixed | READ-ONLY reference only |
| **Reference DB Chinese** (`secondary/Chinese/`) | 15 files | T2–T5 secondary only | n/a | secondary | zh | **NO primary Chinese coverage** |

**Net gap**: 5 of 12 (Track × Subject × Language) combinations have ZERO production content:
- SK Mathematics (none in V3/V4-TEST/pilot)
- SK Science (none in V3/V4-TEST/pilot)
- SJKC Chinese (none anywhere)
- SJKC Mathematics (none)
- SJKC Science (none)
- International English-native (V3/V4-TEST SK English is MFL, not native-level)
- International Mathematics (none)
- International Science (none)

Phase 10.4 must design around this gap. Reference DB is READ-ONLY — it cannot be expanded. All gap content must be 100% KuizKu ORIGINAL.

---

## 2. Final Track Matrix

Three Primary school tracks, each with explicit `curriculum`:

| Track | curriculum enum | Curriculum source | Default medium |
|---|---|---|---|
| SK | `KSSR` | KSSR (Standard-Based Curriculum for Primary Schools, Malaysia) | ms |
| SJKC | `KSSR_SJKC` | KSSR adapted for SJKC (Chinese-medium primary) | zh |
| International | `CAMBRIDGE_PRIMARY` | Cambridge Primary / equivalent international curriculum | en |

---

## 3. Grade Matrix

Primary = Tahun 1..6 (all 3 tracks). **Single canonical form: `"Tahun<n>"`** (e.g., `"Tahun1"`, `"Tahun5"`).

| Track | Grade display | Canonical storage | subjectId grade segment |
|---|---|---|---|
| SK | Tahun 1..6 | `"Tahun<n>"` | `Y<n>` (e.g., `***`) |
| SJKC | Tahun 1..6 | `"Tahun<n>"` | `Y<n>` |
| International | Year 1..6 (display) / `"Tahun<n>"` (storage canonical) | `Y<n>` |

Per 638 §六: "请明确内部 gradeLevel 的规范格式" → ALL storage uses `"Tahun<n>"`. International UI displays "Year" but storage stays canonical.

---

## 4. Subject Matrix

Per 638 §五: "不要把不同 Track 简单视为 UI label. School Track 会影响 curriculum / subject structure / language / grade/year / topic scope / difficulty / question style".

### SK (4 subjects)

| Subject | subjectCode | language | Native | Reference DB coverage |
|---|---|---|---|---|
| Bahasa Melayu | bm | ms | ✅ Native | 🟢 Strong (18 files T1-T6) |
| English | en | en | MFL | 🟡 Moderate (17 files T1-T6, MFL-level) |
| Mathematics | math | ms | ✅ (Malay-medium) | 🟢 Strong (77 files T1-T6) |
| Science | science | ms | ✅ (Malay-medium) | 🟡 Moderate (28 files T1-T6, T4-T6 weak) |

### SJKC (5 subjects)

| Subject | subjectCode | language | Native | Reference DB coverage |
|---|---|---|---|---|
| 中文 (华文 / Bahasa Cina) | bc | zh | ✅ Native | ❌ **NO primary Chinese coverage** (only secondary 15 files) |
| Bahasa Melayu | bm | ms | MFL | 🟢 Strong (BM files apply cross-track) |
| English | en | en | MFL | 🟡 Moderate |
| Mathematics | math | zh | ✅ (Chinese-medium) | ❌ **NO Chinese-medium math references** |
| Science | science | zh | ✅ (Chinese-medium) | ❌ **NO Chinese-medium science references** |

### International (3 subjects)

| Subject | subjectCode | language | Native | Reference DB coverage |
|---|---|---|---|---|
| English | en | en | ✅ Native (literature + composition) | ⚠️ Mismatch — Reference DB has Malaysian MFL English only |
| Mathematics | math | en | ✅ (English-medium) | ❌ NO English-medium math references |
| Science | science | en | ✅ (English-medium) | ❌ NO English-medium science references |

**Conclusion per 638 §五**:
- SK is well-supported by Reference DB (mostly) — generation is feasible.
- SJKC has only 1/5 subjects with usable Reference DB (BM). **Math/Science/Chinese need independent ORIGINAL authoring from KSSR_SJKC syllabus** (no source material available locally — KuizKu product decision).
- International has 0/3 subjects with usable Reference DB at native level. **All English-native, Math, Science need independent ORIGINAL authoring from Cambridge Primary curriculum** (no source material available locally — KuizKu product decision).

**KuizKu product decision required**: Should we expand Reference DB or rely 100% on syllabus knowledge for SJKC Math/Science/Chinese + International Math/Science/English? Per current state, **all gap content is 100% ORIGINAL**.

---

## 5. Language Matrix (per 638 §三: NO direct translation between languages)

Each `(Track × Grade × Subject)` combination must produce **independently authored** questions per `language`. The "no direct translation" rule means:

- `sk_prim_math_ms_Y5` ≠ translated copy of `sk_prim_math_en_Y5`
- `skc_prim_math_zh_Y5` ≠ translated copy of `sk_prim_math_ms_Y5`
- `intl_prim_math_en_Y5` ≠ translated copy of `sk_prim_math_en_Y5`

All 3+ variants of Math are **separate ORIGINAL authoring** with shared knowledge point + shared skill + shared difficulty target, but distinct wording/numbers/context/distractors.

### Per-subject language matrix

| Subject | SK | SJKC | International |
|---|---|---|---|
| Bahasa Melayu | ms (native) | ms (MFL) | n/a |
| English | en (MFL) | en (MFL) | en (native) |
| 中文 | n/a | zh (native) | n/a |
| Mathematics | ms (BM-medium) | zh (BC-medium) | en (EN-medium) |
| Science | ms (BM-medium) | zh (BC-medium) | en (EN-medium) |

Note: SK BM is the SAME language as SJKC BM (ms), but they're taught differently — separate authoring.

---

## 6. Recommended Question Counts

Two plans per 638 §四. **Both include V3/V4-TEST/Phase 10.1 as already-existing content (not regenerated)**.

### Plan A — Conservative (first formal production batch)

Target: each Grade × Track × Subject × Language = **25 Q**. Mathematics & Science = **30 Q**. Lower grades (T1-T2) = fewer topics so same count feasible; higher grades (T5-T6) = more topics = need more.

| Track | Grade | Subject | Lang | Q (Plan A) | Easy | Med | Hard |
|---|---|---|---|---:|---:|---:|---:|
| SK | T1-T6 | Bahasa Melayu | ms | 25 × 6 = **150** | 15 | 7 | 3 |
| SK | T1-T6 | English | en | 25 × 6 = **150** | 15 | 7 | 3 |
| SK | T1-T6 | Mathematics | ms | 30 × 6 = **180** | 18 | 9 | 3 |
| SK | T1-T6 | Science | ms | 30 × 6 = **180** | 18 | 9 | 3 |
| SJKC | T1-T6 | 中文 | zh | 25 × 6 = **150** | 15 | 7 | 3 |
| SJKC | T1-T6 | Bahasa Melayu | ms | 25 × 6 = **150** | 15 | 7 | 3 |
| SJKC | T1-T6 | English | en | 25 × 6 = **150** | 15 | 7 | 3 |
| SJKC | T1-T6 | Mathematics | zh | 30 × 6 = **180** | 18 | 9 | 3 |
| SJKC | T1-T6 | Science | zh | 30 × 6 = **180** | 18 | 9 | 3 |
| International | Y1-Y6 | English (native) | en | 30 × 6 = **180** | 18 | 9 | 3 |
| International | Y1-Y6 | Mathematics | en | 30 × 6 = **180** | 18 | 9 | 3 |
| International | Y1-Y6 | Science | en | 30 × 6 = **180** | 18 | 9 | 3 |
| **TOTAL** | | | | **1,830 Q** | | | |

**Plan A breakdown**:
- Total questions: **1,830**
- Total subject IDs: **36** (12 combinations × 6 grades, but actually 12 Track×Subject × 6 grades = 72 subjectIds — let me recompute)

**Recompute subject IDs**:
- SK: 4 subjects × 6 grades = 24 subjectIds
- SJKC: 5 subjects × 6 grades = 30 subjectIds
- International: 3 subjects × 6 grades = 18 subjectIds
- **Total subject IDs: 24 + 30 + 18 = 72**

**Plan A totals** (recomputed):
- Total questions: **1,830**
- Total subject IDs: **72**
- Total (Track × Grade × Subject × Language) combinations: **72** (one subjectId per combination)
- Total subjects (track × subjectCode): **12** (4 SK + 5 SJKC + 3 International)

### Plan B — Large (token-utilization friendly)

Target: each Grade × Track × Subject × Language = **40 Q** for languages / 50 Q for Mathematics / Science.

| Track | Grade | Subject | Lang | Q (Plan B) | Easy | Med | Hard |
|---|---|---|---|---:|---:|---:|---:|
| SK | T1-T6 | Bahasa Melayu | ms | 40 × 6 = **240** | 22 | 12 | 6 |
| SK | T1-T6 | English | en | 40 × 6 = **240** | 22 | 12 | 6 |
| SK | T1-T6 | Mathematics | ms | 50 × 6 = **300** | 27 | 16 | 7 |
| SK | T1-T6 | Science | ms | 50 × 6 = **300** | 27 | 16 | 7 |
| SJKC | T1-T6 | 中文 | zh | 40 × 6 = **240** | 22 | 12 | 6 |
| SJKC | T1-T6 | Bahasa Melayu | ms | 40 × 6 = **240** | 22 | 12 | 6 |
| SJKC | T1-T6 | English | en | 40 × 6 = **240** | 22 | 12 | 6 |
| SJKC | T1-T6 | Mathematics | zh | 50 × 6 = **300** | 27 | 16 | 7 |
| SJKC | T1-T6 | Science | zh | 50 × 6 = **300** | 27 | 16 | 7 |
| International | Y1-Y6 | English (native) | en | 50 × 6 = **300** | 27 | 16 | 7 |
| International | Y1-Y6 | Mathematics | en | 50 × 6 = **300** | 27 | 16 | 7 |
| International | Y1-Y6 | Science | en | 50 × 6 = **300** | 27 | 16 | 7 |
| **TOTAL** | | | | **3,300 Q** | | | |

**Plan B totals**:
- Total questions: **3,300**
- Total subject IDs: **72** (same combination count, more Q per subjectId)
- Total (Track × Grade × Subject × Language) combinations: **72**

### Plan comparison

| Metric | Plan A (Conservative) | Plan B (Large) |
|---|---:|---:|
| Total questions | 1,830 | 3,300 |
| Total subject IDs | 72 | 72 |
| Total (Track × Grade × Subject × Language) | 72 | 72 |
| Total subject types (Track × SubjectCode) | 12 | 12 |
| Avg Q per (Track × Grade × Subject × Language) | ~25 | ~46 |
| Effort | ~30 batches of ~60 Q each | ~30 batches of ~110 Q each |
| Existing content reusable (V3+V4-T+Phase 10.1) | 222 Q (V3 30 + V4T 92 + P10.1 100) | same |
| NEW content to author | 1,608 Q | 3,078 Q |

**Note**: Existing V3/V4-TEST/Phase 10.1 content is **NOT** counted toward the new content — they remain as legacy banks. Phase 10.5+ builds will use this blueprint to author NEW banks.

---

## 7. Difficulty Distribution (per 638 §七)

Why different grades have different difficulty proportions:
- T1-T2 (age 7-8): basic recognition, recall — heavy Easy
- T3-T4 (age 9-10): application begins — Easy + Medium dominant
- T5-T6 (age 11-12): analytical thinking, UPSR prep — Medium + Hard dominant

| Grade | Easy % | Medium % | Hard % | Rationale |
|---|---:|---:|---:|---|
| T1 (Year 1) | 60 | 30 | 10 | Recognition-heavy; minimal application |
| T2 (Year 2) | 55 | 35 | 10 | Recall + simple application |
| T3 (Year 3) | 50 | 38 | 12 | Application begins; UPSR Year 3 prep |
| T4 (Year 4) | 45 | 40 | 15 | Problem-solving emerges |
| T5 (Year 5) | 38 | 45 | 17 | UPSR Year 5/6 prep — analytical |
| T6 (Year 6) | 35 | 45 | 20 | UPSR Year 6 — peak analytical complexity |

Sum per row = 100. **Not equal distribution** per 638 §七: "不要为了凑数字而平均分配".

### Per-subject difficulty adjustment

| Subject | Easy bias | Hard bias | Rationale |
|---|:---:|:---:|---|
| Bahasa Melayu (native) | +5% | -5% | Comprehension / writing tends to be harder than math mechanics |
| English (MFL) | +10% | -10% | Foreign language — comprehension is harder at low grades |
| 中文 (native, SJKC) | +5% | -5% | Similar to BM |
| English (native, International) | -5% | +5% | Native — slightly harder than MFL English |
| Mathematics | 0% | 0% | Baseline |
| Science | -5% | +5% | Science comprehension requires higher reading at upper grades |

These adjustments apply **on top of** the per-grade base distribution.

### Per-track difficulty adjustment

| Track | Adjustment |
|---|---|
| SK | baseline |
| SJKC | +5% Hard for Math/Science (higher abstraction expected in Chinese-medium) |
| International | +5% Hard for Math/Science (Cambridge-style problem-solving) |

### Final difficulty distribution (Plan A, illustrative for SK Math Tahun 5)

Base: T5 = 38 / 45 / 17
Subject Math: 0/0/0
Track SK: baseline
**Final: 38 / 45 / 17**

### Final difficulty distribution (Plan A, illustrative for SJKC 中文 Tahun 6)

Base: T6 = 35 / 45 / 20
Subject 中文: +5 / -5
Track SJKC: 0/0/0 (Chinese is the language, not Math/Science track-bonus)
**Final: 40 / 40 / 20**

### Final difficulty distribution (Plan A, illustrative for International Mathematics Tahun 6)

Base: T6 = 35 / 45 / 20
Subject Math: 0/0/0
Track International: +0/+0/+5
**Final: 35 / 45 / 25**

---

## 8. Topic / Skill Blueprint

Per 638 §八: each `(Track × Grade × Subject × Language)` defines:
- topic
- skill
- question count (per topic)
- difficulty distribution (per topic — derived from per-grade + per-subject + per-track)
- question type = SINGLE_CHOICE only

### Topic count per (Track × Grade × Subject × Language) — Plan A

| Subject | T1 | T2 | T3 | T4 | T5 | T6 | Total topics |
|---|---:|---:|---:|---:|---:|---:|---:|
| Bahasa Melayu | 5 | 5 | 6 | 6 | 6 | 6 | 34 |
| English | 5 | 5 | 6 | 6 | 6 | 6 | 34 |
| Mathematics | 6 | 6 | 7 | 8 | 9 | 10 | 46 |
| Science | 5 | 6 | 7 | 8 | 9 | 10 | 45 |
| 中文 (SJKC only) | 5 | 5 | 6 | 6 | 6 | 6 | 34 |
| **Total per Grade × Subject × Lang** | varies | varies | varies | varies | varies | varies | |

Per-subject topic detail (Plan A):

#### Bahasa Melayu topics per grade (canonical KSSR-aligned)

| Grade | Topics |
|---|---|
| T1 | Mendengar & Bertutur, Membaca (suku kata / perkataan mudah), Penulisan (huruf / perkataan / ayat mudah), Tatabahasa (imbuhan asas), Perbendaharaan Kata (sinonim / antonim mudah) |
| T2 | Mendengar & Bertutur, Membaca (petikan pendek, cerita), Penulisan (ayat tunggal), Tatabahasa (imbuhan me-/ber-, kata ganti), Perbendaharaan Kata, Sajak & Peribahasa (pengenalan) |
| T3 | Membaca (petikan, cerita, puisi pendek), Penulisan (karangan pendek, ayat majmuk), Tatabahasa (kata hubung, imbuhan ber-/me-/ter-), Perbendaharaan Kata, Pemahaman (petikan pelbagai jenis), Sajak & Peribahasa |
| T4 | Pemahaman (petikan pelbagai genre), Penulisan (karangan, surat, e-mel), Tatabahasa (imbuhan, kata hubung, ayat majmuk), Perbendaharaan Kata, Sajak, Pemahaman Petikan Bergrafik, Bahasa Lisan |
| T5 | Pemahaman (petikan pelbagai jenis, grafik), Penulisan (karangan pelbagai jenis), Tatabahasa (ayat majmuk, kata hubung, imbuhan), Perbendaharaan Kata (peribahasa, simpulan bahasa), Sajak (puisi Melayu moden), Pemahaman Petikan Berimaginasi, Bahasa Lisan |
| T6 | Pemahaman (format UPSR, petikan kompleks), Penulisan (karangan pelbagai jenis, esei pendek), Tatabahasa (semua aspek), Perbendaharaan Kata (peribahasa, simpulan bahasa, bahasa standard), Sajak & Prosa Tradisional, Pemahaman Petikan Bergrafik (carta, jadual, infografik), Bahasa Lisan (diskusi, debat) |

#### English topics per grade

| Grade | Topics |
|---|---|
| Y1 | Listening & Speaking (greetings, instructions), Reading (phonics, sight words), Writing (letters, words, simple sentences), Grammar (articles, plurals, verbs), Vocabulary (colours, animals, family) |
| Y2 | Reading (simple texts, stories), Writing (sentences, descriptions), Grammar (singular/plural, present tense), Vocabulary (school, home, food), Listening Comprehension |
| Y3 | Reading (stories, descriptions), Writing (paragraphs, letters), Grammar (tenses: present, past, future), Vocabulary (weather, transport, hobbies), Comprehension (short passages) |
| Y4 | Reading (comprehension, poetry), Writing (essays, emails, reports), Grammar (tenses, modal verbs, conditionals), Vocabulary (environment, technology, health), Listening Comprehension |
| Y5 | Reading (comprehension, novel excerpts), Writing (essays, letters, reports), Grammar (tenses, conditionals, passive voice), Vocabulary (society, technology, media), Listening Comprehension |
| Y6 | Reading (UPSR comprehension, novel excerpts), Writing (essays, formal letters, reports), Grammar (advanced: mixed tenses, conditionals), Vocabulary (global issues, technology, media), Listening Comprehension |

#### Mathematics topics per grade (KSSR-aligned for SK, parallel for other tracks)

| Grade | Topics |
|---|---|
| T1 | Nombor Bulat 0-100, Tambah & Tolak, Pola & Jujukan, Masa & Waktu, Panjang, Wang, Bentuk 3D & 2D, Data |
| T2 | Nombor Bulat 0-1000, Operasi Asas (Tambah, Tolak, Darab, Bahagi), Pecahan, Wang, Panjang/Jisim/Isipadu, Masa & Waktu, Bentuk 3D & 2D, Data |
| T3 | Nombor Bulat 0-10000, Operasi Asas, Pecahan, Perpuluhan, Wang, Panjang/Jisim/Isipadu, Masa & Waktu, Bentuk 3D/2D & Sudut, Peratusan, Data |
| T4 | Nombor Bulat 0-100000, Operasi Asas, Pecahan (operasi), Perpuluhan (operasi), Peratusan, Wang, Panjang/Jisim/Isipadu/Masa & Waktu, Ruang (Isipadu, Luas, Perimeter), Koordinat, Pengurusan Data |
| T5 | Nombor Bulat 0-1000000, Operasi Bergabung, Pecahan (semua operasi), Perpuluhan (semua operasi), Peratusan (aplikasi), Wang, Panjang/Jisim/Isipadu/Masa & Waktu, Ruang, Koordinat/Nisbah & Kadaran, Pengurusan Data (Purata, Mod, Median) |
| T6 | Nombor Bulat (semua operasi), Pecahan (operasi gabungan), Perpuluhan (operasi gabungan), Peratusan (aplikasi kompleks), Wang (faedah, pelaburan), Panjang/Jisim/Isipadu/Masa & Waktu, Ruang (Isipadu Gabungan), Koordinat/Nisbah & Kadaran, Pengurusan Data (semua topik) |

#### Science topics per grade

| Grade | Topics |
|---|---|
| T1 | Tumbuhan (ciri & kitaran hidup), Haiwan (ciri & tingkah laku), Manusia (tubuh, kesihatan), Benda Bukan Hidup (ciri), Bahan (kayu, kertas, logam, plastik), Cuaca & Musim, Magnet (pengenalan) |
| T2 | Tumbuhan (ciri & kepelbagaian), Haiwan (ciri & kepelbagaian), Manusia (sistem tubuh), Benda Hidup & Bukan Hidup, Bahan (ciri & kegunaan), Tenaga (haba, cahaya), Bumi & Angkasa (cuaca, musim) |
| T3 | Tumbuhan (proses kehidupan), Haiwan (tabiat, habitat), Manusia (sistem pencernaan, pernafasan), Haiwan & Tumbuhan Kepelbagaian, Bahan (sifat & perubahan), Tenaga (haba, cahaya, elektrik), Bumi & Angkasa (cuaca, planet) |
| T4 | Sistem Tubuh Manusia (pencernaan, pernafasan, peredaran darah), Tumbuhan (pembiakan, pengkelasan), Haiwan (tabiat pemakanan, pengkelasan), Bahan (sifat asas, kegunaan), Tenaga (haba, cahaya, elektrik, bunyi), Bumi & Angkasa (sistem solar, pasang surut) |
| T5 | Sistem Tubuh Manusia (semua sistem), Tumbuhan (fotosintesis, pengkelasan), Haiwan (pembiakan, ekosistem), Bahan (asid, alkali, logam, bukan logam), Tenaga (semua bentuk), Bumi & Angkasa (fenomena, sistem solar), Teknologi & Inovasi (pengenalan) |
| T6 | Sistem Tubuh Manusia (semua sistem + gangguan), Tumbuhan (fotosintesis, ekosistem), Haiwan (ekosistem, biodiversiti), Bahan (sebatian, campuran, tindak balas), Tenaga (semua bentuk), Bumi & Angkasa (fenomena, cuaca angkasa), Teknologi & Inovasi (aplikasi) |

#### 中文 (SJKC only) topics per grade

| Grade | Topics |
|---|---|
| T1 | 听说 (问候, 指示), 识字 (笔画, 偏旁, 简单生字), 书写 (笔画, 简单句子), 词汇 (家庭, 身体, 数字), 阅读理解 (简短段落) |
| T2 | 识字 (部首, 常用字), 书写 (完整句子), 词汇 (学校, 食物, 颜色), 阅读理解 (短文), 口语 (自我介绍) |
| T3 | 阅读理解 (各类文体), 书写 (段落, 简短作文), 词汇 (天气, 交通, 爱好), 语法 (量词, 句式), 古诗 (简诗) |
| T4 | 阅读理解 (记叙文, 说明文), 书写 (作文, 书信), 词汇 (环境, 科技, 健康), 语法 (关联词, 复句), 古诗 |
| T5 | 阅读理解 (复杂文体), 书写 (记叙文, 应用文), 词汇 (社会, 媒体, 文化), 语法 (修辞, 复句), 古诗 (唐诗宋词简介) |
| T6 | 阅读理解 (UPSR格式, 长篇节选), 书写 (完整作文, 议论文), 词汇 (全球议题, 科技前沿), 语法 (高级, 修辞综合), 古诗 (经典诗词) |

### Skill type per (Track × Grade × Subject × Language)

Per 638 §八: skill types are RECOGNITION / COMPREHENSION / APPLICATION / ANALYSIS / PROBLEM_SOLVING.

Skill distribution per subject:
- Bahasa Melayu / 中文: heavy COMPREHENSION (50%) + APPLICATION (30%) + ANALYSIS (20%)
- English: similar but with RECOGNITION at T1-T2
- Mathematics: heavy APPLICATION (40%) + PROBLEM_SOLVING (40%) + RECOGNITION (20%)
- Science: heavy COMPREHENSION (40%) + APPLICATION (40%) + ANALYSIS (20%)

---

## 9. Originality Policy (per 638 §九)

**Strict prohibition** on:
- copy
- near-copy
- synonym substitution
- only changing numbers
- only changing names
- only changing context
- reconstructing exam question

**All questions**:
```
contentOrigin = ORIGINAL
licenseStatus = self_authored
commercialReuseAllowed = true
examYear = null
```

**Reference DB usage** (READ-ONLY):
- syllabus reference ✅
- topic reference ✅
- skill reference ✅
- difficulty reference ✅
- question style reference ✅
- (NOT copy / paraphrase / translate)

**Anti-translation rule (per 638 §三)**:
- SK Math ms ≠ translated copy of SK Math en
- SJKC Math zh ≠ translated copy of SK Math ms
- International Math en ≠ translated copy of SK Math en
- All 3 language variants of same subject = **independent ORIGINAL authoring** with shared knowledge point + skill + difficulty target

---

## 10. QA Gates (per 638 §十)

### Structural gate

| Check | Pass criteria |
|---|---|
| JSON schema valid | All required fields present |
| subjectId valid | Matches `^(sk|skc|intl)_(prim|sec)_([a-z]+)_([a-z]+)_[YyTt]\d+$` regex |
| schoolTrack valid | SK / SJKC / INTERNATIONAL enum |
| language valid | ms / zh / en enum |
| gradeLevel valid | `"Tahun<n>"` where n ∈ 1..6 |
| subjectCode valid | bm / bc / en / math / science |
| curriculum valid | KSSR / KSSR_SJKC / CAMBRIDGE_PRIMARY |

### Content gate

| Check | Pass criteria |
|---|---|
| exactly one correct answer | correctAnswerLabel ∈ {A,B,C,D}, single match |
| 4 distinct options | No duplicates across options a/b/c/d |
| correct answer plausible | Matches question context (not absurd) |
| distractors plausible | Wrong but defensible answers |
| difficulty matches | difficultyDistribution aligned with grade baseline |
| topic matches | Question.topic ∈ expected topic list |
| grade appropriate | Vocabulary + complexity suits age |
| language natural | BM/EN/ZH grammar correct, no machine-translation artifacts |

### Originality gate

| Check | Pass criteria |
|---|---|
| exact duplicate | questionText exact match across full KuizKu Q inventory (incl. V3/V4-TEST/Phase 10.1) |
| normalized duplicate | Normalized text (lowercase, strip punctuation) exact match |
| near-duplicate | 5-gram overlap > 0.6 between candidate Q text and any existing Q text |
| cross-language duplicate | Conceptual alignment check (knowledge point + answer equivalence) flagged for human review |
| cross-track duplicate | SJKC Math zh ≠ SK Math ms wording (must be authored separately) |
| Reference DB similarity | ≥5-word phrase in candidate matches any Reference DB sentence → REJECT or REWRITE |

### Distribution gate

| Check | Pass criteria |
|---|---|
| question count | Matches Plan A / Plan B target per (Track × Grade × Subject × Language) |
| topic distribution | All topics have ≥1 Q |
| difficulty distribution | easy/medium/hard sum = 100 |
| language distribution | 100% questions have language ∈ {ms, zh, en} matching subject |

**Any gate fail → batch REJECTED, not published**.

---

## 11. Plan A vs Plan B (per 638 §四)

| | Plan A (Conservative) | Plan B (Large) |
|---|---:|---:|
| Total questions | 1,830 | 3,300 |
| Existing reusable | 222 Q (V3 + V4-TEST + Phase 10.1) | same |
| NEW content to author | 1,608 Q | 3,078 Q |
| Token cost estimate | ~1.5M | ~3M |
| Time to first usable bank | 4-6 weeks | 8-10 weeks |
| Coverage | Sufficient for launch | Comprehensive |
| Recommended for | First batch + validation | Long-term primary coverage |

**Recommendation**: Plan A for first formal production batch; Plan B for subsequent expansion if token budget allows.

---

## 12. Recommended Production Order

### Phase 10.5 — First formal bank (Plan A subset)

Recommended sequence (each step = 1 batch):

1. **SK Bahasa Melayu T1** (25 Q) — validates SK pipeline end-to-end
2. **SK English T1** (25 Q) — second track of same grade (English subject)
3. **SK Mathematics T1** (30 Q) — Math subject (different content type)
4. **SK Science T1** (30 Q) — Science subject
5. **SK Bahasa Melayu T2-T6** (5 batches × 25 Q) — fill SK BM
6. **SK English T2-T6** (5 batches × 25 Q) — fill SK EN
7. **SK Mathematics T2-T6** (5 batches × 30 Q) — fill SK Math
8. **SK Science T2-T6** (5 batches × 30 Q) — fill SK Science
9. **International English T1-T6** (6 batches × 30 Q) — International English-native
10. **International Mathematics T1-T6** (6 batches × 30 Q) — International Math (Cambridge style)
11. **International Science T1-T6** (6 batches × 30 Q) — International Science
12. **SJKC 中文 T1-T6** (6 batches × 25 Q) — SJKC Chinese native
13. **SJKC Bahasa Melayu T1-T6** (6 batches × 25 Q) — SJKC BM (MFL)
14. **SJKC English T1-T6** (6 batches × 25 Q) — SJKC EN (MFL)
15. **SJKC Mathematics T1-T6** (6 batches × 30 Q) — SJKC Math (Chinese-medium)
16. **SJKC Science T1-T6** (6 batches × 30 Q) — SJKC Science (Chinese-medium)

Total batches: **52 batches** (Phase 10.5 wraps after each, with HARD STOP per 638 authorization pattern).

### Recommended first bank (Phase 10.5 first production bank)

`V5-SK-Primary-BahasaMelayu-Tahun1` = 25 Q, schoolTrack=SK, language=ms, grade=Tahun1.

This is the **simplest, most validated first path** (only 25 Q, single subject, single grade, single track). Once this succeeds end-to-end, expand to subsequent batches.

---

## 13. Expected Total Question Count

| Plan | Total Q | Subject IDs | Track×Grade×Subject×Lang combinations | Subject types |
|---|---:|---:|---:|---:|
| **Plan A** | **1,830** | **72** | **72** | **12** (4 SK + 5 SJKC + 3 International) |
| **Plan B** | **3,300** | **72** | **72** | **12** (4 SK + 5 SJKC + 3 International) |

---

## 14. Risks / Unresolved Decisions

| # | Risk / Decision | Impact | Resolution needed |
|---|---|---|---|
| 1 | **SJKC 中文 T1-T6 reference gap** — NO primary Chinese coverage in Reference DB (only 15 secondary files). Cannot use as syllabus-style reference. | Need KSSR_SJKC 中文 syllabus from external source OR pure ORIGINAL from native-speaker authoring. | **638 decision required**: Do we obtain KSSR_SJKC 中文 syllabus docs, or rely on author knowledge? |
| 2 | **SJKC Mathematics/Science Chinese-medium reference gap** — ZERO Chinese-medium math/science references in Reference DB. | Same as #1. | **638 decision required**: Same as #1. |
| 3 | **International English-native reference mismatch** — Reference DB has Malaysian MFL English (UASA/UPSA-style), not Cambridge Primary English-native. | Need Cambridge Primary curriculum docs OR pure ORIGINAL from English-native speaker authoring. | **638 decision required**: Same as #1. |
| 4 | **International Mathematics/Science reference gap** — ZERO English-medium math/science references. | Need Cambridge Primary Math/Science curriculum docs OR pure ORIGINAL. | **638 decision required**: Same as #1. |
| 5 | **Plan A vs Plan B choice** — affects total scope (1,830 vs 3,300 Q). | Different generation volume. | **638 decision required**: Plan A first batch + Plan B later, OR Plan A only? |
| 6 | **Per-batch size** — 25-30 Q per (Track × Grade × Subject) feels small. Larger batches (e.g., 100 Q per grade) reduce per-batch overhead but require more careful QA. | Token efficiency vs QA granularity. | **638 decision required**: Recommended 25-30 Q per batch for first run. |
| 7 | **Question type** — V1 only supports SINGLE_CHOICE. Future question types (TRUE/FALSE, MULTI_CHOICE) deferred to V2 schema (per Phase 10.4 §八). | All Phase 10.4 blueprint limited to SINGLE_CHOICE. | **No decision needed** — Phase 10.4 = SINGLE_CHOICE only. |
| 8 | **Year 1 vs Tahun 1 canonical form** — Display difference but storage canonical. | UI must handle display ("Year 1" for International, "Tahun 1" for SK/SJKC) but storage always `"Tahun1"`. | **No decision needed** — handled by UI layer (HomeScreen Greeting + LevelSelectionScreen). |
| 9 | **Reference DB expansion** — current Reference DB only has SK-aligned content. To support SJKC/International fully, may need to expand Reference DB. | Out of Phase 10.4 scope. | **638 decision required**: Future phase, separate from Phase 10.4. |
| 10 | **Subject granularity** — current blueprint treats Mathematics as 1 subject. KSSR actually has sub-strands (Numbers, Measurement, Geometry, Statistics). | Phase 10.4 blueprint treats each subject as monolithic; sub-strand organization deferred to future. | **No decision needed** — Phase 10.4 = single subject per (Track × Grade × Subject × Language). |
| 11 | **SJKC Bahasa Melayu** — is this MFL (Malaysian national language) or another variant? Per 638 §五: SJKC students learn BM as MFL (compulsory subject). | Subject design + syllabus reference. | **No decision needed** — BM = MFL for SJKC (already specified in blueprint). |
| 12 | **Moral / Islamic Studies / Pendidikan Sivik / Muzik / Pendidikan Seni** — not in Phase 10.4 blueprint. | Subject mix per (Track × Grade) doesn't include these. | **638 decision required**: Future phase, separate from Phase 10.4. |

---

# 🛑 HARD STOPPED — 等待 638 下一步授權

**Phase 10.4 Blueprint COMPLETE** (READ-ONLY):
- ✅ 3 tracks (SK/SJKC/International) × 6 grades × 12 subject types = 72 subject IDs
- ✅ Plan A (1,830 Q) and Plan B (3,300 Q) both designed
- ✅ Difficulty / topic / skill distributions per (Track × Grade × Subject × Language)
- ✅ Anti-translation rule documented
- ✅ QA gates (structural / content / originality / distribution) designed
- ✅ 52-batch production order with first-bank recommendation
- ✅ 12 unresolved decisions flagged for 638

**No questions generated. No Android code modified. No V3/V4-TEST/Reference DB touched. Phase 10.1 JSON SHA preserved (`72ca4e4586...`). No commit. No push.**

**Awaiting 638 authorization to either:**
1. Approve Plan A → Phase 10.5 first batch (SK BM T1, 25 Q)
2. Approve Plan B → larger first batch
3. Adjust blueprint (e.g., add Moral Education, different difficulty ratios)
4. Defer pending answers to unresolved decisions

🚢
