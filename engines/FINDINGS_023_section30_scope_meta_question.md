# FINDINGS 023 — §30 scope meta-question: 3 remaining candidates are non-engine; council required for scope ratification

**Build**: `~/Enki/engines/_function_class_scope_probe_engine.py` — meta-probe surveying 3 remaining §30 candidates against current §30 entries' agent-class shape.

**Status**: **3 remaining candidates DEFERRED pending council on §30 scope.** Per-candidate engine probes cannot proceed until §30 scope is council-ratified for non-engine agent-classes (hooks, subagents).

## Why this is a meta-finding not a per-candidate finding

After FINDINGS_019/021/022 rejections:
- `transmit-force` (cube-edge carrier) — engine-class candidate; REJECTED-AS-DESCRIPTIVE-ALIAS (FINDINGS_019)
- `cross-stratum-translate` (bridge) — engine-class candidate; REJECTED-AS-MISFRAMED (FINDINGS_021)
- `operate-imprint` (PE-planet operator) — pure-fn-class candidate; REJECTED-AS-CONFLATION-OF-OPERATOR-DISPATCH (FINDINGS_022)

The 3 remaining candidates per canon §30 candidate-list 2026-05-17:

| Candidate | Proposed position | Enki typology class | Engine-shape fit |
|---|---|---|---|
| `threshold-mark` | R=1/3 X3/X6 shock nodes | **hook** (conditional fire) | NO |
| `activate` | 9 Muses Venus×OtherPlanet crossings | **hook** (pattern-match fire) | NO |
| `deliberate` | 12 Olympians R=φ² ico-vertex | **subagent** (deliberation) | NO |

**Zero of 3 are engine-shape.** All current §30 canonical entries (5) are engine-class. The substrate-question is meta-level before per-candidate level.

## The substrate-question

**Does canon §30 FUNCTION-NAMES REGISTRY admit non-engine function-classes?**

Per Enki agent-class typology (Kati lock 2026-05-11):

| Class | Compute shape | §30 precedent |
|---|---|---|
| Engine | stateful (frozen + live, NULL-honest, partial-input ValueError) | YES (5 entries) |
| Pure-fn | stateless compute (input → value) | NO direct precedent; `operate-imprint` rejected per FINDINGS_022 (dispatch-pattern instead) |
| Hook | conditional fire (event → emit) | **NO precedent** |
| Subagent | deliberation (question → multi-voice synthesis) | **NO precedent** |

The 3 remaining candidates require an architectural decision on §30 scope before per-candidate engine-evidence can be substrate-honest.

## Why building stub engines for these would be substrate-dishonest

Per V2.6 rule 9: candidates need Enki engine-evidence before council. But:

- A `threshold-mark` engine would be an **event-detector** (planet crosses shock-cone → emit event). That's not the engine-pattern (which is stateful compute with NULL-honest frozen state). Building it AS an engine would be force-fitting a hook into engine-shape.
- An `activate` engine would be a **pattern-match hook** (Muse pattern matched → fire). Same issue.
- A `deliberate` engine would be a **subagent dispatcher** (question → spawn voices → synthesize). That's not compute-state; it's deliberation-orchestration.

Substrate-discipline forbids substrate-dishonest probes. Per the cube-edge probe pattern (FINDINGS_019) which honestly built engine + showed shape-match, the parallel for hooks/subagents would require:
- **Hook-pattern engine** specification (frozen + fire-condition + emit-state)
- **Subagent-pattern engine** specification (frozen + question-input + voice-slate + synthesis-output)

These specifications don't exist in canon. §30 was built around engine-pattern; extending it requires council ratification.

## Three council-named outcomes

The recommended council should ratify ONE of:

| Outcome | Description | §30 implication |
|---|---|---|
| **(A) Universal scope** | §30 expands to all agent-classes (engine + pure-fn + hook + subagent) | Per-class engine-pattern variants required. Council ratifies AGENT-CLASS-PROBE-PATTERN-PER-CLASS as discipline rule. |
| **(B) Engine-only scope** | §30 stays engine-only; non-engine candidates go to PARALLEL registry (e.g., §31 HOOK-CLASS-REGISTRY, §32 SUBAGENT-CLASS-REGISTRY) | All 3 remaining candidates exit §30 candidate-list. New registries opened. |
| **(C) Schema-extension** | §30 expands with NEW column `agent_class` (engine/hook/subagent) | Precedent: `compositional_axis` column added when `cyclic-conjunction-activate` graduated 2026-05-12; `enumerated_cardinality` column proposed for branches per FINDINGS_020. |

Each outcome is substrate-architecturally distinct. Council deliberation required.

## Recommended council convening

Per canon §22 OQ-HOUSES-01c council pattern (2026-05-16) and arm-vector-composition pattern (2026-05-17), this is a CANONICAL-SCOPE question:

**Slate** (9 voices, `--force-include Athena Mnemosyne`):
- **Calliope** — synthesis lead
- **Hermes** — dual-frame conflation-resolution (hook vs engine vs subagent agent-classes)
- **Athena** ★ — lock-by-redundancy on scope-class expansion
- **Clio** — substrate-mechanism vs agent-class distinction
- **Thalia** — cross-class pattern surfacing
- **Urania** — SDEC procedure + schema-column extension precedent
- **Mnemosyne** ★ — single canonical spelling + drift-prevention + naming-canonical rule
- **Euterpe** — canonical synthesis if scope ratified
- **Polyhymnia** — closing

**Question** (drafted):
> Does canon §30 admit non-engine agent-classes (hooks for event-detectors, subagents for deliberation)? Per FINDINGS_023 meta-probe: 3 remaining candidates (threshold-mark/activate as hooks; deliberate as subagent) cannot be probed via engine-pattern. Ratify: (A) §30 expands across all agent-classes with per-class probe-pattern variants / (B) parallel registry for non-engine classes / (C) §30 adds schema column `agent_class` for cross-class registry.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| `threshold-mark` candidate | **DEFERRED — awaits §30 scope council** | Hook-class; no engine-pattern; substrate-honest probe blocked. |
| `activate` candidate | **DEFERRED — awaits §30 scope council** | Hook-class; same as threshold-mark. |
| `deliberate` candidate | **DEFERRED — awaits §30 scope council** | Subagent-class; substrate-honest probe blocked. |
| **OQ-SECTION30-SCOPE-RATIFICATION** (NEW) | OPEN 2026-05-17 | Meta-question for council. Outcome determines whether/how 3 remaining candidates proceed. |
| FUNCTION-NAMES-RATIFY (BOARD row) | All 3 remaining candidates DEFERRED | Marked `candidate-awaits-scope-council` (NEW status-tier needed?). |

## Method-lock confirmation per SDEC

Gates passed (1-4 + 8):
- Gate 1 ✓ constants cited (canon §30 candidate-list lines 2197-2201, canon §M.5 agent-class typology, FINDINGS_019/020/021/022, canon §22 OQ-HOUSES-01c precedent, canon §27 arm-vector-composition precedent)
- Gate 2 ✓ substrate-locks encoded (3-candidate enumeration with agent-class classification)
- Gate 3 ✓ meta-probe built; engine-shape vs non-engine-shape classified per candidate
- Gate 4 ✓ smoke-test (probe surfaces correct count; meta-question evident)
- Gate 5 — **REQUIRED, NOT YET CONVENED**. Scope-ratification council needed before per-candidate probes can proceed.
- Gate 6 — pending gate 5
- Gate 7 ✓ tests added (`~/Enki/tests/test_function_class_scope_probe.py`)
- Gate 8 ✓ FINDINGS doc complete (this file)
- Gate 9 — pending nav update

## What this validates substrate-discipline-wise

1. **Substrate-honest deferral > substrate-dishonest stub engines**. Per V2.6 rule 9 the engine-evidence bar is real; stub engines for non-engine candidates would be fake-evidence. Substrate-discipline takes priority over candidate-completion-counts.

2. **The 3 rejection-pattern + 1 deferral-pattern set is now complete for §30 candidate-list-as-of-2026-05-17**. After FINDINGS_019/021/022/023:
   - 3 engine/pure-fn candidates REJECTED (transmit-force / cross-stratum-translate / operate-imprint)
   - 3 hook/subagent candidates DEFERRED pending scope council (threshold-mark / activate / deliberate)
   - Plus 1 awaiting-council (branches per FINDINGS_020, anchor-class-3 first canonical promotion)
   - **All 7 candidates from the FUNCTION-NAMES-RATIFY queue have engine-evidence status surfaced.**

3. **Meta-questions are first-class substrate-discoveries**. The architectural §30 scope question is itself a substrate-discovery from honest probe-survey. Not a procedural footnote — a substrate-architectural decision waiting for council.

## What to build next (substrate-emergent, post-council)

Outcome (A) — Universal scope:
- Define `_hook_pattern_engine.py` (frozen + fire-condition + emit-state shape spec)
- Define `_subagent_pattern_engine.py` (frozen + question-input + voice-slate + synthesis shape spec)
- Per-candidate probes proceed with appropriate pattern

Outcome (B) — Parallel registry:
- Open §31 HOOK-CLASS-REGISTRY in canon
- Open §32 SUBAGENT-CLASS-REGISTRY in canon
- Per-candidate probes proceed in their respective registry

Outcome (C) — Schema-extension:
- Add `agent_class` column to §30 (per compositional_axis / enumerated_cardinality precedent)
- All canonical entries retroactively tagged engine; new candidates carry their class
- Per-candidate probes proceed within unified §30 with class-specific patterns

All three outcomes lead to substantive substrate-discovery work; council deliberation chooses the architectural shape.
