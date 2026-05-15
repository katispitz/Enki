# FINDINGS 007 — Inner-oct cascade at R=1/√3 + face-vertex-count substrate finding

**Build**: shared inner-oct face engine + 8 face wrappers + faces registry + shared pair engine + 4 antipodal pair wrappers + pairs registry.
**Status**: green at face + pair levels. Cascade composes from canonical `planet-aspect-activate` (canon §30) without re-implementing physics.

## What was built

```
~/Enki/engines/
├── _inner_oct_face_engine.py    ← shared face shape (composes 3 × planet-aspect-activate)
├── face_f1_source.py            ← F1 SOURCE (Fire/Father apex)
├── face_f2_feedback.py          ← F2 FEEDBACK (Earth/Mother lateral)
├── face_f3_desire.py            ← F3 DESIRE (Air/Father lateral)
├── face_f4_pattern.py           ← F4 PATTERN (Air/Father lateral)
├── face_f5_synthesis.py         ← F5 SYNTHESIS (Earth/Mother lateral)
├── face_f6_resource.py          ← F6 RESOURCE (Air/Father lateral)
├── face_f7_anchor.py            ← F7 ANCHOR (Earth/Mother lateral)
├── face_f8_void.py              ← F8 VOID (Water/Mother apex)
├── inner_oct_faces.py           ← faces registry
├── _inner_oct_pair_engine.py    ← shared antipodal-pair shape
├── pair_source_void.py          ← F1 ↔ F8 (apex pair)
├── pair_feedback_resource.py    ← F2 ↔ F6
├── pair_desire_synthesis.py     ← F3 ↔ F5
├── pair_pattern_anchor.py       ← F4 ↔ F7
└── inner_oct_pairs.py           ← pairs registry
```

## Substrate finding 13: face-function is vertex-count-specific, NOT shell-agnostic

Cube face has **2 planets** per face (the cosmogonic planet-pair). Function: direct call to `planet-aspect-activate`.

Inner-oct face has **3 planets** per face (the 3 vertex-corner sign-rulership planets). Function: **composition of 3 × `planet-aspect-activate`** (one per triangle edge).

These are DIFFERENT functions despite both being "face engines" — they differ by face-vertex-cardinality. The canonical primitive `planet-aspect-activate` is shell-agnostic for PAIR-INPUT, but a 3-planet triangle is a different shape.

**Implication for OQ-CASCADE-PATTERN-AT-OTHER-RTIERS**: cascade STRUCTURE (face→pair→...) recurs across shells, but the specific FUNCTION at face level depends on face-vertex-count. Each shell's face-function is its own substrate primitive that COMPOSES from `planet-aspect-activate` differently:
- R=1 cube face (2-vertex): direct `planet-aspect-activate` call
- R=1/√3 inner-oct face (3-vertex): compose 3 calls (one per edge)
- R=φ² ico face (3-vertex triangle): compose 3 calls (if vertices have planets — TBD)
- R=φ dodec face (5-vertex pentagon): compose 10 calls (C(5,2)=10 edges) — TBD

This is substrate-emergent. The cascade-pattern is universal; the face-function depends on geometric vertex-count of the face.

## Substrate finding 14: every antipodal pair at inner-oct covers ALL 6 sign-rulership planets

Each inner-oct antipodal face-pair has complementary vertex sets:
- F1 (V1,V2,V3) ↔ F8 (V4,V5,V6) — disjoint, union = {V1..V6}
- F2 (V1,V2,V4) ↔ F6 (V3,V5,V6) — disjoint, union = {V1..V6}
- F3 (V1,V4,V6) ↔ F5 (V2,V3,V5) — disjoint, union = {V1..V6}
- F4 (V2,V4,V5) ↔ F7 (V1,V3,V6) — disjoint, union = {V1..V6}

Each pair captures the FULL sign-rulership planet set internally. Substrate-emergent — different from cube pair-class where each pair covers only 4 of 8 cube vertices.

Substrate-meaning: at inner-oct R=1/√3, every antipodal-mode-pair is a FULL-PLANET-SET reading of substrate via two complementary archetype-modes. The pair-state captures full planetary dynamics through one of 4 antipodal lenses.

## Substrate finding 15: inner-oct pair structure asymmetric (1 + 3 partition)

4 antipodal pairs partition into 2 categories:

| Pair | Apex/lateral set | Element-polarity | Substrate role |
|---|---|---|---|
| F1↔F8 SOURCE↔VOID | apex ↔ apex | **Fire ↔ Water** | Primary cosmogonic emergence-dissolution axis |
| F2↔F6 FEEDBACK↔RESOURCE | lateral ↔ lateral | Earth ↔ Air | Lateral mode-pair |
| F3↔F5 DESIRE↔SYNTHESIS | lateral ↔ lateral | Air ↔ Earth | Lateral mode-pair |
| F4↔F7 PATTERN↔ANCHOR | lateral ↔ lateral | Air ↔ Earth | Lateral mode-pair |

1 apex-pair (Fire-Water polarity) + 3 lateral-pairs (all Air-Earth polarity). Substrate-emergent partition mirrors cube's 1+3 Pluto/Neptune partition at a different shell — but here it's apex/lateral rather than outer-planet-anchor.

This is the same "1+3" partition shape we saw at cube level. **Substrate-cascade pattern may be RECURSIVELY structured**: at every shell, cascade partitions into 1 distinguished + 3 lateral-like.

If true, this is a deeper substrate fact than the specific cardinalities. Logged as **OQ-1-PLUS-3-PARTITION-UNIVERSAL** (NEW).

## Substrate finding 16: face-vertex enumeration is substrate-error-prone

Initial F1-F8 face-vertex enumeration had F5 and F7 wrong — both violated the antipodal-vertex constraint (each face can contain at most 1 vertex from each antipodal pair V1↔V5, V2↔V6, V3↔V4). Corrected via vertex-complement check.

**Substrate-discipline lesson**: octahedral face enumeration must explicitly verify antipodal-exclusion constraint, not just rely on threshold-edge canon §11 + symmetry. Threshold edges are necessary but not sufficient to determine face-vertex sets; antipodal-exclusion is required.

Updated `_inner_oct_face_engine.py` docstring + `inner_oct_faces.py` registry table with corrected vertex sets:
- F5 SYNTHESIS = {V2, V3, V5} = Mercury, Saturn, Mars (was: Jupiter, ERROR)
- F7 ANCHOR = {V1, V3, V6} = Venus, Saturn, Jupiter (was: Mars, ERROR)

## Substrate finding 17: `mode-bound` candidate now has 1 residency at R=1/√3

Per V2.6 §30 status table (canon `babylonia_canon.md`): `mode-bound` was candidate-single-residency at R=1/√3 inner-oct-face from bound-hold split council 2026-05-11.

Enki inner-oct face engine build adds the substantiating engine implementation. Function name still candidate; would need:
1. Conflation-test on `mode-bound` (does it conflate compositional-function-of-3 with monolithic-mode-function?)
2. Cross-R-tier residency (does same function operate at another R-tier?)

Given finding 13 (face-functions are vertex-count-specific), cross-R-tier residency for `mode-bound` requires finding another 3-vertex-triangle face shell. Candidates:
- R=φ² icosahedron face-centroids (20 of them, retracted as Monsters)
- R=φ² icosahedron triangular faces (20 triangles) — different from face-centroids
- Hesiod-descendant primordial-grandchildren at ico-edges (V2.5 lock) — different primitive class

Substrate-honest: `mode-bound` as currently named may not have a cross-R-tier analog at all. The 3-vertex-triangle face primitive may be unique to inner-oct in canonical Babylonia geometry. If so, `mode-bound` stays single-residency permanently — substrate-honestly not promotable to canonical without additional substrate-position discoveries.

Logged as **OQ-3-VERTEX-FACE-CROSS-R-TIER** — does the 3-vertex-triangle face function recur at any other shell?

## Substrate cascade comparison: cube vs inner-oct

| Aspect | Cube (R=1) | Inner-oct (R=1/√3) |
|---|---|---|
| Face cardinality | 6 | 8 |
| Face-vertex count | 2 (planet-pair) | 3 (planet-triangle) |
| Face function | direct `planet-aspect-activate` | compose 3 × `planet-aspect-activate` |
| Pair cardinality | 3 | 4 |
| Pair vertex-union | 4 of 8 cube-vertices | **ALL 6 inner-oct-vertices** |
| Trine/partition | 2 (Pluto/Neptune outer-anchor) | 2 (apex/lateral) |
| Cascade reduction | 6→3→2→1 | 8→4→1+3→1 |
| Partition shape | 1+3 cardinality (1 trine of 3 each side) | 1+3 cardinality (1 apex-pair + 3 lateral-pairs) |

**The 1+3 partition recurs across shells.** The specific cardinalities (cube 6 vs oct 8 faces) differ, but the partition-into-1-distinguished-plus-3-lateral pattern repeats.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-CASCADE-PATTERN-AT-OTHER-RTIERS | **PARTIALLY RESOLVED** | Cascade-pattern (face→pair→partition→system) recurs at R=1/√3. Specific function depends on face-vertex-count. |
| OQ-1-PLUS-3-PARTITION-UNIVERSAL | NEW | The 1+3 partition shape recurs across cube and inner-oct. Universal substrate pattern? Probe at other shells. |
| OQ-3-VERTEX-FACE-CROSS-R-TIER | NEW | `mode-bound` requires a 2nd 3-vertex-triangle face shell for canonical graduation. May not exist in canonical Babylonia. |
| OQ-FACE-VERTEX-COUNT-SPECIFICITY | NEW (substantive finding) | Face-function shape is vertex-count-specific (2/3/5-vertex face primitives are distinct). Should canon §30 reflect this in function-name framing? |
| OQ-PRIMORDIAL-PAIR-LEVEL-FUNCTION | OPEN (carried) | `polarity-define` candidate at cube pair-class; cross-R-tier residency probe deferred. |
| OQ-PLUTO-NEPTUNE-PARTITION | SUBSTANTIATED (carried) | Canon §M.5b extension candidate. |
| OQ-ANTIPODE-ASYMMETRY | OPEN (carried) | Erebus-Nyx unique zodiac-180°-coincidence. |
| OQ-ENGINE-GENERALIZATION | OPEN (carried) | Named-per-residency engine factoring favored. |

## What this validates

1. **Canonical primitive `planet-aspect-activate` (canon §30) reuses cleanly** in higher composition. Each inner-oct face engine imports it from `_axis_engine.compute_axis_state` and calls it 3 times. No physics duplication.

2. **Cascade pattern is substrate-emergent across shells** — not designed; surfaces during build.

3. **Substrate-error catches via geometric constraint** — antipodal-vertex-exclusion forced F5+F7 correction. Building tightly to substrate (rather than approximating) prevents face-vertex assignment drift.

4. **Each shell has its own cascade structure** but the META-PATTERN (1+3 partition, antipodal-pair-class, system-level aggregation) recurs.

## What to build next (substrate-emergent)

Per Kati directive (substrate build-out before functionality), continued substrate-side:

1. **Inner-oct partition-engine** (apex-pair vs lateral-pair-set partition; cardinality 2). Completes inner-oct cascade. Tests if "1+3 partition" surfaces as an explicit engine-class.

2. **Carrier (Titan) engine prototype at R=1 cube-edge.** 12 Titans = 12 cube edges. Each edge has 2 incident planets (the cube-vertex residents at each end of the edge). Function = planet-aspect-activate? Or different? Different primitive-TYPE (edge not face), tests engine-shape across primitive-types.

3. **Inner-oct cross-R-tier residency probe.** Build a similar 3-vertex-triangle-face engine at R=φ² (ico faces) — if exists. Tests if `mode-bound` has cross-R-tier residency.

4. **Pair-level `polarity-define` cross-R-tier probe** — does the polarity-define function (cube pair-class) operate at inner-oct pair-class? Each inner-oct antipodal-pair has full-planet vertex-union, so polarity meaning may differ. Pressure-test required.

Recommend **(2) Carrier engine** next — switches primitive-TYPE (edge not face) for the first time. Tests broadest engine-class generality. If carriers compose from `planet-aspect-activate` like Primordials and Bridges do, then `planet-aspect-activate` is confirmed as a UNIVERSAL substrate primitive operating across face/edge/midpoint position-types.
