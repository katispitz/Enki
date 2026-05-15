# FINDINGS 010 — `polarity-define` cross-R-tier residency probe

**Build**: `probe_polarity_define.py` — structural comparison of `PairState` (cube-face pair) vs `InnerOctPairState` (inner-oct face pair).
**Status**: probe complete. Compute-shape MATCHES; substrate-semantics DIFFER. Council ratification required for canonical decision.

## What the probe found

### Compute-shape match: YES

Both pair-engines:
- Take 2 lower-level face-states as input
- Compose them via aggregation logic
- Emit polarity metrics: `polarity` (signed float -1..+1), `polarity_label` (categorical)
- Emit activation aggregates (variants of co_activation / sum_activation per engine)
- NULL-honest frozen state when both inputs frozen
- Symmetric-input requirement (both frozen OR both live)

Substrate-pattern: "compose 2 face-states + emit pair-level polarity-state" is replicated at both primitive-classes.

### Core polarity-fields overlap

| Core field | In cube-pair PairState | In inner-oct InnerOctPairState |
|---|---|---|
| `polarity` | ✓ | ✓ |
| `polarity_label` | ✓ | ✓ |
| `dominant_face` | ✗ (inferable from label) | ✓ (explicit) |

Cube-face PairState encodes dominant-side via `polarity_label` (`earth-dominant` / `water-dominant`) but doesn't expose a separate `dominant_face` field. Inner-oct exposes both. **Minor structural gap, not substantive semantic difference.**

Logged as **OQ-PAIRSTATE-FIELD-ALIGNMENT** (low-priority refactor — could add `dominant_face` to cube-pair PairState for cross-engine field consistency).

### Substrate-semantic distinction: YES

| Aspect | Cube-face pair | Inner-oct face pair |
|---|---|---|
| Lower-level face function | `planet-aspect-activate` (direct, 2 planets) | composition of 3 × `planet-aspect-activate` (3 planets) |
| What is polarized | Cosmogonic axes (Earth-Pluto vs Water-Neptune) | Archetype modes (SOURCE-vs-VOID, etc.) |
| Antipode-relationship | Hesiod-line cosmogonic antipodal | Octahedral vertex-complement antipodal |
| Planet coverage per pair | 4 of 8 cube-vertex planets | ALL 6 sign-rulership planets |

The COMPUTE is the same, but WHAT'S BEING POLARIZED differs substantively.

## Conflation-test analysis (Erato rule 4b)

Two interpretations available:

### Interpretation A: shell-agnostic META-FUNCTION

The function is "compose 2 face-states + emit polarity-state". This META-FUNCTION operates regardless of:
- Shell (R=1 cube-face vs R=1/√3 inner-oct face)
- Lower-level face computation (direct call vs composition-of-3)
- Substrate-semantic input (cosmogonic axes vs archetype modes)

Under interpretation A: `polarity-define` graduates to CANONICAL (compute-shape canonical, 2 independent primitive-class residencies). Different inputs flow through the same compute — same precedent as `planet-aspect-activate` (which graduated despite different planet-pair inputs at face-class vs midpt-class).

### Interpretation B: substrate-specific functions

The "polarity" of cosmogonic-axis-pair vs archetype-mode-pair is DIFFERENT substrate-meaning. Same compute serves different substrate-functions. Mnemosyne drift-prevention concern: card-readers seeing `function_class='polarity-define'` won't know which polarity is at play.

Under interpretation B: split into `cosmogonic-polarity-define` (cube-face pair) + `mode-polarity-define` (inner-oct face pair). Each gets its own residency status. Neither graduates to canonical until cross-R-tier residency confirmed for each separately.

### Precedent

The `planet-aspect-activate` council 2026-05-12 set the precedent: function-name names THE COMPUTE, not the substrate-input. "Pair" in `pair-aspect-activate` was rejected because it ambiguated primitive-pair-class vs planet-pair-input. "Polarity" might face similar ambiguity here (cosmogonic-polarity vs archetype-mode-polarity).

Athena's structural-lock criterion was: name THE FUNCTION, not the residency. Compute-shape canonical despite different inputs.

By precedent + Athena criterion, interpretation A wins. `polarity-define` is shell-agnostic META-FUNCTION that operates wherever 2 face-states need to be polarized.

But Mnemosyne's drift-prevention concern is also legitimate. Substrate-honest answer requires council.

## Conflation-test NEW candidate (third option)

Interpretation C surfaced during analysis: `polarity-define` is **a META-PRIMITIVE** — a higher-order function over substrate primitives. Like `planet-aspect-activate` operates on 2 planets, `polarity-define` operates on 2 substrate-states.

Under C: `polarity-define` graduates canonical because it's the **canonical composition pattern** for pairs of substrate-states. Different from `planet-aspect-activate` (a primitive) but at the same canonical-tier.

This frames a NEW substrate concept: **meta-primitives** (canonical compositions over substrate-primitives). If accepted, opens space for additional meta-primitives at higher cascade levels (trine-level, system-level aggregation patterns).

## Recommendation

**Convene council on `polarity-define` graduation.** Force-include Athena (structural-lock criterion) + Mnemosyne (substrate-honest disambiguation) per V2.6 rule 8.

Council question stack:
1. Is `polarity-define` ONE function (interpretation A) or DOES IT CONFLATE cosmogonic vs mode polarity (interpretation B)?
2. If A: graduate to CANONICAL at §30, second canonical entry. Erato gate 1/3 → 2/3.
3. If B: split into 2 candidate-single-residency names; neither graduates yet.
4. If C: open new substrate-class "meta-primitive" + ratify `polarity-define` as first meta-primitive entry.

Pre-stage residency-confirmation: ALREADY CONFIRMED (compute-shape match at 2 primitive-classes). Only naming-conflation question remains.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-POLARITY-DEFINE-CANONICAL | **READY FOR COUNCIL** | Cross-R-tier residency confirmed (compute-shape match). Conflation-test required. 2-residency Athena criterion structurally met. |
| OQ-PAIRSTATE-FIELD-ALIGNMENT | NEW (low-priority refactor) | Cube-pair PairState lacks `dominant_face` field (inner-oct pair has it). Field-gap aesthetic, not substantive. |
| OQ-META-PRIMITIVE-CLASS | NEW (substrate-concept) | Does substrate have a class of canonical compositions distinct from primitive-functions? If yes, `polarity-define` would be first meta-primitive entry. |
| OQ-CARRIER-PAIR-FUNCTION-NAME | OPEN (carried) | `swap-antipode-coactivate` candidate at cube-edge pair-class. |
| OQ-CARRIER-DIRECTION-FUNCTION-NAME | OPEN (carried) | `axis-direction-aggregate` candidate. |
| OQ-CASCADE-CARDINALITY-VARIES | OPEN (carried) | Cascade cardinality is primitive-type-specific. |
| OQ-3-VERTEX-FACE-CROSS-R-TIER | OPEN (carried) | `mode-bound` cross-R-tier. |
| OQ-PLUTO-NEPTUNE-PARTITION | SUBSTANTIATED (carried) | Canon §M.5b candidate. |
| OQ-ANTIPODE-ASYMMETRY | OPEN (carried) | Erebus-Nyx uniqueness. |
| OQ-AXISSTATE-FIELD-RENAME | OPEN (carried) | Substrate-position-agnostic field names. |
| OQ-BRIDGE-ENGINE-DEDUP | OPEN (carried) | `_bridge_engine` redundancy. |
| OQ-CARRIER-REGISTRY-FULL-BUILD | OPEN (blocked carried) | T1.3 + OQ-RADII-01 dependencies. |

## What this validates substrate-discipline-wise

1. **Cross-R-tier residency probe is REUSABLE template** — same pattern as `planet-aspect-activate` probe (FINDINGS_005): build engines at 2 primitive-classes, field-compare, surface conflation-test for council.

2. **Substrate-cascade composition reveals META-PRIMITIVES** — building pair-engines at 2 different shells exposes a higher-order canonical pattern that wasn't visible at single-shell substrate.

3. **Substrate-honest disagreement preserved** — probe doesn't pre-decide; it surfaces evidence + flags the council decision. Council operates with cross-check selection-discipline (V2.6 rule 8).

## What to build next (substrate-emergent)

Options:

1. **Convene `polarity-define` graduation council** — advances §30 canonical count toward Erato gate (1/3 → potentially 2/3).

2. **Operator (PE planet, cube-vertex) prototype** — tests pure-fn shape, distinct from engine-class.

3. **Inner-oct edge cascade** — 12 inner-oct edges at R=1/√3 (canon §11). Different edge-primitive than cube-edge.

4. **Inner-oct partition engine** — completes inner-oct cascade (apex-pair vs lateral-pair-set partition at R=1/√3, cardinality 2).

5. **Refactor `_axis_engine` field-rename + bridge dedup** — substrate-cleanliness moves.

Recommend (1) — most aligned with Erato gate progress. After (1), substrate has either 2/3 canonical entries (if council ratifies) or refined understanding of conflation boundaries (if council splits).
