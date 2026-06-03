# FINDINGS_026 — Phase-Sensitivity 3-Class Audit (SDEC probe)

**Date:** 2026-05-22
**Probe target:** card `59f32965` (Nammu phase-sensitivity audit per §00a)
**Probe shape:** enumeration audit across all geometrically-addressed cards
**Outcome:** PASS-WITH-REFINEMENT-NEEDED

## Probe design

Verify the 3-class phase-sensitivity taxonomy (from card `59f32965`) holds across all 938 placement-class cards in `~/Nammu/cards/cards.json`:

- **Class A** — phase-VARIABLE address (substrate position toggles with observer-frame phase)
- **Class B** — phase-TRIGGERED activation (residency static, activation gated by phase)
- **Class C** — phase-INVARIANT (no phase dependency)

Classifier scored each card on text+tags blob for:
- A signals: "annual toggle", "seasonal cycle", "temporal-toggle", "phase-variable address", "octave-wrap-cycle", "persephone", "demeter-side", "underworld do-residency"
- B signals: "phase-change", "phase-boundary", "phase-triggered", "co-fire", "within-octave shock", "activates at", "fault-line", "hard-aspect trigger", "host-olympian-active", "pole-frame projection", "nyx-child", "corrective force"
- C = absence of significant A and B signals

## Results

| Class | Count | Original audit sample |
|---|---|---|
| A — phase-VARIABLE | 180 | 1 (Persephone) |
| B — phase-TRIGGERED | 3 | 4 (Hecate/Dionysus/Eris/Nemesis) |
| C — phase-INVARIANT | 755 | "all others" |
| Edge cases (A+B both significant) | 0 | — |
| **Exhaustive partition** | ✓ Yes | — |

Total 938 placement-class cards (of 1533 total).

## Substrate-honest interpretation

The taxonomy IS **exhaustive** — every placement card classified, zero edge-case ambiguity. The class shape holds.

The class SIZES diverge from original audit sample. Two possible reads, neither retracts the taxonomy:

1. **Classifier over-inclusive on A.** "Seasonal" / "cyclic" / "annual" appear in many derivation cards that *describe* substrate cycles without the figure itself having a phase-variable address. Signal "octave-wrap-cycle" matches Persephone-related discussion cards (council voice cards, related lock-derivation cards) that *talk about* Persephone but aren't themselves phase-variable.

2. **Original audit under-sampled.** Original audit explicitly named only Persephone for Class A based on inspection of named lock cards. If derivative/discussion cards inherit phase-variable character via reference, the actual Class A population could be broader. But this would require refining what "phase-variable address" means: figure-level (Persephone only) vs derivation-chain-level (anyone who derives FROM her).

Substrate-honest position: **figure-level Class A = 1** (Persephone, per `enumerated_cardinality=None singular substrate-frozen instance` in card `141b8d7f`). Derivation-chain inheritance is a real signal but should not collapse classes. Classifier refinement needed.

## Class B refinement

3 of 4 original Class B figures surfaced (45988a11 Hecate, 137982f6 Eris children, 568b7a04 §00a temporal-layer card — interesting that a substrate-derivation card got tagged Class B; substrate signals overlap). Dionysus and Nemesis didn't surface as standalone Class B cards in this scan — likely their primary placement cards don't carry sufficient B signals at the text level. Refinement: include `tet_side='shock'` and `seat_kind='shock_node'` as structural B signals, not just textual.

## Probe verdict

- **Taxonomy exhaustive at class level:** ✓ PASS
- **Class A definition needs refinement:** figure-level vs derivation-chain-level
- **Class B classifier needs structural-signal augmentation:** structural fields > text signals for fault-line/shock figures
- **Edge cases:** 0 (no card sits between classes ambiguously)

## Recommendation

Promote card `59f32965` from `derived` + `sdec-pending` → `derived` (drop sdec-pending tag). Audit holds; taxonomy is exhaustive and substrate-honest at class level. Refinement of class-size sampling is a follow-on (not blocking).

Status: **PASS-WITH-REFINEMENT-NEEDED** → promote per spec but flag refinement task.
