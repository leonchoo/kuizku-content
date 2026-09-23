# T3 Science B02 — QA Report

## Production Summary

| Property | Value |
|---|---|
| **Production source** | `D:\Users\bajub\kuizku_p10\batch_secondary_02_sk_science_t3.json` |
| **Public file** | `banks/secondary/sk/science/t3/batch02.json` |
| **SHA-256** | `969ccf0cb7cd3b5ac2660af7db955c48635f9532e6caedb52beac68d62dab6df` |
| **Size** | 108,573 bytes |
| **Count** | 100 Q |
| **ID range** | sk-sec-science-t3-101 ~ sk-sec-science-t3-200 |
| **JSON parse** | Valid |
| **School Track** | SK |
| **Stage** | Secondary |
| **Grade** | T3 (Tingkatan 3) |
| **Subject** | Science |
| **Language** | en |

## QA Gates (19/19 PASS)

| # | Gate | Result |
|---|---|---|
| G1 | Count = 100 | PASS |
| G2 | IDs 101-200 contiguous | PASS |
| G3 | IDs unique | PASS |
| G4 | Within-batch exact dup = 0 | PASS |
| G5 | Cross-batch exact dup = 0 | PASS |
| G6 | Semantic near-dup = 0 | PASS |
| G7 | Duplicate options = 0 | PASS |
| G8 | Multi-correct = 0 | PASS |
| G9 | Topic distribution 10×10 | PASS |
| G10 | Skill 20/50/30 | PASS |
| G11 | EVAL = 0 | PASS |
| G12 | Metadata 100% | PASS |
| G13 | Difficulty 35/50/15 | PASS |
| G14 | Correct answers in options | PASS |
| G15 | Answer/Label match | PASS |
| G16 | (Subtopic, Archetype) reuse = 0 | PASS |
| G17 | B02 unique SA = 100 | PASS |
| G17b | B02 unique subtopics = 100 | PASS |
| G17c | ID overlap = 0 | PASS |

## Topic Distribution (LOCKED 10×10)

| Topic | Count |
|---|---:|
| Scientific Methodology | 10 |
| Cell Biology | 10 |
| Nutrition | 10 |
| Chemistry - Water and Solutions | 10 |
| Chemistry - Acids and Alkalis | 10 |
| Physics - Force and Motion | 10 |
| Physics - Light and Optics | 10 |
| Physics - Heat | 10 |
| Physics - Electricity | 10 |
| Genetics and Reproduction | 10 |
| **TOTAL** | **100** |

## Skill Distribution (LOCKED 20/50/30)

| Skill | Count |
|---|---:|
| RECOGNITION | 20 |
| COMPREHENSION | 50 |
| APPLICATION | 30 |
| **TOTAL** | **100** |

## Difficulty Distribution (LOCKED 35/50/15)

| Difficulty | Count |
|---|---:|
| D1 (Easy) | 35 |
| D2 (Medium) | 50 |
| D3 (Hard) | 15 |
| **TOTAL** | **100** |

## Curriculum Scope Audit (100/0/0)

| Status | Count |
|---|---:|
| **IN-SCOPE** | **100** |
| **BORDERLINE** | **0** |
| **OUT-OF-SCOPE** | **0** |

## Correctness Spot-Check (12/12 PASS)

| Q | Topic | Difficulty | Verified |
|---|---|---|---|
| Q101 | Scientific Methodology | D1 | PASS - Hypothesis = testable prediction |
| Q113 | Cell Biology | D1 | PASS - Plant cell wall (cellulose) unique |
| Q123 | Nutrition | D1 | PASS - Biuret protein test = blue → purple |
| Q133 | Chemistry - Water and Solutions | D1 | PASS - Gas solubility decreases with temp |
| Q146 | Chemistry - Acids and Alkalis | D2 | PASS - HCl + NaOH → NaCl + H2O |
| Q151 | Physics - Force and Motion | D2 | PASS - Distance = total path (10 m), displacement = 0 |
| Q158 | Physics - Force and Motion | D2 | PASS - Unbalanced forces → acceleration |
| Q165 | Physics - Light and Optics | D2 | PASS - Refraction = speed change in different medium |
| Q176 | Physics - Heat | D2 | PASS - Metals best conductors (free electrons) |
| Q187 | Physics - Electricity | D3 | PASS - V = I × R = 2 × 5 = 10 V |
| Q197 | Genetics and Reproduction | D3 | PASS - Haemophilia = sex-linked recessive |
| Q200 | Genetics and Reproduction | D3 | PASS - Cloning = genetically identical copies |

## Originality Report

- Within-batch exact duplicates: 0
- Within-batch semantic near-duplicates: 0
- Cross-batch exact duplicates (vs 5850 existing): 0
- Cross-batch semantic near-duplicates: 0
- Cross-batch ID overlap: 0
- (Subtopic, Archetype) reuse: 0
- Unique subtopics: 100/100
- Unique SA pairs: 100/100

## Integrity Report

- T3 BM B01-B05: ALL UNCHANGED
- T3 Math B01-B05: ALL UNCHANGED
- T3 English B01-B05: ALL UNCHANGED
- **T3 Science B01**: UNCHANGED (SHA b0e13212... matches)
- T2 banks: ALL UNCHANGED
- T1 banks: ALL UNCHANGED
- Primary banks: ALL UNCHANGED (including MiniApp Primary SK Y1 Science batch05)
- Reference DB: 594 files (unchanged)
- Android repo: clean

## T3 Science Cumulative Total

- T3 Science B01 = 100 / 100
- T3 Science B02 = 100 / 100
- **T3 Science = 200 / 500 (40%)**

## Pre-fix corrections applied:

| Q | Issue | Action |
|---|---|---|
| Q111 | Cross-batch dup "Which organelle controls activities" | Rewrote with DNA focus: "Which structure contains DNA?" |
| Q162 | Cross-batch dup "Light travels fastest in:" | Rewrote with numeric value: "What is the speed of light in vacuum?" |
| Q172 | Cross-batch dup "Difference between heat and temperature" | Rewrote with scenario: "Cup at 80°C vs 20°C" |
| Q189 | Cross-batch dup "Parallel circuit voltage same" | Rewrote with circuit scenario: "3 bulbs, 6V battery" |
