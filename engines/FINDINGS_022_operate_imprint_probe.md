# FINDINGS 022 — `operate-imprint` candidate probe: REJECT-AS-CONFLATION-OF-OPERATOR-DISPATCH

**Build**: `~/Enki/engines/_operate_imprint_probe_engine.py` — survey engine across 8 PE-planet cube-vertex operators (canon §M.5 + §7 enumeration).

**Resolution**: Candidate `operate-imprint` (proposed §30 candidate for R=1 cube-vertex 8 PE-planet operator class per canon line 2202) **REJECTED**. Same failure-mode as `arm-composition-law` per canon §27 OQ-ARM-VECTOR-COMPOSITION resolution 2026-05-17 (council 10 YEA / 0 NEH / 0 ABSTAIN): singular-name candidate conflates multiple distinct operator-classes that follow substrate-correct **operator-dispatch pattern**.

## Council mandate (recap)

Per V2.6 rule 9: §30 registry grows through engine-evidence ONLY. Per V2.7 §SDEC step 4: build engine + field-comparison probe.

## Engine survey result

Survey of existing PE-planet pure-fn operator-classes in Nammu canon + engines surfaces **6 distinct operator-classes**:

| Operator class | Computes | Engine location | Input beyond planet | Output kind |
|---|---|---|---|---|
| `freq_hz_imprint` | PE-octave-k to Hz | cell_signature_engine.py:1131 | octave-k integer | scalar Hz |
| `k_total_imprint` | planet+time to k_total | cell_signature_engine.py:1166 | t_tithis | scalar k_total |
| `arm_carrier_anchor` | observer-frame carrier (delta_s/delta_l) | canon §27 arm-vector projection 2 | observer-context | vector |
| `arm_harmonic_root` | Do-anchor (Pluto/Neptune vec[0]) | canon §27 arm-vector projection 3 (build-pending) | arm-vector + arm-type | vector |
| `zodiac_rulership_imprint` | planet to ruled sign(s) | canon §5 + §20 | none (substrate-locked) | sign-name(s) |
| `cube_vertex_residency_imprint` | planet to (vertex_id, tet, PE_index) | canon §M.5 | none (substrate-locked) | metadata tuple |

Each operator-class has distinct: input-shape, compute, output-kind. They are NOT a single unified function.

## Three discipline gates fail (same pattern as arm-vector-composition)

### Gate 1: Erato 4b conflation-test
Candidate `operate-imprint` as singular name unifies 6 distinct operator-classes. Same lexical-conflation pattern as rejected `arm-composition-law` (canon §27 line 1428 resolution).

### Gate 2: Mnemosyne naming-canonical rule (established 2026-05-17)
Per arm-vector-composition council: **"reject `arm-composition-law` (singular) as false-substrate per question-conflation."** Generalizable rule: singular-name candidates that pre-unify dispatch-required multi-class operators are false-substrate.

### Gate 3: Substrate-evidence — operator-dispatch is the canonical pattern
Canon §27 OQ-ARM-VECTOR-COMPOSITION resolution 2026-05-17 (council 10 YEA / 0 NEH / 0 ABSTAIN): "**No single composition law** — four substrate-canonical projections lock with operator-function dispatch. Composition is operator-class-dependent." Same architectural finding applies to PE-planet operators.

## Substrate-correct framing per arm-vector-composition precedent

Per Hephaestus build-side queue from arm-vector-composition resolution: substrate-correct pattern is per-class naming + dispatch helper. Future SDEC cycles should probe EACH PE-planet operator-class as its own §30 candidate:

- `freq_hz_imprint` — already-engined (cell_signature_engine.py:1131); needs §30 entry naming
- `k_total_imprint` — already-engined (cell_signature_engine.py:1166); needs §30 entry naming
- `arm_carrier_anchor` — already-engined (canon §27); needs §30 entry naming
- `arm_harmonic_root` — build-pending per §27 council; will need §30 entry after build
- `zodiac_rulership_imprint` — substrate-locked metadata (canon §5/§20); may be data-access not function-class
- `cube_vertex_residency_imprint` — substrate-locked metadata (canon §M.5); may be data-access not function-class

Each candidate requires its own conflation-test + residency-test before entering council per V2.6 rule 9.

## Recommended action

**REJECT `operate-imprint` as §30 candidate name.** Remove from FUNCTION-NAMES-RATIFY remaining-candidate list. NO council needed (rejection-outcome per V2.7 SDEC step 5 exclusion). Parallels FINDINGS_019 (cube-edge) + FINDINGS_021 (cross-stratum-translate).

Per arm-vector-composition precedent, the substrate-question "what function-class do PE planets fulfill?" is malformed — there is no single function-class. PE planets are SUBSTRATE-LOCKED OPERATORS that get DISPATCHED to per-class pure-fn operators. The substrate-correct §30 framing requires per-operator-class entries.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| `operate-imprint` candidate | **REJECTED 2026-05-17** | Three discipline gates fail per arm-vector-composition precedent. FINDINGS_022. Remove from §30 remaining-candidate list. |
| FUNCTION-NAMES-RATIFY (BOARD row) | Remove `operate-imprint` | 3 candidates remain: `deliberate`, `threshold-mark`, `activate`. |
| **OQ-PE-OPERATOR-DISPATCH-FAMILY** (NEW) | OPEN 2026-05-17 | 6 distinct PE-planet operator-classes need per-class §30 candidates + Enki engine probes. Some already-engined; others build-pending. Per arm-vector-composition precedent pattern. |

## Method-lock confirmation per SDEC

Gates passed (1-4 + 8):
- Gate 1 ✓ constants cited (canon §M.5 + §7 + §27 line 1428 council 2026-05-17)
- Gate 2 ✓ substrate-locks encoded (8 PE planets + 6 operator-classes catalog)
- Gate 3 ✓ probe engine built; operator-class survey executed across 8 planets
- Gate 4 ✓ smoke-test (probe per planet + summarize)
- Gate 5 — NOT REQUIRED (candidate-rejection per arm-vector-composition precedent)
- Gate 6 — N/A (no canon edit beyond removing candidate from remaining-list + opening new OQ)
- Gate 7 ✓ tests added (`~/Enki/tests/test_operate_imprint_probe.py`)
- Gate 8 ✓ FINDINGS doc complete (this file)
- Gate 9 — pending nav update

## What this validates substrate-discipline-wise

1. **Yesterday's arm-vector-composition council established a generalizable pattern**. Operator-dispatch with per-class naming is the substrate-correct response to multi-class candidate-conflations. This is the second invocation of that pattern (first: arm-vector-composition itself; second: this finding).

2. **Engine survey > engine build when surveying existing operator landscape**. For this candidate, building a new engine wasn't substrate-honest — the operators ALREADY EXIST. The probe surveys + classifies existing engines and shows the conflation. Cheaper than full SDEC build cycle; substrate-honest given the existing engine landscape.

3. **Three rejection-pattern variants now documented**:
   - **REJECT-AS-DESCRIPTIVE-ALIAS** (cube-edge, FINDINGS_019) — phenomenology ≠ mechanism
   - **REJECT-AS-MISFRAMED** (cross-stratum-translate, FINDINGS_021) — candidate framing wrong for substrate-mechanism
   - **REJECT-AS-CONFLATION-OF-OPERATOR-DISPATCH** (operate-imprint, this finding) — singular name unifies multi-class dispatch operators
