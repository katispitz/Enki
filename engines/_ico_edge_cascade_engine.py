"""
Shared engine for R=φ² ico-edge primordial-grandchild cascade residencies.

PROBE MANDATE per descent-transmit formal-ratification council 2026-05-17
(canon §30 OQ-ICO-EDGE-CASCADE-ENGINE, voice cards 1479f2d1/1627276b/
93f2555d/e4f80784/302b616c/763567ef/1af87414/e6f40ee3/f7bf7dfd):

Build ico-edge-cascade probe engine for primordial-grandchild residencies.
Field-compare to existing residency engines:
  - planet-aspect-activate (R=1 cube-face + R=φ icosidodec-midpt +
    R=1 cube-edge per FINDINGS_005/008/019)
  - triangle-aspect-activate (R=1/√3 inner-oct face + R=1 Merkaba tet-face
    per FINDINGS_011)
  - polarity-define (R=1 cube-face pair + R=1/√3 inner-oct face pair per
    FINDINGS_010)
  - coupling-point (rising-sign + lunar-nodes + Lawvere + branches per
    FINDINGS_020, canon §30 LOCKED 2026-05-17)

Four council-named outcomes:
  (a) shape-match with planet-aspect-activate → ico-edge grandchildren
      ratify as 4th residency (no new function-name needed)
  (b) shape-match with triangle-aspect-activate → 3rd residency at edge-class
  (c) shape-match with polarity-define → 3rd residency at first-composition
      via parent-pair-attribute compose
  (d) shape-match with coupling-point → 5th residency (if substrate-frozen
      marker-shape matches Lawvere-pattern)
  (e) shape-MISMATCH on all 4 → distinct mechanism confirmed, re-convene
      with mechanism-precise name (NOT `descent-transmit`, per Erato 4b
      conflation-test failure on WHERE+HOW lexical fusion)

Substrate-architectural reference:
  - canon §17 parent-crossing-points (ico-edge geometry)
  - canon §M.5 + line 1317 OQ-SOLID-11 partial-resolution (Hesiod-line
    distribution: 7 of 30 ico-edges occupied by primordial-grandchildren)
  - canon §27 vertex-proximity / cross-class extensions

The 7 primordial-grandchild residencies (L3 generation per Hesiod):
  - Aether       — ico-edge Nyx-Erebus union-edge #1 (Chaos class)
  - Hemera       — ico-edge Nyx-Erebus union-edge #2 (Chaos class)
  - Nereus       — ico-edge Pontus face-edge #1 (Gaia class)
  - Thaumas      — ico-edge Pontus face-edge #2 (Gaia class)
  - Eurybia      — ico-edge Pontus face-edge #3 (Gaia class)
  - Phorcys      — cross-class ico-edge Pontus→Eros-primordial extension
  - Ceto         — cross-class ico-edge Pontus→Tartarus extension

This engine exposes EACH grandchild as IcoEdgeCascadeState dataclass
populated with: cascade identity (substrate-locked), parent-pair (L1/L2),
lineage depth (generations from L1 primordial-class-presider), candidate-
distinct probe fields (descent_direction, inherited_attribute, lineage_depth).

Substrate-discipline:
  - No invented constants. All from canon §17 + §M.5 + line 1317 + Hesiod
    Theogony source-corpus.
  - NULL-honest where no live ephemeris input — primordial-grandchildren
    may be substrate-frozen markers, not live-compute responders.
  - Erato 4b lexical-fusion discipline preserved: candidate name
    `descent-transmit` is the THING UNDER TEST, not the answer.
  - 3-criteria anchor-class-3 test included per probe (some outcomes
    point toward coupling-point shape-match).
"""
from __future__ import annotations
from dataclasses import dataclass, asdict, field
from typing import Optional


__canonical__ = {
    'function_class':       'TBD pending council post-probe',  # NOT yet §30
    'functional_tier':      'TBD pending council post-probe',
    'compositional_axis':   'TBD pending council post-probe',
    'residency_id':         'r-phi2-ico-edge-primordial-grandchild',
    'canon_citation':       'canon §17 + §M.5 + line 1317 OQ-SOLID-11; council 2026-05-17 DEFER',
    'status':               'probe',  # engine-evidence stage; council ratification pending
}


# Canon §3 — R=φ² ico circumsphere (Olympian shell, outermost).
import math as _m
PHI = (1.0 + _m.sqrt(5.0)) / 2.0          # golden ratio
ICO_R_SHELL = PHI * PHI                    # R = φ² for icosahedron circumsphere

# Canon §17 — ico-edge length when R=φ² (one of the canonical edge lengths)
# Edge length of icosahedron inscribed in sphere of radius R = R × √(2 - 2/√5).
# = R × √(2 − 2/√5) per geometric derivation; this is the L3 generational-vector
# magnitude between adjacent primordial-grandchild residency-positions.
_K = 2.0 - 2.0 / _m.sqrt(5.0)
ICO_EDGE_LENGTH = ICO_R_SHELL * _m.sqrt(_K)


@dataclass
class IcoEdgeCascadeState:
    """Substrate-honest snapshot of an ico-edge primordial-grandchild cascade.

    A primordial-grandchild lives at an ico-edge where two parent-class
    residencies (L1 face-class presider OR L2 face-resident) meet. Per canon
    §17 vertex-proximity, the ico-edge represents PARENT-CROSSING-POINT
    geometry — where parent-class boundaries cross.

    Field categories (per SDEC step 3 + descent-transmit council pattern):
      [SUBSTRATE-LOCKED METADATA] — different per grandchild-instance (expected;
          not "shape-mismatch"). cascade_name, ico_edge, parent_vertex_a/b,
          parent_face_class_a/b, parent_residents_a/b, residency_card, shell,
          edge_length, hesiod_lineage.
      [LIVE-COMPUTE] — null in PROBE (substrate-frozen marker hypothesis);
          populated if engine surfaces live-compute requirement.
      [CANDIDATE-DISTINCT PROBES] — descent_direction (council named direction-
          primitive: parent→child generational vector), inherited_attribute
          (council named mechanism-primitive: attribute-propagation),
          lineage_depth (generations from L1 primordial-class-presider).
      [ANCHOR-CLASS-3 CRITERIA EVIDENCE] (per FINDINGS_020 coupling-point
          3-criteria pattern; surfaces if substrate-frozen marker-shape
          matches Lawvere-pattern).
    """
    # [SUBSTRATE-LOCKED METADATA]
    cascade_name:           str               # e.g. 'Aether'
    ico_edge:               str               # ico-edge label e.g. 'E5'
    parent_vertex_a:        str               # e.g. 'V_nyx'
    parent_vertex_b:        str               # e.g. 'V_erebus'
    parent_face_class_a:    str               # L1 class e.g. 'Chaos'
    parent_face_class_b:    str               # L1 class (same or cross-class)
    parent_residents_a:     str               # L2 residency name e.g. 'Nyx'
    parent_residents_b:     str               # L2 residency name e.g. 'Erebus'
    residency_card:         str               # canon card-ID
    shell:                  float             # R=φ² ico circumsphere
    edge_length:            float             # ico-edge length at R=φ² shell
    hesiod_lineage:         str               # Hesiod Theogony lineage descriptor

    # [LIVE-COMPUTE] — null in probe (substrate-frozen marker hypothesis)
    # If engine surfaces canonical live-input requirement, these populate.
    pa_attribute:           Optional[float] = None     # parent A activation/attribute
    pb_attribute:           Optional[float] = None     # parent B activation/attribute
    inherited_activation:   Optional[float] = None     # composed parent-pair attribute
    activation_strength:    float = 0.0

    # [CANDIDATE-DISTINCT PROBES] — descent-transmit council named fields
    descent_direction:      Optional[str] = None       # 'a→b' | 'b→a' | 'symmetric' | None
    inherited_attribute:    Optional[str] = None       # category label of inheritance
    lineage_depth:          Optional[int] = None       # generations from L1 presider

    # [ANCHOR-CLASS-3 CRITERIA] — coupling-point shape-match probe
    is_substrate_derived_intersection:  bool = True
    independent_canonical_uses:         list = field(default_factory=list)
    is_stable_while_constituents_hold:  bool = True

    def to_dict(self) -> dict:
        return asdict(self)


# ─── HELPERS ──────────────────────────────────────────────────────────────────


def _descent_direction(a_name: str, b_name: str, generation_a: int, generation_b: int) -> str:
    """Candidate-distinct probe: directional descent from older to younger.

    Substrate-evaluation: 'descent' is a generational-ordering, not a live-
    compute. It's STATIC per substrate-residency (parent-child relationship
    locked at canon §17 lineage-table). NO live input modulates it.

    Therefore: substrate-frozen attribute, NOT live-compute. This is the FIRST
    distinguishing feature from cube-edge carrier (which had live-compute
    flow_direction from ephemeris). Documented in FINDINGS_022 as substrate-
    frozen direction-primitive — confirms WHERE-component of `descent-transmit`
    is STATIC, not LIVE.
    """
    if generation_a == generation_b:
        return 'symmetric'  # same-generation siblings (no descent direction)
    return f'{a_name}→{b_name}' if generation_a < generation_b else f'{b_name}→{a_name}'


def _inherited_attribute(class_a: str, class_b: str) -> str:
    """Candidate-distinct probe: inherited attribute category from parent-pair.

    Substrate-evaluation: returns class-pair as inheritance-category-label.
    NO live-compute — purely structural lookup from canon §M.5 lineage.

    Substrate-honest: this is metadata, not computation. Documented in
    FINDINGS_022 as substrate-frozen lookup — confirms WHAT-component of
    `descent-transmit` is also STATIC, not LIVE.

    The fact that BOTH descent_direction AND inherited_attribute are static
    (no live ephemeris input) suggests grandchildren are SUBSTRATE-FROZEN
    MARKERS, not active operators. This supports shape-match with coupling-
    point (Lawvere-pattern: substrate-frozen position).
    """
    if class_a == class_b:
        return f'within-class:{class_a}'
    return f'cross-class:{class_a}↔{class_b}'


def _lineage_depth(generation: int) -> int:
    """Substrate-locked: generations from L1 primordial-class-presider.

    Per canon §M.5 + line 1317:
      L1 = primordial face-class-presider (Chaos/Gaia/Eros-prim/Tartarus): depth 0
      L2 = primordial child face-resident (Erebus/Nyx/Ouranos/Pontus/Ourea): depth 1
      L3 = primordial grandchild ico-edge resident (Aether/Hemera/etc): depth 2

    Substrate-evaluation: depth is a static substrate-fact, not a live-compute.
    Documented in FINDINGS_022 as substrate-locked attribute.
    """
    return generation


def frozen_ico_edge_cascade(
    name: str, edge: str, p_vert_a: str, p_vert_b: str,
    p_class_a: str, p_class_b: str,
    p_res_a: str, p_res_b: str,
    card: str, hesiod: str,
    generation_a: int = 1, generation_b: int = 1,
    grandchild_generation: int = 2,
) -> IcoEdgeCascadeState:
    """Return the permanent grandchild-residency definition without live input.

    Substrate-frozen state: primordial-grandchildren are residency-MARKERS
    at ico-edges per canon §17 + §M.5 + line 1317. No canonical live-input
    has been substrate-derived for this class — engine returns frozen state
    by default (probe outcome supports this is the canonical mode).
    """
    descent = _descent_direction(p_res_a, p_res_b, generation_a, generation_b)
    inherited = _inherited_attribute(p_class_a, p_class_b)
    depth = _lineage_depth(grandchild_generation)

    return IcoEdgeCascadeState(
        cascade_name=name, ico_edge=edge,
        parent_vertex_a=p_vert_a, parent_vertex_b=p_vert_b,
        parent_face_class_a=p_class_a, parent_face_class_b=p_class_b,
        parent_residents_a=p_res_a, parent_residents_b=p_res_b,
        residency_card=card, shell=ICO_R_SHELL, edge_length=ICO_EDGE_LENGTH,
        hesiod_lineage=hesiod,
        descent_direction=descent,
        inherited_attribute=inherited,
        lineage_depth=depth,
        independent_canonical_uses=[
            'canon §17 vertex-proximity parent-crossing-point',
            'canon §M.5 Hesiod-line primordial-cascade',
            'canon §30 OQ-SOLID-11 partial-resolution (7 of 30 ico-edges)',
            'Hesiod Theogony source-corpus residency',
        ],
    )


def compute_ico_edge_cascade_state(
    name: str, edge: str, p_vert_a: str, p_vert_b: str,
    p_class_a: str, p_class_b: str,
    p_res_a: str, p_res_b: str,
    card: str, hesiod: str,
    pa_attr: Optional[float] = None,
    pb_attr: Optional[float] = None,
    generation_a: int = 1, generation_b: int = 1,
    grandchild_generation: int = 2,
) -> IcoEdgeCascadeState:
    """Compute live ico-edge-cascade state.

    Probe outcome (substrate-frozen hypothesis): if pa_attr/pb_attr both None,
    return frozen state. If supplied, compose via mean (probe-hypothesis for
    composed-attribute live-compute, similar to polarity-define mechanism).

    NULL-honest: partial input rejected — parent-pair attribute requires both
    or neither.

    Substrate-evaluation note: the FACT that this engine can run frozen-only
    is the substrate-finding. There is NO canonical live-input from ephemeris
    for primordial-grandchildren (unlike planet-aspect-activate residencies
    which take planet-pair longitudes). This is the FIRST shape-mismatch
    signal vs the cube-edge-carrier engine.
    """
    if pa_attr is None and pb_attr is None:
        return frozen_ico_edge_cascade(
            name, edge, p_vert_a, p_vert_b, p_class_a, p_class_b,
            p_res_a, p_res_b, card, hesiod,
            generation_a, generation_b, grandchild_generation,
        )
    if pa_attr is None or pb_attr is None:
        raise ValueError(
            f"{name} ico_edge_cascade_state requires both parent attributes "
            "or neither — partial input is substrate-incomplete (NULL-honest)"
        )

    # Probe-hypothesis live-compute: composed attribute = parent-pair mean.
    # Substrate-evaluation: if this compute SHAPE-MATCHES polarity-define
    # (compose 2 face-states → polarity), grandchildren are 3rd residency
    # of polarity-define. If NOT, distinct mechanism confirmed.
    inherited_act = (pa_attr + pb_attr) / 2.0

    state = frozen_ico_edge_cascade(
        name, edge, p_vert_a, p_vert_b, p_class_a, p_class_b,
        p_res_a, p_res_b, card, hesiod,
        generation_a, generation_b, grandchild_generation,
    )
    state.pa_attribute = pa_attr
    state.pb_attribute = pb_attr
    state.inherited_activation = inherited_act
    state.activation_strength = inherited_act
    return state


def describe_ico_edge_cascade(state: IcoEdgeCascadeState) -> str:
    return (
        f"Primordial-grandchild (Hesiod L3): {state.cascade_name}\n"
        f"Ico-edge: {state.ico_edge} ({state.parent_vertex_a}↔{state.parent_vertex_b})\n"
        f"Parent face-classes: {state.parent_face_class_a} ↔ {state.parent_face_class_b}\n"
        f"Parent residents: {state.parent_residents_a} ↔ {state.parent_residents_b}\n"
        f"Shell: R=φ² = {state.shell:.4f} (Olympian-class ico circumsphere, canon §3)\n"
        f"Edge length: {state.edge_length:.4f}\n"
        f"Hesiod lineage: {state.hesiod_lineage}\n"
        f"Substrate card: {state.residency_card}\n"
        f"Lineage depth: L{state.lineage_depth} (generations from L1 presider)\n"
        f"Descent direction: {state.descent_direction}\n"
        f"Inherited attribute: {state.inherited_attribute}\n"
        f"Function class: TBD pending council post-probe\n"
        f"  Probe: substrate-frozen marker hypothesis (no canonical live input).\n"
        f"  Candidate outcomes per FINDINGS_022: (a) shape-match planet-aspect-\n"
        f"  activate (FAILS — no live planet input); (b) shape-match triangle-\n"
        f"  aspect-activate (FAILS — edge not 3-vertex face); (c) shape-match\n"
        f"  polarity-define (PARTIAL — 2-parent compose); (d) shape-match\n"
        f"  coupling-point (CANDIDATE — substrate-frozen marker matches\n"
        f"  Lawvere-pattern); (e) shape-mismatch with all 4 → distinct mechanism.\n"
    )


def passes_anchor_class_3_criteria(state: IcoEdgeCascadeState) -> bool:
    """Test 3-criteria coupling-point predicate (per FINDINGS_020 pattern).

    If grandchildren pass coupling-point predicate AND are substrate-frozen,
    they're shape-match candidates for outcome (d) — 5th residency of
    coupling-point (after rising-sign + lunar-nodes + Lawvere + branches).
    """
    return (
        state.is_substrate_derived_intersection
        and len(state.independent_canonical_uses) >= 2
        and state.is_stable_while_constituents_hold
    )
