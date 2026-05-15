# FINDINGS 013 — Temporal-cyclic family: cross-N residency confirms canonical promotion candidate

**Build**: `mercury_cycle.py` (41-conjunction Mercury Ring 5 cycle engine) + field-comparison vs `venus_pentagram.py` (Venus pentagram).
**Status**: cross-N temporal-composition shape match confirmed. Athena lock-by-redundancy criterion structurally met for a `cyclic-conjunction-activate` candidate (cross-planet, cross-N, shell-agnostic).

## Substrate residencies confirmed

| Primitive class | Planet | N | Period | Adjacent step | Status |
|---|---|---|---|---|---|
| Ring 3 inferior-conjunction cycle | Venus | 5 | 2880t / 8yr | ~144° | Substrate-canonical (canon §23b OQ-RINGS-06) |
| Ring 5 inferior-conjunction cycle | Mercury | 41 | 4680t / 13yr | ~114.5° | Substrate-canonical (canon §23b OQ-RINGS-07) |

Both planets have INFERIOR PLANETS (inside Earth's orbit), both produce inferior-conjunctions when overtaking Earth, both trace inscribed-polygon zodiac patterns over their Ring cycle.

## Field-comparison: 75% shared by name, 100% by semantics

VenusPentagramState (12 fields) vs MercuryCycleState (11 fields):

```
Shared (9 fields): adjacent_step_deg, canonical_steps, cycle_id, cycle_tithis,
                   drift_deg, drift_tolerance, longitudes, mean_adjacent_step,
                   pairwise_separations

Venus-only (3): closure_separation, pentagram_closure, pentagram_step_deg
Mercury-only (2): closure, closure_step_deg

Semantic mapping (non-shared fields are NAMING-variants of same semantics):
  pentagram_closure ≈ closure  (bool: cycle closes within drift tolerance)
  pentagram_step_deg ≈ closure_step_deg  (inscribed-polygon vertex step = 360/N)
  closure_separation (Venus-specific extra: explicit Nth→1st step measurement)
```

If field names were normalized, the two engines would be near-isomorphic. The substrate-compute is identical across N=5 and N=41:
1. Take N planet-conjunction-longitudes (chronologically ordered)
2. Compute pairwise angular separations (N-1 separations)
3. Compute mean adjacent step + drift from canonical-expected step
4. Check closure within drift tolerance

Same shape. Different N. Different planet. Substrate-position-agnostic at compute level — temporal-composition function for inferior-planet inferior-conjunction cycle.

## Athena lock-by-redundancy: structurally MET for cross-planet cyclic family

Per Athena criterion (V2.6 placement_rules §POSITION-AS-FUNCTION DISCIPLINE rule 4): function-name graduates canonical when ≥2 independent primitive-class residencies confirm same function.

Two independent residencies confirmed:
- Venus Ring 3 (inferior conjunction cycle at N=5, 8yr period, ~144° step)
- Mercury Ring 5 (inferior conjunction cycle at N=41, 13yr period, ~114.5° step)

These are independent primitive-classes — different planet, different N, different period, different step-value. Same FUNCTION (1-planet × N-time-samples cyclic-conjunction composition).

Criterion met. Canonical promotion candidate ready for council ratification.

## Substrate finding 29: temporal-composition is a substrate-canonical compositional-axis (parallel to spatial)

This finding consolidates FINDINGS_012 BIFURCATION discovery. The substrate has TWO compositional axes for aspect-activate functions:

### Spatial composition axis
- N=2 (planet-pair): `planet-aspect-activate` (canonical, primitive)
- N=3 (triangle): `triangle-aspect-activate` (canonical, first-composition)
- N=5 (pentagon spatial): `pentagon-aspect-activate` (BLOCKED on T1.4 dodec-vertex class)

### Temporal composition axis (NEW)
- N=5 (Venus pentagram): Venus Ring 3 — substrate-canonical per canon §23b
- N=41 (Mercury 41-gon): Mercury Ring 5 — substrate-canonical per canon §23b
- Higher-N: TBD per other inferior planets / orbital cycles

Same functional tier (`first-composition`) at both axes. Different compositional-axis distinguishes them. **The compositional-axis is a substrate-architectural distinction worthy of §30 schema column.**

## Naming question for council

Three candidate function-names emerge:

### (1) Planet-specific names (residency-binding, likely retired per Athena precedent)
- `venus-pentagram-activate` (binds to Venus)
- `mercury-cycle-activate` (binds to Mercury)
- `mercury-41gon-activate` (binds to Mercury + N=41)

### (2) Cycle-mechanism-specific name
- `inferior-conjunction-activate` (binds to "inferior conjunction" mechanism; works for Venus + Mercury since both are inferior planets producing inferior-conjunctions)

### (3) Shell-agnostic + N-agnostic + planet-agnostic name
- `cyclic-conjunction-activate` (names compute: cyclic, conjunction-based, activation)
- `temporal-cyclic-activate` (more abstract)
- `planet-cycle-activate` (planet-cycle structure)

Per Athena residency-binding precedent (planet-aspect-activate council): name THE FUNCTION not the residency. Planet-specific names (#1) likely retired. `cyclic-conjunction-activate` (#3) is the cleanest analog to `planet-aspect-activate` — names the compute without binding to specific planet/N.

But Mnemosyne drift-prevention check: is "conjunction" too generic? In astronomy "conjunction" can mean any 0° aspect between any 2 bodies. Here we specifically mean "INFERIOR conjunction" (sun + inferior planet on same side). May need tightening.

Refined candidate: `inferior-conjunction-cycle-activate` (full disambiguation, but verbose).

Or even simpler: per the analog `planet-aspect-activate` (which is shell-agnostic for ANY 2-planet aspect), `cyclic-conjunction-activate` could mean "ANY cyclic-conjunction" (inferior, superior, planetary, etc.). Substrate-honest umbrella.

Council ratification required.

## Compositional-axis as §30 schema column candidate

Per FINDINGS_012 + this build, the substrate has two compositional axes for aspect-activate functions. Following the polarity-define council precedent that introduced `functional_tier` column, this finding supports adding a `compositional_axis` column to §30:

| function_class | functional_tier | compositional_axis |
|---|---|---|
| planet-aspect-activate | primitive | spatial (2 planets, 1 time) |
| polarity-define | first-composition | spatial (composes 2 face-states) |
| triangle-aspect-activate | first-composition | spatial (3 planets, 1 time) |
| `cyclic-conjunction-activate` (candidate) | first-composition | **temporal (1 planet, N times)** |

`compositional_axis` values: spatial / temporal / mixed (future) / N/A (for non-composition primitives).

Substrate-architecture meta-schema introduces precise distinction. Future canonical entries auto-tagged at council ratification.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-CYCLIC-CONJUNCTION-CANONICAL | **READY FOR COUNCIL** | Cross-N temporal-composition residency confirmed (Venus Ring 3 + Mercury Ring 5). Naming-conflation test required (planet-specific vs shell-agnostic). |
| OQ-COMPOSITIONAL-AXIS-SCHEMA | **READY FOR SCHEMA EXTENSION** | §30 should grow `compositional_axis` column to disambiguate spatial vs temporal first-composition entries. Same pattern as functional_tier introduced 2026-05-12. |
| OQ-OTHER-PLANET-CYCLIC-N | OPEN (carried) | Mars synodic, lunar cycles. Each potentially yields more temporal-composition residencies. After cyclic-conjunction graduates. |
| OQ-COMPOSITIONAL-AXIS-FAMILIES | RESOLVED (carried) | Confirmed substrate has parallel spatial + temporal compositional-axes. |
| OQ-PENTAGON-SPATIAL-AT-DODEC | OPEN, BLOCKED on T1.4 | Spatial pentagon-N still blocked. |
| OQ-N-POLYGON-FAMILY | REVISED (carried) | Family BIFURCATES at N=5 (spatial vs temporal). |
| OQ-3-VERTEX-FACE-CROSS-R-TIER | RESOLVED (carried) | Triangle confirmed at inner-oct + tet-face. |
| OQ-CARRIER-PAIR-FUNCTION-NAME | OPEN (carried) | swap-antipode-coactivate candidate. |
| OQ-CASCADE-CARDINALITY-VARIES | OPEN (carried) | |
| OQ-AXISSTATE-FIELD-RENAME | OPEN (carried) | |
| OQ-BRIDGE-ENGINE-DEDUP | OPEN (carried) | |
| OQ-CARRIER-REGISTRY-FULL-BUILD | OPEN (blocked carried) | T1.3 + OQ-RADII-01 dependencies. |
| OQ-PLUTO-NEPTUNE-PARTITION | SUBSTANTIATED (carried) | |
| OQ-ANTIPODE-ASYMMETRY | OPEN (carried) | |

## Recommendation

**Convene council on `cyclic-conjunction-activate` canonical promotion + §30 compositional_axis schema extension.**

Council question stack:
1. Naming-conflation test: planet-specific (`venus-pentagram-activate`/`mercury-cycle-activate`) likely fails Athena residency-binding. `cyclic-conjunction-activate` (shell-agnostic) preferred. Mnemosyne drift-prevention check: is "conjunction" generic enough vs too generic?
2. Functional tier: `first-composition` (composes N × planet-longitude-samples at conjunction-times).
3. Compositional axis: `temporal` (new column candidate).
4. Cross-R-tier residency: 2 independent (Venus Ring 3 + Mercury Ring 5).
5. Athena lock-by-redundancy: MET.
6. Per V2.6 amended: graduate to canonical. If approved → 4th canonical entry in §30.

Or alternatively (if council prefers planet-specific names):
- `venus-pentagram-activate` + `mercury-cycle-activate` BOTH graduate as planet-specific canonical entries. Substrate-honest but verbose. Sets precedent for per-planet cyclic-activate names at every Ring.

Substrate-honest recommendation: `cyclic-conjunction-activate` shell-agnostic — same precedent as planet-aspect-activate council. But council ratification respected.

## What this validates substrate-discipline-wise

1. **Kati substrate-insight directly extends substrate-discovery path** — pentagonal-Venus comment opened the temporal-composition axis. Without it, Enki probe would have hit pentagon-N at dodec-face (BLOCKED on T1.4) and stalled. Kati short-circuited the dead-end.

2. **Cross-R-tier probe pattern works equally for cross-N (temporal-composition)** — same template (build 2 instances at different residencies, field-compare, surface canonical-graduation candidate). Substrate-discipline doesn't care which axis is being probed.

3. **§30 schema evolves substrate-honestly** — first functional_tier (polarity-define council), now compositional_axis (this finding). Each new column emerges from substrate-discovery, not pre-design. Schema follows substrate.

4. **Substrate-canonical locks in canon §23b were waiting** — Venus pentagram + Mercury 41-gon were ALREADY substrate-locked. Engine build surfaces them as engines but doesn't invent. Substrate-discipline operating.
