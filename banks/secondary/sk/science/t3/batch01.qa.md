# T3 Science B01 — QA Report

## Production Summary

| Property | Value |
|---|---|
| **Production source** | `D:\Users\bajub\kuizku_p10\batch_secondary_01_sk_science_t3.json` |
| **Public file** | `banks/secondary/sk/science/t3/batch01.json` |
| **SHA-256** | `b0e13212174cfc889ae707e319381016f85fb10eae07421f8d35c973e42a6763` |
| **Size** | 108,336 bytes |
| **Count** | 100 Q |
| **ID range** | sk-sec-science-t3-001 ~ sk-sec-science-t3-100 |
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
| G2 | IDs 001-100 contiguous | PASS |
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
| G17 | B01 unique SA = 100 | PASS |
| G17b | B01 unique subtopics = 100 | PASS |
| G17c | ID overlap = 0 | PASS |

## Topic Distribution

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

## Skill Distribution

| Skill | Count |
|---|---:|
| RECOGNITION | 20 |
| COMPREHENSION | 50 |
| APPLICATION | 30 |
| **TOTAL** | **100** |

## Difficulty Distribution

| Difficulty | Count |
|---|---:|
| D1 (Easy) | 35 |
| D2 (Medium) | 50 |
| D3 (Hard) | 15 |
| **TOTAL** | **100** |

## Curriculum Scope Audit

| Status | Count |
|---|---:|
| **IN-SCOPE** | **100** |
| **BORDERLINE** | **0** |
| **OUT-OF-SCOPE** | **0** |

**100 / 0 / 0 achieved** ✅

## Correctness Spot-Check (12/12 PASS)

| Q | Topic | Difficulty | Verified |
|---|---|---|---|
| Q001 | Scientific Methodology | D1 | PASS - controlled variable identification |
| Q013 | Cell Biology | D1 | PASS - plant cell turgor pressure |
| Q024 | Nutrition | D1 | PASS - vitamin C deficiency = scurvy |
| Q041 | Chemistry - Acids and Alkalis | D2 | PASS - pH 7 = neutral |
| Q050 | Chemistry - Acids and Alkalis | D2 | PASS - strong vs weak acid ionisation |
| Q051 | Physics - Force and Motion | D2 | PASS - speed = 50 km/h (100/2) |
| Q061 | Physics - Light and Optics | D2 | PASS - light travels straight lines |
| Q072 | Physics - Heat | D2 | PASS - specific heat capacity definition |
| Q084 | Physics - Electricity | D2 | PASS - series circuit same current |
| Q091 | Genetics and Reproduction | D3 | PASS - DNA double helix |
| Q099 | Genetics and Reproduction | D3 | PASS - eye colour = inherited variation |
| Q100 | Genetics and Reproduction | D3 | PASS - GM = changing DNA to give new traits |

## Originality Report

- Within-batch exact duplicates: 0
- Within-batch semantic near-duplicates: 0
- Cross-batch exact duplicates (vs 5750 existing): 0
- Cross-batch semantic near-duplicates: 0
- Cross-batch ID overlap: 0
- (Subtopic, Archetype) reuse: 0
- Unique subtopics: 100/100
- Unique SA pairs: 100/100

## Integrity Report

- T3 BM B01-B05: ALL UNCHANGED
- T3 Math B01-B05: ALL UNCHANGED
- T3 English B01-B05: ALL UNCHANGED
- T2 banks: ALL UNCHANGED
- T1 banks: ALL UNCHANGED
- Primary banks: ALL UNCHANGED
- Reference DB: 594 files (unchanged)
- Android repo: clean
- MiniApp files: ALL UNCHANGED

## T3 Science Cumulative Total

- T3 Science B01 = 100 / 100
- **T3 Science = 100 / 500 (20%)**

## Scope Definition Locked (for B02-B05)

**Topics (10 total)**: Scientific Methodology, Cell Biology, Nutrition, Chemistry - Water and Solutions, Chemistry - Acids and Alkalis, Physics - Force and Motion, Physics - Light and Optics, Physics - Heat, Physics - Electricity, Genetics and Reproduction.

**Skill**: RECOGNITION 20 / COMPREHENSION 50 / APPLICATION 30.

**Difficulty**: D1 35 / D2 50 / D3 15.

**Avoid**: T4/T5 advanced (organic chemistry, nuclear physics, EM induction, advanced genetics/CRISPR).

**Subtopic/Archetype**: Must be unique within T3 Science 500 Q pool.
