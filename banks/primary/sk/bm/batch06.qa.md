# QA Report — batch06_sk_bm_y1 (Primary SK Y1 BM Batch 06)

**Batch**: `batch06_sk_bm_y1` (local Production batch number; published as `batch06.json`)
**Local Production Path**: `D:\Users\bajub\kuizku_p10\batch06_sk_bm_y1.json`
**Public Repo Path**: `banks\primary\sk\bm\batch06.json`
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
| **Local production SHA-256** | `0228722ddf6c29bd854bb8558abd6a35b48f6536e3c559d2ad1b69518786bcc6` |
| **Local production file size** | 149,870 bytes |
| **Question ID range** | `sk-bm-y1-351` to `sk-bm-y1-450` |

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

Topic distribution (8 topic labels):
  - Penulisan (Huruf): 4 Q
  - Penulisan (Perkataan): 3 Q
  - Penulisan (Ejaan): 2 Q
  - Penulisan (Ayat Mudah): 12 Q
  - Membaca: 31 Q
  - Tatabahasa: 22 Q
  - Perbendaharaan Kata: 16 Q
  - Mendengar & Bertutur: 10 Q
✅ PASS: 8 topic labels — ✅ all covered

Skill distribution:
  - RECOGNITION: 32 Q
  - COMPREHENSION: 40 Q
  - APPLICATION: 28 Q
✅ PASS: Skill sum=100 (32/40/28) — ✅ exact match

Context diversity: Sekolah, Rumah, Padang, Pasar, Taman, Kelas, Bilik darjah, Halaman, Dapur, Bengkel, Klinik, Ladang, Zoo, Galeri, Lapangan Terbang, Tasik (16 distinct contexts)
✅ PASS: Context diversity ≥ 5

(subtopic, archetype) uniqueness: 100/100 ✅ PASS
100 unique subtopics ✅ PASS

## 4. ORIGINALITY GATE

✅ PASS: Within-batch exact duplicates — 0
✅ PASS: Cross-batch exact duplicates vs B01+B02+B03+B04+B05 — 0
✅ PASS: Cross-batch semantic near-duplicates — 0 (≥4 shared 4-grams, ≥0.5 ratio)
✅ PASS: No subtopic overlap with B01-B05 — 0 shared subtopics
✅ PASS: No ID overlap with B01-B05 — 0

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

- **File SHA-256**: `0228722ddf6c29bd854bb8558abd6a35b48f6536e3c559d2ad1b69518786bcc6`
- **Source / local production batch**: `batch06_sk_bm_y1.json` (D:\Users\bajub\kuizku_p10\)
- **Local production SHA-256**: identical byte-for-byte to this file

## 7. SUMMARY

- Total questions: **100**
- Difficulty: easy=**48** medium=**36** hard=**16**
- Topics: 8 unique
- Skills: RECOGNITION 32, COMPREHENSION 40, APPLICATION 28
- Contexts: 16 distinct
- (subtopic, archetype) uniqueness: **100/100**
- Exact duplicates (within batch): **0**
- Exact duplicates (vs B01-B05): **0**
- Near duplicates (within batch): **0**
- Near duplicates (vs B01-B05): **0**
- Subtopic overlap (vs B01-B05): **0**
- Curriculum scope IN-SCOPE: **100/100**, BORDERLINE: **0**, OUT-OF-SCOPE: **0**
- Correctness spot-check: **12/12 PASS**
- Metadata validation failures: **0**
- Structural validation failures: **0**
- Answer validation failures: **0**
- TOTAL FAILURES: **0**
- TOTAL WARNINGS: **0**

✅ **BATCH 06 QA PASS — ALL 100 QUESTIONS PASS**

---

## Source Provenance Statement (REQUIRED)

> **Local Production Source**: `D:\Users\bajub\kuizku_p10\batch06_sk_bm_y1.json` (SK Primary Year 1 Bahasa Melayu, KSSR curriculum).
>
> **Public Repo Publication**: This is the SIXTH batch published in `leonchoo/kuizku-content` BM primary path. Public repo adopts standardized naming `banks\<school>\<level>\<subject>\batchNN.json` sequential. Local B06 → public `batch06.json` (after batch01..batch05).
>
> **All 100 questions are ORIGINAL / self-authored by KuizKu.** No question text, options, explanation, or structure was copied from any external source. The Reference DB was used ONLY as a KSSR BM Year 1 syllabus/topic/style reference, not as a source of questions.
>
> **Cumulative originality verified against SK Primary Y1 BM local Production (B01 25 Qs + B02 25 Qs + B03 100 Qs + B04 100 Qs + B05 100 Qs = 350 Qs).** Zero ID overlap, zero subtopic overlap, zero exact-duplicate, zero near-duplicate. This batch contributes 100/100 NEW (subtopic, blueprintArchetype) pairs.
>
> **SK Primary Y1 BM cumulative total after this Promotion: 450 questions (B01 25 + B02 25 + B03 100 + B04 100 + B05 100 + B06 100).**
