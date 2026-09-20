# Phase 10.3 IMPLEMENTATION PLAN — KuizKu Multi-Track Schema Preparation

> **READ-ONLY PLAN. NO CODE MODIFICATIONS YET.** Per 638 §十四: "先输出
> IMPLEMENTATION PLAN. 如果计划发现需要重大架构改变，先 HARD STOP".

---

## 0. Decision Recap (from Phase 10.2 + 638 confirmation)

- **Adopted**: Scenario B (Track Separated)
- **Phase 10.1 confirmed**: SK Primary Tahun 1 baseline (frozen, SHA-256
  `72ca4e4586efd27270c38ecbc4d359b21f2c599272468a5097f672c06269c159`)
- **V3 / V4-TEST frozen**
- **Reference DB READ-ONLY**

---

## 1. Files to be Modified

### 1.1 :domain module (4 files modified + 3 new)

**Modified**:
- `Subject.kt` — Add 5 new fields (schoolTrack, language, gradeLevel, subjectCode, curriculum)
- `Question.kt` — Add 2 nullable fields (schoolTrack, curriculum)
- `SubjectGrouping.kt` — Add V5_REGEX parser + backward-compat legacy regex
- `UserLevel.kt` — Add SchoolTrack enum + ParsedSubject data class + UserSelection wrapper

**New**:
- `SchoolTrack.kt` — Enum (SK, SJKC, INTERNATIONAL) + Curriculum enum (KSSR, KSSR_SJKC, CAMBRIDGE_PRIMARY)
- `ParsedSubject.kt` — Result type for SubjectGrouping.parse()
- `UserSelection.kt` — Wraps UserLevel + schoolTrack for UI state

### 1.2 :data module (4 files modified + 1 new)

**Modified**:
- `SubjectEntity.kt` — Add 5 NOT NULL columns with defaults
- `QuestionEntity.kt` — Add 2 NULLABLE columns
- `AppDatabase.kt` — Bump version 2 → 3, register MIGRATION_2_3
- `Migrations.kt` — Add MIGRATION_2_3 with ALTER TABLE + backfill UPDATEs

**New**:
- `DataBackfill.kt` — Helper for migration v2 → v3 backfill (in :data, callable from Migrations.kt)

### 1.3 :sync module (1 file modified)

**Modified**:
- `BankSyncer.kt` — Add MAX_SUPPORTED_SCHEMA_VERSION = 4 constant + reject logic + read schoolTrack/curriculum fields when schemaVersion ≥ 4

### 1.4 :app module (3 files modified — MINIMAL)

**Modified**:
- `HomeViewModel.kt` — Filter subjects by schoolTrack in addition to grade level
- `LevelSelectionViewModel.kt` — Include schoolTrack selection in TierSelection UI state
- `HomeScreen.kt` — Display schoolTrack in greeting; show "Select your school" if track is null

### 1.5 :core:security module (0 files)

**NOT MODIFIED** per 638 §九. V1/V3/V4-TEST keys preserved.

### 1.6 :data:bootstrap (0 files)

**NOT MODIFIED**. BootstrapBank.kt frozen.

---

## 2. New Files to be Created

| File | Module | Purpose |
|---|---|---|
| `SchoolTrack.kt` | :domain | Enum SK/SJKC/INTERNATIONAL + Curriculum enum |
| `ParsedSubject.kt` | :domain | Parser result type |
| `UserSelection.kt` | :domain | UserLevel + schoolTrack wrapper |
| `DataBackfill.kt` | :data | Helper for v2 → v3 backfill |
| `SchoolTrackTest.kt` | :domain:test | Enum round-trip |
| `ParsedSubjectTest.kt` | :domain:test | Parser cases (V5 + legacy) |
| `SubjectGroupingMigrationTest.kt` | :domain:test | Backward compat for legacy subjectIds |
| `UserSelectionTest.kt` | :domain:test | DataStore round-trip |
| `MigrationsV2V3Test.kt` | :data:test | Room migration test |
| `HomeViewModelTrackTest.kt` | :app:test | UI filter by track |

---

## 3. Per-File Modification Reason

### 3.1 Subject.kt (domain)
Add 5 fields: `schoolTrack`, `language`, `gradeLevel`, `subjectCode`, `curriculum`.
- `schoolTrack` — SK/SJKC/INTERNATIONAL
- `language` — ms/zh/en (medium of instruction)
- `gradeLevel` — "Tahun1".."Tahun6" (no longer derived from subjectId regex — explicit)
- `subjectCode` — bm/bc/en/math/science/moral/islam (curriculum-independent code)
- `curriculum` — KSSR/KSSR_SJKC/CAMBRIDGE_PRIMARY

### 3.2 Question.kt (domain)
Add 2 nullable fields: `schoolTrack`, `curriculum`.
- These are denormalized for query efficiency (so Home can filter by track without joining)
- Nullable because per-question override is optional (most questions inherit from Subject)

### 3.3 SubjectGrouping.kt (domain parser)
Add V5_REGEX + backward-compat legacy regex:
- V5 format: `^(sk|skc|intl)_(prim|sec)_([a-z]+)_([YyTt])(\d+)$` (4-segment)
- Legacy format: `^(prim|sec)_([a-z]+)_([YyTt])(\d+)_(.+)$` (5-segment with topic)

### 3.4 UserLevel.kt (domain)
- Add `SchoolTrack` enum (defined here or in new file)
- Add `ParsedSubject` data class
- Extend `UserSelection` wrapper

### 3.5 SubjectEntity.kt (Room)
Add 5 NOT NULL columns with defaults:
```kotlin
val schoolTrack: String = "SK"
val language: String = "ms"
val gradeLevel: String = ""
val subjectCode: String = ""
val curriculum: String = "KSSR"
```

### 3.6 QuestionEntity.kt (Room)
Add 2 NULLABLE columns:
```kotlin
val schoolTrack: String? = null
val curriculum: String? = null
```

### 3.7 AppDatabase.kt (Room)
Bump version: 2 → 3. Register MIGRATION_2_3.

### 3.8 Migrations.kt (Room migration)
Add MIGRATION_2_3:
```kotlin
val MIGRATION_2_3 = object : Migration(2, 3) {
    override fun migrate(db: SupportSQLiteDatabase) {
        // 1. Add columns with defaults
        db.execSQL("ALTER TABLE subject ADD COLUMN schoolTrack TEXT NOT NULL DEFAULT 'SK'")
        db.execSQL("ALTER TABLE subject ADD COLUMN language TEXT NOT NULL DEFAULT 'ms'")
        db.execSQL("ALTER TABLE subject ADD COLUMN gradeLevel TEXT NOT NULL DEFAULT ''")
        db.execSQL("ALTER TABLE subject ADD COLUMN subjectCode TEXT NOT NULL DEFAULT ''")
        db.execSQL("ALTER TABLE subject ADD COLUMN curriculum TEXT NOT NULL DEFAULT 'KSSR'")

        // 2. Add nullable columns to question
        db.execSQL("ALTER TABLE question ADD COLUMN schoolTrack TEXT NULL")
        db.execSQL("ALTER TABLE question ADD COLUMN curriculum TEXT NULL")

        // 3. Backfill gradeLevel + subjectCode from legacy subjectId
        //    (SQLite-compatible LIKE patterns)
        db.execSQL("""
            UPDATE subject SET subjectCode = 'bm'
            WHERE subjectId LIKE 'prim_bm_%' OR subjectId LIKE 'sec_bm_%'
        """)
        db.execSQL("""
            UPDATE subject SET subjectCode = 'math'
            WHERE subjectId LIKE 'prim_math_%' OR subjectId LIKE 'sec_math_%'
        """)
        // ... (similar for en, science, etc.)
        // gradeLevel backfill via SUBSTR pattern matching:
        db.execSQL("""
            UPDATE subject SET gradeLevel =
                'Tahun' || SUBSTR(subjectId, INSTR(subjectId, '_Y') + 2, 1)
            WHERE subjectId LIKE 'prim_%_Y%' AND gradeLevel = ''
        """)
        // 4. Backfill question.schoolTrack + curriculum from subject
        db.execSQL("""
            UPDATE question SET schoolTrack = (SELECT schoolTrack FROM subject s WHERE s.subjectId = question.subjectId)
            WHERE schoolTrack IS NULL
        """)
        db.execSQL("""
            UPDATE question SET curriculum = (SELECT curriculum FROM subject s WHERE s.subjectId = question.subjectId)
            WHERE curriculum IS NULL
        """)
    }
}
```

### 3.9 BankSyncer.kt (sync)
- Add `MAX_SUPPORTED_SCHEMA_VERSION = 4` constant
- Reject if `manifest.schemaVersion > MAX_SUPPORTED_SCHEMA_VERSION`
- Read new fields when schemaVersion ≥ 4

### 3.10 HomeViewModel.kt (app)
- Add `userLevelRepository: UserLevelRepository` injection (already exists from Phase 9)
- Read `UserSelection` (not bare `UserLevel`)
- Filter subjects by `(subject.schoolTrack == userSelection.schoolTrack) AND (grade matches)`
- If schoolTrack is null, show "Please pick your school" empty state

### 3.11 LevelSelectionViewModel.kt (app)
- Include schoolTrack in TierSelection state (3 tracks as sub-options)
- Persist track via `UserLevelRepository.setSchoolTrack()`

### 3.12 HomeScreen.kt (app)
- Display schoolTrack in greeting (e.g., "belajar di Tahun 5 (SK)")
- Show schoolTrack in Change Level card
- Empty state if schoolTrack is null

---

## 4. Room Migration Strategy

### 4.1 MIGRATION_2_3 — 4-phase atomic migration

**Phase 1**: Add columns (atomic per table).
**Phase 2**: Backfill `subject.subjectCode` from subjectId LIKE patterns.
**Phase 3**: Backfill `subject.gradeLevel` from subjectId SUBSTR patterns.
**Phase 4**: Backfill `question.schoolTrack` + `question.curriculum` from subject lookup.

### 4.2 Atomicity guarantees

- Each ALTER TABLE is atomic (SQLite single-statement transaction)
- UPDATE batches run within the same Migration transaction
- If migration fails partway, Room rolls back; app re-runs migration on next launch

### 4.3 Safety: No data deletion

- ALTER TABLE ADD COLUMN is non-destructive
- UPDATE statements only set values (don't remove existing ones)
- No DROP TABLE, no DELETE statements in the migration

### 4.4 Safety: Foreign keys preserved

- Subject → Question CASCADE: Adding nullable columns to `question` doesn't change FK
- QuizAttempt → AnswerRecord CASCADE: AnswerRecord schema unchanged
- No FK changes in this migration

### 4.5 Idempotency

If migration is somehow re-run (shouldn't happen, but defense):
- ALTER TABLE ADD COLUMN fails on second run (column exists)
- UPDATE with WHERE gradeLevel='' is no-op on second run
- Result: migration is naturally idempotent after Phase 1 succeeds

---

## 5. SchemaVersion Strategy

| Bank | schemaVersion | status | fields handled |
|---|---:|---|---|
| V3 production | 3 | FROZEN | defaults applied |
| V4-TEST | 3 | FROZEN | defaults applied |
| V5-SK-Primary (Phase 10.5+) | 4 | NEW | `schoolTrack` + `curriculum` |

### 5.1 BankSyncer schemaVersion handling

```kotlin
const val MAX_SUPPORTED_SCHEMA_VERSION = 4

suspend fun sync() {
    val manifest = fetchManifest()
    if (manifest.schemaVersion > MAX_SUPPORTED_SCHEMA_VERSION) {
        error("schemaVersion ${manifest.schemaVersion} > max supported ($MAX_SUPPORTED_SCHEMA_VERSION). Update app.")
    }
    if (manifest.schemaVersion < 3) {
        error("schemaVersion ${manifest.schemaVersion} < 3 (legacy V1/V2). Not supported.")
    }
    // schemaVersion 3 or 4 → continue with appropriate parsing
}
```

### 5.2 Forward-compat rejection

`schemaVersion > 4` → error and abort sync. App prompts user to update.

### 5.3 Backward-compat acceptance

`schemaVersion == 3` (V3, V4-TEST) → continue normal, fields default.
`schemaVersion == 4` (V5) → continue with new fields read.

### 5.4 Downgrade

`publisherVersion` already guards against downgrade (Phase 0A rule). If somehow V3 bank is loaded after V5: V3's missing fields default; existing V5 data unaffected (BankSyncer only inserts/replaces per-subject).

### 5.5 Partial download

Phase 8D-tested atomic import per subject. BankSyncer's `atomicImportBank` (Phase 3.4A pattern) imports all-or-nothing per subject. Per-subject decryption failure → atomic failure for that subject only.

---

## 6. Backward Compatibility Strategy

### 6.1 V1 bootstrap subjects (`eng_vocab`, `gen_know`)
- SubjectId doesn't match prim/sec regex → migration sets gradeLevel="" + subjectCode=""
- schoolTrack default="SK" (assumption for legacy data)
- Phase 9 hides these from Home (parseStageAndGrade returns null) — behavior preserved

### 6.2 V3 production subjects (27 BM subjects)
- SubjectId: `prim_bm_Y<n>_<topic>`
- Migration backfills: schoolTrack="SK", subjectCode="bm", gradeLevel="Tahun<n>"
- SubjectGrouping recognizes legacy format → returns ParsedSubject(schoolTrack=SK, ...)

### 6.3 V4-TEST subjects (12 BM subjects)
- Same as V3 — all backfilled to SK/BM

### 6.4 Phase 10.1 JSON pilot
- File NOT modified (per 638 §十二)
- SHA-256 `72ca4e4586efd27270c38ecbc4d359b21f2c599272468a5097f672c06269c159` preserved
- Phase 10.5 will produce a NEW V5 file (schemaVersion 4) including schoolTrack="SK" per question

### 6.5 BankManifest schemaVersion
- No change required (BankManifest schemaVersion is a manifest field, not a Subject/Question field)
- V5 manifest can declare `schemaVersion=4` and existing manifests remain at `schemaVersion=3`

---

## 7. V3 / V4-TEST Compatibility

### 7.1 V3 (`/v3/`)
- **Manifest schemaVersion**: 3 (unchanged, frozen)
- **BankSyncer behavior**: reads manifest, sees schemaVersion=3 (≤4), parses V3 JSON (no `schoolTrack` field), defaults applied → `schoolTrack="SK"` for all V3 subjects
- **SubjectEntity after migration**: `schoolTrack="SK"`, `subjectCode="bm"`, `gradeLevel="Tahun<n>"` (backfilled)
- **HomeViewModel**: V3 users see "Tahun 5 (SK)" — minimal change to UI

### 7.2 V4-TEST (`/v4-test/`)
- **Manifest schemaVersion**: 3 (unchanged, frozen)
- **Same behavior as V3**: schoolTrack="SK" default applied

### 7.3 V3 / V4-TEST runtime safety
- BankSyncer does NOT modify V3 / V4-TEST manifest files on disk
- BankSyncer does NOT touch `/v3/` or `/v4-test/` directories
- Only Room database is updated; bank files remain frozen

---

## 8. Phase 10.1 JSON Compatibility

### 8.1 Phase 10.1 pilot file
- File path: `D:\Users\bajub\kuizku_p10\tahun_1_pilot.json`
- SHA-256 (questions-only): `72ca4e4586efd27270c38ecbc4d359b21f2c599272468a5097f672c06269c159`
- **MUST NOT be modified** (per 638 §十二)

### 8.2 Phase 10.1 → V5-SK-Primary transformation
- Phase 10.5 (NOT Phase 10.3) will transform Phase 10.1 JSON into V5 schemaVersion=4 format
- Transformation adds `schoolTrack="SK"` and `curriculum="KSSR"` per question
- Output: NEW V5-SK-Primary bank file (Phase 10.5 scope)
- Phase 10.3 only prepares schema to ACCEPT schemaVersion=4

### 8.3 Phase 10.1 compatibility check
- Phase 10.1 JSON has `language` field (already in schema)
- Phase 10.1 JSON has `gradeLevel="Tahun1"` (already in schema)
- Phase 10.1 JSON does NOT have `schoolTrack` or `curriculum` (NEW fields, optional)
- When Phase 10.5 ships V5, transformation adds these fields. Backward compat with Phase 10.1 JSON is maintained.

---

## 9. UserLevel Migration Strategy

### 9.1 DataStore keys (existing + new)

**Existing** (Phase 9 frozen):
- `user_level_tier` (String: "primary" | "lower_secondary" | "upper_secondary" | "not_selected")
- `user_level_year` (Int: 1..6 for primary)

**NEW** (Phase 10.3):
- `user_level_track` (String: "SK" | "SJKC" | "INTERNATIONAL" | "" for unknown)

### 9.2 Old user behavior

- DataStore has `user_level_tier="primary"`, `user_level_year=5`, `user_level_track` missing
- UserSelection reads as: `UserSelection(level=UserLevel.Primary(5), schoolTrack=null)`
- HomeViewModel detects `schoolTrack == null` → shows "Select your school" empty state with 3 track cards
- User must pick track before subject list shows
- **NO auto-inference to SK** (per 638 §六 "不得凭空猜测他是 SK / SJKC / International")

### 9.3 New user behavior

- First launch: TierSelectionScreen with 3 tier cards (Primary/Secondary/UpperSecondary)
- After tier pick: TrackSelectionScreen with 3 track cards (SK/SJKC/INTERNATIONAL)
- After track pick: YearSelectionScreen (Tahun 1-6)
- After year pick: UserSelection saved, Home shows

### 9.4 Existing user safety

- Per 638 §六 "旧用户不得被错误自动归类"
- V3 / V4-TEST users (currently Note 8) → after app update, see "Select your school" prompt on next launch
- User picks track → saved to DataStore
- Future sessions show same track

---

## 10. SubjectGrouping Parser Strategy

### 10.1 Two regex patterns

```kotlin
// V5 format (Phase 10.3+): 4-segment, NO topic
private val V5_REGEX = Regex(
    "^(sk|skc|intl)_(prim|sec)_([a-z]+)_([YyTt])(\\d+)$"
)

// Legacy V3/V4-TEST format: 5-segment WITH topic (backward compat)
private val LEGACY_REGEX = Regex(
    "^(prim|sec)_([a-z]+)_([YyTt])(\\d+)_(.+)$"
)
```

### 10.2 parse() function

```kotlin
fun parse(subjectId: String): ParsedSubject? {
    val v5Match = V5_REGEX.matchEntire(subjectId)
    if (v5Match != null) {
        val (trackStr, stageStr, subjCode, _, yearStr) = v5Match.destructured
        return ParsedSubject(
            schoolTrack = SchoolTrack.fromString(trackStr),
            stage = if (stageStr == "prim") Stage.Primary else Stage.Secondary,
            subjectCode = subjCode,
            year = yearStr.toInt(),
            topic = null,  // topic not in subjectId
        )
    }
    val legacyMatch = LEGACY_REGEX.matchEntire(subjectId)
    if (legacyMatch != null) {
        val (stageStr, subjCode, _, yearStr, topic) = legacyMatch.destructured
        return ParsedSubject(
            schoolTrack = SchoolTrack.SK,  // default backfill assumption
            stage = if (stageStr == "prim") Stage.Primary else Stage.Secondary,
            subjectCode = subjCode,
            year = yearStr.toInt(),
            topic = topic,
        )
    }
    return null  // legacy bootstrap subjects (eng_vocab etc.)
}
```

### 10.3 Phase 9 backward compat

The Phase 9 function `parseStageAndGrade(subjectId: String): SubjectStageAndGrade?` is preserved as a thin wrapper:
```kotlin
fun parseStageAndGrade(subjectId: String): SubjectStageAndGrade? {
    return parse(subjectId)?.let { SubjectStageAndGrade(stage = it.stage, year = it.year) }
}
```

This way, all existing callers (HomeViewModel, LevelSelectionViewModel, SubjectGroupingTest) continue to work without modification.

### 10.4 Unit tests required

- V5 parsing: `sk_prim_bm_Y5`, `skc_prim_bc_Y5`, `intl_prim_en_Y5`
- Legacy parsing: `prim_bm_Y5_peribahasa`, `sec_bm_T4_essay`
- Edge cases: `bootstrap_gk` (returns null), `RTB_y5_topic` (returns null — RTB disabled)
- SubjectCode preservation across formats
- schoolTrack backfill (legacy → SK)

---

## 11. BankSyncer Strategy

### 11.1 schemaVersion check

```kotlin
// In sync() at line ~78
if (manifest.schemaVersion > MAX_SUPPORTED_SCHEMA_VERSION) {
    error("schemaVersion ${manifest.schemaVersion} exceeds max supported ($MAX_SUPPORTED_SCHEMA_VERSION). Update KuizKu.")
}
```

### 11.2 Conditional field reading

```kotlin
// In parseQuestionsJson() at line ~254
val schoolTrack: String? = if (schemaVersion >= 4) safeString("schoolTrack") else null
val curriculum: String? = if (schemaVersion >= 4) safeString("curriculum") else null
```

### 11.3 Subject parsing (schemaVersion-conditional)

```kotlin
val subjectSchoolTrack = if (schemaVersion >= 4) safeString("schoolTrack") ?: "SK" else "SK"
val subjectLanguage = if (schemaVersion >= 4) safeString("language") ?: "ms" else "ms"
val subjectCurriculum = if (schemaVersion >= 4) safeString("curriculum") ?: "KSSR" else "KSSR"
```

### 11.4 Backward-compat safe

V3 / V4-TEST (schemaVersion=3) → all new fields default. No change in runtime behavior.
V5+ (schemaVersion=4) → fields read from JSON if present.

---

## 12. Test Strategy

### 12.1 Migration test (MigrationsV2V3Test.kt)

```kotlin
@Test
fun migrationV2V3_preservesV3SubjectsAndAnswerRecords() {
    // 1. Create V2 schema with V3-like data
    // 2. Insert sample V3 subjects (prim_bm_Y5_peribahasa etc.)
    // 3. Insert V3 questions + AnswerRecords
    // 4. Run MIGRATION_2_3
    // 5. Verify:
    //    - subject.schoolTrack = "SK"
    //    - subject.subjectCode = "bm"
    //    - subject.gradeLevel = "Tahun5"
    //    - question.schoolTrack = "SK" (backfilled)
    //    - AnswerRecord rows count unchanged
    //    - Favorite rows count unchanged
    //    - QuizAttempt rows count unchanged
}
```

### 12.2 Schema tests

```kotlin
@Test fun schoolTrack_enumRoundTrip() { SK / SJKC / INTERNATIONAL ↔ String }

@Test fun parsedSubject_parseV5() { sk_prim_bm_Y5 → schoolTrack=SK }

@Test fun parsedSubject_parseLegacy() { prim_bm_Y5_peribahasa → schoolTrack=SK, topic="peribahasa" }

@Test fun parsedSubject_parseBootstrapReturnsNull() { bootstrap_gk → null }

@Test fun parsedSubject_parseRTBReturnsNull() { RTB_y5_topic → null (RTB disabled) }

@Test fun userSelection_legacyUserHasNullTrack() { old DataStore → schoolTrack=null }
```

### 12.3 Track + Language + Grade combinations (per 638 §十一)

```kotlin
@Test fun trackLanguageGrade_SK_Tahun1_ms() { schoolTrack=SK, grade=Tahun1, language=ms }

@Test fun trackLanguageGrade_SK_Tahun1_en() { schoolTrack=SK, grade=Tahun1, language=en }

@Test fun trackLanguageGrade_SJKC_Tahun1_zh() { schoolTrack=SJKC, grade=Tahun1, language=zh }

@Test fun trackLanguageGrade_SJKC_Tahun1_en() { schoolTrack=SJKC, grade=Tahun1, language=en }

@Test fun trackLanguageGrade_INTERNATIONAL_Year1_en() { schoolTrack=INTERNATIONAL, grade=Year1, language=en }

@Test fun trackLanguageGrade_INTERNATIONAL_Year1_ms() { schoolTrack=INTERNATIONAL, grade=Year1, language=ms }
```

### 12.4 Legacy compatibility tests

```kotlin
@Test fun legacy_V3_subjectsVisibleTo_SK_Tahun5() { /* V3 subjects in Room, user SK T5 → 27 subjects visible */ }

@Test fun legacy_V4TEST_subjectsVisibleTo_SK_Tahun5() { /* V4-TEST subjects in Room, user SK T5 → 12 subjects visible */ }

@Test fun legacy_BootstrapSubjectsHidden() { /* bootstrap_gk, bootstrap_eng NOT in Home */ }

@Test fun legacy_V3_subjectsHaveDefaultSchoolTrack_SK() { /* post-migration: subject.schoolTrack == "SK" */ }
```

### 12.5 UI integration tests

```kotlin
@Test fun homeScreen_legacyUserShowsTrackSelection() { /* track==null → "Please pick your school" */ }

@Test fun homeScreen_SKUserShowsSKSubjects() { /* track==SK → V3/V4-TEST subjects visible */ }

@Test fun homeScreen_SJKCUserShowsEmptySubjects() { /* track==SJKC → no SJKC bank yet, empty */ }
```

---

## 13. Rollback Strategy

### 13.1 No production data to roll back

Phase 10.3 only adds columns and code paths. No data is deleted. No bank files are modified. Rollback = revert code + Room schema. Existing V2 schema data still works.

### 13.2 If migration fails partway

Room handles partial migration failure by rolling back to previous version. App re-tries migration on next launch. After 2-3 retries, if still failing, Room can be cleared via `fallbackToDestructiveMigration` (NOT recommended) OR user reinstalls app (loses AnswerRecord/History — BAD).

**Mitigation**: The MIGRATION_2_3 is designed to be:
- Idempotent (re-runnable safely)
- Atomic per ALTER TABLE statement
- Tested via Robolectric before shipping

### 13.3 If new code path crashes

Additive design means old code paths still work. If schoolTrack-related code crashes (e.g., NPE in HomeViewModel filter), app falls back to:
- Show all subjects (no track filter) — degraded but functional
- User can manually pick track again from Change Level

### 13.4 If schema bump breaks production users

Migration safety tests in `MigrationsV2V3Test.kt` will validate:
- V2 → V3 migration succeeds on V2 data
- AnswerRecord rows preserved
- Favorite rows preserved
- QuizAttempt rows preserved

If test passes, production migration is safe. If test fails, do NOT ship.

---

## 14. Test Strategy Summary

| Test category | File | Purpose |
|---|---|---|
| Schema | MigrationsV2V3Test.kt | Room migration safety |
| Schema | SubjectGroupingMigrationTest.kt | Backward compat for legacy subjectIds |
| Track | SchoolTrackTest.kt | Enum round-trip |
| Track | ParsedSubjectTest.kt | V5 + legacy parsing |
| Language | (covered in ParsedSubjectTest) | Language is structural metadata |
| Combination | HomeViewModelTrackTest.kt | Filter by track + grade + language |
| Legacy | (covered in MigrationsV2V3Test) | V3/V4-TEST continue to sync + display |

---

## 15. What Will Remain Frozen

| Component | Reason |
|---|---|
| V1 bootstrap subjects (`eng_vocab`, `gen_know`) | Phase 0A legacy, Phase 9 hidden |
| V3 production bank `/v3/` (27 BM subjects, sha `854b41fe`) | Frozen |
| V4-TEST bank `/v4-test/` (12 BM subjects, sha `854b41fe`-equivalent) | Frozen |
| Phase 10.1 `tahun_1_pilot.json` (sha `72ca4e4586efd27270c38ecbc4d359b21f2c599272468a5097f672c06269c159`) | 638 §十二 |
| Reference DB `references\` | READ-ONLY |
| `:core:security` (EncryptionProvider, IntegrityVerifier, SignatureVerifier) | Per 638 §九 |
| BankSyncer Phase 8D.1 keyId allowlist | Per 638 §八 |
| KuizKuApp.kt Phase 8D.16 RTB disable | Frozen |
| Phase 9 UI (HomeScreen, LevelSelectionScreen) | Behavior preserved — additive only |
| Existing unit tests (116+ tests across all modules) | Should continue to pass |

---

## 16. Files Modified vs New — Summary

### Modified (12 files)

```
:domain/
  Subject.kt                 (+5 fields)
  Question.kt                (+2 nullable fields)
  SubjectGrouping.kt         (V5_REGEX added + legacy compat)
  UserLevel.kt               (+SchoolTrack enum + ParsedSubject + UserSelection wrapper)

:data/
  SubjectEntity.kt           (+5 NOT NULL columns)
  QuestionEntity.kt          (+2 NULLABLE columns)
  AppDatabase.kt             (version 2 → 3)
  Migrations.kt              (+MIGRATION_2_3)

:sync/
  BankSyncer.kt              (+MAX_SUPPORTED_SCHEMA_VERSION + conditional field reading)

:app/
  HomeViewModel.kt           (filter by schoolTrack + handle null)
  LevelSelectionViewModel.kt (include schoolTrack in state)
  HomeScreen.kt              (display schoolTrack + empty state)
```

### New (10 files)

```
:domain/  SchoolTrack.kt, ParsedSubject.kt, UserSelection.kt
:data/    DataBackfill.kt
:test/    SchoolTrackTest.kt, ParsedSubjectTest.kt,
          SubjectGroupingMigrationTest.kt, UserSelectionTest.kt,
          MigrationsV2V3Test.kt, HomeViewModelTrackTest.kt
```

### NOT Modified (frozen)

- `:core:security/*` (encryption)
- `:data/bootstrap/BootstrapBank.kt` (V1 frozen)
- `KuizKuApp.kt` (Phase 8D.16 frozen)
- Any bank JSON files (V3, V4-TEST, Phase 10.1 pilot)
- Reference DB
- All existing test files

---

## 17. Implementation Order (suggested execution sequence)

### Step 1: Domain (no Android dependency)
1. Create `SchoolTrack.kt` enum
2. Create `ParsedSubject.kt` data class
3. Create `UserSelection.kt` data class
4. Modify `Subject.kt` (add 5 fields)
5. Modify `Question.kt` (add 2 nullable fields)
6. Modify `UserLevel.kt` (add SchoolTrack import + UserSelection wrapper)
7. Modify `SubjectGrouping.kt` (V5_REGEX + legacy compat)
8. Run domain tests — verify no regression

### Step 2: Data (depends on Domain)
1. Modify `SubjectEntity.kt` (add 5 columns)
2. Modify `QuestionEntity.kt` (add 2 columns)
3. Modify `AppDatabase.kt` (version bump + migration register)
4. Modify `Migrations.kt` (add MIGRATION_2_3)
5. Create `DataBackfill.kt` (helper if needed)
6. Run data tests — verify migration safety

### Step 3: Sync (depends on Domain + Data)
1. Modify `BankSyncer.kt` (schemaVersion check + conditional field reading)
2. Run sync tests — verify V3/V4-TEST still work

### Step 4: App UI (depends on all above)
1. Modify `HomeViewModel.kt` (filter by track)
2. Modify `LevelSelectionViewModel.kt` (track selection state)
3. Modify `HomeScreen.kt` (display track)
4. Modify `KuizKuNavGraph.kt` (optional — add track parameter)
5. Run app tests — verify UI behavior

### Step 5: Verify all tests pass
1. `:domain:test` — SchoolTrack, ParsedSubject, SubjectGrouping, UserSelection, etc.
2. `:data:test` — MigrationsV2V3, AnswerRecord survival
3. `:sync:test` — BankSyncer V3 + V4-TEST continue
4. `:app:test` — HomeViewModel track filter
5. `:core:security:test` — unchanged, should still pass
6. Build `:app:assembleDebug` and `:app:testDebugUnitTest`

---

## 18. Required Authorization Before Execution

Per 638 §十三 "先报告 ... 然后 HARD STOP，等待 638 明确授权 commit":

This IMPLEMENTATION PLAN is READ-ONLY. No code modifications in Phase 10.3 have been made yet. **638 must explicitly authorize the plan before any code change begins.**

Once authorized, execution will:
1. Run Steps 1-5 above
2. Run full test suite
3. Report results (files changed, tests, migration result, legacy compatibility, git diff, working tree)
4. HARD STOP — wait for 638 explicit commit authorization
5. NO push

---

## 19. Scope Verification (638 §十二)

| Forbidden action | Will NOT do |
|---|---|
| ❌ Generate Tahun 2-6 questions | Confirmed — Phase 10.3 is schema prep only |
| ❌ Generate SJKC questions | Confirmed — schema can ACCEPT SJKC subjectIds later, no generation |
| ❌ Generate International questions | Confirmed — schema can ACCEPT International subjectIds later, no generation |
| ❌ Build V5 runtime | Confirmed — V5-SK-Primary build is Phase 10.5 scope |
| ❌ Publish GitHub Pages bank | Confirmed — Phase 10.5 scope |
| ❌ Modify V3 | Confirmed — only read BankSyncer behavior, no JSON modification |
| ❌ Modify V4-TEST | Confirmed — only read BankSyncer behavior, no JSON modification |
| ❌ Modify Reference DB | Confirmed — read-only |
| ❌ Upload Google Play | Confirmed — not in scope |
| ❌ Commit without authorization | Confirmed — HARD STOP after report |
| ❌ Push | Confirmed — never |

---

# 🛑 HARD STOPPED — 等待 638 授权执行 Phase 10.3 IMPLEMENTATION PLAN

**Phase 10.3 IMPLEMENTATION PLAN delivered.** READ-ONLY plan, no code
modifications. Includes:

- 12 files to modify (5 domain, 4 data, 1 sync, 3 app — all minimal)
- 10 new files (3 domain, 1 data, 6 tests)
- V3 / V4-TEST / Phase 10.1 / Reference DB / KuizKuApp.kt / Encryption all preserved
- Room migration v2 → v3 with 4-phase atomic safety
- BankSyncer schemaVersion ≤ 4 (V3/V4-TEST continue, V5 future-ready)
- UserLevel migration with safe fallback (old user must pick track, no auto-inference)

**638 must explicitly authorize before execution begins.**

🚢
