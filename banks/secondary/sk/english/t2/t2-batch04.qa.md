# QA Report — batch_secondary_04_sk_en_t2

**Batch**: `batch_secondary_04_sk_en_t2`
**File (local production source)**: `D:\Users\bajub\kuizku_p10\batch_secondary_04_sk_en_t2.json`
**Public repo path**: `banks/secondary/sk/english/t2/t2-batch04.json`
**Date**: 2026-09-22
**Total Questions**: 100
**Curriculum**: KSSM
**Grade Level**: Tingkatan 2
**Subject ID**: `sk-sec-en-t2`
**schoolTrack**: SK
**stage**: secondary

---

## Hashes

| Item | Value |
|---|---|
| **Local production SHA-256** | `de653697842ce35879beaea9f836160fdf7200175ed04492aad4c2a402bc5747` |
| **Local production file size** | 97,562 bytes |
| **Question ID range** | `***..***` (terminal-redacted; numeric range 301..400) |
| **Subject ID** | `sk-sec-en-t2` |

The public-repo JSON at `banks/secondary/sk/english/t2/t2-batch04.json` is byte-identical to the local production file at the time of upload.

---

## 1. STRUCTURAL GATE

✅ PASS: JSON valid — 100 questions parsed
✅ PASS: All required fields present (subjectId, subjectCode, topic, subtopic, skillType, difficulty, questionText, options, correctAnswer, correctAnswerLabel, explanation, contentOrigin, licenseStatus, commercialReuseAllowed, examYear, language, schoolTrack, stage, gradeLevel, curriculum, blueprintArchetype)
✅ PASS: subjectId consistent (sk-sec-en-t2 across all 100)
✅ PASS: schoolTrack=SK (100/100)
✅ PASS: stage=secondary (100/100)
✅ PASS: gradeLevel=T2 (100/100)
✅ PASS: curriculum=KSSM (100/100)
✅ PASS: language=en (100/100)
✅ PASS: questionType=SINGLE_CHOICE (100/100)

## 2. ANSWER GATE

✅ PASS: exactly one correct answer per question — 100/100
✅ PASS: correctAnswer field non-empty — 100/100
✅ PASS: correctAnswerLabel matches correctAnswer (a↔A, b↔B, c↔C, d↔D) — 100/100
✅ PASS: no duplicate options — 100/100
✅ PASS: no multi-correct — 100/100

## 3. CONTENT GATE

✅ PASS: English language natural (spot-check 12/12) — no typos detected

Difficulty distribution:
  - Easy (diff=1): 35 Q
  - Medium (diff=2): 50 Q
  - Hard (diff=3): 15 Q
✅ PASS: Difficulty matches Plan (35/50/15) — ✅ exact match

Topic distribution:
  - Vocabulary: 30 Q
  - Grammar: 15 Q
  - Reading: 15 Q
  - Sentence Usage: 15 Q
  - Functional English: 10 Q
  - Contextual Language: 10 Q
  - Other: 5 Q
✅ PASS: 7 topic categories × correct counts — ✅ exact

Skill distribution:
  - RECOGNITION: 20 Q
  - COMPREHENSION: 50 Q
  - APPLICATION: 30 Q
✅ PASS: Skill distribution sum=100 — ✅ exact match (20/50/30)

## 4. ORIGINALITY GATE

✅ PASS: Within-batch exact duplicates — 0
✅ PASS: Cross-batch exact duplicates vs B01+B02+B03 — 0 (cumulative over 300 prior Qs)
✅ PASS: Cross-batch semantic near-duplicates (≥4 shared 4-grams, Jaccard ≥0.5) — 0
✅ PASS: No subtopic overlap with B01+B02+B03 — 0 shared subtopics
✅ PASS: No ID overlap with B01+B02+B03 — 0
✅ PASS: No template loops detected — every (subtopic, blueprintArchetype) pair is unique within B04
✅ PASS: All 100 subtopics in B04 are NEW (not seen in any of B01/B02/B03)

## 5. METADATA GATE

✅ PASS: contentOrigin=ORIGINAL (100/100)
✅ PASS: licenseStatus=self_authored (100/100)
✅ PASS: commercialReuseAllowed=true (100/100)
✅ PASS: examYear=null (100/100)
✅ PASS: subjectCode=en (100/100)
✅ PASS: schoolTrack=SK (100/100)
✅ PASS: stage=secondary (100/100)
✅ PASS: gradeLevel=T2 (100/100)

## 6. CURRICULUM SCOPE GATE (KSSM T2 English)

✅ PASS: IN-SCOPE = 100/100
✅ PASS: BORDERLINE = 0/100
✅ PASS: OUT-OF-SCOPE = 0/100

Question types covered (per KSSR T2 syllabus):
- Vocabulary (general, academic, contextual)
- Grammar (verb tenses, modals, pronouns, conjunctions, prepositions)
- Reading (dialogues, fables, fairy tales, menus, labels, news, instructions)
- Sentence usage (error correction, transformation, passive/active, reported speech)
- Functional English (polite expressions, idioms)
- Contextual Language (situational vocabulary)
- Basic English (greetings, time, abbreviations)

## 7. CORRECTNESS SPOT-CHECK

✅ PASS: 12 random questions (5E + 4M + 3H) manually verified — 12/12 answers correct

## 8. SUMMARY

- Total questions: **100**
- Difficulty: easy=**35** medium=**50** hard=**15**
- Topic distribution: Vocabulary 30, Grammar 15, Reading 15, Sentence Usage 15, Functional English 10, Contextual Language 10, Other 5
- Skills: RECOGNITION 20, COMPREHENSION 50, APPLICATION 30
- Within-batch exact duplicates: **0**
- Cross-batch exact duplicates: **0**
- Cross-batch semantic near duplicates: **0**
- Subtopic overlap with prior batches: **0**
- Curriculum scope IN-SCOPE: **100/100**, BORDERLINE: **0**, OUT-OF-SCOPE: **0**
- Correctness spot-check: **12/12 PASS**
- Metadata validation failures: **0**
- Structural validation failures: **0**
- Answer validation failures: **0**
- TOTAL FAILURES: **0**
- TOTAL WARNINGS: **0**

✅ **BATCH 04 QA PASS — ALL 100 QUESTIONS PASS**

---

## Source Provenance Statement

> **Local Production Source**: `D:\Users\bajub\kuizku_p10\batch_secondary_04_sk_en_t2.json` (SK Secondary T2 English, KSSM curriculum).
>
> **Public Repo Publication**: This file is the first batch of SK Secondary T2 English in `leonchoo/kuizku-content`. The public repo adopts the standardized naming convention `banks/<school>/<level>/<subject>/<stage>/<batch>.json`, so the local B04 (Production batch 4 in the internal numbering) is published here as `t2-batch04.json`.
>
> **All 100 questions are ORIGINAL / self-authored by KuizKu.** No question text, options, explanation, or structure was copied from any external source. The Reference DB was used **only** as a KSSM T2 English syllabus/topic/style reference, not as a source of questions.
>
> **Cumulative originality verified against T2 English local Production (B01 100 Qs + B02 100 Qs + B03 100 Qs = 300 Qs total).** Zero ID overlap, zero subtopic overlap, zero exact-duplicate, zero near-duplicate. This batch contributes 100/100 NEW (subtopic, blueprintArchetype) pairs.
