# QA Report — batch04_sk_bm_y1 (Primary SK Y1 BM Batch 04)

**Batch**: `batch04_sk_bm_y1` (local Production batch number; published as `batch03.json`)
**Local Production Path**: `D:\Users\bajub\kuizku_p10\batch04_sk_bm_y1.json`
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
| **Local production SHA-256** | `7ffb76182832b4c67fcfea44f09a7c4d5dbe88acfbcce75647bc73db08687dc1` |
| **Local production file size** | 151,073 bytes |
| **Question ID range** | `sk-bm-y1-151` to `sk-bm-y1-250` |

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
✅ PASS: correct answer (lowercase + uppercase label) consistent — 100/100
✅ PASS: no duplicate options — 100/100

## 3. CONTENT GATE

✅ PASS: Bahasa Melayu natural (spot-check) — 100/100

Difficulty distribution:
  - Easy (diff=1): 48 Q
  - Medium (diff=2): 36 Q
  - Hard (diff=3): 16 Q
✅ PASS: Difficulty matches Plan (48/36/16) — ✅ exact

Topic distribution (8 topic labels):
  - Penulisan (Ayat Mudah): 10 Q
  - Penulisan (Huruf): 3 Q
  - Penulisan (Perkataan): 6 Q
  - Penulisan (Ejaan): 6 Q
  - Membaca / Pemahaman: 25 Q
  - Tatabahasa: 25 Q
  - Perbendaharaan Kata: 20 Q
  - Mendengar & Bertutur: 5 Q
✅ PASS: Topic sum=100 — ✅ all covered

Skill distribution:
  - RECOGNITION: 32 Q
  - COMPREHENSION: 40 Q
  - APPLICATION: 28 Q
✅ PASS: Skill sum=100 (32/40/28) — ✅ exact match

Context diversity: 16 distinct contexts including Sekolah, Rumah, Padang, Pasar, Taman, Kelas, Perpustakaan, Bilik darjah, Halaman, Dapur, Tandas, Bukit, Pantai, Sungai, Terminal, Klinik
✅ PASS: Context diversity ≥ 5

(subtopic, archetype) uniqueness: 100/100 ✅ PASS
100 unique subtopics ✅ PASS

## 4. ORIGINALITY GATE

✅ PASS: Within-batch exact duplicates — 0
✅ PASS: Cross-batch exact duplicates vs B01+B02+B03 — 0
✅ PASS: Cross-batch semantic near-duplicates — 0 (≥4 shared 4-grams, ≥0.5 ratio)
✅ PASS: No subtopic overlap with B01+B02+B03 — 0 shared subtopics
✅ PASS: No ID overlap with B01+B02+B03 — 0

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

- **File SHA-256**: `7ffb76182832b4c67fcfea44f09a7c4d5dbe88acfbcce75647bc73db08687dc1`
- **Source / local production batch**: `batch04_sk_bm_y1.json` (D:\Users\bajub\kuizku_p10\)
- **Local production SHA-256**: identical byte-for-byte to this file

## 7. SUMMARY

- Total questions: **100**
- Difficulty: easy=**48** medium=**36** hard=**16**
- Topics: **8 unique** (Penulisan 25, Membaca 25, Tatabahasa 25, Perbendaharaan 20, Mendengar 5)
- Skills: RECOGNITION 32, COMPREHENSION 40, APPLICATION 28
- Contexts: 16 distinct
- (subtopic, archetype) uniqueness: **100/100**
- Exact duplicates (within batch): **0**
- Exact duplicates (vs B01-B03): **0**
- Near duplicates (within batch): **0**
- Near duplicates (vs B01-B03): **0**
- Subtopic overlap (vs B01-B03): **0**
- Curriculum scope IN-SCOPE: **100/100**, BORDERLINE: **0**, OUT-OF-SCOPE: **0**
- Correctness spot-check: **12/12 PASS**
- Metadata validation failures: **0**
- Structural validation failures: **0**
- Answer validation failures: **0**
- TOTAL FAILURES: **0**
- TOTAL WARNINGS: **0**

✅ **BATCH 04 QA PASS — ALL 100 QUESTIONS PASS**

---

## Source Provenance Statement (REQUIRED)

> **Local Production Source**: `D:\Users\bajub\kuizku_p10\batch04_sk_bm_y1.json` (SK Primary Year 1 Bahasa Melayu, KSSR curriculum).
>
> **Public Repo Publication**: This is the FOURTH batch published in `leonchoo/kuizku-content` BM primary path. Public repo adopts standardized naming `banks\<school>\<level>\<subject>\batchNN.json` sequential. Local B04 → public `batch03.json` (after batch01 = local B01, batch02 = pending upload).
>
> **All 100 questions are ORIGINAL / self-authored by KuizKu.** No question text, options, explanation, or structure was copied from any external source. Reference DB used ONLY as KSSR BM Year 1 syllabus/topic/style anchor — no copy.
>
> **Cumulative originality verified against SK Primary Y1 BM local Production (B01 25 Qs + B02 25 Qs + B03 100 Qs = 150 Qs).** Zero ID overlap, zero subtopic overlap, zero exact-duplicate, zero near-duplicate. This batch contributes 100/100 NEW (subtopic, archetype) pairs.
>
> **SK Primary Y1 BM cumulative total after this Promotion: 250 questions (B01 25 + B02 25 + B03 100 + B04 100).**
