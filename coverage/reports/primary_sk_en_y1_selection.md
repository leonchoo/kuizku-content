# Phase 2 — Next Batch Selection

> **Selection for the next KuizKu Primary batch.**

## Selected Combination

```yaml
schoolTrack: SK
gradeLevel: Tahun1
subjectCode: en
language: en
curriculum: KSSR
subjectId: sk_prim_en_ms_Y1   # SK English, primary, English-subject-code, Malay-medium (SK's English is MFL), Year 1
batchNumber: 02
targetQuestionCount: 25
```

## Why this combination?

1. **Doesn't repeat Batch01's subject** — Batch01 was SK BM Y1 (Bahasa Melayu). SK English Y1 is a new subject.
2. **Pipeline-proven path** — Same track (SK) + grade (Y1), only subject changes. Reuses all the Y1 structural work done for Batch01.
3. **Reference DB has English Y1** — `/references DB/primary/English/Tahun1/(T1 English style anchor)` provides syllabus-style reference for question style, difficulty calibration, and topic distribution.
4. **KSSR-aligned** — SK English is MFL (Bahasa Inggeris sebagai bahasa kedua). The KSSR English framework is well-defined and 638 has full familiarity with it.
5. **Foundation for further expansion** — Once SK English Y1 is established, the natural sequence is SK English Y2-Y6 (5 more batches) to fill the SK English column entirely.

## What 638 must NOT be surprised by

- SK English is **MFL** (Malay-medium school, English as subject) — NOT English-native. Question style, vocabulary, grammar focus differ from International English.
- Year 1 English is heavily **RECOGNITION-focused** (alphabet, sight words, simple vocabulary) — not Cambridge-style comprehension.
- SubjectId format per Phase 10.3: `sk_prim_<subjectCode>_<language>_<grade>` = `sk_prim_en_ms_Y1`.

## Target Difficulty Distribution

Per Phase 10.4 §7 (Year 1 base: 60/30/10):
- Easy: 60% → 15 Q
- Medium: 30% → 8 Q (rounded from 7.5)
- Hard: 10% → 3 Q (rounded from 2.5)

Practical: 15 Easy + 7 Medium + 3 Hard = **25 Q**

## Target Skill Distribution

Per Phase 10.4 §8 (English per grade: heavy RECOGNITION at T1-T2, then more comprehension):
- RECOGNITION: 60% → 15 Q (alphabet, sight words, vocabulary identification)
- COMPREHENSION: 30% → 8 Q (short instructions, simple sentences)
- APPLICATION: 10% → 2 Q (using vocabulary in context, naming objects)

Practical: 15 RECOGNITION + 8 COMPREHENSION + 2 APPLICATION = **25 Q**

## Target Topic Coverage (per Phase 10.4 §8 English Year 1)
- Listening & Speaking (greetings, instructions): 4 Q
- Reading (phonics, sight words): 6 Q
- Writing (letters, words, simple sentences): 3 Q
- Grammar (articles, plurals, verbs): 5 Q
- Vocabulary (colours, animals, family): 7 Q

Total 25 Q distributed across 5 topics (≥ 1 Q per topic, max 7 Q per topic).

## Selection rationale vs alternatives

| Alternative | Why not chosen |
|---|---|
| SK BM Y2 | Violates "不连续大量重复同一个 subject" — would be BM twice in a row |
| SK Math Y1 | Strong candidate but Math topic distribution differs (more abstract); better as 3rd batch to avoid two "abstract" subjects back-to-back |
| SK Science Y1 | Same as Math — better as 4th batch |
| SJKC 中文 Y1 | Reference DB gap; 638 §5 flags as needing external syllabus docs |
| International English Y1 | Reference DB Mismatch; pure ORIGINAL from Cambridge curriculum needed (large scope for first formal Primary batch beyond SK) |
