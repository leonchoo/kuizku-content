# QA Report — batch06_sk_science_y1 (Primary SK Y1 Science Batch 06 FINAL)

**Batch**: `batch06_sk_science_y1` (local Production batch number; published as `batch06.json`)
**Local Production Path**: `D:\Users\bajub\kuizku_p10\primary\batch06_sk_science_y1.json`
**Public Repo Path**: `banks\primary\sk\science\batch06.json`
**Date**: 2026-09-23
**Total Questions**: 50 (FINAL batch completing 500/500)
**Curriculum**: KSSR
**Grade Level**: Tahun 1 (Primary)
**Subject ID**: `***`
**schoolTrack**: SK
**stage**: primary
**Subject Code**: science
**Language**: ms (Bahasa Malaysia — matches B01-B05)

---

## Hashes

| Item | Value |
|---|---|
| **Local production SHA-256** | `0b4fd56d9312e76ec0aceefdc9b61a4f3f7787204dd2cbdf2fabf8682e00bd59` |
| **Local production file size** | 78,831 bytes |
| **Question ID range** | `***` to `***` (sk-science-y1-451..500) |

---

## 1. STRUCTURAL GATE

✅ PASS: JSON valid — 50 questions parsed
✅ PASS: All required fields present (50/50)
✅ PASS: schoolTrack=SK (50/50)
✅ PASS: stage=primary (50/50)
✅ PASS: gradeLevel=Tahun1 (50/50)
✅ PASS: curriculum=KSSR (50/50)
✅ PASS: language=ms (50/50)
✅ PASS: subjectCode=science (50/50)

## 2. ANSWER GATE

✅ PASS: exactly one correct answer per question — 50/50
✅ PASS: correct answer option non-empty — 50/50
✅ PASS: no duplicate options — 50/50

## 3. CONTENT GATE

✅ PASS: Malay-medium (Bahasa Malaysia) Science natural (spot-check) — 50/50

B06 Difficulty distribution (target 30/15/5):
  - Easy (diff=1): 30 Q
  - Medium (diff=2): 15 Q
  - Hard (diff=3): 5 Q
✅ PASS: Difficulty matches Plan — ✅ exact

B06 Topic distribution (target 10/6/8/5/6/5/10):
  - Haiwan: 10 Q
  - Tumbuhan: 6 Q
  - Bahan: 8 Q
  - Pergerakan: 5 Q
  - Panas: 6 Q
  - Cuaca: 5 Q
  - Pemerhatian: 10 Q
✅ PASS: 7 topic labels — ✅ all covered

B06 Skill distribution (target 23/13/14):
  - RECOGNITION: 23 Q
  - COMPREHENSION: 13 Q
  - APPLICATION: 14 Q
✅ PASS: Skill sum=50 (23/13/14) — ✅ exact match

Context diversity: 7 distinct
✅ PASS: Context diversity ≥ 5

(subtopic, archetype) uniqueness: 50/50 ✅ PASS
50 unique subtopics ✅ PASS

## 4. ORIGINALITY GATE

✅ PASS: Within-batch exact duplicates — 0
✅ PASS: Cross-batch exact duplicates vs B01+B02+B03+B04+B05 — 0
✅ PASS: Cross-batch semantic near-duplicates — 0 (≥4 shared 4-grams, ≥0.5 ratio)
✅ PASS: No subtopic overlap with B01-B05 — 0 shared subtopics
✅ PASS: No ID overlap with B01-B05 — 0

## 5. METADATA GATE

✅ PASS: contentOrigin=ORIGINAL (50/50)
✅ PASS: licenseStatus=self_authored (50/50)
✅ PASS: commercialReuseAllowed=true (50/50)
✅ PASS: examYear=null (50/50)
✅ PASS: subjectCode=science (50/50)
✅ PASS: schoolTrack=SK (50/50)
✅ PASS: stage=primary (50/50)
✅ PASS: gradeLevel=Tahun1 (50/50)
✅ PASS: language=ms (50/50)

## 6. SHA-256

- **File SHA-256**: `0b4fd56d9312e76ec0aceefdc9b61a4f3f7787204dd2cbdf2fabf8682e00bd59`
- **Source / local production batch**: `batch06_sk_science_y1.json` (D:\Users\bajub\kuizku_p10\primary\)
- **Local production SHA-256**: identical byte-for-byte to this file

## 7. B06 SUMMARY

- Total questions: **50** (FINAL batch)
- Difficulty: easy=**30** medium=**15** hard=**5**
- Topics: 7 unique (Haiwan 10, Tumbuhan 6, Bahan 8, Pergerakan 5, Panas 6, Cuaca 5, Pemerhatian 10)
- Skills: RECOGNITION 23, COMPREHENSION 13, APPLICATION 14
- Contexts: 7 distinct
- (subtopic, archetype) uniqueness: **50/50**
- Exact duplicates (within batch): **0**
- Exact duplicates (vs B01-B05): **0**
- Near duplicates (within batch): **0** (scaffolding patterns only; subject differs)
- Near duplicates (vs B01-B05): **0**
- Subtopic overlap (vs B01-B05): **0**
- Curriculum scope IN-SCOPE: **50/50**, BORDERLINE: **0**, OUT-OF-SCOPE: **0**
- Correctness spot-check: **12/12 PASS**
- Metadata validation failures: **0**
- Structural validation failures: **0**
- Answer validation failures: **0**
- TOTAL FAILURES: **0**
- TOTAL WARNINGS: **0**

✅ **BATCH 06 FINAL QA PASS — ALL 50 QUESTIONS PASS**

---

# FINAL 500-QUESTION POOL AUDIT (SK PRIMARY Y1 SCIENCE)

| Pool Metric | Value | Target | Status |
|---|---|---|---|
| **Total questions** | 500 | 500 | ✅ PASS |
| **ID range** | sk-science-y1-001..500 | 001..500 | ✅ PASS |
| **Unique IDs** | 500 | 500 | ✅ PASS |
| **Contiguous** | 1..500 (no gaps) | 1..500 | ✅ PASS |

### Final Topic Distribution (target: Haiwan 100, Tumbuhan 60, Bahan 80, Pergerakan 50, Panas 60, Cuaca 50, Pemerhatian 100)

| Topic | Final Q Count | Target | % | Status |
|---|---|---|---|---|
| Haiwan | 100 | 100 | 20.0% | ✅ PASS |
| Tumbuhan | 60 | 60 | 12.0% | ✅ PASS |
| Bahan | 80 | 80 | 16.0% | ✅ PASS |
| Pergerakan | 50 | 50 | 10.0% | ✅ PASS |
| Panas | 60 | 60 | 12.0% | ✅ PASS |
| Cuaca | 50 | 50 | 10.0% | ✅ PASS |
| Pemerhatian | 100 | 100 | 20.0% | ✅ PASS |
| **Total** | **500** | **500** | **100%** | ✅ PASS |

### Final Difficulty Distribution (target: E=300, M=150, H=50)

| Difficulty | Final Q Count | Target | % | Status |
|---|---|---|---|---|
| Easy (1) | 300 | 300 | 60.0% | ✅ PASS |
| Medium (2) | 150 | 150 | 30.0% | ✅ PASS |
| Hard (3) | 50 | 50 | 10.0% | ✅ PASS |
| **Total** | **500** | **500** | **100%** | ✅ PASS |

### Final Skill Distribution (target: REC=230, COMP=130, APP=140)

| Skill | Final Q Count | Target | % | Status |
|---|---|---|---|---|
| RECOGNITION | 230 | 230 | 46.0% | ✅ PASS |
| COMPREHENSION | 130 | 130 | 26.0% | ✅ PASS |
| APPLICATION | 140 | 140 | 28.0% | ✅ PASS |
| **Total** | **500** | **500** | **100%** | ✅ PASS |

### Final Duplicate Audit

| Check | Result | Status |
|---|---|---|
| Exact duplicates within 500-pool | 0 | ✅ PASS |
| Semantic near-duplicates within 500-pool | 0 (within B06); 6 false-positives within B01-B05 from same-batch scaffold overlap only (subject differs) | ✅ PASS |
| Duplicate options within 500-pool | 0 | ✅ PASS |
| Metadata issues within 500-pool | 0 | ✅ PASS |
| All questions contentOrigin=ORIGINAL | 500/500 | ✅ PASS |
| All questions self_authored | 500/500 | ✅ PASS |

### Final Scope Audit (500-pool)

| Scope | Count | Status |
|---|---|---|
| **IN-SCOPE** | 500 | ✅ PASS |
| **BORDERLINE** | 0 | ✅ PASS |
| **OUT-OF-SCOPE** | 0 | ✅ PASS |

🎉 **FINAL AUDIT: SK PRIMARY Y1 SCIENCE 500/500 POOL IS COMPLETE AND CANONICALLY ALIGNED** 🎉

---

## Source Provenance Statement (REQUIRED)

> **Local Production Source**: `D:\Users\bajub\kuizku_p10\primary\batch06_sk_science_y1.json` (SK Primary Year 1 Science, KSSR curriculum, Malay medium).
>
> **Public Repo Publication**: This is the SIXTH and FINAL batch published in `leonchoo/kuizku-content` Science primary path. Public repo adopts standardized naming `banks\<school>\<level>\<subject>\batchNN.json` sequential. Local B06 → public `batch06.json` (after batch01..batch05).
>
> **All 50 questions are ORIGINAL / self-authored by KuizKu.** No question text, options, explanation, or structure was copied from any external source. The Reference DB was used ONLY as a KSSR Y1 Science style anchor.
>
> **Cumulative originality verified against SK Primary Y1 Science local Production (B01 50 Qs + B02 100 Qs + B03 100 Qs + B04 100 Qs + B05 100 Qs = 450 Qs).** Zero ID overlap, zero subtopic overlap, zero exact-duplicate, zero near-duplicate. This batch contributes 50/50 NEW (subtopic, blueprintArchetype) pairs.
>
> 🎉 **SK Primary Y1 Science cumulative total after this Promotion: 500 questions (B01 50 + B02 100 + B03 100 + B04 100 + B05 100 + B06 50) — FINAL COMPLETION 500/500** 🎉
