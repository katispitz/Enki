# FINDINGS 020 — Branch-coupling-point engine probe: predicate-match + compute-shape-distinct

> **2026-05-17 ADDENDUM**: Council ratified outcome (c) per canon §30 line 2006 — schema-extension. Anchor-class-3 graduated to §30 as canonical function-name **`coupling-point`** (renamed from proposed `coupling-point-anchor` per Clio + Mnemosyne to avoid taxonomy-class-name fusion). 4 residencies locked (rising-sign + lunar-nodes + Lawvere + branches). NEW §30 column `enumerated_cardinality ∈ {None, N}` added per compositional_axis precedent. Council 9 voices 9 YEA / 0 NEH / 0 ABSTAIN. This engine package (`_coupling_point_engine.py` + 4 instance modules) is the substrate-evidence that satisfied V2.6 rule 9. Voice cards 4fad7ff1/a0ca109a/9bdac5eb/f9722516/a671db3e/d56077d4/9d5e973c/621be722/735fa32b. Status: **ENGINE-PACKAGE RATIFIED CANONICAL**.

**Build**: `~/Enki/engines/_coupling_point_engine.py` + 4 instance modules — `coupling_branch.py` (12-fold), `coupling_rising_sign.py`, `coupling_lunar_node.py`, `coupling_lawvere_origin.py`.

**Status**: **Engine-evidence stage complete (gates 2-4 SDEC passed). Council ratification required (gate 5).** The probe outcome is NEITHER pure-(a) nor pure-(b) per the council's binary framing — it surfaces a third reading the council should evaluate.

**Substrate-finding**: All 4 instance-classes ADMIT to anchor-class-3 by 3-criteria predicate test, BUT branches differ from the 3 singular references on `n_frames`, `coupling_type`, `requires_input`, and `enumerated_cardinality`. Predicate-match + compute-shape-distinct surfaces a hybrid outcome the engine cannot decide unilaterally.

## Council mandate (recap)

Per Card 8d8887a1 council 2026-05-17 (12 ABSTAIN; OQ-BRANCH-COUPLING-ENGINE opened per Urania SDEC):

- Build cube-edge-carrier-pattern probe engine for branches-as-coupling-points
- Field-compare to 3 existing anchor-class-3 instances: rising-sign, lunar nodes (Rahu/Ketu), Lawvere-origin
- Two council-named outcomes:
  - **(a) shape-match** → branches ratify as 4th residency of anchor-class-3 primitive (first 12-fold enumeration)
  - **(b) shape-mismatch** → upgrade to NEW primitive class (`12-fold-coupling-points-collection`)

## Engine design — substrate-honest probe

`CouplingPointState` dataclass surfaces the substrate-architectural dimensions of anchor-class-3 instances explicitly:

| Category | Fields | Purpose |
|---|---|---|
| **SUBSTRATE-LOCKED METADATA** | coupling_name, coupled_frames, n_frames, coupling_type, substrate_card | Different per instance-class; expected per residency |
| **ANCHOR-CLASS-3 CRITERIA EVIDENCE** | is_substrate_derived_intersection, independent_canonical_uses, is_stable_while_constituents_hold | 3-criteria predicate test per CP6 |
| **POSITION OUTPUT** | canonical_position (frozen-derivable), live_position (input-dependent), requires_input | Static vs dynamic substrate-position |
| **CANDIDATE-DISTINCT PROBE** | enumerated_cardinality | Branches' 12-fold enumeration not present in singular instances |

The 3-criteria test (`passes_anchor_class_3_criteria`) is enforced empirically on each instance.

## Field-comparison probe — empirical result

### 3-criteria predicate test (anchor-class-3 admission)

| Instance | substrate-derived | independent-canonical-use | stable-while-constituents | overall admits? |
|---|---|---|---|---|
| rising-sign | ✓ | ✓ (4 evidences) | ✓ | **TRUE** |
| lunar-nodes (Rahu/Ketu) | ✓ | ✓ (4 evidences) | ✓ | **TRUE** |
| Lawvere-origin | ✓ | ✓ (3 evidences) | ✓ | **TRUE** |
| branch-Zǐ (1/12) | ✓ | ✓ (5 evidences) | ✓ | **TRUE** |
| branch-Mǎo (4/12) | ✓ | ✓ (5 evidences) | ✓ | **TRUE** |
| branch-Xū (11/12) | ✓ | ✓ (5 evidences) | ✓ | **TRUE** |

**All 4 instance-classes admit to anchor-class-3 by predicate.** No exceptions across the 12-branch enumeration.

### Compute-shape comparison

| Feature | rising-sign | lunar-nodes | Lawvere | branch-Zǐ |
|---|---|---|---|---|
| `n_frames` | **2** | **2** | **2** | **4** |
| `coupling_type` | singular | pair-180 | singular | **enumerated-N** |
| `requires_input` | True | True | False | False |
| `enumerated_cardinality` | None | 2 | None | **12** |
| `frozen has canonical_position?` | False | False | True | **True** |
| `# independent canonical uses` | 4 | 4 | 3 | **5** |

**Compute-shape distinctions**:
1. **n_frames = 4 vs 2** — branches couple compass × diurnal-clock × Wu-Xing × Ganzhi-60-cycle (FOUR frames). The 3 references all couple 2 frames each.
2. **coupling_type = enumerated-N** — branches are the FIRST instance with explicit N-fold enumeration. Lunar-nodes are pair-180 (n=2 fixed by orbital geometry); rising-sign and Lawvere are singular.
3. **requires_input = False (joins Lawvere)** — branches are substrate-frozen like Lawvere; positions fully determined by substrate-locks. Rising-sign and lunar-nodes are input-dependent.
4. **enumerated_cardinality = 12** — branches add a substrate-architectural dimension (cardinality of enumeration) that singular instances don't carry.

### Position-shape comparison

| Instance | Position output fields |
|---|---|
| rising-sign (live) | zodiac_segment_idx, zodiac_segment_name, asc_lon_input |
| lunar-nodes (live) | rahu_lon, ketu_lon, pair_separation_deg (≡180°) |
| Lawvere (canonical) | x, y, z, description (3D origin point) |
| branch (canonical) | spatial_compass, temporal_hour, elemental_wu_xing, cyclic_stem_pair, beast, polarity, pinyin, wade_giles |

**Position-shape distinctions**: branches output a 4-feature substrate-locked dict per instance; rising-sign and lunar-nodes output input-derived position; Lawvere outputs 3D coordinate. No two instance-classes have identical position-shape.

## Substrate-honest interpretation

**Predicate level**: branches MATCH anchor-class-3 (all 4 admit; 3-criteria evidence held empirically across the 12-branch enumeration).

**Compute-shape level**: branches DIFFER on 4 dimensions (n_frames, coupling_type, requires_input pattern, enumerated_cardinality). Position-shape also differs across all 4 instance-classes — but that's expected for substrate-locked metadata.

**The substrate-architectural question the engine surfaces**:

Is anchor-class-3 a SINGLE primitive admitting variants on (n_frames, coupling_type, enumeration), OR a FAMILY of primitives differentiated by those dimensions?

The cube-edge-carrier probe (FINDINGS_019) faced an analogous question and resolved cleanly because LIVE-COMPUTE fields were identical across residencies. Here, **there is no shared live-compute** — branches have NO live compute (substrate-frozen), Lawvere has NO live compute (substrate-frozen), rising-sign has 1D live-compute, lunar-nodes has 1D-pair live-compute. The "live-compute identity" criterion that ratified cube-edge as canonical-residency-of-existing-class doesn't have a clean analogue here.

**Possible council readings**:

| Reading | Verdict on branches | §30 implication | Schema implication |
|---|---|---|---|
| **(a) PURE PREDICATE-MATCH = SUFFICIENT** | 4th residency of one anchor-class-3 primitive | One new §30 entry: `coupling-point-anchor` (4 residencies = 3 singular + 1 enumerated) | None new |
| **(b) PURE SHAPE-MISMATCH = NEW CLASS** | New primitive: `12-fold-coupling-points-collection` | Two new §30 entries: `coupling-point-anchor` (3 singular residencies) + `12-fold-coupling-points-collection` (1 residency = branches) | Possibly: `cardinality` column added |
| **(c) HYBRID via SCHEMA EXTENSION** | All 4 same primitive; substrate-architectural dimension added | One new §30 entry: `coupling-point-anchor` with schema column `enumerated_cardinality` (None / N) | NEW §30 column: `enumerated_cardinality` |

Reading (c) follows the precedent of `compositional_axis` being added to §30 when `cyclic-conjunction-activate` graduated (2026-05-12) — schema extension when substrate teaches a new dimension. The engine-evidence supports (c) as the substrate-honest middle path: predicate is shared, but the new dimension is real and should be tracked.

**This is a COUNCIL decision per V2.6 amended rule 9 + SDEC step 5**. Engine-evidence is now complete; council convenes to ratify a/b/c.

## What's NEW vs existing canonical state

Critically, **anchor-class-3 itself is NOT a §30 canonical entry yet**. Canon §22 OQ-HOUSES-01c council 2026-05-16 locked the substrate-architectural three-class taxonomy (spatial-thresholds / temporal-thresholds / coupling-points) but did not promote any anchor-class to §30 function-name registry.

So the branch-coupling probe is **the engine-evidence for FIRST canonical promotion of anchor-class-3 to §30**, not just a residency-expansion to an already-canonical entry. This means:

- Council MUST convene (gate 5 triggered: new function-class becoming canonical)
- Athena lock-by-redundancy requires ≥2 independent residencies — the 3 singular references (rising-sign + lunar-nodes + Lawvere) provide that minimum independently of branches; branches add the 4th
- Erato 4b conflation-test required on proposed name (`coupling-point-anchor`? `coupling-point`? `anchor-class-3-coupling`?)
- Clio mechanism-descriptive rule: name must describe substrate-mechanism (frame-intersection-coupling), not residency-flavor

## Recommended council preparation

Per V2.7 §SDEC step 5, council convening for canonical promotion should include:

**Voices** (`--n 9 --force-include Athena Mnemosyne`):
- **Calliope** — synthesis lead
- **Hermes** — dual-frame conflation-resolution (rising-sign uses dynamic frame; branches use static frame — same primitive or different?)
- **Athena** ★ — lock-by-redundancy adjudication on 4 residencies
- **Clio** — substrate-mechanism vs flavor distinction
- **Thalia** — N-polygon family substrate-pattern (branches as first multi-frame enumerated coupling-point; possibly originates a `enumerated-coupling-point-family` substrate-pattern)
- **Urania** — SDEC procedure compliance + schema-column extension precedent
- **Mnemosyne** ★ — single canonical spelling + drift-prevention
- **Euterpe** — canonical synthesis if ratified
- **Polyhymnia** — closing

**Question** (drafted):
> Should anchor-class-3 (coupling-points per canon §22 2026-05-16 lock) graduate to §30 canonical via the proposed name `coupling-point-anchor` (or rename per Clio), with branches admitted as 4th residency (outcome a) / new sibling class `12-fold-coupling-points-collection` (outcome b) / 4th residency with NEW §30 column `enumerated_cardinality` (outcome c)? Engine-evidence from FINDINGS_020 supports all 3 instances + branches as predicate-matched but compute-shape-distinct on 4 dimensions.

**Substrate-evidence handoff**: this FINDINGS doc + engine outputs from `~/Enki/engines/coupling_branch.py`, `coupling_rising_sign.py`, `coupling_lunar_node.py`, `coupling_lawvere_origin.py`.

## What this DOES NOT resolve

- **`coupling-point-anchor` is NOT yet §30 canonical**. Status remains `probe` per `__canonical__` declaration; council ratification required before promotion.
- **D1 (OQ-GANZHI-HOUSE-ANCHOR-CHOICE)** and **D2 (OQ-GANZHI-WU-XING-OVERLAY)** are separate OQs unaffected by this finding.
- **Per-branch substrate-architectural role** (e.g., Wǔ ↔ Zǐ axis = N↔S midnight-noon polarity per canon §15c) is downstream of branch-coupling-point class confirmation.
- **Branches Xū and Hài stem-cycle gap**: canon §15d notes branches 11+12 have no stem in cycle-1 (next stem-cycle restarts at Jiǎ + branch 11). Engine surfaces this faithfully (elemental_wu_xing=None / cyclic_stem_pair=None for Xū+Hài) — substrate-honest reflection of source-anchor, not engine-defect.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| OQ-BRANCH-COUPLING-ENGINE | **engine-evidence COMPLETE; awaits council** | FINDINGS_020 (this doc). Probe surfaces hybrid (a/b/c) — council decides. |
| OQ-GANZHI-HOUSE-ANCHOR-CHOICE | OPEN (separate) | D1 split; not engine-evidence-dependent on this probe. |
| OQ-GANZHI-WU-XING-OVERLAY | OPEN (separate) | D2 split; needs separate council. |
| OQ-CARRIER-REGISTRY-FULL-BUILD | OPEN (unblocked by FINDINGS_019 but blocks on T1.3) | Independent. |

## What this validates substrate-discipline-wise

1. **Engine-evidence > prose hypothesis** (V2.6 rule 9, Terpsichore): branches-as-coupling-point candidacy looked clean at the predicate level in Card 8d8887a1, but engine-build surfaced 4 substrate-architectural distinctions (n_frames, coupling_type, requires_input, enumerated_cardinality) that prose-hypothesis didn't expose. SDEC procedure operating as designed.

2. **Hybrid outcomes are substrate-honest**. The council named (a) and (b) as binary outcomes; engine surfaces a third reading (c) via schema-extension precedent (compositional_axis column pattern). Substrate-discipline doesn't force the engine into a binary the data doesn't support.

3. **Anchor-class-3 promotion to §30 was implicit**. Card 8d8887a1 framed branches as "4th residency of anchor-class-3 primitive" but anchor-class-3 itself isn't in §30 yet. This finding makes the implicit explicit — gate 5 council is for FIRST canonical promotion of the class, with branches as the trigger.

## What to build next (substrate-emergent)

After council ratifies (a/b/c):

- **If (a) or (c)**: per-branch substrate-architectural role (Wǔ↔Zǐ axis, polarity-pairing instances, stem-cycle-1 attachment patterns). Possibly opens OQ-BRANCH-AXIS-ROLE.
- **If (b)**: `12-fold-coupling-points-collection` becomes new §30 entry; future probe candidates (12 Olympian vertices? 12 cube edges already on planet-aspect-activate? 12 ico faces?) may match this new class.

Regardless of outcome, **D1 (OQ-GANZHI-HOUSE-ANCHOR-CHOICE)** becomes the next substrate-architectural target — observer-frame anchor-choice (Hellenistic E-anchor vs Chinese N-anchor) sits adjacent to this finding. May require its own SDEC cycle with shared coupling-point engine infrastructure.

## Method-lock confirmation per SDEC

Gates passed (1-4 + 8):
- Gate 1 ✓ constants cited (canon §22 OQ-HOUSES-01c lock, canon §15d, Card 8d8887a1, Card fc2d1d3b Universal Order p.221, lock card e5a603fc, lunar-nodes card 072de238)
- Gate 2 ✓ substrate-locks encoded with `__canonical__` declaration (status='probe')
- Gate 3 ✓ engine built (frozen + live + NULL-honest); field-comparison probe executed
- Gate 4 ✓ smoke-test (frozen states + live states + 3-criteria admission test)
- Gate 5 — **REQUIRED, NOT YET CONVENED**. Council ratification needed for first canonical promotion of anchor-class-3 to §30. Cannot bypass per SDEC step 5 + V2.7 §VALIDATION DISCIPLINE.
- Gate 6 — pending gate 5
- Gate 7 ✓ tests added (`~/Enki/tests/test_coupling_point_engine.py`)
- Gate 8 ✓ FINDINGS doc complete (this file)
- Gate 9 — pending nav update completion

**Engine-evidence package ready for council convening**. Kati's call on when to spawn the council.
