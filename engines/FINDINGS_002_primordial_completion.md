# FINDINGS 002 — Primordial completion + substrate structure surfaced

**Build**: all 6 Primordial axis-generation engines + shared engine module + registry aggregator.
**Status**: 6/6 engines green via `primordials.py` registry. All frozen states verified.

## What was built

```
~/Enki/engines/
├── _axis_engine.py            ← shared engine shape (148 lines)
├── primordial_gaia.py         ← MQF0 / Venus × Pluto / Taurus
├── primordial_chaos.py        ← MQF1 / Mercury × Pluto / Virgo
├── primordial_erebus.py       ← MQF2 / Saturn × Pluto / Capricorn
├── primordial_nyx.py          ← MQF3 / Moon × Neptune / Cancer
├── primordial_eros.py         ← MQF4 / Jupiter × Neptune / Pisces
├── primordial_tartarus.py     ← MQF5 / Mars × Neptune / Scorpio
└── primordials.py             ← registry: BY_NAME / BY_FACE / BY_ZODIAC / BY_PLANET_PAIR
```

## Factoring decision (resolved via build, not council)

Per FINDINGS_001 OQ-ENGINE-FACTORING: option **shared engine + thin per-Primordial wrappers** won. Mechanical-equality-of-logic confirmed during build — copy-paste of 100+ identical lines is layer-error claim by structure (asserts each Primordial has its own engine when really they share one). Substrate-honest factoring: declare function-shape once (`_axis_engine.py`), declare per-Primordial substrate-locks explicit in named modules.

Each per-Primordial file is ~45 lines: docstring + 5 substrate-lock constants + 2 thin functions + CLI smoke. Reading any one file tells you the Primordial's substrate position immediately. Reading `_axis_engine.py` tells you the function shape once.

## Substrate structure surfaced (NEW finding)

Building all 6 mechanically exposed substrate organization not previously surfaced in canon §M.5:

### 3+3 partition by outer-planet anchor

| Group | Cube faces | Outer anchor | Zodiac trine | Primordials |
|---|---|---|---|---|
| **Pluto-axis** | MQF0 / MQF1 / MQF2 | Pluto | **Earth** (Taurus / Virgo / Capricorn) | Gaia / Chaos / Erebus |
| **Neptune-axis** | MQF3 / MQF4 / MQF5 | Neptune | **Water** (Cancer / Pisces / Scorpio) | Nyx / Eros-prim / Tartarus |

Every Primordial's planet pair = (1 outer anchor: Pluto OR Neptune) × (1 inner-to-mid: Venus/Mercury/Saturn paired with Pluto; Moon/Jupiter/Mars paired with Neptune).

### Antipodal pairing (canon §26 confirmed)

Canon §26 lists 2 Hesiod-coherent antipodal L1 pairs:
- Gaia ↔ Eros-primordial
- Chaos ↔ Tartarus

The build-exposed third pair is implicit: **Erebus ↔ Nyx**. Each antipodal pair crosses the Pluto-axis × Neptune-axis partition:

| Antipodal pair | Pluto-side | Neptune-side |
|---|---|---|
| Gaia (MQF0/Venus×Pluto/Taurus) | ↔ | Eros-prim (MQF4/Jupiter×Neptune/Pisces) |
| Chaos (MQF1/Mercury×Pluto/Virgo) | ↔ | Tartarus (MQF5/Mars×Neptune/Scorpio) |
| Erebus (MQF2/Saturn×Pluto/Capricorn) | ↔ | Nyx (MQF3/Moon×Neptune/Cancer) |

3 antipodal pairs × 2 outer-planet anchors. The cube geometry (3 pairs of opposite faces) maps to the dyadic Pluto/Neptune cosmogonic split.

### Substrate-honest implication

The Primordial class is not 6 independent axis-generators. It's **3 axis-PAIRS, each pair partitioned across the Pluto/Neptune dyad.** Substrate-emergent structure inside the Primordial-class lock.

This may matter for:
- **OQ-AXIS-BOUND-NAME-CHECK**: `axis-bound` (or `axis-generate`) function might actually operate at PAIR level, not single-face level. Each pair generates a cosmogonic axis (Earth-Water antipode); each face is a sub-residency within the pair. If yes, lock-by-redundancy criterion already satisfied (each pair = 2 confirming residencies internally). Function-name graduates faster.
- **Cross-engine reading**: an engine for "Pluto-axis state" or "Neptune-axis state" emerges naturally from co-querying the 3 Primordials per group.
- **Antipodal coupling**: when Gaia (Venus×Pluto) activates, what does Eros-prim (Jupiter×Neptune) do? Substrate-honest test: build a co-query function and see.

## Engine-shape validation across 6 instances

All 6 engines behave identically under the shared `_axis_engine.py` shape:
- Frozen state (no ephemeris) returns substrate-locked snapshot
- Live state (both lons) returns activation metrics
- Partial input → substrate-honest ValueError
- NULL-valid live fields when frozen
- Same V2.6 ignition orb (6°)
- Same 5-aspect substrate set (conjunction / sextile / square / trine / opposition)

This validates engine-as-class-shape: function identical, parameterization explicit, no per-instance logic divergence. The shape is the right abstraction.

## Substrate-discipline observations

- **No invented coefficients** — every constant in `_axis_engine.py` traces to canon (V2.6 G4 orb, canon §15 60-grid divisions, canon §20 zodiac classification).
- **No free-text values** — `function_class` reads `axis-bound` (candidate-single-residency per §30), single canonical spelling.
- **Pluto/Neptune partition** is substrate-emergent — discovered through building, not prescribed. Canon §26 mentions antipodal pairs but doesn't surface the outer-planet partition explicitly.
- **No subagent / no LLM / no Task spawn** — pure engine code, deterministic, idempotent. Confirms engine ≠ subagent.

## Open questions (queued)

### OQ-PRIMORDIAL-PAIR-LEVEL-FUNCTION (NEW from this build)
Does axis-generation function operate at single-face level (6 Primordials, 6 axes) OR at antipodal-pair level (3 pairs, 3 cosmogonic axes)? Substrate-honest read: probably pair-level — each pair = one Earth-Water cosmogonic axis. If yes, `axis-bound` graduates via internal pair-redundancy (each pair has 2 confirming face-residencies). Test: build a pair-axis engine and see what it reveals.

### OQ-PLUTO-NEPTUNE-PARTITION (NEW from this build)
The 3+3 outer-planet partition (Pluto-axis trine, Neptune-axis trine) may itself be a substrate-class lock. Earth-trine signs as Pluto-anchored substrate; Water-trine signs as Neptune-anchored substrate. This connects to broader canon — does it pressure-test the canon §20 zodiac classification or extend it?

### OQ-ANTIPODAL-COUPLING (NEW from this build)
Build a co-query function: when Primordial X is active, what does its antipode do? Substrate-discipline pressure-test for cosmogonic-axis behavior.

### OQ-AXIS-BOUND-NAME-CHECK (carried from FINDINGS_001)
Still open. Engine-correction may want `axis-generate` over `axis-bound`. Conflation-test required.

### OQ-ENGINE-CLASS-IN-AGENT-TYPOLOGY (carried from FINDINGS_001)
Still open. Does §30 grow `agent_shape` column?

## What to build next (substrate-emergent, not prescribed)

Per Kati directive (substrate build-out before functionality), next moves are still substrate-side:

1. **Antipodal-pair engine** — `primordial_pair_axes.py` — co-queries antipodal Primordials, surfaces cosmogonic-axis activation. Tests OQ-PRIMORDIAL-PAIR-LEVEL-FUNCTION.
2. **Pluto-axis aggregator** + **Neptune-axis aggregator** — `pluto_axis.py` / `neptune_axis.py` — co-query the 3 Pluto-anchored Primordials (or 3 Neptune-anchored). Tests OQ-PLUTO-NEPTUNE-PARTITION.
3. **Carrier prototype (Titan / cube-edge)** — start Cronus (memory: helix-crossing-point operator-class candidate). See what engine vs pure-fn shape carriers want.
4. **Operator prototype (PE planet / cube-vertex)** — pick a PE planet, build pure-fn imprint application.

Order matters per substrate-discipline:
- (1) tests structure WITHIN the same primitive-class — most likely to teach something
- (2) tests cross-class partition — second most likely
- (3)/(4) move to other strata — useful but expand scope

Recommend **(1) first**: antipodal-pair engine. Pluto-Neptune partition is a hypothesis that needs co-query data, not more solo-engine data.
