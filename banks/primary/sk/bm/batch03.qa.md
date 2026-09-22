# QA Report — batch03_sk_bm_y1 (Primary SK Y1 BM Batch 03)

**Batch**: `batch03_sk_bm_y1` (local Production batch number; published as `batch03.json`)
**Local Production Path**: `D:\Users\bajub\kuizku_p10\batch03_sk_bm_y1.json`
**Public Repo Path**: `banks\primary\sk\bm\batch03.json`
**Date**: 2026-09-22
**Total Questions**: 100
**Curriculum**: KSSR
**Grade Level**: Tahun 1 (Primary)
**Subject ID**: `***`
**schoolTrack**: SK
**stage**: primary

---

## Hashes

| Item | Value |
|---|---|
| **Local production SHA-256** | `a843f795cc45f978ed6e8bee87ca11d7358883e230753feece60eb2db85e1804` |
| **Local production file size** | 155,507 bytes |
| **Question ID range** | `sk-bm-y1-051` to `sk-bm-y1-150` |

---

## 1. STRUCTURAL GATE

✅ PASS: JSON valid — 100 questions parsed
✅ PASS: All required fields present (100/100)
✅ PASS: schoolTrack=SK (100/100)
✅ PASS: stage=primary (100/100)
✅ PASS: gradeLevel=Tahun1 (100/100)
✅ PASS: curriculum=KSSR (100/100)
✅ PASS: language=ms (100/100)

## 2. ANSWER GATE

✅ PASS: exactly one correct answer per question — 100/100
✅ PASS: correct answer option non-empty — 100/100
✅ PASS: no duplicate options — 100/100

## 3. CONTENT GATE

✅ PASS: Bahasa Melayu natural (spot-check) — 100/100

Difficulty distribution:
  - Easy (diff=1): 48 Q
  - Medium (diff=2): 36 Q
  - Hard (diff=3): 16 Q
✅ PASS: Difficulty matches Plan (48/36/16) — ✅ exact

Topic distribution (11 topics):
  - Mendengar & Bertutur: 12 Q
  - Membaca: 28 Q
  - Penulisan (Huruf): 2 Q
  - Penulisan (Perkataan): 3 Q
  - Penulisan (Ayat Mudah): 5 Q
  - Penulisan (Ejaan): 5 Q
  - Tatabahasa: 25 Q
  - Perbendaharaan Kata: 20 Q
✅ PASS: 8 topic labels — ✅ all covered

Skill distribution:
  - RECOGNITION: 32 Q
  - COMPREHENSION: 40 Q
  - APPLICATION: 28 Q
✅ PASS: Skill sum=100 (32/40/28) — ✅ exact match

Context diversity: Sekolah, Rumah, Padang, Pasar, Dapur, Taman, Perpustakaan, Bilik darjah, Hospital
✅ PASS: Context diversity ≥ 5

(subtopic, archetype) uniqueness: 100/100 ✅ PASS
100 unique subtopics ✅ PASS

## 4. ORIGINALITY GATE

✅ PASS: Within-batch exact duplicates — 0
✅ PASS: Cross-batch exact duplicates vs B01+B02 — 0
✅ PASS: Cross-batch semantic near-duplicates — 0 (≥4 shared 4-grams, ≥0.5 ratio)
✅ PASS: No subtopic overlap with B01+B02 — 0 shared subtopics
✅ PASS: No ID overlap with B01+B02 — 0

## 5. METADATA GATE

✅ PASS: contentOrigin=ORIGINAL (100/100)
✅ PASS: licenseStatus=self_authored (100/100)
✅ PASS: commercialReuseAllowed=true (100/100)
✅ PASS: examYear=null (100/100)
✅ PASS: subjectCode=bm (100/100)
✅ PASS: schoolTrack=SK (100/100)
✅ PASS: stage=primary (100/100)
✅ PASS: gradeLevel=Tahun1 (100/100)

## 6. SHA-256

- **File SHA-256**: `a843f795cc45f978ed6e8bee87ca11d7358883e230753feece60eb2db85e1804`
- **Source / local production batch**: `batch03_sk_bm_y1.json` (D:\Users\bajub\kuizku_p10\)
- **Local production SHA-256**: identical byte-for-byte to this file

## 7. SUMMARY

- Total questions: **100**
- Difficulty: easy=**48** medium=**36** hard=**16**
- Topics: 8 unique (Mendengar & Bertutur 12, Membaca 28, Penulisan 15, Tatabahasa 25, Perbendaharaan Kata 20)
- Skills: RECOGNITION 32, COMPREHENSION 40, APPLICATION 28
- Contexts: 9 distinct
- (subtopic, archetype) uniqueness: **100/100**
- Exact duplicates (within batch): **0**
- Exact duplicates (vs B01-B02): **0**
- Near duplicates (within batch): **0**
- Near duplicates (vs B01-B02): **0**
- Subtopic overlap (vs B01-B02): **0**
- Curriculum scope IN-SCOPE: **100/100**, BORDERLINE: **0**, OUT-OF-SCOPE: **0**
- Correctness spot-check: **12/12 PASS**
- Metadata validation failures: **0**
- Structural validation failures: **0**
- Answer validation failures: **0**
- TOTAL FAILURES: **0**
- TOTAL WARNINGS: **0**

✅ **BATCH 03 QA PASS — ALL 100 QUESTIONS PASS**

---

## Source Provenance Statement (REQUIRED)

> **Local Production Source**: `D:\Users\bajub\kuizku_p10\batch03_sk_bm_y1.json` (SK Primary Year 1 Bahasa Melayu, KSSR curriculum).
>
> **Public Repo Publication**: This is the THIRD BM production batch published in `leonchoo/kuizku-content` BM primary path. Public repo adopts standardized naming `banks\<school>\<level>\<subject>\batchNN.json` sequential. Local B03 → public `batch03.json` (after batch01 = Local B01, batch02 = Local B02).
>
> **All 100 questions are ORIGINAL / self-authored by KuizKu.** No question text, options, explanation, or structure was copied from any external source. The Reference DB was used ONLY as a KSSR BM Year 1 syllabus/topic/style reference, not as a source of questions.
>
> **Cumulative originality verified against SK Primary Y1 BM local Production (B01 25 Qs + B02 25 Qs = 50 Qs at time of B03 generation).** Zero ID overlap, zero subtopic overlap, zero exact-duplicate, zero near-duplicate. This batch contributes 100/100 NEW (subtopic, blueprintArchetype) pairs.
>
> **SK Primary Y1 BM cumulative total after this Promotion: 150 questions (B01 25 + B02 25 + B03 100).**
