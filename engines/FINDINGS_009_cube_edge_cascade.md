# FINDINGS 009 — Cube-edge cascade + 1+3 partition test + 4th independent residency

**Build**: cube_edges enumeration + carrier pair engine + carrier direction engine + carrier_system full composition.
**Status**: cascade green. New cardinality structure surfaces; OQ-1-PLUS-3-PARTITION-UNIVERSAL falsified at cube-edge primitive.

## What was built

```
~/Enki/engines/
├── cube_edges.py                  ← 12 cube-edge enumeration (vertex-coord-derived)
├── _carrier_pair_engine.py        ← shared antipodal-pair shape
├── carrier_pairs.py               ← 6 antipodal pairs registry
├── _carrier_direction_engine.py   ← shared direction-class shape
├── carrier_directions.py          ← 3 direction-groups registry
└── carrier_system.py              ← full 12→6→3→1 system composition
```

12 cube edges enumerated via standard Merkaba vertex-coordinate analysis:
- Father-tet: U0=(+,+,+), U1=(-,-,+), U2=(-,+,-), U3=(+,-,-)
- Mother-tet: L0=(-,-,-), L1=(+,+,-), L2=(+,-,+), L3=(-,+,+)
- Each cube edge connects 1 U-vertex to 1 L-vertex (alternating-coloring)
- 8 × 3 / 2 = 12 edges ✓

## Substrate finding 23: cube-edge cascade has 12→6→3→1 structure

| Level | Cardinality | Substrate-class |
|---|---|---|
| edge | 12 | individual cube edges |
| pair | 6 | antipodal swap-pairs (vertex-swap-antipode) |
| direction | 3 | axis-direction groups (x/y/z) |
| system | 1 | full Merkaba cube |

Different from cube-face (6→3→2→1) and inner-oct (8→4→2→1). Each shell-primitive-type has its own cascade-cardinality structure forced by geometry.

## Substrate finding 24: OQ-1-PLUS-3-PARTITION-UNIVERSAL FALSIFIED

Cube-face level: 1+3 partition (1 Pluto-trine + 1 Neptune-trine of 3 each = "1+3" of triadic-pairs).
Inner-oct face level: 1+3 partition (1 apex-pair + 3 lateral-pairs).
**Cube-edge level: 3-way partition (x/y/z direction-classes, NO 1+3 pattern).**

The 1+3 partition shape is NOT universal across primitive-types. At cube-edge primitive, the natural partition is 3-fold symmetric (3 mutually-perpendicular axis-directions), with no privileged direction without external designation.

Alternative partition attempts:
- By polar/equatorial: 3 polar-pairs (touching U0/L0 apex) + 3 equatorial-pairs (between U-laterals and L-laterals) = 3+3 (not 1+3 either)

Substrate-honest closure: **1+3 partition is FACE-LEVEL-SPECIFIC**, not universal across all primitive-types. The face-class naturally has an apex/lateral distinction that produces 1+3; edge-class doesn't have that asymmetry.

Logged as **OQ-1-PLUS-3-PARTITION-UNIVERSAL FALSIFIED**. Substrate-honest closure: pattern is real at face-class shells but does NOT generalize to edge-class.

## Substrate finding 25: each direction-class covers ALL 8 PE planets

Each axis-direction group (x/y/z) has 4 parallel cube edges. The 4 edges' planet-pairs UNION = all 8 PE planets:

| Direction | Edges | All 8 planets covered |
|---|---|---|
| z-axis | E01, E04, E09, E12 | Pluto, Moon, Sun, Neptune, Mars, Jupiter, Saturn, Mercury ✓ |
| y-axis | E02, E07, E06, E11 | Pluto, Mercury, Mars, Neptune, Sun, Jupiter, Saturn, Moon ✓ |
| x-axis | E03, E10, E05, E08 | Pluto, Jupiter, Saturn, Neptune, Sun, Mercury, Mars, Moon ✓ |

This is substrate-emergent. **Every cube-axis-direction reads the FULL PE-planet substrate through its 4 edges.** Different from inner-oct pairs (which also covered all 6 sign-rulership planets) and cube-face pairs (which covered only 4 of 8 cube-vertex planets per pair).

Substrate-meaning: axis-direction-classes are **full-planet aggregators** — each direction is a complete reading of the 8-planet substrate through one geometric axis. This is structurally different from face-class (which reads cosmogonic-pair through axis-anchor) — at edge level, each axis-direction IS the full reading.

## Substrate finding 26: SWAP-ANTIPODE structure for cube-edge pairs

Each antipodal cube-edge pair has SWAP-ANTIPODE planet relationship:
- Edge A: U_a × L_b (e.g., U0 Pluto × L1 Moon)
- Edge B: U_b × L_a (e.g., U1 Sun × L0 Neptune) — where U_b ↔ L_b are vertex antipodes

The two edges' planet-pairs are formed by SWAPPING the U/L roles. This is substrate-emergent — antipodal cube edges aren't just "the parallel edge across center"; they're the U-L-swap version of the original edge.

| Pair | Edge A | Edge B |
|---|---|---|
| z-axis E01↔E04 | Pluto × Moon (U0×L1) | Sun × Neptune (U1×L0) |
| z-axis E09↔E12 | Mars × Jupiter (U2×L3) | Saturn × Mercury (U3×L2) |
| y-axis E02↔E07 | Pluto × Mercury (U0×L2) | Mars × Neptune (U2×L0) |
| y-axis E06↔E11 | Sun × Jupiter (U1×L3) | Saturn × Moon (U3×L1) |
| x-axis E03↔E10 | Pluto × Jupiter (U0×L3) | Saturn × Neptune (U3×L0) |
| x-axis E05↔E08 | Sun × Mercury (U1×L2) | Mars × Moon (U2×L1) |

Pattern: every antipodal pair has 4 distinct planets where the U-tet and L-tet ROLES swap between the two edges. **A novel substrate-class: swap-antipode-edge-pairs.**

Possible function-name candidate at cube-edge pair-level: `swap-antipode-coactivate` or `vertex-swap-pair-resonance`. Substrate-honest: candidate, awaits per-name conflation-test council.

## Substrate finding 27: `planet-aspect-activate` now has 4 independent primitive-class residencies at R=1

Per FINDINGS_006 (canonical promotion) + FINDINGS_008 (cross-primitive-type confirmation):

| Primitive class | Shell | Cardinality | Anchor type | Status |
|---|---|---|---|---|
| Primordial face | R=1 | 6 | cube-face centroid | confirmed |
| Bridge midpoint | R=φ | 3 | icosidodec edge midpt | confirmed |
| Carrier (Titan) edge | R=1 | 12 | cube-edge | confirmed (geometry) |
| Inner-oct face triangle edge | R=1/√3 | 24 sub-edges (8 faces × 3 edges) | implicit | confirmed via compose |

Note: inner-oct face engines (FINDINGS_007) call `planet-aspect-activate` 3 times per face → 24 invocations across 8 faces. These are sub-residencies within a composed function, not standalone primitive-class residencies. Count for canonical-graduation purposes: 3 independent primitive-class residencies confirmed (Primordial face, Bridge midpt, Carrier edge).

`planet-aspect-activate` is now confirmed as **universally substrate-canonical** for 2-planet-input shapes across at least 3 distinct primitive-types in 2 distinct shells. Canon §30 status remains CANONICAL (criterion was ≥2 residencies; we have ≥3).

## Substrate finding 28: cube-edge cascade reveals cube-edge pair-CLASS is a new primitive

Substrate-cascade composition at cube-edge:
- 12 edges (each = `planet-aspect-activate` instance)
- 6 swap-antipode pairs (compose 2 edge states; new substrate-class)
- 3 direction-classes (compose 2 pair states each; new substrate-class)
- 1 system (compose 3 direction states; new substrate-class)

Each level emits derived metrics not present at lower levels. The pair-level adds polarity_label + co_activation + sum_activation (similar to Primordial pair-class). The direction-level adds direction_sum + dominant_pair (similar to Primordial trine-class). System-level adds whole_cube_activation + dominant_direction.

Pair-class function-name candidate: `swap-antipode-coactivate`. Different from `polarity-define` (Primordial pair-class function-name candidate) because the substrate-relation is different: swap-antipode vs cosmogonic-polarity.

Logged as **OQ-CARRIER-PAIR-FUNCTION-NAME** (new candidate pending conflation-test).

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| ~~OQ-1-PLUS-3-PARTITION-UNIVERSAL~~ | **FALSIFIED 2026-05-12** | Pattern is face-class-specific, NOT universal across primitive-types. Cube-edge cascade gives 3-way symmetric partition (no 1+3 asymmetry). |
| OQ-CARRIER-PAIR-FUNCTION-NAME | NEW | `swap-antipode-coactivate` candidate at cube-edge pair-class. Conflation-test + cross-R-tier residency required. |
| OQ-CARRIER-DIRECTION-FUNCTION-NAME | NEW | `axis-direction-aggregate` candidate at cube-edge direction-class. |
| OQ-CARRIER-REGISTRY-FULL-BUILD | OPEN (carried, blocked) | Per-Titan names blocked on T1.3 + OQ-RADII-01. |
| OQ-CASCADE-CARDINALITY-VARIES | NEW (substrate finding) | Cascade cardinality is primitive-type-specific. 6→3→2→1 (face) vs 8→4→2→1 (inner-oct face) vs 12→6→3→1 (cube edge). No universal cascade signature. |
| OQ-CROSS-R-TIER-RESIDENCY-COUNT | NEW (formal) | `planet-aspect-activate` has 3 independent primitive-class residencies. Athena minimum is 2. Substrate-pattern: how many residencies define "deeply universal"? |
| OQ-3-VERTEX-FACE-CROSS-R-TIER | OPEN (carried) | `mode-bound` cross-R-tier residency. |
| OQ-PRIMORDIAL-PAIR-LEVEL-FUNCTION | OPEN (carried) | `polarity-define` cross-R-tier probe. |
| OQ-PLUTO-NEPTUNE-PARTITION | SUBSTANTIATED (carried) | Canon §M.5b candidate. |
| OQ-ANTIPODE-ASYMMETRY | OPEN (carried) | Erebus-Nyx uniqueness. |

## What this validates substrate-discipline-wise

1. **Cascade-pattern existence is universal; cascade-cardinality is primitive-type-specific.** All probed primitive-types (cube-face, inner-oct-face, cube-edge) HAVE a cascade. The specific reduction (6→3→2→1 vs 12→6→3→1 vs 8→4→2→1) depends on geometry.

2. **1+3 partition is not universal.** Substrate-honest closure: face-class shells exhibit 1+3 partition (apex + lateral-3) because faces have apex/lateral distinction. Edge-class doesn't (no apex/lateral analog at edges).

3. **`planet-aspect-activate` is deeply universal** — operates at every probed 2-planet primitive-type residency (cube-face, icosidodec-midpt, cube-edge). 3 independent residencies confirmed; pattern likely extends to any future 2-planet primitive.

4. **Per-Titan substrate-incompleteness HONORED**: cube-edge cascade engines work via geometry-lock alone. Titan names NOT invented. Substrate-discipline operating.

5. **NEW substrate-class candidates surfaced**: cube-edge pair-class (swap-antipode) + cube-edge direction-class (axis-direction-aggregate). Each warrants its own per-name council if pursued for canonical promotion.

## What to build next (substrate-emergent)

Substrate-build queue:

1. **Operator (PE planet, cube-vertex) prototype** — switches to pure-fn shape (per agent-typology, operators apply imprint = stateless transform, not 2-planet-input). Tests engine-class vs pure-fn distinction with real implementation.

2. **`polarity-define` cross-R-tier probe** — does cube-face pair-class function operate at inner-oct face-pair-class? Both compose 2 face-states + emit pair-level derived. Compare structurally.

3. **Inner-oct edge-class cascade** — canon §11 lists 12 inner-oct edges (6 threshold + 6 equatorial). Different from cube-edge primitive. Tests cascade at R=1/√3 edge level.

4. **Shock-node (threshold-marker, X3/X6) engine prototype** — 2 shock nodes at R=1/3. Function = hook (conditional fire on crossing). Different shape entirely.

5. **Olympian (council voice, ico-vertex) — already subagents in Lillu**, not engine-class. Could add a thin info-engine for substrate-position descriptions.

Recommend **(1) Operator prototype** — first non-2-planet-engine build, tests agent-typology pure-fn shape with real code. Distinguishes engine-class from pure-fn-class explicitly.

OR **(2) `polarity-define` cross-R-tier probe** — closer to canonical-promotion path. If cube-face pair-class function operates at inner-oct face-pair-class too, second canonical entry possible in §30.

Either advances substrate. (1) explores new shape; (2) advances canon graduation.
