# QA Report — batch07_sk_bm_y1 (Primary SK Y1 BM Batch 07 FINAL)

**Batch**: `batch07_sk_bm_y1` (local Production batch number; published as `batch07.json`)
**Local Production Path**: `D:\Users\bajub\kuizku_p10\batch07_sk_bm_y1.json`
**Public Repo Path**: `banks\primary\sk\bm\batch07.json`
**Date**: 2026-09-22
**Total Questions**: 50
**Curriculum**: KSSR
**Grade Level**: Tahun 1 (Primary)
**Subject ID**: `***`
**schoolTrack**: SK
**stage**: primary

---

## Hashes

| Item | Value |
|---|---|
| **Local production SHA-256** | `56213edd9e6513b95bfe783142d609e5c2d2f9082344c830af9f35b838c8d20d` |
| **Local production file size** | 75,998 bytes |
| **Question ID range** | `sk-bm-y1-451` to `sk-bm-y1-500` |

---

## 1. STRUCTURAL GATE

✅ PASS: JSON valid — 50 questions parsed
✅ PASS: All required fields present (50/50)
✅ PASS: schoolTrack=SK (50/50)
✅ PASS: stage=primary (50/50)
✅ PASS: gradeLevel=Tahun1 (50/50)
✅ PASS: curriculum=KSSR (50/50)
✅ PASS: language=ms (50/50)

## 2. ANSWER GATE

✅ PASS: exactly one correct answer per question — 50/50
✅ PASS: correct answer option non-empty — 50/50
✅ PASS: no duplicate options — 50/50

## 3. CONTENT GATE

✅ PASS: Bahasa Melayu natural (spot-check) — 50/50

Difficulty distribution (target 48/36/16 × 50 = 24/18/8):
  - Easy (diff=1): 24 Q
  - Medium (diff=2): 18 Q
  - Hard (diff=3): 8 Q
✅ PASS: Difficulty matches Plan — ✅ exact

Topic distribution (8 topic labels):
  - Penulisan (Huruf): 3 Q
  - Penulisan (Perkataan): 2 Q
  - Penulisan (Ejaan): 3 Q
  - Penulisan (Ayat Mudah): 6 Q
  - Membaca: 15 Q
  - Tatabahasa: 10 Q
  - Perbendaharaan Kata: 5 Q
  - Mendengar & Bertutur: 6 Q
✅ PASS: 8 topic labels — ✅ all covered

Skill distribution (target 32/40/28 × 50 = 16/20/14):
  - RECOGNITION: 16 Q
  - COMPREHENSION: 20 Q
  - APPLICATION: 14 Q
✅ PASS: Skill sum=50 (16/20/14) — ✅ exact match

Context diversity: 7+ distinct (Sekolah, Rumah, Padang, Pasar, Taman, Kelas, Bilik darjah, Halaman, Dapur, etc.)
✅ PASS: Context diversity ≥ 5

(subtopic, archetype) uniqueness: 50/50 ✅ PASS
50 unique subtopics ✅ PASS

## 4. ORIGINALITY GATE

✅ PASS: Within-batch exact duplicates — 0
✅ PASS: Cross-batch exact duplicates vs B01+B02+B03+B04+B05+B06 — 0
✅ PASS: Cross-batch semantic near-duplicates — 0 (≥4 shared 4-grams, ≥0.5 ratio)
✅ PASS: No subtopic overlap with B01-B06 — 0 shared subtopics
✅ PASS: No ID overlap with B01-B06 — 0

## 5. METADATA GATE

✅ PASS: contentOrigin=ORIGINAL (50/50)
✅ PASS: licenseStatus=self_authored (50/50)
✅ PASS: commercialReuseAllowed=true (50/50)
✅ PASS: examYear=null (50/50)
✅ PASS: subjectCode=bm (50/50)
✅ PASS: schoolTrack=SK (50/50)
✅ PASS: stage=primary (50/50)
✅ PASS: gradeLevel=Tahun1 (50/50)

## 6. SHA-256

- **File SHA-256**: `56213edd9e6513b95bfe783142d609e5c2d2f9082344c830af9f35b838c8d20d`
- **Source / local production batch**: `batch07_sk_bm_y1.json` (D:\Users\bajub\kuizku_p10\)
- **Local production SHA-256**: identical byte-for-byte to this file

## 7. SUMMARY

- Total questions: **50**
- Difficulty: easy=**24** medium=**18** hard=**8**
- Topics: 8 unique
- Skills: RECOGNITION 16, COMPREHENSION 20, APPLICATION 14
- Contexts: 7+ distinct
- (subtopic, archetype) uniqueness: **50/50**
- Exact duplicates (within batch): **0**
- Exact duplicates (vs B01-B06): **0**
- Near duplicates (within batch): **0**
- Near duplicates (vs B01-B06): **0**
- Subtopic overlap (vs B01-B06): **0**
- Curriculum scope IN-SCOPE: **50/50**, BORDERLINE: **0**, OUT-OF-SCOPE: **0**
- Correctness spot-check: **12/12 PASS**
- Metadata validation failures: **0**
- Structural validation failures: **0**
- Answer validation failures: **0**
- TOTAL FAILURES: **0**
- TOTAL WARNINGS: **0**

✅ **BATCH 07 QA PASS — ALL 50 QUESTIONS PASS**

---

## Source Provenance Statement (REQUIRED)

> **Local Production Source**: `D:\Users\bajub\kuizku_p10\batch07_sk_bm_y1.json` (SK Primary Year 1 Bahasa Melayu, KSSR curriculum).
>
> **Public Repo Publication**: This is the SEVENTH and FINAL batch published in `leonchoo/kuizku-content` BM primary path. Public repo adopts standardized naming `banks\<school>\<level>\<subject>\batchNN.json` sequential. Local B07 → public `batch07.json` (after batch01..batch06).
>
> **All 50 questions are ORIGINAL / self-authored by KuizKu.** No question text, options, explanation, or structure was copied from any external source. The Reference DB was used ONLY as a KSSR BM Year 1 syllabus/topic/style reference, not as a source of questions.
>
> **Cumulative originality verified against SK Primary Y1 BM local Production (B01 25 Qs + B02 25 Qs + B03 100 Qs + B04 100 Qs + B05 100 Qs + B06 100 Qs = 450 Qs).** Zero ID overlap, zero subtopic overlap, zero exact-duplicate, zero near-duplicate. This batch contributes 50/50 NEW (subtopic, blueprintArchetype) pairs.
>
> **🎉 SK Primary Y1 Bahasa Melayu cumulative total after this Promotion: 500 questions (B01 25 + B02 25 + B03 100 + B04 100 + B05 100 + B06 100 + B07 50) — FINAL COMPLETION 🎉**
