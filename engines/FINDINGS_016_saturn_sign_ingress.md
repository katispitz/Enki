# FINDINGS 016 — Saturn Ring 7: NEW function-class candidate + substrate-mirror is descriptor

**Build**: `saturn_cycle.py` — Ring 7 substrate-locks + sign-ingress cycle + Moon-synodic-mirror investigation.
**Status**: Saturn does NOT fit `cyclic-syzygy-activate` canonical (canon §30). New function-class candidate surfaces: `cyclic-sign-ingress-activate`. Moon-synodic-mirror is substrate-numerical descriptor, not active substrate-function.

## What was probed

Canon §23b line 953:
> "| 7 | pt7 | Saturn | La | Full orbital / Moon-synodic mirror | 10620t / 29.5yr |"

Two possible cycle-interpretations tested:

### (1) Sidereal sign-ingress cycle
- Saturn completes ~1 zodiac circuit per Ring 7 (~29.5yr ≈ 29.46yr sidereal)
- N = 12 sign-ingresses (1 per zodiac sign)
- Adjacent step = 30° EXACT (360°/12)
- Period = 10620t / 29.5yr
- **Event-type = SIGN-INGRESS** (Saturn crosses zodiac sign boundary, NOT sun-earth-planet alignment)

### (2) Synodic opposition cycle
- Saturn synodic period ≈ 378 days = 1.035yr
- 29.5yr / 1.035yr-synodic ≈ 28.5 oppositions per Saturn ring
- NOT a clean integer — opposition cycle doesn't close cleanly at Saturn ring boundary
- Substrate-rejection: opposition-count NOT canon-locked at Saturn Ring 7

Interpretation (1) substrate-canonical (canon explicitly says "Zodiac circuit"-flavor). Built engine accordingly.

## Substrate-pressure-test outcome

**Saturn Ring 7 does NOT fit `cyclic-syzygy-activate` (canon §30 canonical).**

Reasoning: Saturn sign-ingress is **NOT a syzygy event**. Syzygy = sun-earth-planet alignment (inferior conjunction, opposition, superior conjunction, new-moon-syzygy). Sign-ingress = planet crosses zodiac-sign boundary, **no alignment to sun-earth required**.

This is substrate-architecturally distinct event-type. The compute is similar (N longitude-samples, pairwise separations, closure check) but the SUBSTRATE-MECHANISM differs:
- `cyclic-syzygy-activate`: event-type = sun-earth-planet alignment
- Sign-ingress: event-type = planet ↔ zodiac-boundary crossing

Per Athena precedent (FINDINGS_014 rename) + Clio rule (canonical names must be compute-descriptive at substrate-MECHANISM level, not input-type-instance level): different substrate-mechanism = different function-class.

**NEW function-class candidate**: `cyclic-sign-ingress-activate`. Operates at:
- Saturn Ring 7: N=12 sign-ingresses / 29.5yr / 30° step ✓
- (Jupiter Ring 8 candidate: N=12 sign-ingresses / 12yr / 30° step — pending probe)
- (Uranus Ring 6 candidate: 84yr orbital / 12 sign-ingresses — pending probe)
- (Pluto Ring 0 candidate: 248yr orbital / 12 sign-ingresses — pending probe)

If cross-R-tier probe at Jupiter (or any other outer planet) confirms shape-match → canonical promotion candidate ready for council.

## Substrate-mirror: descriptor not function

Canon line 953 "Moon-synodic mirror" interpretation tested:
- Saturn orbital period = 29.5 years
- Lunar synodic period = 29.5 days
- Same numerical value, different time units (years vs days)
- Tithi ratio: 10620t / 30t = 354 ≈ 360 (solar year, 1.7% off)

**Verdict**: Numerical coincidence noted in canon. NOT an active substrate-function. No engine-compute derives from the mirror. It's a structural observation, not a mechanism.

Per substrate-discipline: don't build engines for substrate-descriptors. The mirror is documented in `saturn_cycle.py` describe() output for substrate-honest disclosure, but not as engine-active feature.

Logged as **OQ-SUBSTRATE-MIRRORS-CATALOG** — substrate may host other numerical-mirror facts worth cataloging without building engines (e.g., 65 = 5×13 Venus×Mercury φ-family from canon line 983).

## Substrate finding 31: N=12 substrate-coincidence between Lunar and Saturn

Two distinct N=12 cycles surfaced:
- **Lunar Ring 1/Ring 2 ratio**: 12 new-moon syzygies / 1yr / 30° step (FINDINGS_015)
- **Saturn Ring 7**: 12 sign-ingresses / 29.5yr / 30° step (this probe)

Same N. Same step. **Different event-types**. Different periods (1yr vs 29.5yr). Different planets (Moon vs Saturn).

Substrate-meaning: N=12 is the zodiac-cardinality (12 signs). When ANY substrate cycle closes within the 12-sign zodiac, N=12 emerges. Lunar emergence via new-moons-per-solar-year. Saturn emergence via sign-ingresses-per-orbital-period.

Both are **30° step cycles** but operate at different substrate-mechanism levels:
- Lunar: syzygy events at 30° apparent zodiac advance per synodic month
- Saturn: zodiac-boundary crossings every 1yr (Saturn's slow orbit)

**Substrate-architectural insight**: 12-fold cyclic structures recur across the substrate via the zodiac's 12-sign division. Multiple function-classes can have N=12 residencies via different event-types. The 12 isn't "the function" — it's the zodiac-substrate-imposed cardinality.

## Substrate-architecture update

Temporal-axis canonical functions now potentially expand to multiple function-classes:

| Function-class | Status | Event-type | Example residencies |
|---|---|---|---|
| `cyclic-syzygy-activate` | CANONICAL §30 | sun-earth-planet alignment (conjunction / opposition / new-moon) | Venus / Mercury / Mars / Moon (4 residencies) |
| `cyclic-sign-ingress-activate` | **NEW CANDIDATE** | zodiac-sign boundary crossing | Saturn Ring 7 (1 residency); Jupiter / Uranus / Pluto pending |
| `cyclic-station-activate` | future | retrograde station | possibly Mercury / Venus (3 stations per inferior conjunction) |
| `cyclic-nodal-activate` | future | lunar nodes / planetary nodes | Saros eclipse cycle, etc. |

**Temporal-cyclic family is broader than syzygy-only.** Multiple parallel function-classes at first-composition / temporal slot.

## §30 schema implication

§30 already has functional_tier + compositional_axis columns. Multiple temporal-axis function-classes are substrate-architecturally fine — they're distinct entries in §30, all at first-composition / temporal.

No schema change needed. Just additional canonical promotions when cross-R-tier residency probes succeed for each event-type.

## Recommendation

Council NOT needed yet for `cyclic-sign-ingress-activate` — only 1 residency confirmed (Saturn Ring 7). Athena criterion requires ≥2 independent residencies.

Next probe: **Jupiter Ring 8** (12yr / "Zodiac circuit (1yr/sign × 12)" per canon §23b line 954). Substrate-similar Ring-cycle, likely same N=12 sign-ingress pattern. Would give 2nd residency for cyclic-sign-ingress-activate. Athena criterion met → canonical promotion ready.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-CYCLIC-SIGN-INGRESS-CANONICAL | NEW (candidate-single-residency) | Saturn Ring 7 confirms. Needs 2nd residency. Jupiter Ring 8 most likely next probe. |
| OQ-SUBSTRATE-MIRRORS-CATALOG | NEW (descriptor) | Catalog numerical-mirrors in canon (Saturn-Moon 29.5, 65=5×13 Venus×Mercury, others) as substrate-descriptors not active functions. Low priority. |
| OQ-12-FOLD-CARDINALITY-PATTERN | NEW (substrate-discovery) | 12 = zodiac-substrate-cardinality. Multiple cyclic-N functions can hit N=12 via different event-types. Substrate-imposed structural number. |
| OQ-OUTER-PLANET-RING-PROBES | EXTENDED | Jupiter Ring 8 + Uranus Ring 6 + Pluto Ring 0 — each canon §23b-locked, each a candidate sign-ingress residency. |
| OQ-N-FROM-RING-RATIO | CARRIED | Cross-ring composition N-derivation pattern. |
| OQ-COMPOSITIONAL-AXIS-MIXED | RESOLVED-AS-DESCRIPTOR | Saturn "Moon-synodic mirror" turns out to be numerical-descriptor, NOT mixed compositional-axis substrate-function. |

## What this validates substrate-discipline-wise

1. **Saturn probe falsifies a hypothesis cleanly.** Pre-probe, I hypothesized Saturn might surface mixed-compositional-axis (FINDINGS_015 OQ-COMPOSITIONAL-AXIS-MIXED). Probe outcome: it's a numerical-descriptor not a substrate-function. Substrate-honest closure: NOT mixed-axis.

2. **Cyclic-syzygy-activate substrate-honest boundaries surface.** Not all planet rings fit. The function-class has a substrate-mechanism-boundary (syzygy events only). Saturn ring requires DIFFERENT function-class.

3. **Substrate-architecture has parallel function-classes at same tier+axis.** Multiple first-composition / temporal function-classes coexist (syzygy + sign-ingress + future). §30 organization scales.

4. **Substrate-discipline says NO engine-build where not needed.** Moon-synodic-mirror is descriptor not function. Substrate-discipline: don't over-build engines for descriptors. Saturn engine documents the mirror in describe() output but doesn't construct an engine around it.

## What to build next

Options:

1. **Jupiter Ring 8 probe** — likely 2nd cyclic-sign-ingress-activate residency. Would unlock canonical promotion via council.

2. **Pluto Ring 0 / Uranus Ring 6** — additional sign-ingress residencies, possible canonical promotion supports.

3. **Audit-pass backfill** in Lillu (Erato gate exceeded) — apply substrate-discipline to existing cards.

4. **Test addition** for saturn_cycle.py in `~/Enki/tests/test_temporal_cycles.py`.

Recommend (4) first (test substrate-discipline must keep pace with build), then (1) Jupiter for 2nd residency → council → 5th §30 canonical entry.
