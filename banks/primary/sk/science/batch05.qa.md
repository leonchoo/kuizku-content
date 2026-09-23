# QA Report — batch05_sk_science_y1 (Primary SK Y1 Science Batch 05)

**Batch**: `batch05_sk_science_y1` (local Production batch number; published as `batch05.json`)
**Local Production Path**: `D:\Users\bajub\kuizku_p10\primary\batch05_sk_science_y1.json`
**Public Repo Path**: `banks\primary\sk\science\batch05.json`
**Date**: 2026-09-23
**Total Questions**: 100
**Curriculum**: KSSR
**Grade Level**: Tahun 1 (Primary)
**Subject ID**: `***`
**schoolTrack**: SK
**stage**: primary
**Subject Code**: science
**Language**: ms (Bahasa Malaysia — matches B01-B04)

---

## Hashes

| Item | Value |
|---|---|
| **Local production SHA-256** | `88a58ad3a4cf8e5a1926ac22c9193071f1139f14499f541f8d91fdc485220bd0` |
| **Local production file size** | 155,503 bytes |
| **Question ID range** | `***` to `***` (sk-science-y1-351..450) |

---

## 1. STRUCTURAL GATE

✅ PASS: JSON valid — 100 questions parsed
✅ PASS: All required fields present (100/100)
✅ PASS: schoolTrack=SK (100/100)
✅ PASS: stage=primary (100/100)
✅ PASS: gradeLevel=Tahun1 (100/100)
✅ PASS: curriculum=KSSR (100/100)
✅ PASS: language=ms (100/100)
✅ PASS: subjectCode=science (100/100)

## 2. ANSWER GATE

✅ PASS: exactly one correct answer per question — 100/100
✅ PASS: correct answer option non-empty — 100/100
✅ PASS: no duplicate options — 100/100

## 3. CONTENT GATE

✅ PASS: Malay-medium (Bahasa Malaysia) Science natural (spot-check) — 100/100

Difficulty distribution (target 60/30/10 per B01-B04 canonical):
  - Easy (diff=1): 60 Q
  - Medium (diff=2): 30 Q
  - Hard (diff=3): 10 Q
✅ PASS: Difficulty matches Plan — ✅ exact

Topic distribution (7 topic labels, matches B01-B04):
  - Haiwan: 20 Q
  - Tumbuhan: 12 Q
  - Bahan: 16 Q
  - Pergerakan: 10 Q
  - Panas: 12 Q
  - Cuaca: 10 Q
  - Pemerhatian: 20 Q
✅ PASS: 7 topic labels — ✅ all covered

Skill distribution (target 46/26/28 per B01-B04 canonical):
  - RECOGNITION: 46 Q
  - COMPREHENSION: 26 Q
  - APPLICATION: 28 Q
✅ PASS: Skill sum=100 (46/26/28) — ✅ exact match

Context diversity: 7+ distinct
✅ PASS: Context diversity ≥ 5

(subtopic, archetype) uniqueness: 100/100 ✅ PASS
100 unique subtopics ✅ PASS

## 4. ORIGINALITY GATE

✅ PASS: Within-batch exact duplicates — 0
✅ PASS: Cross-batch exact duplicates vs B01+B02+B03+B04 — 0
✅ PASS: Cross-batch semantic near-duplicates — 0 (≥4 shared 4-grams, ≥0.5 ratio)
✅ PASS: No subtopic overlap with B01-B04 — 0 shared subtopics
✅ PASS: No ID overlap with B01-B04 — 0

## 5. METADATA GATE

✅ PASS: contentOrigin=ORIGINAL (100/100)
✅ PASS: licenseStatus=self_authored (100/100)
✅ PASS: commercialReuseAllowed=true (100/100)
✅ PASS: examYear=null (100/100)
✅ PASS: subjectCode=science (100/100)
✅ PASS: schoolTrack=SK (100/100)
✅ PASS: stage=primary (100/100)
✅ PASS: gradeLevel=Tahun1 (100/100)
✅ PASS: language=ms (100/100)

## 6. SHA-256

- **File SHA-256**: `88a58ad3a4cf8e5a1926ac22c9193071f1139f14499f541f8d91fdc485220bd0`
- **Source / local production batch**: `batch05_sk_science_y1.json` (D:\Users\bajub\kuizku_p10\primary\)
- **Local production SHA-256**: identical byte-for-byte to this file

## 7. SUMMARY

- Total questions: **100**
- Difficulty: easy=**60** medium=**30** hard=**10**
- Topics: 7 unique (Haiwan 20, Tumbuhan 12, Bahan 16, Pergerakan 10, Panas 12, Cuaca 10, Pemerhatian 20)
- Skills: RECOGNITION 46, COMPREHENSION 26, APPLICATION 28
- Contexts: 7+ distinct
- (subtopic, archetype) uniqueness: **100/100**
- Exact duplicates (within batch): **0**
- Exact duplicates (vs B01-B04): **0**
- Near duplicates (within batch): **0**
- Near duplicates (vs B01-B04): **0**
- Subtopic overlap (vs B01-B04): **0**
- Curriculum scope IN-SCOPE: **100/100**, BORDERLINE: **0**, OUT-OF-SCOPE: **0**
- Correctness spot-check: **12/12 PASS**
- Metadata validation failures: **0**
- Structural validation failures: **0**
- Answer validation failures: **0**
- TOTAL FAILURES: **0**
- TOTAL WARNINGS: **0**

✅ **BATCH 05 QA PASS — ALL 100 QUESTIONS PASS**

---

## Source Provenance Statement (REQUIRED)

> **Local Production Source**: `D:\Users\bajub\kuizku_p10\primary\batch05_sk_science_y1.json` (SK Primary Year 1 Science, KSSR curriculum, Malay medium).
>
> **Public Repo Publication**: This is the FIFTH batch published in `leonchoo/kuizku-content` Science primary path. Public repo adopts standardized naming `banks\<school>\<level>\<subject>\batchNN.json` sequential. Local B05 → public `batch05.json` (after batch01..batch04).
>
> **All 100 questions are ORIGINAL / self-authored by KuizKu.** No question text, options, explanation, or structure was copied from any external source. The Reference DB was used ONLY as a KSSR Y1 Science style anchor.
>
> **Cumulative originality verified against SK Primary Y1 Science local Production (B01 50 Qs + B02 100 Qs + B03 100 Qs + B04 100 Qs = 350 Qs).** Zero ID overlap, zero subtopic overlap, zero exact-duplicate, zero near-duplicate. This batch contributes 100/100 NEW (subtopic, blueprintArchetype) pairs.
>
> **SK Primary Y1 Science cumulative total after this Promotion: 450 questions (B01 50 + B02 100 + B03 100 + B04 100 + B05 100).**
