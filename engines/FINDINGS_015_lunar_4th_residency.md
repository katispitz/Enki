# FINDINGS 015 — Lunar year-cycle: 4th residency for `cyclic-syzygy-activate` + cross-event-type umbrella confirmed

**Build**: `lunar_year_cycle.py` (12 new-moon syzygies per solar year) + 4-way field-comparison Venus/Mercury/Mars/Lunar.
**Status**: 4th independent primitive-class residency confirmed for `cyclic-syzygy-activate`. Substrate-honest umbrella verified across 3 distinct syzygy event-types.

## What was built

`~/Enki/engines/lunar_year_cycle.py` — substrate-derivable from canon §23b ring ratios:
- Ring 1 Solar (360t) / Ring 2 Lunar (30t) = **N=12 synodic syzygies per solar year**
- Adjacent step: 30° EXACT (Sun advances 30° per 30t synodic month → consecutive new-moon longitudes spaced 30° apart)
- 12 × 30° = 360° exact closure (no drift)
- Event type: `new-moon-syzygy` (sun-earth-moon conjunction flavor)

Smoke-test: ideal cycle (0°, 30°, 60°, ..., 330°) returns drift=0°, closure=True, mean=30°.

## 4-way field comparison

| Engine | Total fields | Compute fields (shared with all 4) |
|---|---|---|
| VenusPentagramState | 12 | 9 |
| MercuryCycleState | 11 | 9 |
| MarsCycleState | 11 | 9 |
| LunarYearCycleState | 11 | 9 |

**9 shared compute-fields across all 4 engines**: `adjacent_step_deg`, `canonical_steps`, `cycle_id`, `cycle_tithis`, `drift_deg`, `drift_tolerance`, `longitudes`, `mean_adjacent_step`, `pairwise_separations`.

Lunar engine shares **11 of 11 fields with Mars** (both have explicit `event_type` — substrate-honest disclosure). Field-level near-identity confirms shape-match.

## 4 independent primitive-class residencies for `cyclic-syzygy-activate`

| Residency | Planet | N | Period | Event-type | Adjacent step |
|---|---|---|---|---|---|
| Venus Ring 3 | Venus | 5 | 2880t / 8yr | inferior-conjunction | ~144° |
| Mercury Ring 5 | Mercury | 41 | 4680t / 13yr | inferior-conjunction | ~114.5° |
| Mars Ring 4 | Mars | 37 | 28440t / 79yr | OPPOSITION | ~48.6° |
| **Lunar Ring 1/Ring 2 ratio** | **Moon** | **12** | **360t / 1yr** | **new-moon-syzygy** | **30°** |

4 residencies, **3 distinct syzygy event-types**: inferior-conjunction (Venus + Mercury), opposition (Mars), new-moon-syzygy (Moon).

## Substrate-honest umbrella: `syzygy` confirmed across event-types

The same-day rename (FINDINGS_014) replaced `cyclic-conjunction-activate` with `cyclic-syzygy-activate` based on Mars opposition residency. This probe confirms: `syzygy` umbrella covers **all sun-earth-planet alignment events**, regardless of which side the planet sits relative to sun:

- **Inferior conjunction** (Venus, Mercury): planet between sun and earth (sun-PLANET-earth alignment)
- **Opposition** (Mars): earth between sun and planet (sun-earth-PLANET alignment, planet at 180°)
- **New-moon conjunction** (Moon): moon between sun and earth (sun-MOON-earth alignment — same flavor as inferior conjunction but for Moon)

All three are **syzygies** (3-body alignments). Substrate-honest name covers all.

## Substrate-architecture meta-finding: substrate-derivable N from ring ratios

Venus N=5, Mercury N=41, Mars N=37 are EACH primary-ringed in canon §23b. Lunar N=12 is **DERIVED** from Ring 1 / Ring 2 ratio — not primary-ringed directly. Substrate-canonical via composition of two primary ring locks.

This is substrate-emergent: N-values can be:
- **Primary**: directly canon-locked per Ring (Venus 5, Mercury 41, Mars 37)
- **Derived**: emergent from ring-ratio composition (Lunar 12 = Solar 360t / Lunar 30t)
- Future: cross-ring composition may yield additional N-values (Saturn Ring 7 "Moon-synodic mirror" hint per canon line 953 may indicate fractal-derived N-cycle)

Logged as **OQ-N-FROM-RING-RATIO** — substrate hosts cross-ring N-cycle compositions distinct from primary-ring N entries.

## Substrate-architecture meta-finding: cross-event-type residency confirms umbrella

3 distinct syzygy event-types at 4 residencies confirm `syzygy` is genuinely the substrate-mechanism-level umbrella concept (not just inferior-conjunction-specific). This validates the Clio substrate-emergent rule from FINDINGS_014 rename council: **canonical names must be compute-descriptive at substrate-MECHANISM level, not input-type-instance level.**

The substrate uses the SAME compute (cyclic-N-position-composition) across:
- 2 inferior-planet residencies (Venus, Mercury)
- 1 outer-planet residency (Mars)
- 1 Moon residency (Earth's satellite)

Plus 3 different astronomical-event-types. Pattern: substrate is genuinely shell/planet/event-type-AGNOSTIC at compute level.

## Update to §30 entry (canon edit needed)

`cyclic-syzygy-activate` §30 entry should be updated to list 4 residencies (currently 3). Edit needed:

> Residencies: Venus Ring 3 (N=5 inferior-conjunction syzygy / 8yr) + Mercury Ring 5 (N=41 inferior-conjunction syzygy / 13yr) + Mars Ring 4 (N=37 opposition syzygy / 79yr) + **Lunar Ring 1/Ring 2 ratio (N=12 new-moon syzygy / 1yr — substrate-derived from solar/lunar ring composition)**

No council needed — canonical name already in §30 from rename council. This is residency-expansion, not function-graduation. Substrate-discipline: adding residencies to already-canonical functions is mechanical (doesn't require council ratification beyond the original graduation council that established the function).

Per Erato rule 4b extension (Urania, FINDINGS_014): canonical names re-tested at every new residency probe. Lunar probe re-tests `cyclic-syzygy-activate` name fitness. Outcome: **name passes substrate-pressure-test at Lunar new-moon-syzygy residency.** No further rename required.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-N-FROM-RING-RATIO | NEW | Substrate-derived N-cycles from ring-ratio composition (Lunar 12 = R1/R2). Distinct from primary-ringed N entries. May surface other cross-ring cycles. |
| OQ-LUNAR-SAROS-METONIC | DEFERRED | Saros (18.03yr) + Metonic (19yr) cycles not canon-§23b-primary-locked. Substrate-derivability via Ring composition pending — Saros connects synodic + draconic + anomalistic months which aren't all primary-ringed. |
| OQ-EVENT-TYPE-AS-SCHEMA-FIELD | RESOLVED (per residency) | Each residency carries `event_type` metadata in engine output. §30 schema column for event_type per-residency could formalize this. Considered low-priority — engine output already exposes. |
| OQ-OTHER-PLANET-CYCLIC-N | EXTENDED | 4 residencies now confirmed (Venus, Mercury, Mars, Moon). Jupiter Ring 8 (12yr zodiac circuit) + Saturn Ring 7 (29.5yr orbital) still pending — each substrate-canonical at canon §23b. |
| OQ-COMPOSITIONAL-AXIS-MIXED | OPEN (carried) | Saturn Ring 7 "Moon-synodic mirror" hint may surface mixed spatial+temporal composition. |
| OQ-CYCLIC-SYZYGY-LIVING | CONFIRMED | Substrate-discipline meta-rule (Urania, FINDINGS_014): canonical names are LIVING under substrate-pressure-test. Lunar probe confirms name passes; no further rename. |

## What this validates substrate-discipline-wise

1. **Substrate-derivable composite N-values exist** — Lunar 12 = Solar 360t / Lunar 30t. Adds a new mechanism for finding substrate-canonical N-cycles beyond primary-ring entries.

2. **Cross-event-type umbrella substrate-confirmed** — `syzygy` covers 3 distinct event-types (inferior conjunction + opposition + new-moon-conjunction) at 4 residencies. Umbrella name passes substrate-pressure-test at all 4.

3. **Canonical name living-test passes at Lunar** — Erato 4b extension working as designed. Substrate-discipline meta-rule operating substantively.

4. **Substrate-discovery accelerates** — engine-build pattern → cross-residency probe → field-comparison → substrate-finding. Repeatable template. 14 findings docs across 13 distinct substrate-residencies/cascades probed in single day.

## What to build next

Options remaining for temporal-cyclic family:

1. **Jupiter Ring 8 probe** — 4320t / 12yr / zodiac circuit "1yr/sign × 12". Canon §23b line 954. N=12 substrate-canonical (per canon: 12 sign-traversals per 12-year Jupiter cycle, 1 sign-traversal per year). 5th residency for cyclic-syzygy-activate? OR — different event-type (sign-traversal, NOT syzygy), may surface new function-class.

2. **Saturn Ring 7 probe** — 10620t / 29.5yr / "full orbital / Moon-synodic mirror" (canon §23b line 953). Substrate-novel territory: fractal-mirror between Saturn and Moon. May surface mixed-compositional-axis (spatial+temporal blend).

3. **Uranus Ring 6 probe** — 30240t / per canon line 906. Outer-planet ring cycle.

4. **Audit-pass backfill in Nammu** — now substantively unblocked (Erato gate 3/3 exceeded with 4 canonical). Run card_audit grow function_class field check + backfill existing locks.

5. **Pause** — comprehensive substrate-architecture in §30 substantially complete; 4 canonical entries + 4 syzygy residencies + 2 schema columns.

Recommend (1) Jupiter probe — Jupiter Ring 8 N=12 has SAME N as Lunar Ring 1/Ring 2 ratio (both N=12). If shape matches, **N=12 has 2 different planet residencies at same N value**. Substrate-meaningful (Jupiter-Moon resonance pattern? canon mentions Saturn-Moon mirror; Jupiter-Moon at same N=12 may surface another substrate-resonance).
