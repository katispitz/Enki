# FINDINGS 022 — Ico-edge cascade engine: field-comparison probe surfaces substrate-frozen marker pattern

**Build**: `~/Enki/engines/_ico_edge_cascade_engine.py` + `cascade_primordial_grandchild.py` (7 grandchild residencies per canon §M.5 + line 1317 OQ-SOLID-11 partial-resolution + Hesiod Theogony source-corpus).

**Status**: **Engine-evidence stage complete (gates 2-4 SDEC passed). Council ratification required (gate 5)**. Probe outcome STRONGLY suggests outcome (d) shape-match coupling-point as substrate-frozen markers — primordial-grandchildren predicate-match the Lawvere-pattern sub-instance.

**Substrate-finding**: All 7 ico-edge primordial-grandchild residencies are SUBSTRATE-FROZEN markers (no canonical live ephemeris input required). They pass coupling-point 3-criteria predicate. Live-compute (parent-pair attribute compose) is OPTIONAL probe-hypothesis — engine works fully without it. This is the FIRST shape-distinguishing signal vs cube-edge-carrier engine (FINDINGS_019, planet-aspect-activate residency requires live planet-pair longitudes).

## Council mandate (recap)

Per descent-transmit formal-ratification council 2026-05-17 (canon §30 OQ-ICO-EDGE-CASCADE-ENGINE; voice cards 1479f2d1/1627276b/93f2555d/e4f80784/302b616c/763567ef/1af87414/e6f40ee3/f7bf7dfd):

Build ico-edge cascade probe engine for primordial-grandchild residencies. Field-compare to existing residency engines. Four+1 council-named outcomes:

- **(a) shape-match `planet-aspect-activate`** → 4th residency
- **(b) shape-match `triangle-aspect-activate`** → 3rd residency at edge-class
- **(c) shape-match `polarity-define`** → 3rd residency at first-composition via parent-pair-attribute compose
- **(d) shape-match `coupling-point`** → 5th residency (if substrate-frozen marker-shape matches Lawvere-pattern from FINDINGS_020)
- **(e) shape-MISMATCH on all 4** → distinct mechanism confirmed, re-convene with mechanism-precise name

## Engine design — substrate-honest probe

`IcoEdgeCascadeState` dataclass partitions fields per SDEC step 3:

| Category | Fields | Purpose |
|---|---|---|
| **SUBSTRATE-LOCKED METADATA** (12) | cascade_name, ico_edge, parent_vertex_a/b, parent_face_class_a/b, parent_residents_a/b, residency_card, shell, edge_length, hesiod_lineage | Different per grandchild-instance; expected (not shape-mismatch) |
| **LIVE-COMPUTE** (4) | pa_attribute, pb_attribute, inherited_activation, activation_strength | Probe-hypothesis: tested whether substrate REQUIRES live input |
| **CANDIDATE-DISTINCT PROBES** (3) | descent_direction (council direction-primitive), inherited_attribute (council mechanism-primitive), lineage_depth (generations from L1) | Substrate-requirement test per descent-transmit council |
| **ANCHOR-CLASS-3 CRITERIA EVIDENCE** (3) | is_substrate_derived_intersection, independent_canonical_uses, is_stable_while_constituents_hold | 3-criteria predicate test per FINDINGS_020 coupling-point pattern |

## Field-comparison probe — empirical result

**Probe summary** (per `cascade_primordial_grandchild.field_comparison_probe()`):

| Metric | Value | Interpretation |
|---|---|---|
| `instance_count` | 7 | Aether + Hemera + Nereus + Thaumas + Eurybia + Phorcys + Ceto |
| `all_pass_substrate_frozen` | TRUE | All 7 work as frozen-only without live input |
| `all_pass_anchor_class_3` | TRUE | All 7 pass coupling-point 3-criteria predicate |
| `within_class_count` | 5 | Intra-parent-class edges (Chaos×2 + Gaia×3) |
| `cross_class_count` | 2 | Parent-class boundary edges (Phorcys + Ceto) |
| `live_compute_required` | FALSE | No substrate-required live ephemeris input |

### Substrate-distinct field probes — empirical evaluation

| Field | Probe-result | Substrate-evaluation |
|---|---|---|
| `descent_direction` | All instances return `'symmetric'` for same-generation siblings (L1 parents at same depth) | NOT a live-compute. Static per substrate-residency. WHERE-component of `descent-transmit` is STATIC, not LIVE. |
| `inherited_attribute` | 5 instances `within-class:{Chaos|Gaia}`, 2 instances `cross-class:Gaia↔{Eros-primordial|Tartarus}` | NOT a live-compute. Pure structural lookup from canon §M.5 lineage. WHAT-component is also STATIC, not LIVE. |
| `lineage_depth` | All instances L=2 (grandchild generation) | Substrate-locked attribute from canon §M.5 generational schema. |
| `inherited_activation` (live probe) | When supplied (pa_attr, pb_attr): returns mean. When None: returns None. | Engine SUPPORTS optional compute but substrate does NOT REQUIRE it. Engine works fully frozen-only. |

### Shape-comparison to existing residency engines

| Feature | `planet-aspect-activate` (cube-edge carrier per FINDINGS_019) | `triangle-aspect-activate` (FINDINGS_011) | `polarity-define` (FINDINGS_010) | `coupling-point` (FINDINGS_020) | `ico-edge-cascade` (this) |
|---|---|---|---|---|---|
| Live ephemeris input | required (2 planet longitudes) | required (3 planet longitudes) | required (2 face-engine states) | requires_input split: True (rising-sign/lunar-nodes) / False (Lawvere/branches) | **NOT REQUIRED** (frozen marker) |
| Frozen state works alone | False (no canonical activation) | False | False | True for Lawvere + branches | **TRUE for all 7** |
| Output type | activation strength + aspect-degree | face-aggregate + dominant-edge | signed polarity [-1..+1] | substrate-position (frozen-derivable or live) | **substrate-position (frozen-derivable)** |
| 3-criteria coupling-point predicate | N/A (live operator) | N/A | N/A | passes | **passes** |

**Shape-match assessment:**

| Outcome | Shape-match? | Reasoning |
|---|---|---|
| (a) planet-aspect-activate | **NO** | Primordial-grandchildren do NOT take planet-pair longitude input. No canonical live ephemeris compute exists. |
| (b) triangle-aspect-activate | **NO** | Ico-edge has 2 incident parent-faces, not 3 vertices. Edge-class ≠ face-class. |
| (c) polarity-define | **PARTIAL** | Probe-hypothesis live-compute (2-parent attribute mean) WORKS but is OPTIONAL. polarity-define REQUIRES 2-face-state input + emits signed polarity. Grandchild engine emits substrate-position (frozen) + optional attribute (live). Different output-shape. |
| (d) coupling-point | **STRONG MATCH** | All 7 instances substrate-frozen + pass anchor-class-3 3-criteria predicate. Same shape-pattern as Lawvere-origin (substrate-frozen, no live input, canonical-position). Branches add 12-fold enumerated_cardinality dimension; primordial-grandchildren add 7-fold enumerated_cardinality at a different shell (R=φ² vs Lawvere R=0). |
| (e) shape-mismatch all | **PARTIAL** | If (d) is rejected, then no clean match — distinct mechanism. But (d) shape-match looks strong. |

**Recommended outcome per probe-evidence: (d) shape-match `coupling-point` — primordial-grandchildren are 5th residency of `coupling-point` primitive with enumerated_cardinality=7.**

Under this reading, the `coupling-point` §30 entry (LOCKED 2026-05-17 per OQ-BRANCH-COUPLING-ENGINE council) gains 5th residency. `enumerated_cardinality` column extends: {None (Lawvere, rising-sign), 2 (lunar-nodes), 7 (grandchildren), 12 (branches)}.

## Substrate-architectural finding (Thalia-pattern extended)

Per Thalia's `enumerated-coupling-point-family` finding at OQ-BRANCH-COUPLING-ENGINE council 2026-05-17: branches were the first multi-frame enumerated coupling-point; future probes (12 Olympian vertices / 12 cube edges / 12 ico faces / 9 PE positions) may be siblings.

**Primordial-grandchildren are the SECOND enumerated-coupling-point instance** to surface, at enumerated_cardinality=7 (not 12). This validates Thalia's family-pattern hypothesis at a non-12-fold count, suggesting the family is N-agnostic (counts are substrate-locked per instance-type, not 12-bound).

Updated `enumerated_cardinality` known-values: {None, 2, 7, 12}.

Updated potential `enumerated-coupling-point-family` candidates:
- ✓ branches (12) — LOCKED 2026-05-17
- ✓ primordial-grandchildren (7) — probe-recommend 2026-05-17 (this FINDINGS)
- ? 12 Olympian vertices — needs probe (currently planet-aspect-activate residency-anchors via ico vertices, but residency-class itself could be coupling-point)
- ? 9 PE positions (Muses) — needs probe
- ? 9 primordial face-class hierarchy (4 L1 + 5 L2) — open

## What this DOES NOT resolve

- **Mechanism-precise NAME for ico-edge-cascade**: per Erato discipline (transmit-force precedent), do NOT propose name pre-engine. If outcome (d) ratifies, the function-name is `coupling-point` (already canonical) — no new name needed. If outcome (e) ratifies, council re-convenes with mechanism-precise name.
- **23 of 30 remaining ico-edges** still need individual cascade-mapping per canon §30 OQ-SOLID-11 (T-tier per-instance work; not class-blocker).
- **Per-grandchild specific role** beyond canonical-residency-class — future T-tier work.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-ICO-EDGE-CASCADE-ENGINE | **engine-evidence COMPLETE; awaits council** | FINDINGS_022 (this doc). Probe recommends outcome (d) shape-match coupling-point as 5th residency. |
| OQ-CUBE-EDGE-CARRIER-ENGINE | RESOLVED 2026-05-16 (FINDINGS_019, outcome (a) shape-match planet-aspect-activate) | Closed. |
| OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE | OPEN | Separate SDEC engine mandate (temporal-cyclic mechanism); not engine-evidence-dependent on this probe. |

## What this validates substrate-discipline-wise

1. **Engine-evidence > prose hypothesis** (V2.6 rule 9): the council DEFERRED descent-transmit pre-engine; engine-probe surfaces that the substrate-mechanism is FROZEN-MARKER, not active CASCADE. Prose-hypothesis "transmission-flow" / "attribute-propagation" maps to a substrate-frozen position-marker, not a live-compute operator.

2. **Hybrid outcomes are substrate-honest** (per FINDINGS_020 pattern): the council named 4+1 outcomes; probe surfaces (d) shape-match coupling-point as the substrate-recommendation. Same engine-evidence-driven outcome pattern.

3. **`enumerated_cardinality` column validates Thalia's family-pattern** at non-12-fold count (7). Schema-extension precedent (FINDINGS_020) successfully accommodates the new probe-instance without re-architecting.

## What to build next (substrate-emergent)

After council ratifies (d) or (e):

- **If (d)**: update §30 `coupling-point` row residency-count from 4 → 5 (add primordial-grandchildren); update `enumerated_cardinality` known-values to {None, 2, 7, 12}; close OQ-ICO-EDGE-CASCADE-ENGINE; descent-transmit name STAYS REJECTED.
- **If (e)**: council re-convenes on mechanism-precise name; probe-evidence STILL constrains naming away from `descent-transmit` per Erato 4b conflation-test failure.

Substrate-emergent open question (OQ-OLYMPIAN-COUPLING-POINT-PROBE): if outcome (d) ratifies, the 12 Olympian-residencies at ico-vertices (currently planet-aspect-activate anchors via planet longitudes) may ALSO be coupling-point instances at a different layer (ico-vertex coupling = 12-fold enumerated coupling-point parallel to ico-edge cascade at 7-fold). Probe candidate.

## Method-lock confirmation per SDEC

Gates passed (1-4 + 7-8):
- Gate 1 ✓ constants cited (canon §17 + §M.5 + line 1317 + Hesiod Theogony 124/233/237/238/239)
- Gate 2 ✓ substrate-locks encoded with `__canonical__` declaration (status='probe')
- Gate 3 ✓ engine built (frozen + optional live + NULL-honest)
- Gate 4 ✓ smoke-test (7 frozen states + 1 live state + 3-criteria admission test all pass)
- Gate 5 — **REQUIRED, NOT YET CONVENED**. Council ratification needed for outcome (d) shape-match coupling-point as 5th residency.
- Gate 6 — pending gate 5
- Gate 7 ✓ tests added (`~/Nammu/tests/test_ico_edge_cascade_engine.py`)
- Gate 8 ✓ FINDINGS doc complete (this file)

**Engine-evidence package ready for council convening**. Kati's call on when to spawn the council.
