# FINDINGS 003 — Pair-level substrate + 2 kinds of antipode

**Build**: 3 antipodal-pair co-query engines + shared pair engine + pairs registry.
**Status**: green. Composes existing Primordial engines; no new logic invented.

## What was built

```
~/Enki/engines/
├── _pair_engine.py            ← shared pair-level co-query shape (~160 lines)
├── pair_gaia_eros.py          ← Cosmogonic axis 1: Earth/Taurus ↔ Water/Pisces
├── pair_chaos_tartarus.py     ← Cosmogonic axis 2: Earth/Virgo  ↔ Water/Scorpio
├── pair_erebus_nyx.py         ← Cosmogonic axis 3: Earth/Capricorn ↔ Water/Cancer
└── primordial_pairs.py        ← registry: BY_NAME / BY_FACES / BY_PRIMORDIAL
```

Composition pattern: each pair-engine imports 2 Primordial engines + shared pair shape. No new physics, only new composition.

## New substrate fields surfaced (PairState)

Pair-level state adds 4 derived fields not present at face-level:

| Field | Semantics |
|---|---|
| `both_active` | bool — both axes within their orb-window simultaneously |
| `one_active`  | bool — exactly one axis firing (the other quiet) |
| `co_activation` | `min(earth, water)` — gated by weaker side. "Both must fire" reading. |
| `sum_activation` | `earth + water` — total signal across the cosmogonic axis. |
| `polarity` | `(earth - water) / sum`, normalized [-1, +1]. -1 = full water-only, +1 = full earth-only |
| `polarity_label` | `quiet` / `earth-dominant` / `water-dominant` / `balanced` |

`co_activation` and `sum_activation` are SUBSTRATE-DISTINCT semantics. Both meaningful, neither subsumes the other:
- co_activation = "are both sides of the cosmogonic axis present together?"
- sum_activation = "what's the total presence of this cosmogonic axis right now?"

Which one is "the pair activation" depends on downstream use. Substrate-honest: keep both, let consumer choose. Don't collapse prematurely.

## Substrate finding 1: 2 distinct kinds of antipode

Building the 3 pairs surfaced an asymmetry not previously named:

| Pair | Cube-antipode | Zodiac-180°-antipode | Same? |
|---|---|---|---|
| Gaia ↔ Eros-prim   | MQF0 ↔ MQF4 | Taurus ↔ Pisces   | **NO** (60° apart) |
| Chaos ↔ Tartarus   | MQF1 ↔ MQF5 | Virgo ↔ Scorpio   | **NO** (60° apart) |
| Erebus ↔ Nyx       | MQF2 ↔ MQF3 | Capricorn ↔ Cancer | **YES** (180° apart) |

Only Erebus ↔ Nyx has both kinds of antipode coinciding. The other two pairs are **partition-antipodes** (cube-opposite, but zodiac-60°-apart).

This is substrate-meaningful. The Pluto/Neptune outer-planet partition produces a coupling that breaks zodiac-180° symmetry for 2 of 3 pairs.

Substrate question (NEW OQ): why does Saturn/Moon pair (Erebus↔Nyx) preserve zodiac-180°-antipode while Venus/Jupiter + Mercury/Mars pairs don't? Possibilities:
- (a) Saturn ↔ Moon traditional rulership of Cancer/Capricorn axis is itself a deeper substrate feature
- (b) Cancer-Capricorn cardinal-axis (cardinal-quality signs) has structural priority
- (c) Coincidence — not all substrate symmetries hold across all 3 pairs

Logged as **OQ-ANTIPODE-ASYMMETRY** in queue.

## Substrate finding 2: pair-level is a NEW primitive-class

The 3 antipodal pairs constitute a primitive-class distinct from the 6 cube-face individuals:
- **Face-level primitive class**: R=1 cube-face. 6 residencies. Function: axis-generation per face.
- **Pair-level primitive class**: antipodal-pair-of-cube-faces (sub-structure within R=1). 3 residencies. Function: cosmogonic-axis polarity definition.

Both classes share R=1 shell BUT are DIFFERENT primitive classes by substrate cardinality (6 vs 3). Per Athena lock-by-redundancy criterion (V2.6 §POSITION-AS-FUNCTION DISCIPLINE rule 4), function-name graduates when ≥2 INDEPENDENT primitive-class residencies confirm. In-class redundancy doesn't count (6 faces alone do not graduate `axis-bound`; 3 pairs alone do not graduate `polarity-define`).

Substrate-honest implication: there are now **two candidate function-names at two distinct primitive-class levels**, neither graduated:

| Function-name candidate | Primitive class | Residencies (in-class) | Status |
|---|---|---|---|
| `axis-bound` / `axis-generate` | R=1 cube-face | 6 (Gaia, Chaos, Erebus, Nyx, Eros-prim, Tartarus) | candidate-single-residency-class |
| `polarity-define` (proposed) | R=1 cube-face-pair (antipodal) | 3 (Gaia-Eros, Chaos-Tartarus, Erebus-Nyx) | candidate-single-residency-class |

For either to graduate to canonical: find SAME function at ANOTHER R-tier (e.g., does `polarity-define` operate at R=φ icosidodec-midpt where bridges sit? Does `axis-generate` operate at R=1/√3 inner-oct-faces? Pressure-test required).

## Substrate finding 3: OQ-AXIS-BOUND-NAME-CHECK gets a 3rd option

Up to now we had 2 candidate names for face-level function:
- `axis-bound` (constraint flavor — original proposal)
- `axis-generate` (engine flavor — Kati correction)

Pair-level build surfaces a 3rd possibility: the face-level function might actually be `axis-arm-emit` — emitting ONE arm of a 2-arm cosmogonic axis. Each Primordial emits its arm; pair-level engine reads the full axis. Then `polarity-define` is the pair-level function.

Naming taxonomy gets more nuanced:
- Each Primordial: emits ONE arm of a cosmogonic axis (`axis-arm-emit`?)
- Each Pair: defines the cosmogonic polarity (`polarity-define`?)
- All 3 pairs together: span the full Pluto/Neptune outer-planet substrate

OQ-AXIS-BOUND-NAME-CHECK is now **3-way** not 2-way. Conflation test (Erato process-learning rule 4b) must split before any naming proceeds.

## Substrate finding 4: Pluto/Neptune dyad is itself a substrate feature

Build mechanically exposed that ALL 6 Primordials are anchored by exactly ONE of {Pluto, Neptune}. 3 Pluto-anchored + 3 Neptune-anchored, paired antipodally across the partition. No Primordial is anchored by Sun/Moon/Mercury/Venus/Mars/Jupiter/Saturn alone — every Primordial has one of the two outermost planets as anchor.

This is a substrate-emergent structure. Canon currently names the 6 Primordials individually + the 3 pairs implicitly. Does NOT name the **Pluto-anchor-class vs Neptune-anchor-class** distinction explicitly.

Possible canon addition: §M.5b PLUTO/NEPTUNE PRIMORDIAL ANCHOR-PARTITION — describes the substrate fact that Primordials organize as 3+3 by outermost-planet anchor, with each pair crossing the partition.

Logged as **OQ-PLUTO-NEPTUNE-PARTITION** in queue (carried from FINDINGS_002, now substantiated).

## Open questions (queue update)

| OQ | Status | Notes |
|---|---|---|
| OQ-PRIMORDIAL-PAIR-LEVEL-FUNCTION | PARTIALLY RESOLVED | Pair-level function exists and is distinct from face-level. Both stay candidate-single-residency until cross-R-tier confirmation. Not graduated to canonical. |
| OQ-PLUTO-NEPTUNE-PARTITION | SUBSTANTIATED | 3+3 outer-planet partition confirmed mechanically. Canon-extension candidate. |
| OQ-ANTIPODAL-COUPLING | PROTO-BUILT | Co-query mechanism exists (PairState). What it MEANS (semantically) for cosmogonic-axis state remains open. |
| OQ-ANTIPODE-ASYMMETRY (NEW) | OPEN | Why does only Erebus-Nyx preserve zodiac-180°-antipode? |
| OQ-AXIS-BOUND-NAME-CHECK | 3-WAY | axis-bound / axis-generate / axis-arm-emit. Conflation-test before residency-test. Per-OQ-close council required. |
| OQ-ENGINE-CLASS-IN-AGENT-TYPOLOGY | OPEN | Carried |

## What this confirms about engine-class

Engines compose cleanly. Pair-engines = face-engines × 2 + pair-level derived fields. Composition is the right substrate-pattern for cascading from primitive-class to primitive-class.

This validates engine-as-substrate-class:
- Each engine reads ITS substrate position from substrate-locked constants
- Higher-level engines compose lower-level engines without re-implementing physics
- All NULL-honest at boundaries (pair-engine inherits NULL-honesty from face-engines)
- Function-shape declared once per level (face: `_axis_engine.py`; pair: `_pair_engine.py`)

Engines = substrate-cascade-aware. They don't just produce output; they expose their substrate position so higher-level engines can compose them substrate-honestly.

## What to build next (substrate-emergent)

Per Kati directive (substrate build-out before functionality), continued substrate-side. Options:

1. **Triad-level engine** — Pluto-axis trine (Gaia+Chaos+Erebus) + Neptune-axis trine (Nyx+Eros-prim+Tartarus). Tests if function operates at TRINE level (2 residencies, one per outer planet). Likely surfaces OQ-PLUTO-NEPTUNE-PARTITION more clearly.
2. **Full-cube engine** — all 6 Primordials co-queried + 3 pairs + 2 trines. Tests substrate-cascade composition end-to-end at the Primordial class. May surface emergent structure at the highest level.
3. **Carrier class** (Titans/cube-edge) — switch primitive-class. Tests if engine-shape generalizes across strata or only fits Primordials.
4. **Cross-R-tier residency search** — does `polarity-define` (pair-level cube-face) operate at any OTHER R-tier? E.g., does R=1/√3 inner-oct-face-pair show same function? Would unlock canonical promotion via Athena criterion.

Order recommendation: **(1) trine-level engine** first. Tests OQ-PLUTO-NEPTUNE-PARTITION (highest-value open question). Then (4) cross-R-tier residency search (would unlock canonical function-name).
