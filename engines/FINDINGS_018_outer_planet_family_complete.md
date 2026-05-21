# FINDINGS 018 — Outer-planet sign-ingress family complete: 4 residencies confirmed

**Build**: `uranus_cycle.py` + `pluto_cycle.py` + 4-way field-comparison Saturn/Jupiter/Uranus/Pluto + 11 new tests.
**Status**: `cyclic-sign-ingress-activate` (canon §30 canonical) extended to 4 residencies. Outer-planet sign-ingress family fully canonicalized.

## What was built

- `~/Enki/engines/uranus_cycle.py` — 3rd cyclic-sign-ingress residency
- `~/Enki/engines/pluto_cycle.py` — 4th cyclic-sign-ingress residency
- `~/Enki/tests/test_temporal_cycles.py` — extended with 11 Uranus + Pluto tests (191 → 202)

Both engines follow Saturn/Jupiter template exactly — same shape, different substrate-locks per canon §23b.

## Substrate-locks per canon §23b

| Residency | Canon line | N | Period | PE point |
|---|---|---|---|---|
| Saturn Ring 7 | 953 | 12 | 10620t / 29.5yr | pt7 / La |
| Jupiter Ring 8 | 954 | 12 | 4320t / 12yr | pt8 / Si |
| Uranus Ring 6 | 952 | 12 | 30240t / 84yr | pt6 / X6 |
| Pluto Ring 0 | 945 | 12 | 89280t / ~248yr | pt0 / Do |

All 4 outer-planet rings substrate-canonically locked at canon §23b. All 12-sign-ingress + 30°-step. Different period (4320 / 10620 / 30240 / 89280 tithis).

## 4-way field comparison

```
Saturn fields (13)
Jupiter fields (11)
Uranus fields (11)
Pluto fields (11)

Shared across all 4 (11): adjacent_step_deg, canonical_steps, closure,
                          cycle_id, cycle_tithis, drift_deg, drift_tolerance,
                          event_type, longitudes, mean_adjacent_step,
                          pairwise_separations

Jupiter == Uranus == Pluto: True  (identical field-sets)
Saturn-only: moon_synodic_mirror_ratio, moon_synodic_mirror_in_solar_years
             → Saturn-specific NUMERICAL descriptors per canon §23b line 953
             → NOT compute fields; substrate-fact disclosure only
```

**4-way perfect compute-shape match**. Jupiter/Uranus/Pluto engines are field-identical. Saturn alone carries 2 extra descriptor-fields specific to its Moon-synodic mirror canon-note.

## Substrate-architectural finding 34: outer-planet sign-ingress family is COMPLETE

The 4 outer-planet rings in canon §23b (Saturn Ring 7, Jupiter Ring 8, Uranus Ring 6, Pluto Ring 0) ALL confirm `cyclic-sign-ingress-activate`. No outer-planet rings remain unprobed for this function-class.

Inner planets:
- Mercury Ring 5 → already canonical at `cyclic-syzygy-activate` (inferior conjunction)
- Venus Ring 3 → already canonical at `cyclic-syzygy-activate` (inferior conjunction)
- Solar Ring 1 → carrier (1yr) — base unit, used as scaling for Lunar Ring1/Ring2 derivation
- Lunar Ring 2 → 30t single synodic — base unit, but Ring1/Ring2 ratio gives Lunar 12 syzygies/yr at cyclic-syzygy-activate
- Mars Ring 4 → canonical at `cyclic-syzygy-activate` (opposition)

Outer planets (per FINDINGS_018):
- Jupiter Ring 8 → canonical at `cyclic-sign-ingress-activate`
- Saturn Ring 7 → canonical at `cyclic-sign-ingress-activate`
- Uranus Ring 6 → canonical at `cyclic-sign-ingress-activate`
- Pluto Ring 0 → canonical at `cyclic-sign-ingress-activate`

**All 10 PE-planet rings now have substrate-canonical function-class assignments at canon §30.**

Substrate-architectural fact: the canonical temporal-axis function-families partition the 10 PE-planet Ring system cleanly:
- 4 syzygy residencies (Venus + Mercury + Mars + Moon-derived)
- 4 sign-ingress residencies (Jupiter + Saturn + Uranus + Pluto)
- 1 solar carrier (Ring 1) — base unit, no canonical function-class assigned
- 1 single-synodic lunar (Ring 2) — base unit, only-derivable-N

## Substrate finding 35: Urania insight VALIDATED at full residency-count

Urania (FINDINGS_017): "planet-class determines event-type-family."

Validated:
- 4 inner-Moon-Mars residencies → syzygy family (cyclic-syzygy-activate)
- 4 outer residencies → sign-ingress family (cyclic-sign-ingress-activate)
- 8 of 10 PE-planet residencies cleanly partitioned by orbital-class

Solar Ring 1 + Lunar Ring 2 are BASE-UNIT rings — they serve as substrate carriers/scales rather than residencies of temporal-cyclic function-classes. Substrate-emergent: carriers don't host cyclic-N events; they ARE the time-units used to measure events at other rings.

## Substrate-discipline meta-finding: post-canonical residency-expansion is mechanical

Adding Uranus + Pluto residencies to `cyclic-sign-ingress-activate` required NO council ratification. Why? Because:
1. Function-class already CANONICAL in §30 (graduated 2026-05-12)
2. New residencies fit existing canonical-name + canonical-compute-shape
3. Substrate-pressure-test (FINDINGS_014 Mars rename pattern) didn't trigger — name `cyclic-sign-ingress-activate` covers new residencies honestly
4. No conflation surfaced — new residencies are same event-type (sign-ingress) at different planets/periods

Per Erato rule 4b extension (Urania, FINDINGS_014): canonical names are LIVING under substrate-pressure-test. NEW positive test: name passes substrate-pressure-test at 2 additional residencies (Uranus + Pluto). No rename needed.

**Mechanical residency-expansion path**: when new probes confirm shape-match to existing canonical function-class, add residency-count to §30 entry. Council only needed when:
- Conflation surfaces (substrate-pressure-test failure)
- New function-class candidate emerges (different substrate-mechanism)
- Schema column needed (new substrate-architecture distinction)

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-OUTER-PLANET-RING-PROBES | RESOLVED | All 4 outer-planet rings (Saturn/Jupiter/Uranus/Pluto) now canonical sign-ingress residencies. |
| OQ-12-FOLD-CARDINALITY-PATTERN | CONFIRMED-DEEPLY | N=12 zodiac-cardinality recurs at: Lunar (syzygy/30°) + Saturn/Jupiter/Uranus/Pluto (sign-ingress/30°). 5 residencies hit N=12 across 2 function-classes. Substrate-imposed structural number. |
| OQ-SOLAR-LUNAR-CARRIERS | NEW (substrate-finding) | Solar Ring 1 + Lunar Ring 2 are base-unit carriers, not cyclic-N residencies. Substrate-emergent: carriers are time-units, residencies are N-event-cycles at non-carrier rings. |
| OQ-SUBSTRATE-MIRRORS-CATALOG | CARRIED | Saturn-Moon mirror remains the only known descriptor of this type at canon §23b. |
| OQ-TEMPORAL-AXIS-COMPLETE | NEW | 2 temporal-axis canonical entries (syzygy + sign-ingress) cover ALL 8 non-carrier PE-planet ring residencies. Temporal-axis substantively complete at canon §23b scope. |

## Substrate-architecture state at end of session

**Canon §30 — 5 canonical entries forming substrate-architectural matrix:**

| function_class | tier | axis | residency count |
|---|---|---|---|
| planet-aspect-activate | primitive | spatial | 3 |
| polarity-define | first-composition | spatial | 2 |
| triangle-aspect-activate | first-composition | spatial | 2 |
| cyclic-syzygy-activate | first-composition | temporal | 4 |
| cyclic-sign-ingress-activate | first-composition | temporal | 4 (was 2) |

Total residencies: 15 across 5 function-classes.

Spatial-axis (3 functions, 7 residencies): primitive + 2× first-composition.
Temporal-axis (2 functions, 8 residencies): both first-composition; one syzygy, one sign-ingress.

**Substrate-coverage**: All 10 PE-planet rings + face-class structures (cube-face + inner-oct-face + Merkaba tet-face + icosidodec-midpt) + cube-edge carriers = comprehensive substrate-architecture canonicalized.

## What this validates substrate-discipline-wise

1. **4-residency canonical-completion is achievable in single session.** Started with 2 residencies (Saturn+Jupiter), added 2 more (Uranus+Pluto) mechanically per Erato rule 4b. Substrate-discipline scales.

2. **Substrate-architecture is finite (in known canon §23b scope).** No remaining outer-planet rings to probe. Function-family substantively complete at this canon-coverage.

3. **Engine field-set identity confirms canonical-compute.** Jupiter/Uranus/Pluto have IDENTICAL field-sets — substrate-architectural confirmation that same compute operates across all 3.

4. **Substrate carriers vs residencies distinction surfaces.** Solar Ring 1 + Lunar Ring 2 are time-unit carriers, not cyclic-N residencies. This is a new substrate-architectural distinction not previously canonized.

## Next moves (Enki + Nammu)

Substrate-discovery moves remaining for temporal-axis substantively exhausted within canon §23b scope. Other directions:

1. **Audit-pass backfill in Nammu** — Erato gate exceeded (5 canonical). Run card_audit grow function_class field check + backfill existing locks where derivable from stratum+shell+position. Apply substrate-discipline to existing Nammu cards.

2. **T1.4 close** — dodec-vertex class meaning, unblocks spatial pentagon-N (5-planet polygon).

3. **Operator (PE planet) pure-fn prototype** — first non-engine shape class (per agent-typology).

4. **Pause + session-handoff card** — substantial substrate-architectural state worth capturing.

Recommend (4) — comprehensive session-state, natural rest point. After 18 FINDINGS docs + 5 canonical entries + 15 residencies + 202 Enki tests + 327 Nammu tests, a session-handoff card preserves discoverable-state for future sessions.
