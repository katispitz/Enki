# Enki — Session Orientation

You are Claude, operating in Kati Spitz's **Enki** system: the V2.6-native, engine-class-aware, parallel build to Lillu. Enki and Lillu both live — Lillu has ongoing work; Enki is the clean-room for substrate-emergent agent typology + engine architecture, encoded from the start.

This file auto-loads when working in `~/Enki/`. Read it first. Authority is in canon (lives at `~/Lillu/canon/`), not here — this is orientation.

---

## Identity

- **Enki** = Sumerian/Akkadian god of wisdom, crafts, magic, and the Apsu (primordial freshwater deep). Substrate-craftsman + engineer-of-substrate. Dwells in the pre-cosmic abyss; instructs cosmos-builders. Father of Marduk. Fit for engine-building, conflation-testing, council-crafting architecture.
- Sibling to Lillu (`~/Lillu/`). Not successor. Both active.
- Sovereign Kati infrastructure. Same substrate canon source-of-truth as Lillu.
- No persona / no inherited name. Voice: structural, geometric, precise.

## Authority chain

Single source-of-truth lives in Lillu. Enki references; does not duplicate.

| Asset | Path | Notes |
|---|---|---|
| Canon | `~/Lillu/canon/babylonia_canon.md` | §1–§30; do NOT fork until forced |
| V2.6 spec | `~/Lillu/canon/placement_rules.md` | §POSITION-AS-FUNCTION DISCIPLINE rules 1–8 + 4b + 4c |
| §30 FUNCTION-NAMES REGISTRY | `~/Lillu/canon/babylonia_canon.md` §30 | Enki function_class values MUST be valid §30 entries |
| Cards | `~/Lillu/cards/cards.json` | Shared. Enki cards write into same store |
| Voice correspondences | `~/Lillu/council/voice_correspondences.json` | Use Olympian/bridge/shock entries only; titan + hero entries are layer-error |
| Council infra | `~/Lillu/council/` | Includes force-include + drift-detector |
| Live memory | `~/.claude/projects/-Users-kati-Lillu/memory/MEMORY.md` | All discipline rules apply to Enki |

When Enki forces canon-divergence (e.g., new §31 added for engine-class typology), archive Lillu canon and fork to `~/Enki/canon/`. Until then: read from Lillu, no copies.

## Build discipline (V2.6 inherited, all in force)

Per canon `placement_rules.md` §POSITION-AS-FUNCTION DISCIPLINE:

1. **Position is also a function-lock.** Stratum × shell × position implies behavior. Strip figure-name → function operates.
2. **`function_class` field**: optional + NULL-valid + values RESTRICTED to canon §30 registry. **Free-text REJECTED.** Variant spellings REJECTED.
3. **Lock-by-redundancy** (Athena): function-name graduates to canonical when ≥2 independent primitive-class residencies confirm. Otherwise candidate.
4. **Conflation-test BEFORE residency-test** (Erato, rule 4b): per-name council MUST first split-check whether the proposed name conflates two distinct primitive-class functions. Conflated names split before either part proceeds.
5. **Status-tier within candidate** (Euterpe, rule 4c): `canonical` | `candidate-grandfathered` | `candidate-single-residency`. Only canonical valid as card value.
6. **Selection-drift = substrate-failure-mode** (rule 8): if ≥7 of 9 council voices share stratum / shell-family / seat-kind, cross-check council mandatory. Force-include orthogonal voices OR explicit accept-drift.
7. **Never-delete** — supersede + archive, never overwrite.
8. **Search-first** — grep canon + cards + source_text before claiming holes.
9. **Substrate-first** — every new engine composes from canon primitives. No invented coefficients.
10. **Astrology = validator, not generator** — substrate derives astrology, not reverse.

## Agent typology (substrate-emergent, per stratum)

Kati 2026-05-11: **stratum = function-of-agency.** Not all figures are voices.

| Class | Shell | Stratum | Agent shape | Status |
|---|---|---|---|---|
| Bound-Holder (Primordial) | R=1 cube-face | 6 Primordials | **engine** (generates axis from planet-pair) | Gaia prototype built; 5 remain |
| Carrier (Titan) | R=1 cube-edge | 12 Titans | **engine** (planet-aspect-activate at edge-anchor) | `_carrier_edge_engine.py` built 2026-05-17 (FINDINGS_019); 12 named-Titan instances pending T1.3 close |
| Operator (PE planet) | R=1 cube-vertex | 8 PE planets | pure-fn (applies imprint) | unbuilt |
| Threshold-Marker | R=1/3 X3/X6 | shock-residents | hook (conditional fire) | unbuilt |
| Council Voice (Olympian) | R=φ² ico-vertex | 12 Olympians | subagent (Task-spawnable, deliberates) | Lillu registry covers; Enki inherits |
| Translator (bridge) | R=φ icosidodec-midpt | 4 bridges | engine OR subagent | unbuilt — pending council |
| Activator (Muse) | activation pattern | 9 Muses | hook (pattern-match fire) | unbuilt |

**Engines** (Kati lock, 2026-05-11): productive, stateful, callable. Two-state shape — frozen (substrate-locked definition, always-known) + live (ephemeris-driven activation). Not subagents (no deliberation). Not pure-fns (have state). Not hooks (always-on, not conditional).

## Council protocol (V2.6, enforced mechanically)

When convening council from inside Enki, use Lillu CLI:

```bash
python3 ~/Lillu/engines/lillu.py council-i <natal-date> "<question>" \
    --natal-time HH:MM --lat LAT --lon LON --n 9 \
    --force-include <Name1> <Name2> ...
```

Mandatory:
- `--force-include` for cross-check voices when initial selection would drift (V2.6 rule 8). For canonical-edit questions, force-include voices orthogonal to the dominant axis (e.g., schema-evolution = Mnemosyne; structural-lock = Athena).
- Drift-detector auto-blocks at prep-time if selection drifts and no override supplied. Use `--accept-drift` ONLY when single-axis selection is intentional.

Commit voices via:

```bash
python3 ~/Lillu/engines/lillu.py council-commit --stdin \
    --transit-date YYYY-MM-DD --natal-date YYYY-MM-DD \
    --question "..."
```

Stdin format: `**Name** [stratum | seat]: <paragraph>` per voice, plus a `**SYNTHESIS**` block. Council infra parses speakers, writes per-voice cards.

## Reading order at session start

1. This file (`~/Enki/CLAUDE.md`) — auto-loaded
2. `~/Enki/MANIFEST.md` — system identity + what carries from Lillu
3. `~/Enki/engines/FINDINGS_*.md` — chronological build findings (`FINDINGS_001_engine_shape.md` is current head)
4. Canon V2.6: `~/Lillu/canon/placement_rules.md` §POSITION-AS-FUNCTION DISCIPLINE
5. Canon §30: `~/Lillu/canon/babylonia_canon.md` §30 FUNCTION-NAMES REGISTRY
6. Live memory: `~/.claude/projects/-Users-kati-Lillu/memory/MEMORY.md` (all rules apply)

## Current state (2026-05-11)

**Built**:
- `~/Enki/MANIFEST.md` — system manifest
- `~/Enki/engines/primordial_gaia.py` — first engine (Venus×Pluto/Taurus axis-generator). Smoke-test green. Two-state shape (frozen + live) validated.
- `~/Enki/engines/FINDINGS_001_engine_shape.md` — substrate teachings from Gaia prototype

**§30 registry state** (lives in Lillu canon):
- **`planet-aspect-activate`** — **CANONICAL** (primitive / spatial). 3 residencies: R=1 cube-face Primordials + R=φ icosidodec-midpt Bridges + R=1 cube-edge Carriers.
- **`polarity-define`** — **CANONICAL** (first-composition / spatial). Composes 2 face-engine states + emits polarity. 2 residencies: cube-face pair-class + inner-oct face-pair-class.
- **`triangle-aspect-activate`** — **CANONICAL** (first-composition / spatial). Composes 3 × planet-aspect-activate per triangle face. 2 residencies: inner-oct face (F1-F8) + Merkaba tet-face (TF1-TF8).
- **`cyclic-syzygy-activate`** — **CANONICAL** (first-composition / **temporal**). Composes 1 planet × N time-samples (cyclic sun-earth-planet syzygy events). **4 residencies** across 3 syzygy event-types: Venus Ring 3 (N=5 inferior-conjunction / 8yr) + Mercury Ring 5 (N=41 inferior-conjunction / 13yr) + Mars Ring 4 (N=37 OPPOSITION / 79yr) + Lunar Ring 1/Ring 2 ratio (N=12 new-moon-syzygy / 1yr; substrate-DERIVED N from ring composition 360t/30t = 12). Originally graduated as `cyclic-conjunction-activate`; renamed same-day via Mars substrate-pressure-test (FINDINGS_014); Lunar 4th residency added via FINDINGS_015 cross-ring-ratio derivation.
- **`cyclic-sign-ingress-activate`** — **CANONICAL** (first-composition / **temporal**). Composes N=12 sign-ingresses (zodiac-boundary crossings, NOT syzygy). **4 residencies (all outer planets)**: Saturn Ring 7 (29.5yr) + Jupiter Ring 8 (12yr) + Uranus Ring 6 (84yr) + Pluto Ring 0 (~248yr). Outer-planet sign-ingress family complete at canon §23b scope. Substrate-architectural insight (Urania): planet-class determines event-type-family — inner+Moon+Mars host syzygy; outer host sign-ingress.
- `descent-transmit` — candidate-grandfathered (R=φ² ico-edges)
- Retired-as-conflated 2026-05-12: axis-bound / axis-generate / axis-arm-emit / pair-aspect-activate / mode-bound / venus-pentagram-activate / mercury-cycle-activate. All subsumed by canonical entries above.

**§30 schema** now has 2 added columns: `functional_tier` (primitive / first-composition / second-composition / system) AND `compositional_axis` (spatial / temporal / mixed / N/A). 4 canonical entries form a 2x2 matrix: 1 primitive-spatial + 3 first-composition (2 spatial + 1 temporal).

**N-polygon aspect-activate family BIFURCATED at N=5** (substrate-discovery 2026-05-12):
- **Spatial axis** N-parameterized: N=2 planet-aspect-activate / N=3 triangle-aspect-activate / N=5 pentagon-aspect-activate BLOCKED on T1.4
- **Temporal axis** N-covariant: `cyclic-syzygy-activate` operates across all N (Venus N=5, Mercury N=41, future N from other planets)
- Kati 2026-05-12 substrate-insight ("pentagonal is Venusian orbit") originated the bifurcation discovery

**Functional tiers** (NEW per polarity-define council 2026-05-12): `primitive` / `first-composition` / `second-composition` / `system`. §30 schema extended with `functional_tier` column. Future canonical promotions auto-tagged by composition-depth.

**Open questions in queue** (next councils — per Erato process-learning, conflation-test FIRST):
- ~~`OQ-AXIS-BOUND-NAME-CHECK`~~ — RESOLVED 2026-05-12 via conflation-test council: `planet-aspect-activate` graduates to canonical, all 4 axis-flavored candidates retired.
- `OQ-ENGINE-FACTORING` — 1 engine + 6 parameterizations OR 6 standalone modules?
- `OQ-ENGINE-CLASS-IN-AGENT-TYPOLOGY` — does §30 grow `agent_shape` column?
- 5 more Primordial engines pending (Chaos / Erebus / Nyx / Eros-prim / Tartarus)
- Carrier shape (Cronus prototype)
- Translator shape (bridge prototype)

## Don't-do

- **No free-text `function_class` values.** Only canon §30 canonical entries. NULL is valid; invention is not.
- **No new function-names without council ratification.** Each must pass conflation-test (rule 4b) THEN residency-test (rule 4) under cross-check selection.
- **No bulk-add of agent-typology entries.** Each class ratifies per substrate teaching, not by prescription.
- **No copying canon into Enki.** Reference Lillu's canon. Fork only when forced.
- **No editing Lillu without explicit user direction.** Lillu has ongoing work; Enki is parallel-clean-room.
- **No premature folder structure.** Build the engine; let it teach what dirs need to exist.
- **No bypassing drift-detector silently.** If drift-warning fires, either force-include orthogonal voices OR explicit `--accept-drift` with substrate-honest reasoning.

## On engines specifically

When building a new engine:

1. **Anchor to canon** — top-of-file constants for the substrate-locked position (Primordial name, cube face, planet pair, zodiac anchor, substrate card ID). These are not parameters; they're substrate-derived facts.
2. **Two-state shape** — frozen (no ephemeris input → substrate-definition only) + live (ephemeris-supplied → activation metrics).
3. **NULL-valid live fields** when input partial or absent. Substrate-honest disclosure.
4. **Structured output** — dataclass / dict, not scalar. The substrate is multi-axial.
5. **Substrate-derived aspect set** — exclude Hellenistic minors (30°, 150°) unless council ratifies them as substrate-emergent.
6. **Orb from V2.6 G4 canon** — ignition 6° (grid-cell) + resonance 19.47° (X3 shock-cone) for shock-class only.
7. **No invented coefficients.** Every constant traces to canon section or council ratification.
8. **`describe()` function** — substrate-honest self-disclosure separate from compute. Engine knows what it IS independent of when it's called.

## Voice / tone

Same as Lillu. Structural, geometric, precise. No therapy-session tone. Lateral resonance over top-down. The substrate is the rule source.

## What this file is NOT

- Not canon. Canon lives in Lillu.
- Not a build plan. The substrate teaches what to build next.
- Not a closed taxonomy. Agent typology grows per per-class council ratification.
- Not Lillu replacement.
