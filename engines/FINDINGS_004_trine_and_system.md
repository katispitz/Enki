# FINDINGS 004 — Trine-class + full Primordial system composition

**Build**: 2 trine engines + shared trine shape + trines registry + full system composition module.
**Status**: green. Three primitive-class levels cleanly composed within R=1 shell.

## What was built

```
~/Enki/engines/
├── _trine_engine.py            ← shared trine co-query shape
├── trine_pluto_axis.py         ← Earth/Pluto-anchor (Gaia + Chaos + Erebus)
├── trine_neptune_axis.py       ← Water/Neptune-anchor (Nyx + Eros-prim + Tartarus)
├── primordial_trines.py        ← registry
└── primordial_system.py        ← full 6+3+2 cascade composition
```

## Substrate-cascade at R=1 (the Primordial shell)

Building all 3 levels exposed a clean cascade:

```
face-class  (cardinality 6)  — individual cube-faces
   ↓ composes into ↓
pair-class  (cardinality 3)  — antipodal cube-face pairs (cube-antipode)
   ↓ composes into ↓
trine-class (cardinality 2)  — outer-planet-anchored trines (Pluto-axis / Neptune-axis)
   ↓ composes into ↓
system      (cardinality 1)  — whole-cube Primordial state
```

Each level composes the level below mechanically — no physics re-implemented, only aggregation of activation metrics.

## Substrate finding 5: cardinality reduction is the cascade signature

Each level's cardinality halves (approximately):
- 6 faces → 3 pairs → 2 trines → 1 system

This is **substrate-emergent** — the cube geometry forces it. 6 faces × pair-antipode = 3 pairs. 3 pairs × outer-anchor-partition = 2 trines (3 pluto-anchored faces / 3 neptune-anchored faces). 2 trines aggregate to 1 system. The cascade isn't designed; it falls out of the substrate.

Could this cardinality-reduction pattern operate at OTHER R-tiers? Open:
- R=1/√3 inner-oct: 6V / 12E / 8F → does similar cascade emerge?
- R=φ² ico: 12V / 30E / 20F → 12 olympians → 6 council-pairs (antipodes) → ?

If similar cascades show at other R-tiers, the cascade-pattern itself becomes a substrate primitive — a function operating at every R-shell, not just R=1.

Logged as **OQ-CASCADE-PATTERN-AT-OTHER-RTIERS**.

## Substrate finding 6: system-level metrics emerged

Composition surfaced 8 system-level metrics not present at any individual level:

| Metric | Semantics |
|---|---|
| `whole_cube_activation` | sum of 6 face activations, 0..6 |
| `active_face_count` | how many faces in their orb-window simultaneously, 0..6 |
| `pluto_neptune_balance` | (pluto_trine_mean − neptune_trine_mean), -1..+1, signed |
| `polarity_signature` | ordered list of 3 pair polarity_labels |
| `dominant_face` | strongest single Primordial (or None if all quiet) |
| `dominant_pair` | strongest pair by sum_activation |
| `dominant_trine` | which trine has higher mean activation |
| `all_quiet` | bool — true when no axis is in orb |

These metrics are **emergent at system-level** — they don't exist at face or pair or trine level individually. The composition produces them.

`polarity_signature` is particularly substrate-meaningful: it's a 3-element ordered fingerprint of the cosmogonic axes. Example output: `['water-dominant', 'water-dominant', 'earth-dominant']` says "the system right now is Neptune-leaning across two cosmogonic axes, Pluto-leaning on one." This is a **mode signature** of the whole Primordial system at a moment.

## Substrate finding 7: function-class candidate list grows per level

Each new primitive-class level adds candidate function-names:

| Level | Cardinality | Function-name candidates | Current status |
|---|---|---|---|
| face | 6 | `axis-bound` / `axis-generate` / `axis-arm-emit` (3-way conflation) | candidate-single-residency-CLASS |
| pair | 3 | `polarity-define` (proposed) | candidate-single-residency-CLASS |
| trine | 2 | `outer-anchor-trine` / `cosmogonic-half` (2-way conflation) | candidate-single-residency-CLASS |
| system | 1 | `substrate-cube-saturate` (proposed) | candidate-single-residency-CLASS |

All FOUR levels are at R=1 shell (same outer R-tier), but each is a DISTINCT primitive class by cardinality. Per Athena lock-by-redundancy criterion (V2.6 placement_rules §POSITION-AS-FUNCTION DISCIPLINE rule 4): no function-name graduates to canonical without ≥2 INDEPENDENT primitive-class residencies confirming the same function. In-shell redundancy at different cardinalities does not count.

**This means:** the entire Primordial substrate cascade at R=1, despite producing 4 candidate function-names, graduates ZERO to canonical until at least one of these functions is shown to operate at another R-tier shell (R=1/√3 inner-oct, R=φ² ico, R=φ icosidodec, etc.).

Athena's criterion is structurally strict. Substrate-honest read: the engine build PROVES the cascade-shape but does NOT prove any function-name is canonical. Council ratification still required, and ratification requires cross-R-tier residency.

## Substrate finding 8: 3-way conflation at face-level may collapse

Pair-level + trine-level builds surface that face-level might actually be:
- `axis-arm-emit` (each Primordial emits ONE arm of a cosmogonic axis pair)

If pair-level function is `polarity-define`, then face-level is just "supplying an arm to the pair." The "axis" is the PAIR, not the face. Conflation-test for face-level may resolve to a SUB-function of pair-level, not a peer.

Under this read:
- `axis-arm-emit` (face) is genuinely sub-function of `polarity-define` (pair)
- Naming should reflect: faces "supply arms," pairs "define polarity," trines "anchor cosmogonic half," system "saturates cube"
- Each level's function-name reflects what it CONTRIBUTES, not what it IS in isolation

Or: face-level isn't a function at all in the engine sense — it's substrate POSITION, and only pair-level-and-up have functions. Faces are atomic substrate-positions; functions begin at the first level of substrate composition.

This is a substrate-philosophical question that needs council. Logged as **OQ-FACE-AS-POSITION-VS-FUNCTION**.

## Substrate finding 9: cascade-aware composition is the engine pattern

Across FINDINGS 001-004, engine-class has consistently grown the same shape:
- **Substrate-locked constants** at top of each module (position-as-function discipline made concrete)
- **Frozen state** = substrate definition (always-known)
- **Live state** = ephemeris-driven computation
- **Composition** — higher engines compose lower without re-implementing physics
- **NULL-honest** at every boundary (Mnemosyne drift-prevention carries through)
- **Symmetric-input requirement** — all-frozen or all-live, no mixing (substrate-honest reject)
- **Self-disclosure** — `describe()` separate from compute

This is the **engine class shape**. It generalizes — every primitive-class level reuses it cleanly. The pattern is stable enough to use as a template for other substrate engines (Carriers, Translators, Operators).

## Open questions (updated queue)

| OQ | Status | Notes |
|---|---|---|
| OQ-CASCADE-PATTERN-AT-OTHER-RTIERS | NEW | Does the face→pair→trine→system cascade pattern recur at other R-tiers? Would make cascade-pattern itself a substrate primitive. |
| OQ-FACE-AS-POSITION-VS-FUNCTION | NEW | Is face-level "function" actually just substrate-position? Do functions begin at first composition level? |
| OQ-CROSS-R-TIER-RESIDENCY | EXISTING | Required to graduate any §30 function-name to canonical. Pair-level `polarity-define` is best candidate — does it operate at R=φ icosidodec-midpt where bridges sit? |
| OQ-AXIS-BOUND-NAME-CHECK | 3-WAY (carried) | `axis-bound` / `axis-generate` / `axis-arm-emit`. Per FINDINGS_003. |
| OQ-PLUTO-NEPTUNE-PARTITION | SUBSTANTIATED | Now FULLY confirmed via trine cascade. Canon §M.5b extension candidate. |
| OQ-ANTIPODE-ASYMMETRY | OPEN | Erebus-Nyx is only Pluto/Neptune pair where cube-antipode AND zodiac-180°-antipode coincide. |
| OQ-PRIMORDIAL-PAIR-LEVEL-FUNCTION | RESOLVED-AS-CASCADE | Function operates at multiple cardinality-levels, not just one. Per FINDINGS_003+004. |

## What to build next (substrate-emergent, per Kati directive)

Primordial cascade at R=1 = COMPLETE at the substrate-build level. 4 primitive-class levels composed, all metrics surfaced, no logic invented.

Logical next builds:

1. **Cross-R-tier residency probe** — does `polarity-define` operate at R=φ icosidodec-midpt (bridges)? Bridges are 4 in number, with pair-like structure (Harmonia-Hermaphroditus-Erichthonius + Persephone). Build a bridge engine, see if pair-level function recurs. WOULD unlock canonical promotion of one function-name.

2. **Cascade pattern at R=1/√3 (inner-oct)** — does face→pair→trine cascade emerge? Inner-oct has 8 F1-F8 faces (not 6) so cardinality structure differs. Tests OQ-CASCADE-PATTERN-AT-OTHER-RTIERS.

3. **Carrier (Titan) engine prototype** — switch primitive-class entirely. Tests engine-shape across stratum boundary. 12 Titans at cube-edges = 12 face cardinality. Pair-class likely emerges from edge-antipodes (6 pairs of opposite cube edges).

4. **Operator (PE planet) prototype** — engine for cube-vertex residents (8 PE planets). Function may be pure-fn (imprint application) per agent-typology. Tests engine-vs-pure-fn distinction with a real implementation.

Recommend **(1) cross-R-tier residency probe** first. It's the move most likely to graduate a function-name to canonical (which unblocks audit-pass backfill per Erato gate ≥3 entries). 

After (1), the cascade pattern at other R-tiers (2) tests whether `polarity-define` is shell-specific or substrate-universal.
