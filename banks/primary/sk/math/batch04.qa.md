# QA Report — batch_secondary_08_sk_math_y1 (Primary SK Y1 Math Batch 08)

**Batch**: `batch_secondary_08_sk_math_y1` (local Production batch number; published as `batch04.json`)
**Local Production Path**: `D:\Users\bajub\kuizku_p10\primary\batch08_sk_math_y1.json`
**Public Repo Path**: `banks\primary\sk\math\batch04.json`
**Date**: 2026-09-22
**Total Questions**: 100
**Curriculum**: KSSR
**Grade Level**: Tahun 1 (Primary)
**Subject ID**: `sk_pri...s_Y1`
**schoolTrack**: SK
**stage**: primary

---

## Hashes

| Item | Value |
|---|---|
| **Local production SHA-256** | `a81a9fba63190f21e7a4c094f88d3dc442614dd6b8529d125bd88574e54b3f54` |
| **Local production file size** | 108,593 bytes |
| **Question ID range** | `v5-sk-math-y1-401` to `v5-sk-math-y1-500` |

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
  - Nombor Bulat: 14 Q
  - Tambah & Tolak: 16 Q
  - Wang: 10 Q
  - Masa & Waktu: 8 Q
  - Bentuk 3D & 2D: 12 Q
  - Panjang: 8 Q
  - Pecahan: 8 Q
  - Berat: 5 Q
  - Isipadu: 5 Q
  - Pola & Jujukan: 7 Q
  - Data: 7 Q
✅ PASS: 11 topics — ✅ all covered

Skill distribution:
  - RECOGNITION: 32 Q
  - COMPREHENSION: 40 Q
  - APPLICATION: 28 Q
✅ PASS: Skill sum=100 (32/40/28) — ✅ exact match

Context diversity: Sekolah, Rumah, Pasar, Dapur, Taman, Padang, Perpustakaan, Bilik darjah
✅ PASS: Context diversity ≥ 5

(subtopic, archetype) uniqueness: 100/100 ✅ PASS
100 unique subtopics ✅ PASS

## 4. ORIGINALITY GATE

✅ PASS: Within-batch exact duplicates — 0
✅ PASS: Cross-batch exact duplicates vs B02-B03-B04-B05-B06-B07 — 0
✅ PASS: Cross-batch semantic near-duplicates — 0
✅ PASS: No subtopic overlap with B02-B07 — 0 shared subtopics
✅ PASS: No ID overlap with B02-B07 — 0

## 5. METADATA GATE

✅ PASS: contentOrigin=ORIGINAL (100/100)
✅ PASS: licenseStatus=self_authored (100/100)
✅ PASS: commercialReuseAllowed=true (100/100)
✅ PASS: examYear=null (100/100)
✅ PASS: subjectCode=math (100/100)
✅ PASS: schoolTrack=SK (100/100)
✅ PASS: stage=primary (100/100)
✅ PASS: gradeLevel=Tahun1 (100/100)

## 6. SHA-256

- **File SHA-256**: `a81a9fba63190f21e7a4c094f88d3dc442614dd6b8529d125bd88574e54b3f54`
- **Source / local production batch**: `batch08_sk_math_y1.json` (D:\Users\bajub\kuizku_p10\primary\)
- **Local production SHA-256**: identical byte-for-byte to this file

## 7. SUMMARY

- Total questions: **100**
- Difficulty: easy=**48** medium=**36** hard=**16**
- Topics: **11 unique** (Nombor Bulat 14, Tambah & Tolak 16, Wang 10, Masa & Waktu 8, Bentuk 3D & 2D 12, Panjang 8, Pecahan 8, Berat 5, Isipadu 5, Pola & Jujukan 7, Data 7)
- Skills: RECOGNITION 32, COMPREHENSION 40, APPLICATION 28
- Contexts: 8 distinct
- (subtopic, archetype) uniqueness: **100/100**
- Exact duplicates (within batch): **0**
- Exact duplicates (vs B02-B07): **0**
- Near duplicates (within batch): **0**
- Near duplicates (vs B02-B07): **0**
- Subtopic overlap (vs B02-B07): **0**
- Curriculum scope IN-SCOPE: **100/100**, BORDERLINE: **0**, OUT-OF-SCOPE: **0**
- Correctness spot-check: **12/12 PASS**
- Metadata validation failures: **0**
- Structural validation failures: **0**
- Answer validation failures: **0**
- TOTAL FAILURES: **0**
- TOTAL WARNINGS: **0**

✅ **BATCH 08 QA PASS — ALL 100 QUESTIONS PASS**

---

## Source Provenance Statement (REQUIRED)

> **Local Production Source**: `D:\Users\bajub\kuizku_p10\primary\batch08_sk_math_y1.json` (SK Primary Year 1 Mathematics, KSSR curriculum).
>
> **Public Repo Publication**: This is the fourth Math batch published in `leonchoo/kuizku-content` (after `batch01.json` = local B05, `batch02.json` = local B06, `batch03.json` = local B07). The public repo adopts the standardized naming convention `banks\<school>\<level>\<subject>\batchNN.json` (sequential numbering), so this fourth batch is published as `batch04.json`.
>
> **All 100 questions are ORIGINAL / self-authored by KuizKu.** No question text, options, explanation, or structure was copied from any external source. The Reference DB was used ONLY as a KSSR Year 1 Mathematics syllabus/topic/style reference, not as a source of questions.
>
> **Cumulative originality verified against SK Primary Y1 Math local Production (B02 20 Qs + B03 25 Qs + B04 25 Qs + B05 100 Qs + B06 100 Qs + B07 100 Qs = 370 Qs total).** Zero ID overlap, zero subtopic overlap, zero exact-duplicate, zero near-duplicate. This batch contributes 100/100 NEW (subtopic, blueprintArchetype) pairs.
>
> **SK Primary Y1 Math cumulative total after this Promotion: 470 questions (B02 20 + B03 25 + B04 25 + B05 100 + B06 100 + B07 100 + B08 100).**
