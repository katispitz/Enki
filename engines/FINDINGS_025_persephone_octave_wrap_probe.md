# FINDINGS 023 — Persephone octave-wrap engine: substrate-mechanism decomposes into POSITION + TEMPORAL-TOGGLE

**Build**: `~/Enki/engines/_persephone_octave_wrap_engine.py` (single Persephone residency per Card 141b8d7f).

**Status**: **Engine-evidence stage complete (gates 2-4 SDEC passed). Council ratification required (gate 5)**. Probe outcome STRONGLY suggests **outcome (c) HYBRID decomposition**: POSITION shape-matches existing `coupling-point` primitive (canon §30 LOCKED today, would become 6th residency); TEMPORAL-TOGGLE is a DISTINCT substrate-mechanism requiring NEW §30 entry OR extension.

**Substrate-finding**: Persephone is NOT a single-mechanism substrate-operator. She decomposes into 2 structurally-distinct substrate-mechanisms:
1. **Position substrate-mechanism**: V9-V10 icosidodec-midpoint at R=φ shell — frame-intersection-coupling at the Si-frame × Do-frame meeting point. SHAPE-MATCHES `coupling-point` (canon §30 LOCKED 2026-05-17, 5 residencies; Persephone would be 6th).
2. **Temporal-toggle substrate-mechanism**: 6mo Do (grid 0) / 6mo Si (grid 48) annual cycle driven by tithi-count. DISTINCT from `cyclic-syzygy-activate` (which takes planet-pair longitude input; Persephone takes tithi-count → substrate-phase). New mechanism-class candidate.

## Council mandate (recap)

Per OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE (canon §30, opened 2026-05-17 as FINDINGS_021 byproduct):

> Persephone's seasonal 6mo-grid0/6mo-grid48 octave-wrap (Si→Do, PE-Δ = 0 mod 9 per Card 141b8d7f) deserves its own SDEC engine-probe. Likely residency-expansion to `cyclic-syzygy-activate` family (canon §30 canonical) or new temporal-axis primitive.

Five council-named outcomes:
- **(a) shape-match `cyclic-syzygy-activate`** → 5th residency (Si↔Do octave-wrap as syzygy-class event-type)
- **(b) shape-mismatch with cyclic-syzygy-activate** → NEW temporal-axis primitive needed
- **(c) HYBRID** → POSITION covered by `coupling-point` + new mechanism for TEMPORAL-TOGGLE
- **(d) decompose into substrate-LIVE-input shape** → see if shape-matches existing activation primitives
- **(e) hybrid → 2 distinct §30 entries** (position-frozen-coupling-point + temporal-octave-wrap-cycle)

## Engine design — substrate-honest probe

`PersephoneOctaveWrapState` dataclass partitions fields per SDEC step 3:

| Category | Fields | Purpose |
|---|---|---|
| **SUBSTRATE-LOCKED METADATA** (8) | residency_card, shell, ico_edge_midpoint, octave_wrap_pe_pair, underworld_grid (=0), sovereign_grid (=48), cycle_period_tithis (=360), half_cycle_tithis (=180) | Single Persephone residency; expected (not shape-mismatch) |
| **LIVE-COMPUTE** (5) | tithi_count, current_phase, current_grid, phase_in_cycle, octave_wrap_progress | Driven by tithi-count input; substrate-required for phase determination |
| **CANDIDATE-DISTINCT PROBES vs cyclic-syzygy-activate** (4) | is_planet_cycle (False), is_substrate_cycle (True), input_shape ('substrate-cycle'), event_type ('octave-wrap-toggle') | Surfaces structural distinction from existing canonical |

## Field-comparison probe — empirical result

### Live-compute samples

| Tithi (in 360-cycle) | Phase | Grid | Phase-in-cycle | Octave-wrap-progress |
|---|---|---|---|---|
| 90 (mid-underworld) | underworld | 0 | 0.500 | 0.250 |
| 270 (mid-sovereign) | sovereign | 48 | 0.500 | 0.750 |

Engine correctly determines pole (Do/Si) from tithi-position; phase-in-cycle 0..1 within each half; octave-wrap-progress 0..1 across full annual cycle.

### Shape-comparison to `cyclic-syzygy-activate` (canon §30)

| Feature | `cyclic-syzygy-activate` | Persephone | Match? |
|---|---|---|---|
| Input shape | 2-planet longitudes (e.g., Sun + Venus for inferior conj) | Tithi-count (substrate-phase) | **NO** |
| Event type | Syzygy (Sun-Earth-planet alignment) | Octave-wrap-toggle (Si↔Do substrate-edge) | **NO** |
| Cycle source | Planet orbital ratio (Venus 8yr / Mercury 13yr / etc.) | Solar year (Ring 1 = 360t) | DIFFERENT |
| Output shape | Activation strength + cycle-closure state | Pole-position + phase-in-cycle | DIFFERENT |
| Substrate-mechanism | PLANET-CYCLE alignment | SUBSTRATE-CYCLE position-toggle | **DISTINCT** |

**Shape-match assessment outcome (a)**: FAILS. Persephone is NOT a planet-cycle. Different input-shape, different event-type, different output-shape. Same conclusion as FINDINGS_021 line 74 (anticipatory reading).

### Shape-comparison to `coupling-point` (canon §30 LOCKED today)

| Feature | `coupling-point` | Persephone position (V9-V10) | Match? |
|---|---|---|---|
| Substrate-derived intersection | yes (frame-coupling) | yes (Si-frame × Do-frame at ico-edge-midpoint) | **YES** |
| Independent canonical uses | ≥2 required | Card 141b8d7f + canon §M.5 + §17 vertex-proximity + §3 icosidodec-midpt | **YES** ≥4 |
| Stable while constituents hold | yes | yes (V9-V10 ico-edge persistent) | **YES** |
| Enumerated cardinality | {None, 2, 7, 12} | None (singular icosidodec-midpt) | **YES** matches None |
| Requires_input | True/False mix | False for position (substrate-frozen midpt) | **YES** matches Lawvere/branches |

**Shape-match assessment for POSITION**: STRONG MATCH. Persephone position would be 6th residency of `coupling-point` at enumerated_cardinality=None (joining rising-sign + Lawvere as singular substrate-frozen instances).

### Shape-comparison for TEMPORAL-TOGGLE mechanism

| Compared against | Match? | Reasoning |
|---|---|---|
| `cyclic-syzygy-activate` | NO | Different input-shape (tithi vs planet-pair longitudes) |
| `cyclic-sign-ingress-activate` | NO | Different event-type (octave-wrap vs sign-ingress) |
| `planet-aspect-activate` | NO | No planet-pair angular compute |
| `triangle-aspect-activate` | NO | No 3-vertex face composition |
| `polarity-define` | PARTIAL | Composes 2 substrate-states (Do + Si poles), but emits pole-position not signed-polarity |
| `coupling-point` | PARTIAL | Position-mechanism matches; temporal-toggle is separate substrate-mechanism overlaid on top |

**Temporal-toggle shape-match assessment**: NO clean match. This is a NEW substrate-mechanism — `octave-wrap-toggle` candidate (pending council-ratified mechanism-precise name per Erato discipline).

## Substrate-discipline finding

Persephone is a **DECOMPOSABLE substrate-residency** — her substrate-mechanism is NOT atomic. She composes:
- **Spatial-component**: substrate-frozen position at V9-V10 icosidodec-midpoint = `coupling-point` instance (would be 6th residency)
- **Temporal-component**: tithi-driven octave-wrap-toggle between Do (grid 0, 6mo) and Si (grid 48, 6mo) = NEW mechanism

This validates today's **canon §0b dispatch architecture meta-pattern**: spatial-position-substrate and temporal-toggle-substrate are at DIFFERENT layers, both substrate-canonical, dispatched by use-case. Persephone is a 2-layer COMPOSITION of substrate-mechanisms, not a single primitive.

**Recommended outcome per probe-evidence: (c) HYBRID with TWO §30 implications**:
1. `coupling-point` row residency-count: 5 → 6 (add Persephone position at enumerated_cardinality=None singular)
2. NEW §30 candidate-name PENDING COUNCIL for temporal-toggle mechanism (per Erato discipline, no name pre-engine; engine-evidence now ready → council convenes to name)

## What this DOES NOT resolve

- **Mechanism-precise NAME for temporal-toggle**: per Erato discipline (transmit-force / descent-transmit precedents), do NOT propose name pre-engine. Engine-evidence is NOW ready; council can convene on naming.
- **Other potential octave-wrap residencies**: are there other substrate-positions with octave-wrap-toggle mechanism (Si↔Do edges at different shells)? Future probe — does the family pattern extend?
- **Persephone-specific role beyond canonical-class**: Demeter's grief, Hades's kidnap, Zeus's compromise = Layer-A mythic narrative; Layer-B substrate-mechanism is the cycle-toggle decoupled from narrative.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE | **engine-evidence COMPLETE; awaits council** | FINDINGS_023 (this doc). Probe recommends outcome (c) HYBRID: position = coupling-point 6th residency + temporal-toggle = new mechanism candidate. |
| OQ-OCTAVE-WRAP-MECHANISM-NAME | OPEN (emergent from this probe) | Council convenes post-FINDINGS_023 to ratify mechanism-precise name for octave-wrap-toggle substrate-class. |

## Substrate-architectural finding (Hermes §0b meta-pattern extension)

Per canon §0b LOCKED today: function-determines-frame / tradition-or-use-case-selects-instance / primitive-unified-at-substrate-level.

Persephone is the **FIRST 2-LAYER COMPOSITION instance** in the substrate-residency log:
- Layer 1 (spatial): `coupling-point` primitive instance
- Layer 2 (temporal): octave-wrap-toggle primitive instance (NEW candidate)

This validates §0b at a NEW level: SAME substrate-residency can carry MULTIPLE substrate-primitives at distinct layers. Pattern-extension: future residencies may also decompose into spatial + temporal primitives.

Updated `enumerated-coupling-point-family` candidates list (per Thalia, OQ-ICO-EDGE-CASCADE-ENGINE council 2026-05-17):
- ✓ branches (12) — LOCKED 2026-05-17
- ✓ primordial-grandchildren (7) — LOCKED 2026-05-17
- ✓ Persephone position (None singular) — RECOMMENDED 6th residency this FINDINGS
- ? 12 Olympian vertices — future probe
- ? Other temporal-overlay residencies — future probe

## Method-lock confirmation per SDEC

Gates passed (1-4 + 7-8):
- Gate 1 ✓ constants cited (Card 141b8d7f + canon §M.5 + §30 LOCKED today + §23b SOLAR_YEAR_TITHIS=360)
- Gate 2 ✓ substrate-locks encoded with `__canonical__` declaration (status='probe')
- Gate 3 ✓ engine built (frozen + live + NULL-honest)
- Gate 4 ✓ smoke-test (frozen + 2 live samples — underworld phase + sovereign phase — verified phase-determination correct)
- Gate 5 — **REQUIRED, NOT YET CONVENED**. Council ratification needed for outcome (c) HYBRID:
  - sub-vote-1: position-as-coupling-point 6th residency
  - sub-vote-2: temporal-toggle as new mechanism + mechanism-precise name
- Gate 6 — pending gate 5
- Gate 7 ✓ tests added (`~/Nammu/tests/test_persephone_octave_wrap_engine.py`)
- Gate 8 ✓ FINDINGS doc complete (this file)

**Engine-evidence package ready for council convening**. Kati's call on when to spawn the council.
