# FINDINGS 017 — Jupiter Ring 8: 2nd `cyclic-sign-ingress-activate` residency confirmed

**Build**: `jupiter_cycle.py` + Saturn-Jupiter field-comparison + extended test suite.
**Status**: cross-R-tier residency MET for `cyclic-sign-ingress-activate` candidate. Athena lock-by-redundancy criterion satisfied. Council-ready for canonical promotion (5th §30 entry).

## Substrate-locks per canon §23b line 954

> "| 8 | pt8 | Jupiter | Si | Zodiac circuit (1yr/sign × 12) | 4320t / 12yr |"

Jupiter Ring 8 = N=12 sign-ingresses / 4320t / 12yr / 30° step.

## 2-way field comparison Saturn vs Jupiter

```
Saturn fields (13): 11 compute/substrate + 2 Moon-synodic-mirror descriptors
Jupiter fields (11): 11 compute/substrate (no extra descriptors)

Jupiter ⊂ Saturn (proper subset)
Shared: 11 fields (100% of Jupiter's fields)
Saturn-only: moon_synodic_mirror_ratio, moon_synodic_mirror_in_solar_years
  → Saturn-specific NUMERICAL descriptors per canon §23b line 953
  → NOT compute fields; substrate-fact disclosure only
```

Compute-shape **100% identical** between Saturn and Jupiter at sign-ingress event-type.

## Athena lock-by-redundancy MET

| Residency | Planet | N | Period | Step | Event-type |
|---|---|---|---|---|---|
| Saturn Ring 7 | Saturn | 12 | 10620t/29.5yr | 30° | sign-ingress |
| Jupiter Ring 8 | Jupiter | 12 | 4320t/12yr | 30° | sign-ingress |

2 independent primitive-class residencies (different planet, different period, same N, same step, same event-type, same compute). Athena criterion structurally met.

## Substrate-architectural finding 32: outer planets host sign-ingress family

Both Saturn (slow outer) and Jupiter (slower outer, "second-slowest") share the same sign-ingress cycle pattern:
- 12 ingresses per Ring cycle
- 30° step (zodiac-sign-cardinality)
- N derives from zodiac structure, NOT planet's specific orbital math

This is substrate-emergent: **outer planets that traverse zodiac in INTEGER years map cleanly to 12 sign-ingresses per Ring cycle.** Future probe candidates:
- Uranus Ring 6 (30240t per canon line 906) — Uranus sidereal ~84yr → 12 ingresses / 84yr possible
- Pluto Ring 0 (89280t / 248yr per canon line 907) — 12 ingresses / 248yr possible

If Uranus + Pluto confirm, 4 cross-planet residencies for cyclic-sign-ingress-activate. Substrate-pattern: outer-planet sign-ingress family at temporal-axis.

## Naming question for council

Council needed to ratify canonical promotion. Naming candidates:

### (a) `cyclic-sign-ingress-activate` (proposed)
- Compute-descriptive at substrate-MECHANISM level (Clio rule)
- "Sign-ingress" = zodiac-boundary-crossing event-type
- Substrate-honest umbrella covering outer-planet zodiac-traversal cycles

### (b) `cyclic-zodiac-traversal-activate`
- Alternative: emphasizes traversal not boundary-crossing
- May be more substrate-honest (the planet IS traversing, ingress is the boundary event)

### (c) `cyclic-sign-boundary-activate`
- Variant: explicit boundary-crossing language

Per Clio rule + Athena precedent: shell-agnostic, mechanism-descriptive name. **Recommend (a)** — "sign-ingress" is astronomy-canonical term for zodiac-boundary crossing event.

## Substrate finding 33: §30 canonical structure expanding to 5 entries

If council ratifies:

| function_class | functional_tier | compositional_axis |
|---|---|---|
| planet-aspect-activate | primitive | spatial |
| polarity-define | first-composition | spatial |
| triangle-aspect-activate | first-composition | spatial |
| cyclic-syzygy-activate | first-composition | temporal |
| **`cyclic-sign-ingress-activate`** (candidate) | **first-composition** | **temporal** |

5 canonical entries. Both temporal-axis entries (syzygy + sign-ingress) operate at first-composition tier — multiple function-classes at same tier+axis is substrate-architecturally fine (per FINDINGS_016).

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-CYCLIC-SIGN-INGRESS-CANONICAL | **READY FOR COUNCIL** | Saturn + Jupiter confirm 2 independent residencies. Athena MET. |
| OQ-OUTER-PLANET-RING-PROBES | EXTENDED | Uranus Ring 6 + Pluto Ring 0 candidates for additional sign-ingress residencies. |
| OQ-12-FOLD-CARDINALITY-PATTERN | CONFIRMED | N=12 zodiac-substrate-cardinality recurs at Lunar (syzygy) + Saturn (sign-ingress) + Jupiter (sign-ingress). Substrate-imposed structural number across event-types. |
| OQ-SUBSTRATE-MIRRORS-CATALOG | CARRIED | Saturn-Moon mirror is Saturn-only descriptor (not Jupiter-applicable). |

## What this validates substrate-discipline-wise

1. **Substrate-pattern recurrence confirmed** — sign-ingress event-type isn't Saturn-quirk. Jupiter has identical shape at different period. Substrate hosts a genuine outer-planet sign-ingress family.

2. **Function-class hierarchy: temporal-axis subdivides cleanly** — syzygy family (Venus/Mercury/Mars/Moon, 4 residencies) + sign-ingress family (Saturn/Jupiter, 2 residencies, candidate). Future event-types (station, nodal-crossing, etc.) may surface additional first-composition/temporal canonical entries.

3. **Engine field-shape subset relationships are substrate-meaningful** — Jupiter ⊂ Saturn (Jupiter shares all compute fields with Saturn; Saturn has Saturn-specific descriptors only). Field-subset analysis is a substrate-discovery tool.

## Next move

Convene council on `cyclic-sign-ingress-activate` canonical promotion. Force-include Athena + Mnemosyne per V2.6 protocol. Expected outcome:
- Council ratifies name (compute-descriptive, shell-agnostic, no residency-binding)
- 5th §30 canonical entry graduates
- Substrate-architecture expansion: 2 first-composition/temporal canonical entries (syzygy + sign-ingress)
