# Phase 10.2 — Primary Trilingual Curriculum Architecture Preflight Report

> **READ-ONLY PREFLIGHT.** No questions generated. No Android code modified. No
> V3 / V4-TEST / Reference DB touched. No commit. No push. No Google Play upload.

---

## A. Current Architecture

### A.1 Question schema (Android source — FROZEN Phase 0A + V3 addendum Phase 4.2)

```kotlin
data class Question(
    val questionId: String,         // globally unique, immutable
    val subjectId: String,          // e.g. "prim_bm_Y5_peribahasa"
    val topic: String?,             // optional subtopic
    val difficulty: Int,            // 1..3
    val questionText: String,
    val questionType: QuestionType, // V1: SINGLE_CHOICE only
    val language: String,           // V1 default "en"; V3 typically "ms"
    val options: QuestionOptions,   // exactly 4 (a, b, c, d)
    val correctAnswer: String,
    val explanation: String?,
    val versionId: Int,

    // === V3 addendum (Phase 4.2) ===
    val contentOrigin: String?,     // "ORIGINAL" | "OFFICIAL_PAST_PAPER"
    val contentYear: Int?,          // ORIGINAL authoring year
    val examYear: Int?,             // OFFICIAL_PAST_PAPER year (mutually exclusive)
    val gradeLevel: String?,        // "Tahun1".."Tahun6"
)
```

### A.2 Subject schema

```kotlin
data class Subject(
    val subjectId: String,
    val displayNameKey: String,
    val iconResName: String?,
    val totalQuestions: Int,
    val displayOrder: Int,
    val versionId: Int,
    // NO schoolTrack, NO language, NO gradeLevel, NO stage
)

@Entity(tableName = "subject")
data class SubjectEntity(
    // identical fields, same gap
)
```

### A.3 SubjectId naming convention (the "schoolTrack proxy")

```
V1/V3/V4-TEST/RTB production:
  prim_<subj>_[Yy]<n>_<topic>   → Primary, Tahun n
  sec_<subj>_[Tt]<n>_<topic>    → Secondary, Tingkatan n

Examples currently in banks:
  prim_bm_Y5_peribahasa          → Primary BM Tahun 5
  prim_bm_Y1_kemahiran_membaca   → Primary BM Tahun 1
  bootstrap_gk / bootstrap_eng   → LEGACY (no parseable prefix) — Phase 9 hidden
```

The SubjectId is currently the **only** mechanism that encodes stage + grade.
There is NO schoolTrack dimension. There is NO language code in the prefix.

### A.4 Room schema

```kotlin
@Database(
    entities = [
        SubjectEntity::class,         // table "subject"
        QuestionEntity::class,        // table "question"
        QuizAttemptEntity::class,
        AnswerRecordEntity::class,
        FavoriteEntity::class,
        QuestionBankVersionEntity::class,
    ],
    version = 2,
)
```

`QuestionEntity` carries a `language` column (indexed). No `schoolTrack` column.

### A.5 BankSync (key constraints)

```kotlin
// BankSyncer.kt
val language = q["language"]?.jsonPrimitive?.content ?: "en"  // optional, default "en"
val contentOrigin = safeString("contentOrigin")
val contentYear = safeInt("contentYear")
val examYear = safeInt("examYear")
val gradeLevel = safeString("gradeLevel")

// Invariants enforced:
//   contentOrigin = ORIGINAL           ⇒ contentYear must be set, examYear null
//   contentOrigin = OFFICIAL_PAST_PAPER ⇒ examYear must be set, contentYear null
```

**No schoolTrack field is read or enforced** in BankSyncer. The schema is silent on this dimension.

### A.6 SubjectGrouping (Phase 9)

```kotlin
private val SUBJECT_ID_REGEX = Regex(
    "^(prim|sec)_([a-z]+)_([YyTt])(\\d+)_(.+)$"
)
fun parseStageAndGrade(subjectId: String): SubjectStageAndGrade? =
    null if regex doesn't match; otherwise {stage = Primary|Secondary, year}
```

The regex accepts `prim_<subj>` and `sec_<subj>` only. Any new prefix (e.g., `skc_<subj>` for SJKC) would NOT parse and would be treated as legacy/hidden — a fundamental architecture constraint.

### A.7 UserLevel (Phase 9)

```kotlin
sealed interface UserLevel {
    data class Primary(val year: Int) : UserLevel       // Tahun 1..6
    data object LowerSecondary : UserLevel              // T1..T3
    data object UpperSecondary : UserLevel              // T4..T5
    data object NotSelected : UserLevel
}
```

**No schoolTrack axis.** UserLevel only models educational stage + year.

### A.8 Home UI (Phase 9)

- Greeting: "belajar di Tahun X" (single grade)
- Continue Learning: open most recent subject
- Recent Score card: aggregate stats
- **Change Level card: navigates to TierSelection** — only Tier (Primary/Secondary/UpperSecondary), no schoolTrack
- Filter: `filterByLevel` uses `SubjectGrouping.parseStageAndGrade` only

### A.9 LevelSelectionScreen (Phase 9)

3 tier cards only (Primary, Secondary, Upper Secondary). No schoolTrack.

---

## B. Problem with the current 600-question plan

### B.1 The "100 questions per Tahun" plan conflates school track with language

The original Phase 10 Blueprint (Phase 10.3) was:

```
Tahun 1 = 30 BM + 28 Math + 22 Science + 20 English = 100 Q
Tahun 2..6 = same structure × 5 years
Total: 600 Q (all Bahasa Melayu, all SK-aligned implicitly)
```

**Problems**:

1. **Implicit schoolTrack assumption.** "Bahasa Melayu" in a 100-Q blueprint assumes SK (Sekolah Kebangsaan, Malay-medium national school). For SJKC (Chinese-medium) schools, 华文 (Bahasa Cina / Chinese) is a *separate* mandatory subject, not a translation of BM. For International Schools, English is the medium of instruction and BM is a *language subject* taught as a foreign/second language.

2. **Math/Science monolingual assumption.** "Mathematics 28 Q" assumes BM-medium math. SJKC students learn Mathematics in 中文 (Bahasa Cina). International students learn Math in English. Three parallel Math content sets may be needed for the same knowledge point — but they are NOT translations of each other (terminology differs, problem framing differs, word problem scenarios differ).

3. **English ≠ International School subject.** "English 20 Q" implicitly assumes SK English (Bahasa Inggeris as a subject). In International Schools, English IS the medium — so International "English" content may be literature, comprehension, or composition, not just basic vocabulary.

4. **No mechanism to filter by schoolTrack.** Even if we wrote 600 questions for SK, SJKC, and International tracks, the current Home UI + SubjectGrouping + LevelSelection cannot differentiate them. All 600 would show up for every user.

5. **Phase 10.1's 100 questions implicitly targeted SK.** All 100 questions are written in MS or EN with Malaysian-Malay cultural context. They fit SK Math/Science/Bahasa Melayu but are NOT appropriate as "Bahasa Cina" content for SJKC.

### B.2 SubjectEntity schema gap

SubjectEntity has no place to store:
- which `schoolTrack` this subject belongs to
- which `language` is the medium of instruction for this subject
- which `gradeLevel` (currently derived from subjectId regex — fragile)

This means the SAME `prim_math_Y5_*` subjectId could contain:
- SK math (Malay-medium)
- SJKC math (Chinese-medium)
- International math (English-medium)

…indistinguishable from each other in Room.

### B.3 Language field is per-question, not per-subject

QuestionEntity has a `language` column. But a subject that is intrinsically BM-medium (like Bahasa Melayu itself) shouldn't have an option to be `language=en`. Conversely, a Chinese-medium Math subject wouldn't make sense for `language=ms`.

The current model allows any language on any subject, which is too permissive.

---

## C. Recommended Data Model

### C.1 Three independent axes

```
1. schoolTrack    — SK | SJKC | INTERNATIONAL
2. language       — ms | zh | en
3. gradeLevel     — Tahun 1..6 (primary); Tingkatan 1..5 (secondary, future)
```

These axes are **independent dimensions**, NOT a single combined "locale" or "track".
A question belongs to exactly one schoolTrack, one language, and one gradeLevel.

### C.2 Why axes are independent (not coupled)

| Subject (knowledge domain) | SK (Malay-medium) | SJKC (Chinese-medium) | International (English-medium) |
|---|---|---|---|
| Bahasa Melayu | ✅ native | ✅ MFL (modern foreign language) | ✅ ESL (English as second language) — but taught in English |
| Bahasa Cina / 华文 | ✅ MFL | ✅ native | ✅ MFL |
| Bahasa Inggeris / English | ✅ MFL | ✅ MFL | ✅ native |
| Mathematics | ✅ in BM | ✅ in BC | ✅ in EN |
| Science | ✅ in BM | ✅ in BC | ✅ in EN |
| Pendidikan Moral / Moral / Moral Ed | ✅ in BM | ✅ (if offered) | ❌ not offered |
| Pendidikan Islam | ✅ in BM | ❌ | ❌ |

→ The SAME knowledge point (e.g., "fraction addition with denominator 4") exists three times — once for each medium — with different vocabulary, word problem framing, and terminology.

→ A SJKC student MUST do 华文 (native) + BM (MFL) + English (MFL) + Math (in BC) + Science (in BC). Their subjects are NOT "translations" of SK subjects.

### C.3 Subject granularity proposal

Instead of one `Subject` per topic, the model should treat `(schoolTrack, language, subjectCode)` as a subject triple:

```
subjectId = "<track>_<subjectCode>_<grade>_<topic>"

Examples:
  sk_prim_bm_Y5_peribahasa           → SK, Primary, Bahasa Melayu, Tahun 5, Peribahasa
  skc_prim_bc_Y5_peribahasa          → SJKC, Primary, Bahasa Cina (华文), Tahun 5, Peribahasa
  intl_prim_en_Y5_literature         → International, Primary, English, Tahun 5, Literature
  sk_prim_math_Y5_fraction_addition  → SK, Primary, Math (in BM), Tahun 5, Fraction Addition
  skc_prim_math_Y5_fraction_addition → SJKC, Primary, Math (in BC), Tahun 5, Fraction Addition
  intl_prim_math_Y5_fraction_addition → International, Primary, Math (in EN), Tahun 5, Fraction Addition
```

**The SubjectId encoding must be redesigned** — `prim_/sec_` prefix is no longer sufficient. We need:

```
subjectId = "<track>_<stage>_<subjectCode>_<grade>_<topic>"
            ^^^^^^^
            NEW: sk | skc | intl
```

This is a breaking change to the existing `prim_<subj>_Y<n>_<topic>` regex (Phase 9's SubjectGrouping). It would require:
1. New schema (with migration policy)
2. Updated parser
3. Updated SubjectEntity (or a parallel one)

### C.4 Subject-level metadata proposal

```kotlin
data class Subject(
    val subjectId: String,
    val displayNameKey: String,
    val displayName: Map<String, String>,     // locale-keyed display name (already in SubjectDescriptor)
    val iconResName: String?,
    val totalQuestions: Int,
    val displayOrder: Int,
    val versionId: Int,

    // === Phase 10.2 NEW fields (additive) ===
    val schoolTrack: SchoolTrack,             // SK | SJKC | INTERNATIONAL
    val language: String,                     // ms | zh | en (medium of instruction)
    val gradeLevel: String,                   // "Tahun1".."Tahun6" (no longer derived)
    val subjectCode: String,                  // bm | bc | en | math | science | moral | islam
    val curriculum: String,                   // "KSSR" | "KSSR_SJKC" | "CAMBRIDGE_PRIMARY" | etc.
)
```

### C.5 Question metadata (additive, no schema break)

```kotlin
data class Question(
    // ... existing fields ...

    // === Phase 10.2 NEW (additive, optional in V3 schema) ===
    val schoolTrack: SchoolTrack? = null,     // SK | SJKC | INTERNATIONAL; null = inherited from Subject
    val curriculum: String? = null,           // overrides subject curriculum if needed
    val learningFocus: String? = null,        // "vocabulary" | "comprehension" | "problem-solving" (already exists)
)
```

### C.6 UserLevel (Phase 10.2 additive)

```kotlin
sealed interface UserLevel {
    data class Primary(val year: Int) : UserLevel
    data object LowerSecondary : UserLevel
    data object UpperSecondary : UserLevel
    data object NotSelected : UserLevel

    // === Phase 10.2 NEW: schoolTrack + language preference ===
    val schoolTrack: SchoolTrack,             // default SK
    val preferredLanguage: String?            // optional, defaults to schoolTrack's medium
}
```

---

## D. School Track Model

### D.1 The three Malaysian primary school systems

```
┌─────────────────────────────────────────────────────────────────────────┐
│  School Track (schoolTrack)                                              │
│                                                                         │
│  SK         — Sekolah Kebangsaan (national, Malay-medium)              │
│              Medium of instruction: Bahasa Melayu (ms)                  │
│              Curriculum: KSSR                                            │
│              Compulsory subjects: BM, English, Math, Science,            │
│                                    Moral, Islamic Studies (Muslims)       │
│                                                                         │
│  SJKC       — Sekolah Jenis Kebangsaan (Chinese-medium)                  │
│              Medium of instruction: Bahasa Cina (zh)                    │
│              Curriculum: KSSR_SJKC (KSSR adapted for SJKC)               │
│              Compulsory subjects: BC (华文, native), BM, English,         │
│                                    Math (in BC), Science (in BC)          │
│              Source: SJKC uses Chinese-medium textbooks published by     │
│                       Chinese-language publishers (e.g., 董教总)           │
│                                                                         │
│  INTERNATIONAL — Private international schools                          │
│              Medium of instruction: English (en)                        │
│              Curriculum: Cambridge Primary / IB Primary                 │
│              Compulsory subjects: English (native), BM (as MFL),         │
│                                    Math (in EN), Science (in EN)          │
└─────────────────────────────────────────────────────────────────────────┘
```

### D.2 Why "schoolTrack" is a separate concept from "language"

A subject like "Mathematics" exists in three versions:
- SK Math (Malay medium) — "Pecahan" + Malay word problems
- SJKC Math (Chinese medium) — "分数" + Chinese word problems
- International Math (English medium) — "Fractions" + English word problems

The **knowledge content** (concept of fraction addition) is the SAME, but the
**language of the question text, terminology, and word-problem scenarios** differ.

A SINGLE Malay-medium Math question is **inappropriate** for an SJKC student
because the word problem uses "Ali membeli 3 biji epal" instead of "小明买3个苹果".

### D.3 SubjectId encoding for schoolTrack

Current (Phase 9 frozen):
```
prim_<subjCode>_<grade>_<topic>
sec_<subjCode>_<grade>_<topic>
```

Proposed (Phase 10.2 NEW — additive if existing banks frozen, breaking if migrated):
```
<track>_<stage>_<subjCode>_<grade>_<topic>

where track ∈ {sk, skc, intl}
      stage ∈ {prim, sec}
      subjCode ∈ {bm, bc, en, math, science, moral, islam, art, music, ...}
      grade ∈ Y1..Y6 (primary) | T1..T5 (secondary)
```

This makes schoolTrack a **first-class prefix** that the SubjectGrouping parser
must recognize — and it would NOT recognize `prim_bm_Y5_*` anymore (or it would
treat them as `schoolTrack=SK` by default for backward compat).

---

## E. Language Model

### E.1 Three languages, not mapped 1-1 to school track

```
language ∈ {ms, zh, en}

ms (Bahasa Melayu)
  - Native in SK
  - MFL in SJKC (taught as a subject)
  - MFL in International Schools (taught as a subject)

zh (中文 / Bahasa Cina)
  - Native in SJKC (华文)
  - MFL in some SK (offered as elective subject at some schools)
  - Rare in International Schools (some offer it as enrichment)

en (English)
  - Native in International Schools (medium of instruction)
  - MFL in SK (Bahasa Inggeris — taught as a subject)
  - MFL in SJKC (taught as a subject)
```

### E.2 Per-subject language is INHERENT

A subject's language is determined by the **medium of instruction in that
school track**, not user preference:

| Subject | SK language | SJKC language | International language |
|---|---|---|---|
| Bahasa Melayu | ms (native) | ms (MFL) | ms (MFL) |
| 华文 (BC) | zh (MFL) | zh (native) | zh (MFL) |
| English | en (MFL) | en (MFL) | en (native) |
| Mathematics | ms (BM textbook) | zh (BC textbook) | en (English textbook) |
| Science | ms | zh | en |

→ The language of a question is **structural metadata** determined by
`(schoolTrack, subjectCode)`, NOT a per-question free-form choice.

→ The current Question.language field can stay (for content-language hints),
but it should be CONSTRAINED by Subject.schoolTrack + Subject.subjectCode.

### E.3 Why English in SK is NOT International English

SK students learning "Bahasa Inggeris" learn:
- Vocabulary, grammar, sentence construction
- Reading comprehension with Malaysian cultural context (e.g., "kampung", "pasar malam")
- BM-MFL English, not native-English literature

International School students learning "English" learn:
- Literature, creative writing, composition
- Native-level reading comprehension
- Different scope entirely — NOT a translation of SK English

These two English "subjects" have **different learning objectives** and
should be tracked separately.

---

## F. Subject Model

### F.1 Subject granularity

**Old model (current Android schema)**:
```
Subject = (subjectId) → 1 unit of "things to study"
  subjectId encodes: stage + grade + subjCode + topic
  e.g. "prim_bm_Y5_peribahasa" = Primary BM Tahun 5 Peribahasa
```

**New model (Phase 10.2 proposal)**:
```
Subject = (schoolTrack, subjectCode, gradeLevel, topic) → 1 unit
  subjectId encodes: schoolTrack + stage + subjCode + gradeLevel + topic
  e.g. "sk_prim_bm_Y5_peribahasa"   = SK Primary BM Tahun 5 Peribahasa
       "skc_prim_bc_Y5_peribahasa"  = SJKC Primary BC Tahun 5 Peribahasa
       "intl_prim_en_Y5_literature" = International Primary English Tahun 5 Lit
```

### F.2 SubjectEntity additions

```kotlin
@Entity(tableName = "subject")
data class SubjectEntity(
    @PrimaryKey val subjectId: String,
    val displayNameKey: String,
    val displayName: Map<String, String>,  // NEW (was in SubjectDescriptor, now in entity)
    val iconResName: String?,
    val totalQuestions: Int,
    val displayOrder: Int,
    val versionId: Int,

    // === Phase 10.2 NEW ===
    val schoolTrack: String,             // "SK" | "SJKC" | "INTERNATIONAL"
    val language: String,                // "ms" | "zh" | "en"
    val gradeLevel: String,              // "Tahun1".."Tahun6" (no longer derived)
    val subjectCode: String,             // "bm" | "bc" | "en" | "math" | "science" | ...
    val curriculum: String,              // "KSSR" | "KSSR_SJKC" | "CAMBRIDGE_PRIMARY"
)
```

### F.3 SubjectGrouping parser changes

```kotlin
// Current (Phase 9): recognizes prim_<subj>_Y<n>_<topic>
// New (Phase 10.2): recognizes <track>_<stage>_<subjCode>_<grade>_<topic>

private val SUBJECT_ID_REGEX_V2 = Regex(
    pattern = "^(sk|skc|intl)_(prim|sec)_([a-z]+)_([YyTt])(\\d+)_(.+)$"
)

fun parseSubject(subjectId: String): SubjectMetadata? {
    val match = SUBJECT_ID_REGEX_V2.matchEntire(subjectId) ?: return null
    val (trackStr, stageStr, subjCode, _, yearStr, topic) = match.destructured
    return SubjectMetadata(
        schoolTrack = SchoolTrack.from(trackStr),
        stage = if (stageStr == "prim") Primary else Secondary,
        subjectCode = subjCode,
        year = yearStr.toInt(),
        topic = topic,
        language = SubjectLanguage.from(trackStr, subjCode),  // structural
    )
}
```

### F.4 Room schema migration risk

Adding 5 columns to SubjectEntity and 3 to QuestionEntity means a schema bump
(version 2 → 3). For existing banks V1 / V3 / V4-TEST, all existing subjectIds
must be **backfilled** with default values:
- `schoolTrack = "SK"` (assumed — current banks are all SK-aligned)
- `curriculum = "KSSR"`
- `subjectCode = parsed from existing subjectId`
- `gradeLevel = parsed from existing subjectId`
- `language = existing question.language`

---

## G. Question Metadata Model

### G.1 Current (Phase 4.2 V3 addendum)

```kotlin
data class Question(
    val questionId, subjectId, topic, difficulty, questionText,
    val questionType, language, options, correctAnswer, explanation,
    val versionId, createdAtMillis, updatedAtMillis,
    val contentOrigin, contentYear, examYear, gradeLevel  // V3 addendum
)
```

### G.2 Proposed (Phase 10.2 additive)

```kotlin
data class Question(
    // ... all existing fields preserved ...

    // === Phase 10.2 NEW (additive, nullable for V1/V3 backward compat) ===
    val schoolTrack: String? = null,       // "SK" | "SJKC" | "INTERNATIONAL"
    val curriculum: String? = null,         // "KSSR" | "KSSR_SJKC" | "CAMBRIDGE_PRIMARY"
    val syllabusRef: String? = null,        // free-form: "KSSR BM Y5 Std 1.2.3"
    val learningObjective: String? = null,  // free-form description
)
```

### G.3 Why additive (not breaking)

V3 production bank has 30 questions, V4-TEST has 92 — both fully deployed to
GitHub Pages with frozen SHA. Adding nullable fields means existing questions
remain unchanged; new banks (Phase 10.2+) can populate the new fields.

### G.4 schoolTrack MUST come from Subject, not from question

The schoolTrack on a Question is **inherited from SubjectEntity**. Storing it
on QuestionEntity too is denormalization — useful for querying, but conceptually
secondary. BankSyncer should validate: `q.schoolTrack == q.subjectEntity.schoolTrack`
(or null).

---

## H. V3 Mapping

### H.1 Current V3 inventory (live read from /v3/manifest.json)

```
bankId: llcai_kuizku_my_v3_bm_original
keyId: v3-bm-original-master
schemaVersion: 3
publisherVersion: 1
totalQuestions: 30
subjects: 27 (all Bahasa Melayu)
grade coverage: Primary Y1-Y6 only
language: ms (implicit, default)
```

### H.2 V3 schoolTrack mapping

All 30 V3 questions are **implicitly SK-aligned**:
- SubjectId pattern: `prim_bm_Y<n>_<topic>` — only SK uses Bahasa Melayu as
  native medium
- Question text: Malaysian-Malay cultural context (skolah, kelas, guru)
- BM as native language (not MFL)

**Proposed backfill (no schema change)**:
- `schoolTrack = "SK"` for all 30 questions
- `curriculum = "KSSR"` for all 30
- `subjectCode = "bm"` for all 30
- `gradeLevel = parsed from subjectId`
- `language = "ms"` (explicit, was implicit)

### H.3 Future V3 augmentation (NOT in scope now)

If V3 is ever extended with SJKC or International content, it would need to:
1. Add `schoolTrack` field to manifest JSON schema (schemaVersion 4)
2. New encrypted files for SJKC BC and International EN variants
3. SubjectId rename from `prim_*` to `sk_prim_*` / `skc_prim_*` / `intl_prim_*`

**Recommendation**: V3 should remain **frozen** at its current state (SK-aligned,
30 Q, ms only). New track expansion happens via new bank IDs (Phase 10.5+),
not by extending V3.

---

## I. V4-TEST Mapping

### I.1 Current V4-TEST inventory

```
bankId: llcai_kuizku_v4_test
keyId: v4-test-master
schemaVersion: 3
publisherVersion: 2
totalQuestions: 92
subjects: 12 (all Bahasa Melayu)
grade coverage: Primary Y1-Y5 only
```

### I.2 V4-TEST schoolTrack mapping

Same as V3: all 92 questions are **SK-aligned BM content**:
- `schoolTrack = "SK"` (backfill)
- `curriculum = "KSSR"`
- `subjectCode = "bm"`
- `language = "ms"`

V4-TEST is internal pilot, not yet distributed, so schema changes are easier
than for V3 (still need to preserve V4-TEST-A and V4-TEST-B SHA history if
re-publication is desired).

### I.3 Recommendation

V4-TEST should also remain **frozen** at its current state for now. Any
multi-track expansion happens via new banks.

---

## J. Phase 10.1 Mapping

### J.1 Phase 10.1 inventory

```
File: D:\Users\bajub\kuizku_p10\tahun_1_pilot.json
SHA-256: 72ca4e4586efd27270c38ecbc4d359b21f2c599272468a5097f672c06269c159
Size: 124,695 bytes
Total: 100 questions (all ORIGINAL)
Distribution:
  BM (Bahasa Melayu, ms):  30 Q
  Math (Mathematics, ms): 28 Q
  Science (Science, ms):   22 Q
  BI (English, en):       20 Q
Difficulty: easy=60, medium=30, hard=10
Grade: Tahun 1
```

### J.2 Phase 10.1 schoolTrack mapping

All 100 questions have:
- BM/English text (Malaysian-English cultural context)
- Malay medium for Math/Science questions ("Ali", "ibu", "cikgu")
- Bahasa Melayu used in word problems and context

→ **All 100 are SK-aligned** (Bahasa Melayu medium).

**Proposed backfill**:
- `schoolTrack = "SK"` for all 100
- `curriculum = "KSSR"` for all 100
- `subjectCode = "bm" | "math" | "science" | "en"`
- `gradeLevel = "Tahun1"`
- `language = "ms" | "en"` (per question, already set)

### J.3 Reusability across tracks

| Phase 10.1 Subject | SK reuse | SJKC reuse | International reuse |
|---|---|---|---|
| Bahasa Melayu (ms, 30 Q) | ✅ native | ⚠️ partial — needs BC vocabulary equivalents for SJKC students learning BM as MFL | ⚠️ partial — needs English equivalents for International students learning BM as MFL |
| Mathematics (ms, 28 Q) | ✅ | ❌ — Math in SJKC requires Chinese word problems | ❌ — Math in International requires English word problems |
| Science (ms, 22 Q) | ✅ | ❌ — Science in SJKC requires Chinese-medium | ❌ — Science in International requires English-medium |
| English (en, 20 Q) | ✅ for SK Bahasa Inggeris | ⚠️ partial — needs Malaysian-Chinese cultural context adjustments | ❌ — International English is at a higher proficiency level (literature, composition, etc.) |

→ **Conclusion**: Phase 10.1's 100 questions are a **SK Tahun 1 baseline** only.
SJKC and International tracks need their OWN ORIGINAL questions, even for the
same grade level.

### J.4 Recommendation

Phase 10.1's 100 questions are ready to be **the SK Tahun 1 baseline** of a
future V5 (SK-aligned production bank). They are NOT reusable as direct
content for SJKC or International tracks.

The 100 questions are not deleted. They are preserved as-is for the SK track
of a future multi-track deployment.

---

## K. Reference DB Coverage

### K.1 What Reference DB covers (by school track)

| School Track | BM/ms | BC/zh | EN/en | Math | Science |
|---|---|---|---|---|---|
| SK (Malay-medium) | 🟢 Strong (18 files T1-T6) | ❌ None | 🟡 Moderate (17 files T1-T6) | 🟢 Strong (77 files T1-T6) | 🟡 Moderate (28 files T1-T6) |
| SJKC (Chinese-medium) | ❌ None | ❌ **None in Primary** (15 files T2-T5 only — secondary) | ❌ None | ❌ None | ❌ None |
| International (English-medium) | ❌ None | ❌ None | 🟡 Moderate (17 files T1-T6, mostly Malaysian UASA/UPSA English — not Cambridge Primary) | ❌ None | ❌ None |

### K.2 Coverage strength detail (per 638 Phase 10.1 analysis)

**SK BM (Bahasa Melayu)** 🟢
- 18 files across T1-T6 (LATIH-TUBI modules + KSSR Akhir Tahun + exam-style)
- Strong topic coverage: pemahaman / penulisan / tatabahasa / peribahasa / karangan

**SK English (Bahasa Inggeris)** 🟡
- 17 files T1-T6 (UASA + UPSA + standard primary English textbooks + supplementary readers)
- Mostly exam-style + Malaysian-English textbooks; NOT native-English literature
- Sufficient for SK "Bahasa Inggeris as MFL" content

**SK Mathematics** 🟢
- 77 files T1-T6 (MOBIM + comprehensive BAB exercises covering JISIM,
  KOORDINAT, MASA, OPERASI ASAS, PECAHAN, PERATUS, PERPULUHAN, RUANG, WANG,
  NISBAH, PENGURUSAN DATA, PANJANG, ISIPADU CECAIR)
- Excellent topic coverage

**SK Science** 🟡
- 28 files T1-T6 (MOBIM BI/BM/BC/BT for T1-T3 + UASA-style for T4-T6)
- T4-T6 coverage weak (only 1 UASA file each)

**SJKC BC (Bahasa Cina / 华文)** ❌ **MISSING in Primary**
- 15 files in `secondary/Chinese/T2-T5` only
- ZERO coverage for `primary/Chinese/T1-T6`
- This is the **biggest gap**

**SJKC Mathematics (in Chinese)** ❌
- ZERO SJKC math references
- SJKC schools use Chinese-medium math textbooks published by Chinese-language
  publishers (e.g., 董教总, 嘉阳出版社) — KuizKu would need to obtain these
  independently OR write purely ORIGINAL content based on KSSR_SJKC syllabus

**SJKC Science (in Chinese)** ❌
- ZERO SJKC science references
- Same gap as SJKC Math

**International English** ⚠️ (no separate files, only English-medium content)
- The 17 `primary/English/` files are Malaysian UASA/UPSA English, NOT
  Cambridge Primary or IB Primary English
- Cambridge Primary curriculum (UK National Curriculum Key Stage 1/2) is
  structurally different from KSSR English

**International Mathematics** ❌
- ZERO Cambridge Primary Math references
- Cambridge Primary Math is structured differently (year-based, not Y1-Y6)

**International Science** ❌
- ZERO Cambridge Primary Science references

### K.3 Sufficiency assessment per track

| Track | Sufficiency | Notes |
|---|---|---|
| SK (Malay-medium) | ✅ **Sufficient** | BM/Math strong; English/Science moderate — adequate for blueprint + style reference |
| SJKC (Chinese-medium) | ⚠️ **Insufficient** | ZERO Chinese-medium references in Primary. Requires independent ORIGINAL content + Chinese-language syllabus lookup |
| International | ❌ **Insufficient** | ZERO Cambridge Primary references. Requires independent ORIGINAL content + Cambridge curriculum lookup |

### K.4 Blueprint design implication

For Phase 10 SJKC + International blueprint:
- Cannot rely on Reference DB for Chinese-medium or English-medium style analysis
- Must rely on **curriculum documents** (KSSR_SJKC, Cambridge Primary) — NOT
  present in Reference DB
- Must rely on **teacher experience** / **native speaker authoring**
- All content must be 100% KuizKu ORIGINAL

### K.5 Reference DB usage scope (preserved)

Per Phase 10.2 §copyright:
```
Reference DB
  → syllabus/topic/difficulty/style/skill reference (✅ ALLOWED)
NOT:
  → copy (❌)
  → near-paraphrase (❌)
  → synonym substitution (❌)
  → number-only change (❌)
  → name-only change (❌)
  → context-only change (❌)
  → reconstructed exam question (❌)
```

Even for SK (where Reference DB has Malaysian exam papers), Phase 10.1's 100
questions passed all anti-copy checks (Check 11/12/14/15 in quality_gate.py).

---

## L. Three Volume Scenarios

### L.0 Assumptions

- **Common subjects**: BM (ms), English (en), Math, Science exist in all 3 tracks
- **Track-specific subjects**: 华文 (BC) is native in SJKC only; Moral is SK-only;
  Islamic Studies is SK-only (and SJKC-Islamic)
- **Per-grade**: 6 primary grades (Tahun 1-6)
- **Per-subject per-grade**: 25-30 questions as baseline (per Phase 10.1's 100-Q
  Tahun 1 experience)
- **NOT generated for**: Secondary T1-T5 (separate Phase 11+ planning)

### L.1 Scenario A — Core multilingual (one bank, language variants)

**Design**: A single bank per grade containing questions with multiple
`language` tags. Each question belongs to one schoolTrack + one language.

```
subjectId = "<track>_<stage>_<subjCode>_<grade>_<topic>"

Per Tahun N, per subject:
  BM (ms, native SK only): 30 Q
  BC (zh, native SJKC only): 30 Q
  English (en, MFL for SK/SJKC, native for Intl): 20 Q
  Mathematics (ms/zh/en depending on track):
    SK Math (ms): 28 Q
    SJKC Math (zh): 28 Q
    International Math (en): 28 Q
  Science (ms/zh/en):
    SK Science (ms): 22 Q
    SJKC Science (zh): 22 Q
    International Science (en): 22 Q
```

**Per-grade totals**:
| Subject | Q per grade (sum of 3 tracks) |
|---|---:|
| BM (SK only) | 30 |
| BC (SJKC only) | 30 |
| English (all tracks) | 60 (20 × 3) |
| Math (all tracks) | 84 (28 × 3) |
| Science (all tracks) | 66 (22 × 3) |
| **Per-grade total** | **270 Q** |

**Total for 6 years**:
- 270 × 6 = **1,620 Q**

**Track totals across all years**:
- SK: (30 BM + 20 EN + 28 Math + 22 Science) × 6 = 600 Q
- SJKC: (30 BC + 20 EN + 28 Math + 22 Science) × 6 = 600 Q
- International: (20 EN + 28 Math + 22 Science) × 6 = 420 Q

**Language totals across all years**:
- ms: SK BM (30×6) + SK Math (28×6) + SK Science (22×6) = 480 Q
- zh: SJKC BC (30×6) + SJKC Math (28×6) + SJKC Science (22×6) = 480 Q
- en: EN all tracks (20×3×6) + Intl Math (28×6) + Intl Science (22×6) = 660 Q

**Math language variants**: 3 (ms/zh/en) × 6 years × 28 Q = 504 Q
**Science language variants**: 3 (ms/zh/en) × 6 years × 22 Q = 396 Q

### L.2 Scenario B — School-track separated (3 parallel banks)

**Design**: Three separate banks — `V5-SK-Primary`, `V5-SJKC-Primary`,
`V5-International-Primary`. Each bank is self-contained.

```
V5-SK-Primary:
  Per grade: 30 BM + 20 EN + 28 Math + 22 Science = 100 Q
  6 grades × 100 = 600 Q

V5-SJKC-Primary:
  Per grade: 30 BC + 20 EN + 28 Math(in BC) + 22 Science(in BC) = 100 Q
  6 grades × 100 = 600 Q

V5-International-Primary:
  Per grade: 20 EN(native) + 28 Math(in EN) + 22 Science(in EN) = 70 Q
  (NO BM/BC — those are MFL, not in International scope by default)
  6 grades × 70 = 420 Q
```

**Track totals**:
- SK: 600 Q
- SJKC: 600 Q
- International: 420 Q

**Grand total**: **1,620 Q** (same as Scenario A — but organized in 3 banks)

**Language totals**:
- ms: SK only — 30 BM × 6 + 28 Math × 6 + 22 Science × 6 = 480 Q
- zh: SJKC only — 30 BC × 6 + 28 Math × 6 + 22 Science × 6 = 480 Q
- en: 20 (SK EN) × 6 + 20 (SJKC EN) × 6 + 20 (Intl EN native + Intl Math + Intl Science)
  × 6 = 660 Q

### L.3 Scenario C — Hybrid (common core + track-specific)

**Design**: A "core" bank containing Math/Science/EN content that's
language-agnostic (i.e., the knowledge concept) + track-specific language
variants as overlays.

```
Common Core (per grade):
  - Math (concepts): 28 Q (e.g., "fraction addition")
  - Science (concepts): 22 Q (e.g., "photosynthesis")
  - English (concepts): 20 Q (e.g., "reading comprehension")

Track-specific (per grade):
  - SK: BM 30 Q + (Math/Science/EN with Malay word problems)
  - SJKC: BC 30 Q + (Math/Science/EN with Chinese word problems)
  - International: EN 20 Q (native-level literature/composition) + (Math/Science/EN with English word problems)
```

**Total per grade**:
- Common core: 70 Q (Math + Science + English)
- SK track: 30 BM + 70 (with Malay overlays)
- SJKC track: 30 BC + 70 (with Chinese overlays)
- International track: 20 EN native + 70 (with English overlays)

**Grand total**: 
- Common core: 70 × 6 = 420 Q
- Per track: 100 × 6 = 600 Q × 3 tracks = 1,800 Q
- Total: **2,220 Q** (some overlap if concepts are reused)

**Note**: Scenario C is conceptually clean but operationally complex (overlapping
content + overlays). Realistically, Scenario A or B is more practical.

### L.4 Scenario comparison

| Metric | A (Core multilingual) | B (Track separated) | C (Hybrid) |
|---|---:|---:|---:|
| Grand total | 1,620 Q | 1,620 Q | ~2,220 Q |
| SK | 600 | 600 | 600 |
| SJKC | 600 | 600 | 600 |
| International | 420 | 420 | 420 |
| Math variants | 3 (ms/zh/en) | 3 (ms/zh/en) | 3 |
| Science variants | 3 | 3 | 3 |
| EN variants | 3 | 3 | 3 |
| Bank count | 1 | 3 | 4+ |
| Operational complexity | Medium | High (3 banks to manage) | Very High |
| Phase 10.1 reuse | Yes (SK Tahun 1) | Yes (SK Tahun 1) | Yes (SK Tahun 1) |

### L.5 Recommended Scenario

**Scenario B (Track separated)** — recommended for these reasons:

1. **Clear semantic boundaries**: Each bank has well-defined school track +
   medium of instruction. No risk of a Malay-medium Math question leaking into
   a SJKC student's app.

2. **Phased delivery**: Can ship SK-first (Phase 10.5), SJKC-next (Phase 11+),
   International-last (Phase 12+) — each is independently deployable.

3. **Independent encryption keys**: V5-SK, V5-SJKC, V5-Intl each get their own
   AES-256-GCM key — no cross-bank key reuse.

4. **Phase 10.1 alignment**: Phase 10.1's 100 SK-aligned Tahun 1 questions map
   directly to V5-SK-Primary Tahun 1.

5. **No architectural changes needed**: Scenario B keeps SubjectId as the
   primary filter; schoolTrack is just an additional first-class prefix.

**Scenario A** is acceptable but harder to filter in Home UI without schoolTrack
being a first-class Subject attribute.

**Scenario C** is rejected for Phase 10+ due to operational complexity.

---

## M. Recommended Implementation Phases

### M.1 Phase 10.2 (this report) — Preflight + Recommendation
- ✅ READ-ONLY analysis
- Output: this report
- Status: HARD STOP, awaiting 638 authorization

### M.2 Phase 10.3 — Android source preparation for schoolTrack
- Add `schoolTrack` + `language` + `curriculum` fields to `Subject` domain
- Add `schoolTrack` + `curriculum` fields to `Question` domain (nullable)
- Update `SubjectEntity` (Room schema bump v2 → v3)
- Update `SubjectGrouping` parser to recognize `<track>_<stage>_<subjCode>` prefix
- Update `BankSyncer` to read + validate `schoolTrack` field
- Update `HomeViewModel` to filter by schoolTrack
- Update `LevelSelectionViewModel` + `LevelSelectionScreen` to include
  schoolTrack choice (3 cards: 🎒 SK / 🟡 SJKC / 🌐 International)
- Update `UserLevel` to include schoolTrack

**Risk**: schema bump requires Android source modification. **Strict scope
lock**: Phase 10.3 cannot start without 638 explicit authorization + Phase 10.2
report approval.

### M.3 Phase 10.4 — SK Tahun 2-6 generation
- Use Phase 10.1's 100 SK Tahun 1 questions as baseline
- Generate 500 more SK-aligned questions (T2-T6, 100 each)
- Strict 16-check quality gate per batch
- Total SK bank: 600 Q (matches Scenario B V5-SK-Primary)

### M.4 Phase 10.5 — V5-SK-Primary bank build + publish
- Encrypt all 600 SK Tahun 1-6 questions
- bankId: `llcai_kuizku_my_v5_sk_primary_original`
- keyId: `v5-sk-primary-original-master`
- schemaVersion: 4 (NEW — adds schoolTrack, curriculum)
- publisherVersion: 1
- Publish to `/v5-sk/` GitHub Pages
- Note 8 UAT (DEBUG runtime: add v5-sk path detection + key allowlist)

### M.5 Phase 11+ — SJKC + International tracks (separate authorization)
- Phase 11.1: SJKC Tahun 1-6 (600 Q in BC + Math-in-BC + Science-in-BC)
- Phase 11.2: International Tahun 1-6 (420 Q in EN native + Math-in-EN + Science-in-EN)
- Phase 11.3: Build V5-SJKC + V5-International banks
- Phase 11.4: Runtime test multi-track
- Phase 11.5: Home UI multi-track selection

### M.6 Phase 12+ — Secondary schools (T1-T5)
- Same architecture applies
- T1-T3 = LowerSecondary (BM + English + Math + Science)
- T4-T5 = UpperSecondary (BM + English + Math + Science + addtl. subjects)
- Scope expansion deferred

---

## N. Migration Risk

### N.1 Schema migration (SubjectEntity v2 → v3)

```
ADD COLUMN schoolTrack TEXT NOT NULL DEFAULT 'SK'
ADD COLUMN language TEXT NOT NULL DEFAULT 'ms'
ADD COLUMN gradeLevel TEXT NOT NULL DEFAULT ''
ADD COLUMN subjectCode TEXT NOT NULL DEFAULT ''
ADD COLUMN curriculum TEXT NOT NULL DEFAULT 'KSSR'
ADD COLUMN displayName TEXT NOT NULL DEFAULT '{}'  -- JSON map
```

**Risk**: existing banks V1/V3/V4-TEST in Room will be migrated automatically
with default values. V1 bootstrap (eng_vocab / gen_know) gets
schoolTrack="SK" (incorrect — but these are Phase 9 hidden anyway).

**Mitigation**: 
- Add migration script in `Migrations.kt` (Phase 10.3)
- For existing subjects, populate `subjectCode` from subjectId via parser
- For existing questions, populate `schoolTrack` from subject (inherited)

### N.2 SubjectGrouping breaking change

The Phase 9 regex `^(prim|sec)_([a-z]+)_([YyTt])(\d+)_(.+)$` will NOT match
new `sk_prim_*` / `skc_prim_*` / `intl_prim_*` subjectIds.

**Mitigation**:
1. Add new regex `^(sk|skc|intl)_(prim|sec)_([a-z]+)_([YyTt])(\d+)_(.+)$`
2. Keep old regex as fallback (for backward-compat with V1/V3/V4-TEST
   subjectIds that haven't been renamed yet)
3. New banks MUST use new format; old banks continue with old format

### N.3 QuestionEntity migration (v2 → v3)

```
ADD COLUMN schoolTrack TEXT NULL
ADD COLUMN curriculum TEXT NULL
ADD COLUMN syllabusRef TEXT NULL
ADD COLUMN learningObjective TEXT NULL
```

Nullable columns = no risk of breaking existing data.

### N.4 BankSyncer version compatibility

Current BankSyncer expects schemaVersion ≤ 3. If a new V5 bank ships with
schemaVersion 4 (schoolTrack field), BankSyncer would fail to load it
without code changes.

**Mitigation**: Phase 10.3 must update BankSyncer to accept schemaVersion 4
BEFORE V5-SK-Primary can be deployed.

### N.5 UserLevel change

`UserLevel.Primary(year)` currently has NO schoolTrack. Adding schoolTrack
breaks the sealed interface contract.

**Mitigation**: Make schoolTrack part of UserLevel (or a sibling model).
Auto-inference logic must also be updated to infer schoolTrack (default SK).

### N.6 Phase 10.1 backward compatibility

Phase 10.1's `tahun_1_pilot.json` does NOT have schoolTrack/curriculum
fields. If Phase 10.5 builds V5-SK-Primary from this + 500 new SK questions,
the JSON schema must add these fields (schemaVersion 4).

**Mitigation**: Update generate_tahun_1_data.py to include new fields in
every question.

---

## O. What Should Remain Frozen

| Component | Status | Reason |
|---|---|---|
| V1 bootstrap (eng_vocab / gen_know) | 🧊 Frozen | Legacy data, Phase 9 hidden |
| V3 production bank (`/v3/`) | 🧊 Frozen | Phase 5.6A released, SHA `854b41fe` is locked |
| V4-TEST bank (`/v4-test/`) | 🧊 Frozen | Internal pilot only; not for distribution |
| Phase 10.1 `tahun_1_pilot.json` | 🧊 Frozen | SHA-256 `72ca4e4586efd27270c38ecbc4d359b21f2c599272468a5097f672c06269c159` preserved |
| Reference DB (`references\`) | 🧊 READ-ONLY | Per 638 §"不修改 Reference DB" |
| SubjectGrouping regex (Phase 9 frozen format) | 🧊 Backward-compat fallback | Old banks still use it |
| BankManifest `schemaVersion=3` (V3/V4-TEST) | 🧊 Frozen | V3/V4-TEST locked |
| KuizKuApp.kt (Phase 8D.16 RTB disable) | 🧊 Frozen | Phase 8D closed |
| BankSyncer (Phase 8D.1 keyId allowlist) | 🧊 Partially frozen — may need additive change for schemaVersion 4 |
| Encryption keys V1 / V3 / V4-TEST | 🧊 Frozen | Production keys |

**Mutable with 638 authorization**:
- Android source code (Phase 10.3 schema + SubjectGrouping + BankSyncer + Home/Level UI)
- New banks (V5-SK-Primary, V5-SJKC-Primary, V5-International-Primary)
- Generate_tahun_1_data.py (Phase 10.1 update for new schema fields)
- Room Migrations.kt (v2 → v3 schema bump)

**Hard NO**:
- ❌ Modify V3 / V4-TEST bank content
- ❌ Modify Reference DB
- ❌ Upload to Google Play
- ❌ Push to remote (local commits only)
- ❌ Auto-migrate SubjectEntity without schema version bump + Migration script

---

## P. Exact Next-Step Authorization Required

To proceed beyond Phase 10.2 (READ-ONLY), 638 must explicitly authorize each
of the following — separately:

### P.1 Phase 10.3 — Android schema preparation (Phase 10.2 → 10.3)

Required authorization:
> "授权 Phase 10.3 — Android source modifications for schoolTrack + language
> + curriculum metadata. Schema bump SubjectEntity v2 → v3 with Migration
> script. SubjectGrouping parser update. BankSyncer schemaVersion 4 support.
> NO V3 / V4-TEST / Reference DB modifications."

### P.2 Phase 10.4 — SK Tahun 2-6 generation (Phase 10.3 → 10.4)

Required authorization (per grade, NOT all at once):
> "授权 Phase 10.4 — Tahun N generation (100 SK-aligned ORIGINAL questions).
> Per-grade authorization, hard STOP after each grade."

### P.3 Phase 10.5 — V5-SK-Primary build + publish (Phase 10.4 → 10.5)

Required authorization:
> "授权 Phase 10.5 — Build V5-SK-Primary bank (600 Q) + publish to `/v5-sk/`
> GitHub Pages + Note 8 runtime test."

### P.4 Phase 11+ — SJKC + International tracks

Each track is a SEPARATE authorization:
> "授权 Phase 11 — [SJKC | International] track planning + generation."

### P.5 What 638 should NOT expect from Phase 10.2

- ❌ No questions generated
- ❌ No Tahun 2-6
- ❌ No V5 runtime bank
- ❌ No Android source modification
- ❌ No Reference DB modification
- ❌ No commit
- ❌ No push

Phase 10.2 output = this READ-ONLY architecture report.

---

## Q. Critical Decisions Still Pending 638

The following decisions are flagged for explicit 638 resolution before any
further phase starts:

1. **Scenario selection** — A, B, or C? (Recommendation: B)
2. **SJKC scope confirmation** — Does KuizKu intend to serve SJKC schools?
   (Reference DB has zero primary Chinese coverage; building SJKC bank
   requires new ORIGINAL content from scratch.)
3. **International scope confirmation** — Does KuizKu intend to serve
   International Schools? (Cambridge Primary curriculum is structurally
   different from KSSR; needs separate blueprint.)
4. **Moral Education + Islamic Studies** — Include in SK bank?
   (Phase 10.1 does not include them; current V3/V4-TEST do not include them.)
5. **Phase 10.1 → SK Tahun 1 baseline** — Approved to proceed as SK Tahun 1
   in V5-SK-Primary bank? (Recommended: yes, after schema migration.)

---

## ✅ Phase 10.2 Scope Compliance

| Forbidden action | Status |
|---|---|
| ❌ Generate any new question | NOT DONE ✅ |
| ❌ Generate Tahun 2-6 | NOT DONE ✅ |
| ❌ Build V5 runtime bank | NOT DONE ✅ |
| ❌ Modify V3 | NOT DONE ✅ |
| ❌ Modify V4-TEST | NOT DONE ✅ |
| ❌ Modify Android source | NOT DONE ✅ |
| ❌ Modify Room schema | NOT DONE ✅ |
| ❌ Modify sync/encryption | NOT DONE ✅ |
| ❌ Modify Reference DB | NOT DONE ✅ |
| ❌ Commit | NOT DONE ✅ |
| ❌ Push | NOT DONE ✅ |
| ❌ Google Play upload | NOT DONE ✅ |

All Phase 10.2 work = READ-ONLY analysis of existing Android source, V3/V4-TEST
manifest, Phase 10.1 pilot JSON, Reference DB directory structure, and
production of this architecture report.

---

# 🛑 HARD STOPPED — 等待 638 下一步明確授權

Phase 10.2 = READ-ONLY architecture report only. **No questions generated.
No source modified. No commit.** SHA of Phase 10.1 pilot preserved.

**Next-step authorization required (per §P.1–P.5)** — 638 must explicitly
authorize Phase 10.3 (Android schema) before any implementation begins.

🚢
