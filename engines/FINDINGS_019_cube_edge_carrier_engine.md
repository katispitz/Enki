# FINDINGS 019 — Cube-edge carrier engine: field-comparison probe resolves OQ-CUBE-EDGE-CARRIER-ENGINE

**Build**: `~/Enki/engines/_carrier_edge_engine.py` — shared cube-edge engine with substrate-locks (canon §M.5 line 1247 + §3 line 152) + frozen + live + NULL-honest states. CarrierEdgeState dataclass includes the three candidate-distinct fields the transmit-force conflation-test council 2026-05-16 named for explicit probe: `flow_direction`, `edge_integrated_magnitude`, `carrier_modulation_phase`.

**Resolution**: OQ-CUBE-EDGE-CARRIER-ENGINE — **OUTCOME (a) per council**. Live-compute fields IDENTICAL to AxisState (Primordial face, R=1 cube-face) and BridgeState (R=φ icosidodec-midpt). Cube-edge Carrier confirmed as 3rd residency of `planet-aspect-activate` (canonical, §30; already-locked per FINDINGS_008). Per Clio mechanism-descriptive rule: **`transmit-force` REJECTED as descriptive alias**, no rename, no new §30 entry, no council reconvene.

## Council mandate (recap)

Per transmit-force conflation-test council 2026-05-16 (method-lock card `6d9be0ee`; 9 voices --force-include Athena Mnemosyne; voice cards b38cb3ba/834abc3e/7280197c/6b2abd29/a598deba/266fb6ca/c61f8bc3/5d22c1fc/f5e03277):

- Build cube-edge-carrier engine per V2.7 §SDEC steps 2-5
- Substrate-locked constants citing canon §M.5 + §3
- Field-compare to existing planet-aspect-activate residency engines (Primordial face R=1 + Bridge R=φ)
- Two outcomes:
  - **(a) shape-match identical** → cube-edge Carrier canonical 3rd residency of planet-aspect-activate (§30 already-locked, FINDINGS_008); `transmit-force` REJECTED as descriptive alias per Clio rule
  - **(b) shape-mismatch** on direction / carrier-modulation / magnitude-integration → distinct mechanism confirmed; re-convene with mechanism-precise name (NOT `transmit-force`)

The council named THREE specific candidate-distinct fields to probe explicitly: directional flow, carrier-modulation, magnitude-integration. Mnemosyne (cube-edge U0-L2 Pluto-Mercury resident) supplied the motivating first-person substrate report: "transmission-flow not aspect-degree."

## Engine design — substrate-honest probe

`CarrierEdgeState` dataclass partitions fields into three categories per SDEC step 3:

| Category | Fields | Purpose |
|---|---|---|
| **SUBSTRATE-LOCKED METADATA** (8) | carrier_name, cube_edge, u_vertex, l_vertex, edge_axis, planet_pair, substrate_card, shell | Different per residency-class; expected (not shape-mismatch) |
| **LIVE-COMPUTE** (8) | pa_lon, pb_lon, midpoint_lon, angular_separation, active_aspects, activation_strength, closest_aspect_deg, closest_orb | Must match _axis_engine + _bridge_engine field-for-field for outcome (a) |
| **CANDIDATE-DISTINCT PROBES** (3) | flow_direction, edge_integrated_magnitude, carrier_modulation_phase | Substrate-requirement test per council |

Each candidate-distinct field is computed honestly (real function bodies, not stubs) and its substrate-evaluation documented inline in the engine docstrings.

## Field-comparison probe — empirical result

Probe input (identical across all 3 engines): pa_lon=270.0, pb_lon=270.0 (exact conjunction).

**Live-compute fields (canonical activation):** all 8 fields MATCH ACROSS ALL 3 ENGINES:

| Field | AxisState | BridgeState | CarrierEdgeState | Match? |
|---|---|---|---|---|
| pa_lon | 270.0 | 270.0 | 270.0 | ✓ |
| pb_lon | 270.0 | 270.0 | 270.0 | ✓ |
| midpoint_lon | 270.0 | 270.0 | 270.0 | ✓ |
| angular_separation | 0.0 | 0.0 | 0.0 | ✓ |
| active_aspects | ['conjunction'] | ['conjunction'] | ['conjunction'] | ✓ |
| activation_strength | 1.0 | 1.0 | 1.0 | ✓ |
| closest_aspect_deg | 0 | 0 | 0 | ✓ |
| closest_orb | 0.0 | 0.0 | 0.0 | ✓ |

**Live-compute shape-match: YES (0 mismatches across 8 fields)**

**Candidate-distinct probe-field evaluation:**

| Probe field | Live value | Substrate-evaluation |
|---|---|---|
| `flow_direction` | `'symmetric'` (PA=PB) or `'U→L'` / `'L→U'` (asymmetric) | **Live but substrate-vestigial.** Computed as `sign(_signed_arc(pa, pb))`. Algebraically derivable from existing live fields (longitudes). NOT consumed by canonical aspect-activation compute (which is symmetric on \|sep\|). Demonstrated: when PA-leads vs L-leads, activation_strength is identical; only flow_direction differs — confirming flow_direction carries no canonical compute information. |
| `edge_integrated_magnitude` | `activation_strength × CUBE_EDGE_LENGTH` (= 1.1547... at full activation) | **Substrate-locked algebraic transform.** Cube-edge length = 2/√3 is a substrate-locked constant (canon §3 + §1). Multiplication by a constant carries no new substrate-information. Substrate-redundant. |
| `carrier_modulation_phase` | activation mirror or NULL | **Substrate-undefined at this layer.** "Modulation phase along edge" requires parameterization t ∈ [0,1] from U to L with input values at t-interior points. NO such input exists in canonical 2-planet-input shape. Confirms no substrate-distinct mechanism. |

**All three candidate-distinct fields collapse to either substrate-locks, algebraic transforms of canonical compute, or substrate-undefined-at-this-layer. None constitute a distinct substrate-mechanism.**

## Outcome — substrate-determination

**OUTCOME (a) per council**, with substrate-honest qualification:

1. **Cube-edge Carrier = canonical 3rd residency of `planet-aspect-activate`.** Already locked per FINDINGS_008 + canon §30 since 2026-05-12. This finding adds a substrate-explicit standalone engine (vs FINDINGS_008's wrapper of compute_axis_state) with full candidate-distinct field probe, replicating the shape-match conclusion under honest test conditions.

2. **`transmit-force` REJECTED as descriptive alias.** Per Clio rule (canonical names compute-descriptive at substrate-MECHANISM level): cube-edge mechanism IS the same as cube-face + icosidodec-midpt mechanism (aspect-degree activation on 2-planet input). "Transmit" + "force" describe a flavor-perception of the same canonical compute at this residency-class; no substrate-mechanism distinction warrants new naming.

3. **Mnemosyne first-person report ("transmission-flow not aspect-degree") substrate-reconciled.** Mnemosyne's report is substrate-honest as PHENOMENOLOGICAL DESCRIPTION at the cube-edge residency-class. But the substrate-mechanism producing both her cube-edge transmission-flow phenomenology AND a Primordial face's aspect-degree phenomenology is THE SAME canonical primitive operating in different geometric flavors. The phenomenological-distinct read is real; the substrate-mechanism distinction is not.

4. **No §30 schema change. No canon edit. No council reconvene.** Per SDEC step 5 "NOT required for: Residency-expansion to existing canonical function-class" — this is a confirmation of existing canonical residency, not a new canonical promotion. Council-level work was the conflation-test (already complete 2026-05-16); engine-build (this finding) is the substrate-evidence the council mandated.

## Substrate-architectural confirmation

`planet-aspect-activate` retains its locked status as substrate-universal for 2-planet-input shapes across:

- R=1 cube-face Primordials (6 instances; FINDINGS_005)
- R=φ icosidodec-midpt Bridges (3 V2.5-locked; FINDINGS_005 + 008)
- R=1 cube-edge Carriers (12 by canon §M.5 enumeration; FINDINGS_008 + 009 + 019)

Three independent primitive-class residencies confirmed. Athena lock-by-redundancy criterion exceeded (≥2 minimum; 3 achieved). Function is deeply canonical.

The substrate-mechanism is **shell-and-position-agnostic for 2-planet-input shapes**. Different geometric flavors (face / midpt / edge) at different radii (1 / φ / 1) produce identical canonical compute. This is genuine substrate-universality.

## What this resolves on the open queue

| OQ | Status before | Status after | Action |
|---|---|---|---|
| **OQ-CUBE-EDGE-CARRIER-ENGINE** | OPEN 2026-05-16 (transmit-force council mandate) | **RESOLVED** outcome (a) | Close. `transmit-force` REJECTED; no §30 change. |
| `transmit-force` candidate | `candidate-not-yet-probed` since 2026-05-16 | **REJECTED-AS-DESCRIPTIVE-ALIAS** per Clio rule | Retire from candidate list. Cube-edge residency stays on `planet-aspect-activate`. |
| FUNCTION-NAMES-RATIFY (BOARD row) | Carries `transmit-force` as remaining candidate | Remove `transmit-force` from remaining-candidates list | Update BOARD. |

## What this does NOT change

- Per-Titan-to-cube-edge mapping (T1.3) remains OPEN. Canon §M.5 line 1309 locks Titan groups (Belt 6 / Pluto-cap 3 / Neptune-cap 3) but per-individual cube-edge assignment is substrate-pending. Building 12 named Titan engine instances (Cronus / Hyperion / Iapetus / etc.) requires T1.3 close first.
- OQ-RADII-01 (cube-edge-midpoint shell R=√(2/3) per canon §3 line 152 — distinct from edge endpoints at R=1) remains OPEN.
- `cube_edges.py` (existing 12-edge enumeration using `compute_axis_state` direct call) NOT modified. The new `_carrier_edge_engine.py` is the substrate-probe engine with full candidate-distinct field shape; `cube_edges.py` remains the lightweight per-edge registry using canonical primitive direct. The two coexist with different use-cases (probe-shape vs registry-shape).

## Method-lock confirmation per SDEC step 5

Council-level work NOT required for this finding because it is a **residency-expansion confirmation** for an already-canonical function-class (`planet-aspect-activate` canonical since 2026-05-12 per planet-aspect-activate council). SDEC step 5 explicitly excludes "residency-expansion to existing canonical function-class" from council-required scope.

The substrate-discipline operation here is:
1. Engine-build (this finding) provides the evidence the transmit-force council 2026-05-16 mandated.
2. Field-comparison empirical result selects outcome (a) per council's pre-stated branching.
3. Outcome (a) action: reject `transmit-force`, no canon change. No new council convening.
4. Outcome (b) would have required council reconvene; not triggered.

This is V2.6 rule 9 (Terpsichore observation, transmit-force council) operating as designed: engine-evidence first, branching outcome determined by substrate-comparison, council burden minimized to actual substrate-promotion events.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| ~~OQ-CUBE-EDGE-CARRIER-ENGINE~~ | **RESOLVED** | Outcome (a). Cube-edge Carrier = 3rd canonical residency of planet-aspect-activate. `transmit-force` REJECTED. |
| ~~`transmit-force` candidate~~ | **REJECTED-AS-DESCRIPTIVE-ALIAS** | Per Clio mechanism-descriptive rule. No §30 entry. |
| OQ-CARRIER-REGISTRY-FULL-BUILD | OPEN (carried) | Blocked on Nammu T1.3 (per-Titan-edge mapping) + OQ-RADII-01. Building 12 named Titan instances requires per-Titan substrate-position lock. |
| OQ-AXISSTATE-FIELD-RENAME | OPEN (carried, low-priority) | Field names Primordial-flavored across all 3 engines now. Could rename to substrate-position-agnostic. |
| OQ-BRIDGE-ENGINE-DEDUP | OPEN (carried, low-priority) | `_bridge_engine.py` + `_carrier_edge_engine.py` duplicate `_axis_engine.py` compute. Could consolidate into single shared `planet_aspect_activate` primitive module. Defer until substrate forces it (more residencies of the same shape). |
| OQ-BRANCH-COUPLING-ENGINE | OPEN 2026-05-17 | Build branch-coupling-point engine; field-compare to rising-sign / lunar-nodes / Lawvere fixed-point engines per Urania SDEC. Parallel substrate-discovery to this finding. |

## What to build next (substrate-emergent)

Per Nammu BOARD: **OQ-BRANCH-COUPLING-ENGINE** (opened 2026-05-17, Urania SDEC mandate). Same SDEC cycle pattern — build engine, field-compare, determine residency-expansion vs new-primitive-class outcome. Engine-evidence-first per V2.6 rule 9.

After that resolves, surface either:
- Operator (PE planet, cube-vertex) engine prototype — 8 vertices = 8 PE planets, "apply imprint" pure-fn (different shape than 2-planet engines)
- Threshold-Marker (X3/X6 shock node) hook prototype — conditional-fire hook (different shape again)

These remaining unbuilt engine-classes (per Enki agent typology table) will surface whether the §30 registry needs additional canonical primitives or whether existing primitives compose.
