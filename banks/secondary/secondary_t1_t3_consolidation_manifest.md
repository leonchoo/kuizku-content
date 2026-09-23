# Secondary SK T1–T3 Consolidation Manifest

**Mode:** READ-ONLY content preservation. No question regenerated, no answer changed.
**Source of Truth:** `D:\Users\bajub\kuizku_p10\` (production QA-confirmed JSON)
**Date:** 2026-09-23

---

## A. Canonical Source Inventory

| Year | Subject | Source Batches | Count | Target | Status |
|---|---|---|---|---|---|
| T1 | Bahasa Melayu | b01,b02,b03,b04,b05,b06,b07 | 550 | 550 | ✅ |
| T1 | English | b01,b02,b03,b04,b05,b06 | 500 | 500 | ✅ |
| T1 | Mathematics | b01,b02,b03,b04,b05 | 500 | 500 | ✅ |
| T1 | Science | b01,b02,b03,b04,b05 | 500 | 500 | ✅ |
| T2 | Bahasa Melayu | b01,b02,b03,b04,b05 | 500 | 500 | ✅ |
| T2 | English | b01,b02,b03,b04,b05 | 500 | 500 | ✅ |
| T2 | Mathematics | b01,b02,b03,b04,b05 | 500 | 500 | ✅ |
| T2 | Science | b01,b02,b03,b04,b05 | 500 | 500 | ✅ |
| T3 | Bahasa Melayu | b01,b02,b03,b04,b05 | 500 | 500 | ✅ |
| T3 | English | b01,b02,b03,b04,b05 | 500 | 500 | ✅ |
| T3 | Mathematics | b01,b02,b03,b04,b05 | 500 | 500 | ✅ |
| T3 | Science | b01,b02,b03,b04,b05 | 500 | 500 | ✅ |

---

## B. Consolidated Files (kuizku_p10 staging)

| Year | Subject | File | Count | Bytes | SHA-256 |
|---|---|---|---|---|---|
| T1 | Bahasa Melayu | `secondary_t1_sk_bm_consolidated.json` | 550 | 820,207 | `6cf559bbde686349...` |
| T1 | English | `secondary_t1_sk_en_consolidated.json` | 500 | 543,836 | `9608275ef98ee4ce...` |
| T1 | Mathematics | `secondary_t1_sk_math_consolidated.json` | 500 | 658,063 | `fba896d7ce901f00...` |
| T1 | Science | `secondary_t1_sk_science_consolidated.json` | 500 | 544,142 | `4045f5a80cf97d0d...` |
| T2 | Bahasa Melayu | `secondary_t2_sk_bm_consolidated.json` | 500 | 542,019 | `54e32f4fa700f320...` |
| T2 | English | `secondary_t2_sk_en_consolidated.json` | 500 | 486,036 | `043b7291884311df...` |
| T2 | Mathematics | `secondary_t2_sk_math_consolidated.json` | 500 | 492,345 | `1ff656951826e7c6...` |
| T2 | Science | `secondary_t2_sk_science_consolidated.json` | 500 | 522,139 | `be0cf7a9ed7e1951...` |
| T3 | Bahasa Melayu | `secondary_t3_sk_bm_consolidated.json` | 500 | 530,189 | `a31c3eb0ed42b0ce...` |
| T3 | English | `secondary_t3_sk_en_consolidated.json` | 500 | 512,832 | `f540c8339f9b29e1...` |
| T3 | Mathematics | `secondary_t3_sk_math_consolidated.json` | 500 | 498,632 | `d2d9fb187c34fff1...` |
| T3 | Science | `secondary_t3_sk_science_consolidated.json` | 500 | 537,092 | `e8c915ff925443bd...` |

---

## C. Final Totals

| Track | T1 | T2 | T3 | Total |
|---|---|---|---|---|
| BM | 550 | 500 | 500 | 1550 |
| English | 500 | 500 | 500 | 1500 |
| Mathematics | 500 | 500 | 500 | 1500 |
| Science | 500 | 500 | 500 | 1500 |
| **TOTAL** | **2050** | **2000** | **2000** | **6050** |

---

## D. Excluded Files

- `batch_secondary_03_sk_math_t2_REJECTED.json` (rejected - excluded)
- `batch_secondary_04_sk_en_t2.json.backup.*` (backup - excluded)
- All T4 Science WIP files (consolidation is T1-T3 only)
- All Primary Y4 Science files (consolidation is T1-T3 only)
- All Primary Y1/Y2/Y3 files (not in scope)

---

## E. Preserved Question ID Conventions

- T1 BM: v5-t1-bm-sec-001..025 + v5-t1-bm-sec2-001..025 + sk-***-001..500

- T1 English: v5-t1-en-sec-001..050 + sk-***-001..450

- T1 Math: sk-***-001..500 (per batch)

- T1 Science: sk-***-001..500 (per batch)

- T2 BM/English/Math/Science: original batch IDs preserved per batch

- T3 BM/English/Math/Science: original batch IDs preserved per batch

T3 English Q098 (poem/figurative language) is intentionally preserved as BORDERLINE per user directive.

---

## F. Safety Verification

- ✅ T4 Science WIP preserved (NOT touched, NOT committed)
- ✅ Primary Y4 untouched
- ✅ Reference DB untouched
- ✅ Android repo untouched
- ✅ Other agent files untouched
- ✅ Original batch files preserved in public (NOT deleted)
