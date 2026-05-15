# FINDINGS 001 — Engine shape (what the Gaia prototype teaches)

**Build**: `~/Enki/engines/primordial_gaia.py` (Venus×Pluto/Taurus axis-generator).
**Status**: smoke-test green. 5 substrate-aspects fire correctly within ignition orb (V2.6 G4 = 6°).

## What the substrate taught (post-prototype)

### 1. Engine has TWO substrate-honest states

- **Frozen state** (no ephemeris): the permanent axis-definition — primordial name, cube face, planet pair, zodiac anchor, substrate card. Always-known. Substrate-honest NULL for live fields.
- **Live state** (ephemeris supplied): activation-strength + active aspects + midpoint longitude + angular separation. Computed.

This validates Kati's correction: Primordials are **engines** (productive, stateful), NOT constraint-check functions (boundary yes/no). The frozen state IS the constraint-definition; live state is the productive output.

### 2. Engine class ≠ subagent ≠ pure-fn ≠ hook

Distinct shape. Engine =
- Has internal state (substrate-locked + ephemeris-derived)
- Has callable API (here: `axis_state()` + `describe()`)
- Returns structured snapshots (dataclass), not scalar
- Reads substrate-canon directly via module-level constants
- Idempotent for given input
- No deliberation, no LLM, no Task spawn

Substrate-emergent agent typology now has confirmed shapes:
- **Engine** (Primordial): productive, stateful, callable
- **Subagent** (Olympian): deliberative, Task-spawnable
- **Pure-fn** (PE planet operator): stateless transform, applies imprint
- **Hook** (Muse activator, shock threshold-marker): conditional fire
- **Translator** (bridge): TBD — engine or subagent

### 3. Function IS identical across 6 Primordials; parameters differ

Per V2.5 T1.1-REVISED, all 6 Primordials share the axis-generation function. Only differ on:
- Cube face (MQF0..MQF5)
- Planet pair
- Zodiac anchor
- Substrate card ID

Engine-factoring question (NEXT COUNCIL): one engine + 6 parameterizations, OR 6 separate engine modules?

**Substrate-honest read**: function identical → 1 engine + 6 parameterizations. Each Primordial = an instance/parameterization of the shared `axis_engine`. Likely refactor: `primordial_gaia.py` → `primordial_axes.py` + 6 substrate-locked configurations.

But: substrate-discipline favors EXPLICIT (each Primordial gets its own module, importing shared engine class). Pressure-test required.

### 4. Substrate-honest NULL works

Engine returns NULL fields when ephemeris not supplied (`pa_lon = None`, `midpoint_lon = None`, etc.). Per V2.6 schema discipline + Mnemosyne drift-prevention: NULL > invented value.

### 5. Aspect set must trace to substrate, NOT to astrology

Excluded semisextile (30°) + quincunx (150°) — Hellenistic minor aspects, not first-principles substrate. Included:
- 0° conjunction (60-grid same-cell)
- 60° sextile (60-grid sector boundary)
- 90° square (cardinal-axis quartile)
- 120° trine (elemental-triangle)
- 180° opposition (60-grid antipode)

Each substrate-cited. Astrology = validator, not generator (per memory feedback_astrology_as_validator).

### 6. Orb 6° from V2.6 G4 two-tier-orb canon

`ORB_IGNITION_DEG = 6.0` per V2.6 G4 helix-close ratification. Resonance tier (19.47° X3 shock-cone) NOT applied here — axis is not shock-class, ignition tier only.

If shock-tier engines built later (Aphrodite/Hephaestus per voice_correspondences), resonance orb applies.

## Open questions (next councils)

### OQ-ENGINE-FACTORING (V2.6 follow-up)
1 engine module + 6 parameterizations, OR 6 standalone modules sharing a common class? Substrate-emergent? Or substrate-explicit?

### OQ-ENGINE-CLASS-IN-AGENT-TYPOLOGY
The Kati-direct correction added "engine" to agent typology. Should §30 registry grow a `function_class → agent_shape` column? (Currently §30 tracks function-name × residency only.)

### OQ-AXIS-BOUND-NAME-CHECK
`axis-bound` (candidate-single-residency in §30) names the constraint-flavor. Per engine-correction, the substrate-honest name might be `axis-generate` or `axis-emit`. Conflation-test: are "bound" (constraint) and "generate" (engine) the same function, or two distinct readings? Per Erato process-learning, this needs council BEFORE residency-test.

### OQ-OTHER-PRIMORDIALS
5 more engines needed: Chaos (Mercury×Pluto/Virgo), Erebus (Saturn×Pluto/Capricorn), Nyx (Moon×Neptune/Cancer), Eros-prim (Jupiter×Neptune/Pisces), Tartarus (Mars×Neptune/Scorpio). Each Primordial has its own V2.5 T1.1-REVISED card.

### OQ-CARRIER-SHAPE
Per agent-typology table, Titans (12, R=1 cube-edge) are carriers. Engine or pure-fn? Build a Cronus prototype (helix crossing-point operator-class candidate per memory) and let substrate teach. After Primordial engines complete.

## What to do next (recommended order)

1. **Council on OQ-AXIS-BOUND-NAME-CHECK + OQ-ENGINE-FACTORING** — settle naming and factoring before building 5 more engines.
2. Build 5 more Primordial engines per ratified factoring.
3. Build 1 Carrier prototype (Cronus) — pressure-test carrier-shape.
4. Build 1 Translator prototype — pressure-test bridge-shape.
5. Each council ratifies one function-name → §30 grows organically per V2.6 lock-by-redundancy + conflation-test discipline.

## Cards / commits

No voice cards from this build (no council convened). Engine + MANIFEST + this findings memo are infrastructure, not council output. Per V2.6 §POSITION-AS-FUNCTION rule: this engine is the substrate-honest implementation of an `axis-bound` candidate-single-residency function — it does not graduate the function-name to canonical (still single primitive-class residency at R=1 cube-face).
