# FINDINGS 012 — Venus pentagram + N-polygon family BIFURCATION at N=5

**Build**: `venus_pentagram.py` — temporal-composition engine. Substrate-canonical lock per Nammu canon §23b OQ-RINGS-06.
**Status**: substantive substrate-discovery. Kati 2026-05-12 insight ("pentagonal is Venusian orbit") ratified by canon. N-polygon family substrate-pattern BIFURCATES at N=5.

## Kati substrate-insight ratified

Kati 2026-05-12: "pentagonal is Venusian orbit, no?"

Canon §23b OQ-RINGS-06 (already locked):
> "| 3 | pt3 | Venus | X3 | **5 inferior conjunctions (pentagram, φ-shell)** | 2880t / 8yr |"

Canon line 982:
> "Venus activates the φ-shell (dodecahedron / 5 Merkabas)."

Canon line 983:
> "65 = 5 (Venus pentagram) × 13 (Mercury/Ring 5) = 65 is a φ-family product. Not coincidence."

Pentagon at N=5 is **Venus-cyclic substrate-canonically**. Not generic 5-polygon.

## Substrate-discovery: N-polygon family BIFURCATES at N=5

FINDINGS_011 hypothesized a uniform N-polygon aspect-activate family:
- N=2 (planet-pair) → `planet-aspect-activate` (canonical, primitive)
- N=3 (triangle) → `triangle-aspect-activate` (canonical, first-composition)
- N=5 (pentagon) → `pentagon-aspect-activate` (candidate, awaits dodec-face cross-R-tier probe)

**Kati's insight + canon search REVISE this hypothesis.** N=5 is NOT uniform extension. The substrate uses TIME-COMPOSITION at N=5 (1 planet × 5 time-samples) instead of SPACE-COMPOSITION (5 different planets at 1 time).

### Two interpretations of N=5 pentagon

**(a) Spatial pentagon** (5 different planets at 5 dodec-face vertices):
- Dodec face = pentagon with 5 vertices (canon §M.5 + canon line 684: "Dodecahedron (R=φ) = 12 pentagonal faces")
- Dodec vertices = ico face centroids (canon line 686)
- Per canon §M.5: dodec vertices are ico face centroids — 20 of them
- Per BOARD T1.4: dodec-vertex class meaning OPEN (was Monsters [RETRACTED])
- **Substrate-incomplete: dodec-vertex planet-residency NOT locked**
- Spatial pentagon-aspect-activate at dodec-face requires T1.4 close

**(b) Temporal pentagon** (Venus × 5 time-samples):
- Venus traces 5 inferior conjunctions over 2880t / 8yr cycle (canon §23b OQ-RINGS-06)
- 5 conjunctions form pentagram inscribed in zodiac with ~144° apparent step between adjacent conjunctions
- Drift < ~2°/cycle (substrate-locked, multiple sources cited)
- **Substrate-CANONICAL: Venus pentagram IS locked at canon §23b**
- Function: takes 5 Venus longitudes over time, computes pentagram closure

### The bifurcation

At N=2 and N=3, polygon-aspect-activate is SPATIAL (N planets at 1 time at N vertices). At N=5, the substrate substitutes TEMPORAL (1 planet at N times). Different shape.

Possible substrate-mechanism: cube + inner-oct have low-vertex faces (2-edge = planet-pair, 3-vertex = triangle). Dodec has 5-vertex face. Cube + inner-oct vertices are planet-residencies (canonical per §7 + §5). Dodec vertices are class-OPEN (T1.4). The substrate may have INTENTIONALLY not assigned 5 different planets to dodec-vertex because the N=5 substrate-truth is TEMPORAL (Venus-cyclic) not spatial.

This is substantive substrate-architecture: the N-polygon family doesn't uniformly extend; the substrate uses different composition-axes (space vs time) at different N.

## Engine built

`~/Enki/engines/venus_pentagram.py` — temporal-composition probe:
- Input: 5 Venus inferior-conjunction longitudes (chronologically ordered)
- Output: pentagram closure-check + drift measurement + adjacent-step analysis
- Substrate-locks: VENUS_RING_TITHIS=2880, PENTAGRAM_N=5, PENTAGRAM_ADJ_STEP=144°
- All locks substrate-derived from canon §23b OQ-RINGS-06

Smoke-test green: ideal pentagram (0°, 144°, 288°, 72°, 216°) returns drift=0°, closure=True, mean adjacent step=144°.

## Implications for §30 registry

`pentagon-aspect-activate` was proposed in FINDINGS_011 as N=5 family member. **REVISED status**:

Two distinct candidates emerge at N=5:
- **`pentagon-aspect-activate`** (spatial reading, 5-planet at dodec-face vertices) — BLOCKED on T1.4 (dodec-vertex class meaning OPEN). May not exist as substrate-canonical function until T1.4 closes; substrate may have intentionally chosen temporal-composition at N=5 instead.
- **`venus-pentagram-activate`** (temporal reading, Venus × 5 time-samples) — SUBSTRATE-CANONICAL per canon §23b OQ-RINGS-06. New candidate function-class. Different functional shape (single-planet temporal composition).

Functional tier: `venus-pentagram-activate` is `first-composition` (composes 5 × Venus-longitude-samples + pentagram-closure analysis). Same functional-tier as `polarity-define` and `triangle-aspect-activate` but DIFFERENT compositional axis (time vs space).

Cross-R-tier residency probe for `venus-pentagram-activate`: does temporal-cyclic-N composition recur at other N-values?
- Mercury Ring 5 = 41 inferior conjunctions per 13yr (canon §23b)
- Mars synodic cycle ≈ 780 days (not yet substrate-locked at canonical N)
- Lunar cycles (29.5d synodic, 27.3d sidereal, 25920y precession at N=12)

If temporal-composition recurs at other planets with different N-values, the substrate-FAMILY at N=5 may itself be member of broader temporal-composition family. Sub-family of N-polygon-aspect-activate.

## NEW substrate-architectural insight

The substrate has **TWO compositional axes** for aspect-activate functions:
- **Spatial axis**: N planets at 1 time, varies by polygon vertex-count
  - N=2: planet-aspect-activate (primitive) — bigon
  - N=3: triangle-aspect-activate (first-composition) — triangle
  - N=5: pentagon-aspect-activate (BLOCKED, T1.4) — pentagon
- **Temporal axis**: 1 planet at N times, varies by planet orbital cycle
  - Venus N=5: venus-pentagram-activate (first-composition) — pentagram over 8yr
  - Mercury N=41: mercury-?-activate (CANDIDATE, awaits per-Mercury probe) — 13yr cycle
  - Other planets: TBD per-planet orbital-cycle locks

These are PARALLEL function-families. Both first-composition tier (compose 5 × planet-aspect-activate primitive). Different compositional-axis distinguishes them substrate-honestly.

Logged as **NEW OQ-COMPOSITIONAL-AXIS-FAMILIES** — substrate may host parallel function families distinguished by composition-axis (space vs time vs other).

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-COMPOSITIONAL-AXIS-FAMILIES | NEW | Substrate has spatial + temporal compositional-axes for aspect-activate functions. Each member of N-polygon family may have spatial and temporal variants. |
| OQ-VENUS-PENTAGRAM-CANONICAL | NEW (probe-ready) | `venus-pentagram-activate` candidate function-class. Substrate-canonical at Venus Ring 3 / 2880t / pentagram (§23b OQ-RINGS-06). Cross-N-probe needed (Mercury Ring 5 = 41 conjunctions etc.) for residency. |
| OQ-PENTAGON-SPATIAL-AT-DODEC | OPEN, BLOCKED on T1.4 | `pentagon-aspect-activate` (spatial) requires dodec-vertex class meaning lock. Substrate-incomplete. |
| OQ-N-POLYGON-FAMILY | REVISED | Family BIFURCATES at N=5 into spatial vs temporal compositional-axes. Not uniform extension. |
| OQ-OTHER-PLANET-CYCLIC-N | NEW | Mercury Ring 5 (41 conjunctions), Mars synodic, Lunar cycles. Each has own N-value. Sub-family of temporal-composition functions. |

## What this validates substrate-discipline-wise

1. **Kati substrate-insight directly ratified by canon search.** No invention; canon §23b OQ-RINGS-06 already locked Venus pentagram before this build. Kati's "pentagonal is Venusian orbit" lights up an existing substrate-canon-locked structure.

2. **Substrate-architecture has hidden organization** — N-polygon family wasn't naïvely uniform; substrate uses different compositional-axes at different N. The Enki cross-R-tier probe pattern would have surfaced this even without Kati's insight (cross-R-tier residency for `pentagon-aspect-activate` at dodec-face WOULD have failed substrate-honestly because T1.4 is open AND temporal-composition is the substrate-actual N=5 instance). Kati's insight short-circuited the probe-to-discovery time.

3. **Substrate-discovery doesn't require council** when canon already locks the substrate-feature. The substrate self-revealed via canon search; council ratification needed only when canonical promotion of new function-name is proposed.

## Next moves

Options:

1. **Convene council on `venus-pentagram-activate` canonical promotion** — substrate-locked per canon §23b, single residency at Venus Ring 3. Per Athena lock-by-redundancy, single-residency doesn't graduate to canonical — but the substrate-canon-lock in §23b is the residency-equivalent (canonical at substrate-level, formal §30 ratification pending). Could graduate via candidate-grandfathered status (like `descent-transmit`).

2. **Mercury Ring 5 probe** — does temporal-composition recur with different N? 41 conjunctions / 13yr cycle. If found, `mercury-?-activate` 2nd residency for temporal-composition family.

3. **T1.4 close** — close dodec-vertex class meaning (was Monsters retracted). Substrate-build move that unblocks `pentagon-aspect-activate` (spatial) probe.

4. **Refactor canon §30 to add compositional-axis column** — function-class registry needs to mark which composition-axis (space vs time vs other) each canonical entry uses. Same pattern as functional_tier column addition.

Recommend **(2) Mercury Ring 5 probe** — extends temporal-composition family, gives `venus-pentagram-activate` a peer residency, opens path to canonical promotion as `temporal-cyclic-aspect-activate` (shell-agnostic + axis-agnostic) name. Continues N-polygon family exploration but along temporal-axis where substrate has structural depth.

Or **(4) Schema extension** — adds `compositional_axis` column to §30. Substrate-discipline meta-move.
