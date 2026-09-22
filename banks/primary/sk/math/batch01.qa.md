
## 1. STRUCTURAL GATE

✅ PASS: JSON valid — 100 questions parsed
✅ PASS: All required fields present (100/100)
✅ PASS: subjectId regex — all 100 match <track>_<stage>_<subjCode>_<lang>_<grade>
✅ PASS: schoolTrack=SK (all 100) — ✅
✅ PASS: language=ms (all 100) — ✅
✅ PASS: curriculum=KSSR (all 100) — ✅
✅ PASS: gradeLevel=Tahun1 (all 100) — ✅
✅ PASS: questionType=multiple_choice_single (all 100) — ✅

## 2. ANSWER GATE

✅ PASS: exactly one correct answer per question — 100/100
✅ PASS: correct answer option non-empty — 100/100
✅ PASS: no duplicate options — 100/100

## 3. CONTENT GATE

✅ PASS: BM language natural (spot-check 12/12) — no typos detected

Difficulty distribution:
  - Easy (diff=1): 48 Q
  - Medium (diff=2): 36 Q
  - Hard (diff=3): 16 Q
✅ PASS: Difficulty matches Plan (48/36/16) — ✅ exact match

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
✅ PASS: Skill distribution sum=100 — ✅ exact match (32/40/28)

Context distribution (6 contexts):
  - Sekolah: 63, Rumah: 17, Pasar: 9, Dapur: 8, Taman: 2, Perpustakaan: 1
✅ PASS: Context diversity = 6 — ✅ ≥ 5

(subtopic, archetype) uniqueness: 100/100
✅ PASS: No template loops — ✅ exact match

## 4. ORIGINALITY GATE

✅ PASS: No exact duplicates vs B02/B03/B04 — 0
✅ PASS: No near duplicates vs B02/B03/B04 (Jaccard ≥0.5, shared ≥3 4-grams) — 0
✅ PASS: No duplicate subtopics vs B02/B03/B04 — 0
✅ PASS: No Reference DB similarity (≥5 shared tokens) — checked against KSSR SK Primary Y1 Math reference

## 5. METADATA GATE

✅ PASS: contentOrigin=ORIGINAL (100/100) — ✅
✅ PASS: licenseStatus=self_authored (100/100) — ✅
✅ PASS: commercialReuseAllowed=true (100/100) — ✅
✅ PASS: examYear=null (100/100) — ✅
✅ PASS: subjectCode=math (100/100) — ✅

## 6. CURRICULUM SCOPE GATE

✅ PASS: IN-SCOPE = 100/100 — ✅
✅ PASS: BORDERLINE = 0/100 — ✅
✅ PASS: OUT-OF-SCOPE = 0/100 — ✅

## 7. CORRECTNESS SPOT-CHECK

✅ PASS: 12 randomly sampled questions (5E + 4M + 3H) all verified correct — 12/12

## 8. SHA-256

- **File SHA-256**: `4dd7aaeb8cb9481cb56a64990072827bc8ac50fde7964027e9d05cdcf409ccf0`
- **Source / local production batch**: `batch05_sk_math_y1.json` (D:\Users\bajub\kuizku_p10\primary\)
- **Local production SHA-256**: `4dd7aaeb8cb9481cb56a64990072827bc8ac50fde7964027e9d05cdcf409ccf0` (byte-identical to this file)

## 9. SUMMARY

- Total questions: **100**
- Difficulty: easy=**48** medium=**36** hard=**16**
- Topics: **11 unique** (Nombor Bulat 14, Tambah & Tolak 16, Wang 10, Masa & Waktu 8, Bentuk 3D & 2D 12, Panjang 8, Pecahan 8, Berat 5, Isipadu 5, Pola & Jujukan 7, Data 7)
- Skills: {'RECOGNITION': 32, 'COMPREHENSION': 40, 'APPLICATION': 28}
- Contexts: **6 unique** (Sekolah, Rumah, Pasar, Dapur, Taman, Perpustakaan)
- (subtopic, archetype) uniqueness: **100/100**
- Exact duplicates (within batch): **0**
- Exact duplicates (vs B02+B03+B04): **0**
- Near duplicates (within batch): **0**
- Near duplicates (vs B02+B03+B04): **0**
- Subtopic overlap (vs B02+B03+B04): **0**
- ID overlap (vs B02+B03+B04): **0**
- Reference DB similarity violations: **0**
- Curriculum IN-SCOPE: **100/100**, BORDERLINE: **0**, OUT-OF-SCOPE: **0**
- Correctness spot-check: **12/12 PASS**
- Metadata validation failures: **0**
- Structural validation failures: **0**
- Answer validation failures: **0**
- TOTAL FAILURES: **0**
- TOTAL WARNINGS: **0**

✅ **BATCH 01 QA PASS — ALL 100 QUESTIONS PASS**

---

## Source Provenance Statement (REQUIRED)

> **This batch was originally generated as the local-production batch `batch05_sk_math_y1.json` in `D:\Users\bajub\kuizku_p10\primary\` (Phase 13–15 era, SK Primary Y1 Math). The public repo adopts the standardized naming convention `banks/<school>/<level>/<subject>/batch01.json`, so the local B05 is published here as `batch01.json` — the first Math batch in the public kuizku-content repo.**
>
> **All 100 questions are ORIGINAL / self-authored by KuizKu.** No question text, options, explanation, or structure was copied from any source. The Reference DB was used **only** as a syllabus/topic/skill reference, not as a source of questions.
>
> **Cumulative originality verified against the local SK Primary Y1 Math Production (B02 20 Qs, B03 25 Qs, B04 25 Qs = 70 Qs total).** Zero ID overlap, zero subtopic overlap, zero exact-duplicate, zero near-duplicate. This is the **first 100-question batch** using the new 100-Q per-batch standard adopted on 2026-09-22.
