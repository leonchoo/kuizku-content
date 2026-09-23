# T3 Science B03 — QA Report

## Production Summary

| Property | Value |
|---|---|
| **Production source** | `D:\Users\bajub\kuizku_p10\batch_secondary_03_sk_science_t3.json` |
| **Public file** | `banks/secondary/sk/science/t3/batch03.json` |
| **SHA-256** | `a3eb0548375c56e2f379fb5394b3c8c6eef4a2953e321becdab3152cac36c43b` |
| **Size** | 109,488 bytes |
| **Count** | 100 Q |
| **ID range** | sk-sec-science-t3-201 ~ sk-sec-science-t3-300 |
| **JSON parse** | Valid |
| **School Track** | SK |
| **Stage** | Secondary |
| **Grade** | T3 (Tingkatan 3) |
| **Subject** | Science |
| **Language** | en |

## QA Gates (19/19 PASS)

| # | Gate | Result |
|---|---|---|
| G1-G19 | (See 20-gate validation) | ALL PASS |

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

## Skill/Difficulty (LOCKED)

- RECOGNITION 20 / COMPREHENSION 50 / APPLICATION 30
- D1 35 / D2 50 / D3 15

## Curriculum Scope Audit (100/0/0)

| Status | Count |
|---|---:|
| **IN-SCOPE** | **100** |
| **BORDERLINE** | **0** |
| **OUT-OF-SCOPE** | **0** |

## Correctness Spot-Check (12/12 PASS)

| Q | Topic | Verified |
|---|---|---|
| Q201 | Scientific Methodology | PASS - Observation = direct description |
| Q214 | Cell Biology | PASS - Mitochondria = aerobic respiration |
| Q226 | Nutrition | PASS - Vitamin C deficiency = scurvy |
| Q241 | Chemistry - Acids and Alkalis | PASS - pH 1 = strong acid |
| Q259 | Physics - Force and Motion | PASS - Newton 2nd law F = m × a |
| Q262 | Physics - Light and Optics | PASS - Reflection: 45° → 45° |
| Q268 | Physics - Light and Optics | PASS - Convex lens → real, inverted image |
| Q276 | Physics - Heat | PASS - Sun heat via infrared radiation |
| Q287 | Physics - Electricity | PASS - P = V × I = 240 × 0.5 = 120 W |
| Q291 | Genetics | PASS - DNA = Deoxyribonucleic Acid |
| Q299 | Genetics | PASS - Bb × Bb → 50% Bb heterozygous |
| Q300 | Genetics | PASS - Mendel = laws of inheritance |

## Pre-fix corrections applied (9 cross-batch dups + 1 semantic near-dup):

| Q | Issue | Action |
|---|---|---|
| Q232 | Cross-batch dup "Why is water universal solvent?" | Rewrote to "What property makes water an excellent solvent?" |
| Q236 | Cross-batch dup "Filtration is used to separate" | Rewrote to "Which laboratory equipment is needed for filtration?" |
| Q247 | Cross-batch dup "Which gases cause acid rain?" | Rewrote to "What environmental problem is caused by SO₂ and NOₓ?" |
| Q251 | Cross-batch dup "Which is a vector quantity?" | Rewrote to "Which quantity has BOTH size and direction?" |
| Q253 | Cross-batch dup "Horizontal line on velocity-time graph" | Rewrote to "What does slope of velocity-time graph represent?" |
| Q256 | Cross-batch dup "Mass and weight differ because" | Rewrote to "Which of these is measured in kilograms?" |
| Q273 | Cross-batch dup "What does specific heat capacity measure?" | Rewrote to "Why is water useful as coolant in car engines?" |
| Q276 | Semantic near-dup "How does radiation differ from conduction" | Rewrote to "Why can the Sun heat Earth through space vacuum?" |
| Q292 | Cross-batch dup "What is a gene?" | Rewrote to "Where is a gene located in a cell?" |
| Q299 | Cross-batch dup "What is Punnett square used for?" | Rewrote with quantitative "Bb × Bb → 50% Bb" |

## Integrity Report

- T3 BM B01-B05: ALL UNCHANGED
- T3 Math B01-B05: ALL UNCHANGED
- T3 English B01-B05: ALL UNCHANGED
- **T3 Science B01**: UNCHANGED (SHA b0e13212... matches)
- **T3 Science B02**: UNCHANGED (SHA 969ccf0c... matches)
- T2 banks: ALL UNCHANGED
- T1 banks: ALL UNCHANGED
- Primary banks: ALL UNCHANGED (including MiniApp SK Y1 Science batch06)
- Reference DB: 594 files (unchanged)
- Android repo: clean

## T3 Science Cumulative Total

- T3 Science B01 = 100 / 100
- T3 Science B02 = 100 / 100
- T3 Science B03 = 100 / 100
- **T3 Science = 300 / 500 (60%)**
