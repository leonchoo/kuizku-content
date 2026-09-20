# KuizKu Primary Coverage Matrix

> **READ-ONLY inventory. Built from Phase 10.4 Plan A + existing banks.**
> **Date**: 2026-09-20 (Phase 10.5 pre-batch prep)
> **Plan**: A (Conservative) — 25 Q per (Track × Grade × Language) for non-STEM, 30 Q for Math/Science
> **Total**: 72 combinations, 1,830 Q target

## Legend
- ✅ DONE = full batch generated, ORIGINAL
- 🟡 PARTIAL = existing content from V3/V4-TEST/pilot (legacy)
- ⬜ EMPTY = no content yet
- 🔒 BLOCKED = awaiting external source (Reference DB gap)
- 🚫 SKIP = combination intentionally not in scope

---

## SK — Sekolah Kebangsaan (KSSR, BM-medium)

| Grade | BM | English | Math | Science |
| --- | --- | --- | --- | --- |
| **Y1 (Tahun1)** | ✅ Batch01 (25 Q, ORIGINAL) + 🟡 Phase 10.1 pilot (30 BM) | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y2 (Tahun2)** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y3 (Tahun3)** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y4 (Tahun4)** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y5 (Tahun5)** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y6 (Tahun6)** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |

**SK Y1 BM has highest priority for next batch** — already 1 full batch done, builds confidence on the pipeline.

---

## SJKC — Sekolah Jenis Kebangsaan Cina (KSSR_SJKC, Chinese-medium)

| Grade | 中文 (BC) | Bahasa Melayu (BM) | English | Math | Science |
| --- | --- | --- | --- | --- | --- |
| **Y1** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y2** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y3** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y4** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y5** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y6** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |

**BLOCKED** — Reference DB has NO primary Chinese coverage; Math/Science in Chinese-medium also absent. Per 638 §5, **next batch should NOT be SJKC without external syllabus docs**.

---

## International — Cambridge Primary (CAMBRIDGE_PRIMARY, English-medium native)

| Grade | English (native) | Math | Science |
| --- | --- | --- | --- |
| **Y1** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y2** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y3** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y4** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y5** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |
| **Y6** | ⬜ EMPTY | ⬜ EMPTY | ⬜ EMPTY |

**BLOCKED** — Reference DB has Malaysian MFL English (UASA/UPSA style), NOT Cambridge Primary native. All English-native/Math/Science need pure ORIGINAL.

---

## Existing banks inventory (not to be regenerated)

| Source | Location | Total Q | Notes |
|---|---|---:|---|
| V3 production | `/v3/` | 30 | Legacy, NOT KuizKu ORIGINAL schema |
| V4-TEST pilot | `/v4-test/` | 92 | Legacy, schemaVersion 3 |
| Phase 10.1 pilot | local `tahun_1_pilot.json` | 100 | Pre-multi-track, BM+Math+Science+English Y1 mix |
| **Phase 10.5 Batch01 SK BM Y1** | `batch01_sk_bm_y1.json` | **25** | **KuizKu ORIGINAL, current schema** ✅ |

**Net new ORIGINAL content needed for Plan A**:
- Plan A total: 1,830 Q
- Already covered (this round): 25 Q (Phase 10.5 Batch01)
- Remaining: 1,805 Q

## Next-batch decision criteria (per 638 §)
1. ✅ Don't repeat completed batches
2. ✅ Build SK Primary base coverage first (low risk, validates pipeline)
3. ✅ Don't mass-repeat same subject
4. ✅ Consider Reference DB coverage
5. ✅ Maintain Track × Subject × Grade matrix

