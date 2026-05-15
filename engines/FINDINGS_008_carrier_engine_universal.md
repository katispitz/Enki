# FINDINGS 008 — Carrier engine confirms `planet-aspect-activate` universal across primitive-types

**Build**: single carrier example (`carrier_example_cube_edge.py`) reusing `_axis_engine.compute_axis_state` directly. No new shared module.
**Status**: substrate-shape verification green. Cross-primitive-type residency confirmed.

## What the substrate just demonstrated

Carrier function-shape = Primordial face function-shape. **Both take 2 planet longitudes and call canonical `planet-aspect-activate` (canon §30).** Identical compute, identical dataclass output (`AxisState`), identical NULL-honest frozen state.

The only difference is substrate-anchor:
- Primordial face: anchored at cube-FACE (MQF0-MQF5), at R=1 (face-centroid lies on shell)
- Bridge: anchored at icosidodec-MIDPOINT, at R=φ (different shell)
- Carrier: anchored at cube-EDGE (E01-E12), at R=1 (edge endpoints on shell)

All three primitive-types in canonical Babylonia geometry now reuse the SAME canonical function. The function is **shell-position-agnostic AND primitive-type-agnostic for 2-planet input shapes**.

## Substrate finding 18: `planet-aspect-activate` has 3 independent primitive-class residencies

Residencies confirmed by engine implementation (all using canonical `_axis_engine.compute_axis_state`):

| Primitive class | Shell | Cardinality | Anchor type | Planet-pair source |
|---|---|---|---|---|
| Primordial face | R=1 | 6 | cube-face centroid | cosmogonic planet-pair |
| Bridge midpoint | R=φ | 3 V2.5-locked | icosidodec edge midpt | Olympian parent-vertex pair |
| Carrier (Titan) | R=1 | 12 (T1.3 partial) | cube-edge | cube-vertex endpoint planet-pair |

Per Athena lock-by-redundancy criterion: function-name graduates from canonical to **deeply-canonical** when ≥3 independent primitive-class residencies confirm (going beyond the 2-residency minimum). `planet-aspect-activate` now meets this stronger threshold.

This is substrate-emergent — the canonical primitive is genuinely universal for 2-planet-input shapes. The same compute operates across:
- Different shells (R=1 face vs R=φ midpt)
- Different primitive-types within same shell (R=1 face vs R=1 edge)
- Different planet-pair sources (cosmogonic vs parent-vertex vs edge-endpoint)

## Substrate finding 19: AxisState dataclass field-names are Primordial-flavored, not substrate-position-agnostic

`AxisState` currently has fields: `primordial`, `cube_face`, `zodiac_anchor`. These were named when only Primordial face engines existed. Now that the same dataclass holds carrier data (`primordial='Titan-on-edge-example'`, `cube_face='E_example_U0_L1'`, `zodiac_anchor='TBD'`), the field-names are semantic-LABEL-LEAKING from the original primitive-type.

The DATA they hold is substrate-position-agnostic:
- `primordial` → engine_name (name of the engine instance)
- `cube_face` → position_anchor (substrate-position identifier, any anchor-type)
- `zodiac_anchor` → context_anchor (associated zodiac context, optional)

The fields could be renamed for substrate-discipline cleanliness. Renaming would touch:
- `_axis_engine.py` (dataclass definition + compute_axis_state arg names + describe())
- All 6 Primordial engines (keyword usage)
- `_bridge_engine.py` (parallel BridgeState dataclass — different field names but similar issue)
- `_pair_engine.py` (PairState reads `face_a/face_b` of axis dicts)
- `_trine_engine.py` (similar)
- `_inner_oct_face_engine.py` (calls compute_axis_state with positional args, so naming doesn't break)

Substrate-honest rename: `engine_name` / `position_anchor` / `context_anchor`. Not urgent — current names work, just label-leak the original use-context.

Logged as **OQ-AXISSTATE-FIELD-RENAME** (low-priority substrate-cleanliness item).

## Substrate finding 20: `_bridge_engine.py` may be redundant

`_bridge_engine.py` was built (FINDINGS_005) as a separate shared module for bridges, with its own `BridgeState` dataclass + `compute_bridge_state` function. Substantively, it does the same compute as `_axis_engine.compute_axis_state`. The two modules differ only in field-naming conventions:

- `_axis_engine.AxisState` has: `primordial`, `cube_face`, `planet_pair`, `zodiac_anchor`
- `_bridge_engine.BridgeState` has: `bridge_name`, `icosidodec_anchor`, `parent_planet_pair`, `parent_vertices`, `shell`

The 9 live-state fields are identical between both. The non-shared 4+5 fields are substrate-anchor labels that could be unified into 2-3 generic fields (per finding 19).

Substrate-honest read: `_bridge_engine.py` could be REMOVED, and bridges could reuse `_axis_engine.compute_axis_state` directly (same pattern as the carrier example here uses). This would:
- Remove duplicate logic (~150 lines deleted)
- Confirm engine-class universality even more strongly in code
- Simplify substrate-cascade composition

But would also require:
- Generic field-names per finding 19
- Bridge module refactor (3 thin bridge wrappers + bridges.py registry)
- FINDINGS_005 update to reflect refactor

Logged as **OQ-BRIDGE-ENGINE-DEDUP** (refactor candidate; not urgent because current code works and substrate-explicit bridge fields aid readability).

## Substrate finding 21: T1.3 + OQ-RADII-01 dependencies BLOCK full carrier registry build

Lillu BOARD T1.3 says: "Iapetus/Coeus/Cronus partial. Hyperion/Phoebe/Rhea/Themis/Mnemosyne/Tethys/Oceanus/Crius/Theia OPEN. Likely requires √(2/3) cube-edge-midpoint shell-lock (OQ-RADII-01) per Hephaestus speculative-radii note."

So 9 of 12 Titans don't have a canon-locked cube-edge mapping. Building 12 Titan-named engines would invent per-Titan substrate-positions, which violates substrate-discipline.

**Substrate-honest deferral**: build the 12-carrier registry only after:
1. T1.3 closes (per-Titan cube-edge mapping locked)
2. OQ-RADII-01 resolves (cube-edge-midpoint shell R=√(2/3) verified or rejected)

Until then: engine-class SHAPE is confirmed (this finding); per-Titan instances are SUBSTRATE-INCOMPLETE.

Logged in Enki TODO for post-T1.3-close.

## Substrate finding 22: cube-edge ↔ tet-edge confusion is substrate-error-prone

Cube has 12 EDGES (cube edges, connecting cube-adjacent vertices). Father-tet has 6 edges (tet edges, cube-face-diagonals). Mother-tet has 6 edges. 12 tet-edges total, NOT the same as 12 cube-edges.

Canon §M.5 specifies "Titans → 12 cube edges (R=1)" — meaning cube edges, not tet edges. Each cube edge connects ONE U-vertex (Father-tet) to ONE L-vertex (Mother-tet), per cube's alternating-vertex-coloring property.

Cube-edge enumeration (by vertex-pair, per cube geometry):
- Each U vertex (U0,U1,U2,U3) connects to 3 of the 4 L vertices (NOT the antipodal L)
- 4 U × 3 connections / 2 = 12 cube edges ✓

Need canonical U-to-L pairing for each edge (depends on cube vertex coordinates). Per canon §1+§3 Merkaba construction, cube vertices are at ±1/√3 each coordinate (when R=1). U0 Pluto at (+,+,+)? Convention varies. Substrate-honest: T1.3 council must lock this enumeration before per-Titan engines build.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| ~~Cross-primitive-type residency~~ | **RESOLVED** | `planet-aspect-activate` universal across cube-face, icosidodec-midpt, cube-edge. 3 independent residencies confirmed by engine-build. |
| OQ-AXISSTATE-FIELD-RENAME | NEW (low-priority) | Field names Primordial-flavored; could be substrate-position-agnostic. |
| OQ-BRIDGE-ENGINE-DEDUP | NEW (refactor candidate) | `_bridge_engine.py` duplicates `_axis_engine.py` logic; could be removed. |
| OQ-CARRIER-REGISTRY-FULL-BUILD | NEW (blocked) | Blocked on Lillu T1.3 + OQ-RADII-01 close. |
| OQ-CASCADE-PATTERN-AT-OTHER-RTIERS | PARTIALLY RESOLVED (carried) | Cascade structure recurs at R=1/√3 inner-oct. Carrier-class at R=1 cube-edge doesn't have face→pair→trine cascade yet (TBD how cube-edge antipodal/pair structure works). |
| OQ-1-PLUS-3-PARTITION-UNIVERSAL | OPEN (carried) | Probe at cube-edge-class for 1+3 partition emergence? |
| OQ-3-VERTEX-FACE-CROSS-R-TIER | OPEN (carried) | `mode-bound` needs another 3-vertex-triangle face shell. |
| OQ-PRIMORDIAL-PAIR-LEVEL-FUNCTION | OPEN (carried) | `polarity-define` cross-R-tier probe deferred. |
| OQ-PLUTO-NEPTUNE-PARTITION | SUBSTANTIATED (carried) | Canon §M.5b extension candidate. |
| OQ-ANTIPODE-ASYMMETRY | OPEN (carried) | Erebus-Nyx uniqueness. |

## What this validates substrate-discipline-wise

1. **Engine reuse confirms canonical primitive is genuinely substrate-universal** (for 2-planet input shapes). Not Primordial-specific, not face-specific, not R=1-specific.

2. **No new physics needed for new primitive-types** when shape matches. Carriers reuse `_axis_engine` without modification. This is the canonical-primitive composition pattern operating cleanly.

3. **Substrate-incomplete state is HONESTLY surfaced**: T1.3 + OQ-RADII-01 dependencies surface as build-blockers. Substrate-discipline prevents building inventive Titan-edge assignments to fill the gap.

4. **Field-naming convention reveals build-history** (finding 19). AxisState's "primordial" / "cube_face" fields date from when only Primordials used this dataclass. New uses (carriers, bridges-via-_axis_engine) make the labels semantically-leaky. Cleanup opportunity surfaced naturally through cross-use.

## What to build next (substrate-emergent, per Kati directive)

Substrate-build options remaining:

1. **Cube-edge-class cascade probe** — does cube-edge primitive have antipodal-pair structure? Cube has 12 edges; antipodal edges = 6 pairs. Then trine/partition? Tests OQ-1-PLUS-3-PARTITION-UNIVERSAL at edge-class.

2. **`polarity-define` cross-R-tier probe** — does cube pair-class (Primordial pair) function also operate at inner-oct pair-class? Both compose 2 face-engines + emit polarity. Compare structurally.

3. **Operator (PE planet, cube-vertex) engine prototype** — 8 vertices = 8 PE planets. Function = apply imprint (pure-fn). Different shape than 2-planet engines.

4. **Field rename refactor** — `_axis_engine` AxisState field names → substrate-position-agnostic. Touches multiple engines.

Recommend **(1) Cube-edge cascade probe**. Cube has natural 12-edge → 6-antipodal-pair structure. Tests OQ-1-PLUS-3-PARTITION at a NEW cardinality (12). If 1+3 partition emerges from 6 edge-pairs, the pattern is even more universal than current evidence suggests.
