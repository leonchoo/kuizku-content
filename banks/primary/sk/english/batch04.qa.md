# QA Report — batch04_sk_en_y1 (Primary SK Y1 English Batch 04)

**Batch**: `batch04_sk_en_y1` (local Production batch number; published as `batch04.json`)
**Local Production Path**: `D:\Users\bajub\kuizku_p10\primary\batch04_sk_en_y1.json`
**Public Repo Path**: `banks\primary\sk\english\batch04.json`
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
| **Local production SHA-256** | `8ec9c579fe8cf54a2f4d01a4a3bbbf1fc2b00fbcfe227afe3ae9c13fb594786a` |
| **Local production file size** | 152,651 bytes |
| **Question ID range** | `sk-en-y1-151` to `sk-en-y1-250` |

---

## 1. STRUCTURAL GATE

✅ PASS: JSON valid — 100 questions parsed
✅ PASS: All required fields present (100/100)
✅ PASS: schoolTrack=SK (100/100)
✅ PASS: stage=primary (100/100)
✅ PASS: gradeLevel=Tahun1 (100/100)
✅ PASS: curriculum=KSSR (100/100)
✅ PASS: language=en (100/100)

## 2. ANSWER GATE

✅ PASS: exactly one correct answer per question — 100/100
✅ PASS: correct answer option non-empty — 100/100
✅ PASS: no duplicate options — 100/100

## 3. CONTENT GATE

✅ PASS: English natural (spot-check) — 100/100

Difficulty distribution (target 50/40/10):
  - Easy (diff=1): 50 Q
  - Medium (diff=2): 40 Q
  - Hard (diff=3): 10 Q
✅ PASS: Difficulty matches Plan — ✅ exact

Topic distribution (5 topic labels):
  - Listening & Speaking: 20 Q
  - Reading: 25 Q
  - Vocabulary: 25 Q
  - Writing: 15 Q
  - Grammar: 15 Q
✅ PASS: 5 topic labels — ✅ all covered

Skill distribution (target 52/20/28):
  - RECOGNITION: 52 Q
  - COMPREHENSION: 20 Q
  - APPLICATION: 28 Q
✅ PASS: Skill sum=100 (52/20/28) — ✅ exact match

Context diversity: 7+ distinct
✅ PASS: Context diversity ≥ 5

(subtopic, archetype) uniqueness: 100/100 ✅ PASS
100 unique subtopics ✅ PASS

## 4. ORIGINALITY GATE

✅ PASS: Within-batch exact duplicates — 0
✅ PASS: Cross-batch exact duplicates vs B01+B02+B03 — 0
✅ PASS: Cross-batch semantic near-duplicates — 0 (≥4 shared 4-grams, ≥0.5 ratio)
✅ PASS: No subtopic overlap with B01-B03 — 0 shared subtopics
✅ PASS: No ID overlap with B01-B03 — 0

## 5. METADATA GATE

✅ PASS: contentOrigin=ORIGINAL (100/100)
✅ PASS: licenseStatus=self_authored (100/100)
✅ PASS: commercialReuseAllowed=true (100/100)
✅ PASS: examYear=null (100/100)
✅ PASS: subjectCode=en (100/100)
✅ PASS: schoolTrack=SK (100/100)
✅ PASS: stage=primary (100/100)
✅ PASS: gradeLevel=Tahun1 (100/100)

## 6. SHA-256

- **File SHA-256**: `8ec9c579fe8cf54a2f4d01a4a3bbbf1fc2b00fbcfe227afe3ae9c13fb594786a`
- **Source / local production batch**: `batch04_sk_en_y1.json` (D:\Users\bajub\kuizku_p10\primary\)
- **Local production SHA-256**: identical byte-for-byte to this file

## 7. SUMMARY

- Total questions: **100**
- Difficulty: easy=**50** medium=**40** hard=**10**
- Topics: 5 unique
- Skills: RECOGNITION 52, COMPREHENSION 20, APPLICATION 28
- Contexts: 7+ distinct
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

> **Local Production Source**: `D:\Users\bajub\kuizku_p10\primary\batch04_sk_en_y1.json` (SK Primary Year 1 English, KSSR curriculum).
>
> **Public Repo Publication**: This is the FOURTH batch published in `leonchoo/kuizku-content` EN primary path. Public repo adopts standardized naming `banks\<school>\<level>\<subject>\batchNN.json` sequential. Local B04 → public `batch04.json` (after batch01 = Local B01, batch02 = Local B02, batch03 = Local B03).
>
> **All 100 questions are ORIGINAL / self-authored by KuizKu.** No question text, options, explanation, or structure was copied from any external source. The Reference DB was used ONLY as a KSSR Y1 English style anchor (1 T1 English file).
>
> **Cumulative originality verified against SK Primary Y1 EN local Production (B01 25 Qs + B02 25 Qs + B03 100 Qs = 150 Qs).** Zero ID overlap, zero subtopic overlap, zero exact-duplicate, zero near-duplicate. This batch contributes 100/100 NEW (subtopic, blueprintArchetype) pairs.
>
> **SK Primary Y1 English cumulative total after this Promotion: 250 questions (B01 25 + B02 25 + B03 100 + B04 100).**
