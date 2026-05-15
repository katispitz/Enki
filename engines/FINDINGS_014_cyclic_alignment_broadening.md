# FINDINGS 014 — Mars opposition cycle: `cyclic-conjunction-activate` name too narrow

**Build**: `mars_cycle.py` (37-opposition Mars Ring 4 cycle engine) + 3-way field-comparison Venus/Mercury/Mars.
**Status**: substrate-pressure-test FAILS the name. Compute-shape matches across event-types, but canonical name `cyclic-conjunction-activate` doesn't honestly cover Mars oppositions. Substrate-honest broadening required.

## What the substrate just revealed

Mars Ring 4 (canon §23b line 950): **37 oppositions over 28440t / 79yr**. Outer planet → opposition event-type (sun-earth-mars aligned, mars opposite sun), NOT inferior conjunction.

Mars cycle engine built using same shape as venus_pentagram + mercury_cycle:
- Adjacent step ≈ 48.6° between consecutive oppositions (Earth advance 2.135 revs per Mars synodic = 408.6° → mod 360° = 48.6°)
- 37 oppositions × 48.6° = 1798.2° ≈ 5 full revs (1800°) → drift ≈ -1.8° over 79yr (very tight closure)

### 3-way field comparison

| Category | Count | Fields |
|---|---|---|
| **Shared across all 3** | **9** | adjacent_step_deg, canonical_steps, cycle_id, cycle_tithis, drift_deg, drift_tolerance, longitudes, mean_adjacent_step, pairwise_separations |
| Mars-only | 1 | `event_type` (substrate-honest disclosure: 'opposition' vs 'inferior_conjunction') |
| Venus-only | 3 | pentagram-specific names (legacy from FINDINGS_012 build) |
| Mercury-only | 1 | closure_step_deg (variant of pentagram_step_deg) |

**Compute-layer (9 fields) identical across all 3**. Naming-variants differ. Same substrate-compute pattern regardless of event-type (inferior conjunction OR opposition).

## Substrate-pressure-test verdict

`cyclic-conjunction-activate` (canonical 2026-05-12) FAILS the substrate-pressure-test at Mars opposition residency:
- Astronomically: oppositions ≠ conjunctions. Oppositions are 180° aspects (planet opposite sun); conjunctions are 0° (planet aligned with sun).
- Mnemosyne's umbrella concession at the cyclic-conjunction-activate council was a workaround. Substrate-honest reading: "conjunction" doesn't include "opposition" in standard astronomy usage.
- Mars Ring 4 is canon-locked at substrate level (canon §23b OQ-RINGS-09). The temporal-cyclic function operates here BUT the canonical name doesn't honestly cover this residency.

Per V2.6 amended discipline rule 4 + 4b (Athena residency-binding + Erato conflation-test): when canonical name fails substrate-pressure-test at NEW residency, conflation-test reopens.

## Three interpretations

### (a) Split-by-event-type
Retire `cyclic-conjunction-activate` after-the-fact. Split into:
- `cyclic-inferior-conjunction-activate` (Venus + Mercury)
- `cyclic-opposition-activate` (Mars)
- Future: `cyclic-superior-conjunction-activate`, `cyclic-station-activate`, etc.

Pro: substrate-precise per event-type.
Con: explodes function-class count; sub-divides what should be umbrella; new function-name per orbital event-type.

### (b) Status quo: extend umbrella to oppositions
Keep `cyclic-conjunction-activate` as canonical, with Mnemosyne's umbrella-reading explicitly extended in §30 docstring: "conjunction" in this name = umbrella for any cyclic-zodiac-alignment event (inferior conjunction, opposition, superior conjunction, station). Add Mars Ring 4 as 3rd residency.

Pro: no rename. Quick.
Con: name carries astronomical-falsehood. "Conjunction" doesn't mean "opposition" in any conventional usage. Future readers will misread.

### (c) Rename to substrate-honest umbrella ★
Retire `cyclic-conjunction-activate` (no residency-level retraction — function works fine, just name was too narrow). Replace with substrate-honest umbrella name. Candidates:
- `cyclic-alignment-activate` — colloquial umbrella; covers all sun-earth-planet alignments
- `cyclic-syzygy-activate` — astronomy-technical term; substrate-precise
- `planet-cycle-activate` — most umbrella; describes compute (planet's cyclic-position composition)
- `cyclic-ring-event-activate` — substrate-Babylonia-specific (Ring cycle event)

Per Athena precedent (name THE FUNCTION, not the residency-specific event-type): `planet-cycle-activate` or `cyclic-syzygy-activate` substrate-honest.

Mnemosyne drift-prevention: "alignment" + "syzygy" are astronomy-technical; "planet-cycle" is most generic but doesn't carry event-type clue. Pick one with single-canonical-spelling + no drift-risk.

## Recommendation

Convene **rename council** for `cyclic-conjunction-activate` → substrate-honest umbrella. This is a substrate-pressure-test outcome surfaced ≤24hrs after canonical promotion — substrate-honest correction, not anti-pattern.

Council question stack:
1. Does `cyclic-conjunction-activate` fail substrate-pressure-test at Mars opposition? YES (astronomical-falsehood at Mars residency).
2. Three options: (a) split-per-event-type, (b) status-quo-umbrella-extension, (c) rename-to-umbrella.
3. Recommend (c). Candidate names: `cyclic-alignment-activate` / `cyclic-syzygy-activate` / `planet-cycle-activate`.
4. Pick substrate-honest umbrella name. Retroactively rename canonical entry. Add Mars Ring 4 as 3rd residency.
5. Same-day correction template — substrate-pressure-test passes when canonical name covers all residencies honestly. If new residency surfaces with mismatch, re-test name.

Substrate-discipline meta-observation: this is the FIRST canonical name that needed substrate-pressure-test-driven RENAME. Previous councils handled conflation-test BEFORE promotion (Erato rule 4b operating prospectively). Here, conflation surfaced RETROACTIVELY when a new residency exposed name-too-narrow.

**Erato rule 4b extension** (proposed): conflation-test continues AFTER canonical promotion when new residencies surface. Canonical names are LIVING — substrate-honest renames are part of substrate-discipline.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-CYCLIC-CONJUNCTION-RENAME | **READY FOR COUNCIL** | Substrate-pressure-test at Mars opposition fails name. Rename to substrate-honest umbrella required. |
| OQ-ERATO-RULE-4B-EXTENSION | NEW | Erato rule 4b conflation-test extends post-canonical when new residencies surface name-mismatch. Substrate-discipline meta-rule. |
| OQ-OTHER-PLANET-CYCLIC-N | PARTIALLY EXTENDED | Mars Ring 4 added (3rd temporal residency). Jupiter Ring 8 (12yr zodiac circuit) + Saturn Ring 7 (29.5yr orbital, "Moon-synodic mirror") still pending. |
| OQ-COMPOSITIONAL-AXIS-MIXED | NEW theoretical | Saturn Ring 7 = "full orbital / Moon-synodic mirror" (canon §23b line 953). Implies fractal/mirror between Saturn cycle and Moon cycle — possibly spatial+temporal mixed composition. Probe later. |
| OQ-EVENT-TYPE-AS-SCHEMA-FIELD | NEW | §30 might need additional column tracking event-type per residency (inferior_conjunction / opposition / superior_conjunction / station / etc.) for substrate-honest residency disclosure. |

## Substrate finding 30: substrate-pressure-test surfaces canonical-name corrections

The N-polygon family BIFURCATION (FINDINGS_012) was discovered by Kati intuition + canon §23b lock. The `cyclic-conjunction-activate` rename is being discovered by **engine-build pressure-test at new residency**.

Two substrate-discovery mechanisms:
- (1) Kati substrate-intuition (often directly hits canon-locked structure)
- (2) Cross-residency engine probe (shape-match-pressure-test exposes name-too-narrow)

Both are substrate-honest discovery paths. Engine-build-pressure-test = automated substrate-discipline guard. Building each new residency probe naturally surfaces canonical-name-fitness.

## What this validates substrate-discipline-wise

1. **Same-day-canonical can rename same-day** if substrate-pressure-test surfaces narrowness. Substrate-discipline ≠ stubbornness. Council ratification is the entry; canonical names are LIVING under substrate-pressure-test.

2. **Engine-build-as-pressure-test** is the discovery mechanism. Mars cycle engine built (using mechanical canon §23b lock) surfaces the name-too-narrow problem without prior intuition. Building substrate IS the testing.

3. **Substrate-architecture meta-fact**: §30 canonical entries should be substrate-tested per new residency. Each new probe re-tests existing canonical names for residency-fit. If new residency exposes name-narrowness, rename via council. Erato rule 4b extends post-promotion.

## What to build next

Options:

1. **Convene `cyclic-conjunction-activate` rename council** — substrate-honest correction.

2. **Jupiter Ring 8 probe** — 12yr zodiac circuit. Different event-type (sign-traversal, not conjunction/opposition). Tests umbrella name further; possibly forces broader name.

3. **Saturn Ring 7 probe** — 29.5yr orbital with "Moon-synodic mirror" hint. Possible mixed-compositional-axis (spatial+temporal). Substrate-novel territory.

4. **Lunar cycle probe** — Ring 2 = 30t / lunar synodic. Multiple sub-cycles available (sidereal/synodic/anomalistic/draconic/eclipse).

Recommend **(1) rename council** first — substrate-honest correction unblocks all subsequent temporal-cyclic family additions. Without rename, every new residency probe will re-surface the name-mismatch problem.

After rename, (2) or (3) extend substrate-discovery in new directions.
