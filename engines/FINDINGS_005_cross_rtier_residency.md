# FINDINGS 005 — Cross-R-tier residency probe (R=1 cube-face × R=φ icosidodec-midpt)

**Build**: 3 V2.5-locked bridge engines + shared bridge shape + bridges registry + field-by-field shape comparison.
**Status**: green. Cross-R-tier function-shape MATCH confirmed structurally.

## What was built

```
~/Enki/engines/
├── _bridge_engine.py           ← shared bridge shape (R=φ icosidodec-midpt)
├── bridge_harmonia.py          ← Venus × Mars midpoint (V2 ↔ V7)
├── bridge_hermaphroditus.py    ← Mercury × Venus midpoint (V3 ↔ V2)
├── bridge_erichthonius.py      ← Saturn × Uranus midpoint (V4 ↔ V8)
└── bridges.py                  ← registry
```

3 bridges = the 3 V2.5-locked icosidodec-midpoint compound bridges per Nammu canon §M.5 (cards 52ad9413 / 91697158 / 3de9d703). Persephone (also a bridge per V2.5) is NOT a midpoint-compound; she's seasonal-bridge anchored at Pluto. Excluded from this probe.

## Field-by-field shape comparison (programmatic)

```
AxisState  (Primordial face): 13 fields
BridgeState (icosidodec-midpt):14 fields

Shared (9 — 100% of live-state fields):
  activation_strength, active_aspects, angular_separation,
  closest_aspect_deg, closest_orb, midpoint_lon,
  pa_lon, pb_lon, substrate_card

Axis-only (4 — substrate-locks specific to Primordial):
  primordial, cube_face, zodiac_anchor, planet_pair

Bridge-only (5 — substrate-locks specific to Bridge):
  bridge_name, icosidodec_anchor, parent_vertices, parent_planet_pair, shell
```

**100% of live-state (computed) fields match.** Differences are substrate-position labels (which shell, which position-anchor) — they identify WHERE the engine sits, not WHAT it computes.

## What the substrate confirmed

Building the bridge engines exposed that the SAME function-shape operates at two distinct R-tier shells:

| Primitive class | Shell | Cardinality | Position-anchor | Planet-pair source |
|---|---|---|---|---|
| Primordial face | R=1 | 6 | cube-face MQFn | cosmogonic axis-pair |
| Bridge midpoint | R=φ | 3 | icosidodec edge midpt | Olympian parent-vertex pair |

These are **two independent primitive-class residencies** of the same function. Substrate-honest: the function computes "planet-pair angular separation → aspect detection within orb → activation strength" given any substrate-anchored position. Whether the position is a cube-face (Primordial) or an icosidodec-midpoint (Bridge), the FUNCTION is the same — only the geometric anchor differs.

This is precisely what Athena lock-by-redundancy criterion requires (V2.6 placement_rules §POSITION-AS-FUNCTION DISCIPLINE rule 4):

> A function-name graduates from candidate to canonical when at least two independent primitive-class residencies confirm the same function.

Cube-face primitive class ≠ icosidodec-midpoint primitive class (different shells, different position-types, different cardinalities). Two independent confirmations. **Criterion structurally met.**

## What this does NOT yet resolve

**Conflation-test still pending** (Erato process-learning rule 4b: conflation-test BEFORE residency-test).

The face-level function is still in 3-way candidate ambiguity (FINDINGS_003):
- `axis-bound` (constraint flavor — original)
- `axis-generate` (engine flavor — Kati correction)
- `axis-arm-emit` (per-arm-of-pair flavor — emerged from FINDINGS_003 pair analysis)

Now that bridge-residency confirms function-shape recurs, a fourth candidate is forced into consideration:
- **`midpt-pair-activate`** or **`pair-aspect-activate`** — describes what the function actually COMPUTES regardless of geometric anchor. Both Primordials and Bridges produce activation from planet-pair angular separation; "axis" framing was R=1-specific. The shared function is closer to "planet-pair aspect activation" than to anything axis-flavored.

4-way conflation-test now required. Per Erato rule 4b, council MUST split-test before any name graduates. Athena residency-criterion is staged (pre-confirmed); naming is the only blocker.

## Substrate finding 10: function-name framing was R=1-anchored, not function-shape-anchored

The original candidates (`axis-bound` / `axis-generate` / `axis-arm-emit`) all use "axis" because the original primitive class was R=1 cube-face → cosmogonic axes. When the function-shape replicates at R=φ icosidodec-midpt, the bridges don't generate "axes" in any cosmogonic sense — they generate midpoint-resonance between two Olympian planetary seats.

Naming should be:
- **Shell-specific**: at R=1, the function generates an axis-arm; at R=φ, it generates a midpoint-resonance. Same function, different shell-meaning. Two function-NAMES per shell.
- **Shell-agnostic**: the function is `planet-pair-aspect-activate` regardless of shell. One function-NAME, recognized as operating at multiple positions.

V2.6 rule 1 (position-as-function-lock) supports shell-agnostic naming — position implies SPECIFIC behavior at that R-tier, but the underlying function is the substrate-emergent computation. Shell-anchored interpretation is downstream.

Recommend shell-agnostic name. Logged as **OQ-FUNCTION-NAME-FRAMING** (shell-specific vs shell-agnostic naming).

## Substrate finding 11: bridges = engines, NOT translators

Earlier agent-typology (V2.6 carried forward) had bridges as "translators" with shape "engine OR subagent — pending per-class council." This probe answers that pending question:

**Bridges are engines.** Same shape as Primordials. They COMPUTE midpoint-activation from parent-vertex planet-pair, return structured state, are stateful (substrate-locked + ephemeris-driven), are deterministic, do not deliberate. Engine class confirmed by build, not council.

The agent-typology table updates:

| Class | Shell | Stratum | Agent shape |
|---|---|---|---|
| Bound-Holder (Primordial) | R=1 cube-face | 6 Primordials | engine (was: confirmed) |
| **Translator (Bridge)** | **R=φ icosidodec-midpt** | **3 V2.5 bridges** | **engine (newly confirmed)** |
| Carrier (Titan) | R=1 cube-edge | 12 Titans | engine OR pure-fn — pending |
| Operator (PE planet) | R=1 cube-vertex | 8 PE planets | pure-fn — pending |
| Threshold-Marker | R=1/3 X3/X6 | shock-residents | hook — pending |
| Council Voice | R=φ² ico-vertex | 12 Olympians | subagent — confirmed (Nammu) |
| Activator (Muse) | activation pattern | 9 Muses | hook — pending |

3 of 7 strata now have engine-shape confirmed (Primordials, Bridges, and possibly Carriers).

## Substrate finding 12: substrate-locks are 2-layer, not 1-layer

Both engine types have:
- **Layer A** (geometric): name + shell + position-anchor type
- **Layer B** (planet): planet-pair + zodiac/parent context + substrate card

These two layers are orthogonal. Layer A says "where in the substrate." Layer B says "which planetary inputs at that position." The compute fields (9 shared) are the same regardless of A/B specifics.

This means the engine shape can probably generalize even further — a fully-parameterized engine taking (name, shell, position-type, planet-pair, card) inputs could in principle handle ANY engine-class substrate residency. We don't NEED separate Primordial vs Bridge classes if they share function-shape. The current split is partly aesthetic (named modules per residency) and partly substrate-explicit (each Primordial/Bridge has its own canon-locked identity).

Logged as **OQ-ENGINE-GENERALIZATION** — do we need named-per-residency files, or can one engine handle all residencies via lookup?

Substrate-discipline favors **named-per-residency** because each lock is a council-ratified canonical position. Folding them into a lookup table loses explicit-position visibility in code. Keep current factoring.

## Updated open-question queue

| OQ | Status | Notes |
|---|---|---|
| OQ-CROSS-R-TIER-RESIDENCY | **PARTIALLY RESOLVED** | Function-shape match confirmed (Primordial face × Bridge midpt). Conflation-test still required to settle which canonical NAME graduates. |
| OQ-AXIS-BOUND-NAME-CHECK | **4-WAY** | Now `axis-bound` / `axis-generate` / `axis-arm-emit` / `midpt-pair-activate` (or `pair-aspect-activate`). Council required. |
| OQ-FUNCTION-NAME-FRAMING | NEW | Shell-specific vs shell-agnostic function naming. Affects whether one name covers both shells or different names per shell. |
| OQ-ENGINE-GENERALIZATION | NEW | Do we need named-per-residency engine files, or one parameterized engine? Substrate-discipline favors named. |
| OQ-CASCADE-PATTERN-AT-OTHER-RTIERS | OPEN | Carried — does face→pair→trine→system cascade emerge at other R-tiers? Bridges at R=φ have cardinality 3 — too few for full cascade. Inner-oct (R=1/√3, 8 faces) is better test target. |
| OQ-FACE-AS-POSITION-VS-FUNCTION | OPEN | Carried. Probably resolves with shell-agnostic naming. |
| OQ-PLUTO-NEPTUNE-PARTITION | SUBSTANTIATED | Carried — canon-extension candidate. |
| OQ-ANTIPODE-ASYMMETRY | OPEN | Carried — Erebus-Nyx unique zodiac-180°-coincidence. |
| OQ-ENGINE-CLASS-IN-AGENT-TYPOLOGY | OPEN | Carried. |

## What this unblocks downstream

Once conflation-test resolves the function-name (4-way council needed), the chosen name graduates to **canonical** in canon §30 — first canonical entry. Then:

1. **Audit-pass backfill** unblocks when §30 has ≥3 canonical entries (Erato gate). Need 2 more canonical-graduations after this one.
2. **Agent-typology by class-prefix** (currently blocked on §30 ≥3 entries) becomes possible.
3. Future cross-R-tier probes can use this one as template.

Two more cross-R-tier probes that might unlock additional graduations:
- Inner-oct face residency probe (R=1/√3 inner-oct-faces × R=φ² ico-faces? × something else?)
- Carrier (Titan) cross-R-tier (R=1 cube-edge × R=φ² ico-edge?)

## What to build next (substrate-emergent)

Per Kati directive (substrate build-out before functionality), continued substrate-side. Highest-value moves:

1. **Cascade-pattern probe at R=1/√3** (inner-oct, 8 F1-F8 archetype faces). Tests OQ-CASCADE-PATTERN-AT-OTHER-RTIERS. Inner-oct has 8 faces, 12 edges, 6 vertices — different cardinality structure than cube. Will the cascade-shape recur or be substrate-specific?
2. **Carrier (Titan) prototype** at R=1 cube-edge. Tests whether engine-shape generalizes across primitive-type (edge vs face vs midpoint). 12 Titans = 12 cube edges; engine probably emits edge-resonance from incident vertex-planet pairs.
3. **Persephone bridge** — the 4th bridge, NOT midpoint-compound. Different bridge shape. Tests whether ALL bridges are engines or whether seasonal-bridges have different shape.
4. **Council on conflation-test for face-level function-name** — settle the 4-way naming. Once settled, function graduates to canonical, §30 progresses, agent-typology refactor unblocks.

Recommend (4) — council on conflation. It's the move that converts staged residency into canonical promotion. Without it, all 4 candidates remain candidate-single-residency-CLASS (each at one cardinality, plus cross-R-tier confirmation pending name-resolution).

If staying purely substrate-build (no councils right now), (1) or (2) next.
