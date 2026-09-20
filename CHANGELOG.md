# Changelog

All notable changes to this repository are documented here.

## [Unreleased] — 2026-09-21

### Initial commit
- **3 finalized production banks**:
  - `banks/primary/sk/bm/batch01.json` — SK Primary Year 1 Bahasa Melayu (25 questions)
  - `banks/primary/sk/english/batch01.rev3.json` — SK Primary Year 1 English Rev3 (25 questions)
  - `banks/secondary/sk/bm/t1/batch01.json` — SK Secondary T1 Bahasa Melayu (25 questions)
  - `banks/secondary/sk/bm/t1/batch02.json` — SK Secondary T1 Bahasa Melayu Batch 02 (25 questions)

- **Companion QA markdown files** for each bank:
  - `banks/primary/sk/bm/batch01.qa.md`
  - `banks/secondary/sk/bm/t1/batch01.qa.md`
  - `banks/secondary/sk/bm/t1/batch02.qa.md`

- **Blueprints**:
  - `blueprints/primary/sk/english/y1.blueprint.md` — SK Primary Y1 English Blueprint
  - `blueprints/secondary/sk/bm/t1.batch01.blueprint.md` — T1 BM Blueprint v1
  - `blueprints/secondary/sk/bm/t1.batch02.blueprint.md` — T1 BM Blueprint v2
  - `blueprints/secondary/sk/bm/t1.scope_review.md` — T1 BM Scope Review

- **Coverage matrix and selection reports**:
  - `coverage/COVERAGE_MATRIX.md`
  - `coverage/reports/primary_sk_en_y1_selection.md`

- **Phase 10 implementation docs**:
  - `docs/phase10_blueprint.json` — Master blueprint for Phase 10 content
  - `docs/phase10_2_preflight_report.md` — Preflight report
  - `docs/phase10_3_implementation_plan.md` — Implementation plan
  - `docs/phase10_4_blueprint.md` — Phase 10.4 blueprint
  - `docs/phase10_5r_b_preflight_report.md` — Phase 10.5b preflight report

- **Forensic source**:
  - `forensic/primary_sk_en_y1.json` — LOCKED audit source for Y1 English

- **Legacy content**:
  - `legacy/tahun_1_pilot.json` — Phase 10.1 pilot (not for production use)

- **Tools** (Python generators + QA + utils):
  - `tools/generators/gen_batch_secondary_01.py`
  - `tools/generators/gen_batch_secondary_02.py`
  - `tools/generators/gen_primary_sk_en_y1.py`
  - `tools/generators/generate_batch01_legacy.py`
  - `tools/generators/generate_tahun_1_legacy.py`
  - `tools/generators/generate_tahun_1_data_legacy.py`
  - `tools/qa/qa_batch_secondary_01.py`
  - `tools/qa/qa_batch_secondary_02.py`
  - `tools/qa/qa_primary_sk_en_y1.py`
  - `tools/qa/qa_primary_sk_en_y1_rev3.py`
  - `tools/utils/apply_audit_fixes.py`
  - `tools/tests/part_f_test.py`

- **Apps Script backend**:
  - `apps-script/backend_v6.gs` — Production version
  - `apps-script/.clasp.json` — clasp configuration

- **Repository scaffolding**:
  - `README.md` — Repository overview
  - `LICENSE` — CC BY 4.0
  - `.gitignore` — Excludes secrets, credentials, local paths, Reference DB, runtime artifacts
  - 7 placeholder READMEs for empty track directories (SJKC/International Primary/Secondary, etc.)

### Privacy guarantees
- ✅ No encryption keys (decryption secrets for runtime banks)
- ✅ No API keys or OAuth tokens
- ✅ No personal email addresses
- ✅ No local filesystem paths
- ✅ No Reference DB content (only generic provenance metadata)
- ✅ No published runtime encrypted artifacts (live in a separate artifact store)
