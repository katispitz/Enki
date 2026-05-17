"""
Shared engine for anchor-class-3 substrate-coupling-points.

PROBE MANDATE per Card 8d8887a1 council 2026-05-17 (12 ABSTAIN deferral;
OQ-BRANCH-COUPLING-ENGINE opened per Urania SDEC):

Build cube-edge-carrier-pattern probe engine for branches-as-coupling-points
candidate. Field-compare to 3 existing anchor-class-3 instances:
  - rising-sign (ASC × zodiac-grid)
  - lunar nodes Rahu/Ketu (Moon-orbital-plane × ecliptic)
  - Lawvere-origin (observer × Merkaba-center, 50th-position fixed point)

Two council-named outcomes:
  (a) shape-match → branches ratify as 4th residency of anchor-class-3
      primitive (notable: first 12-fold enumeration among singular instances)
  (b) shape-mismatch on compute-shape (n_frames, coupling_type, input-
      requirement) → upgrade to NEW primitive class
      (`12-fold-coupling-points-collection`)

Substrate-architectural reference (canon §22 OQ-HOUSES-01c council 2026-05-16):
Anchor-class-3 coupling-points are substrate-derived intersections between
substrate-frames where frames COUPLE rather than CROSS. Stable while
constituents hold (distinct from class-1 spatial-threshold EVENTS and
class-2 temporal-threshold EVENTS).

This engine exposes EACH coupling-point as a CouplingPointState dataclass
populated with: coupled-frames identity (substrate-locked), canonical
position (frozen-derivable or live-computed per instance type), coupling
metadata (n_frames, coupling_type, requires_input). Field-comparison
across instances reveals predicate-match vs compute-shape distinctions
empirically.

Substrate-discipline:
  - No invented constants. All from canon §22 + §15d + Card 8d8887a1
    + Universal Order p.221 (Card fc2d1d3b).
  - Honest n_frames distinction (2 vs 4) exposed, not papered over.
  - Honest coupling_type distinction (singular / pair-180 / enumerated-N)
    exposed.
  - Honest requires_input distinction (dynamic-live vs substrate-frozen)
    exposed.
  - 3-criteria anchor-class-3 test enforced per instance per
    test_coupling_points_20260516.py:
      (a) substrate-derived intersection
      (b) independent canonical use
      (c) stable property (not event)
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


__canonical__ = {
    'function_class':       'coupling-point-anchor',  # CANDIDATE pending council
    'functional_tier':      'primitive',
    'compositional_axis':   'spatial',  # CANDIDATE; branches may force 'mixed'
    'residency_id':         'r3-anchor-class-3-coupling-point',
    'canon_citation':       'canon §22 OQ-HOUSES-01c council 2026-05-16 + §15d',
    'status':               'probe',  # engine-evidence stage; council ratification pending
}


@dataclass
class CouplingPointState:
    """Substrate-honest snapshot of an anchor-class-3 coupling-point.

    A coupling-point is a substrate-derived intersection of 2+ substrate-frames
    where the frames COUPLE rather than CROSS. Stable while constituents hold.

    Field categories (per SDEC step 3 + transmit-force council pattern):
      [SUBSTRATE-LOCKED METADATA] coupling_name, coupled_frames, n_frames,
          coupling_type, substrate_card.
      [ANCHOR-CLASS-3 CRITERIA EVIDENCE] is_substrate_derived_intersection,
          independent_canonical_uses, is_stable_while_constituents_hold.
      [POSITION OUTPUT] canonical_position (frozen-derivable per instance),
          live_position (input-dependent), requires_input.
      [CANDIDATE-DISTINCT PROBES vs branches] n_frames > 2 flag,
          enumerated_cardinality.
    """
    # [SUBSTRATE-LOCKED METADATA]
    coupling_name:     str
    coupled_frames:    tuple                  # tuple of frame-identifier strings
    n_frames:          int                    # cardinality of coupled-frames
    coupling_type:     str                    # 'singular' | 'pair-180' | 'enumerated-N'
    substrate_card:    str

    # [ANCHOR-CLASS-3 CRITERIA EVIDENCE]
    is_substrate_derived_intersection: bool
    independent_canonical_uses:        tuple  # evidence-pointer strings
    is_stable_while_constituents_hold: bool

    # [POSITION OUTPUT]
    canonical_position: Optional[dict]        # frozen-derivable (Lawvere, branch instance)
    live_position:      Optional[dict]        # input-dependent (rising-sign, lunar-nodes)
    requires_input:     bool

    # [CANDIDATE-DISTINCT PROBES vs branches per Card 8d8887a1]
    enumerated_cardinality: Optional[int]    # 12 for branches; None for singular

    def to_dict(self) -> dict:
        d = asdict(self)
        d['coupled_frames'] = list(self.coupled_frames)
        d['independent_canonical_uses'] = list(self.independent_canonical_uses)
        return d


def frozen_coupling_point(
    name: str,
    coupled_frames: tuple,
    coupling_type: str,
    substrate_card: str,
    canonical_position: Optional[dict],
    requires_input: bool,
    independent_canonical_uses: tuple,
    enumerated_cardinality: Optional[int] = None,
    is_substrate_derived: bool = True,
    is_stable: bool = True,
) -> CouplingPointState:
    """Construct a coupling-point in frozen (no-input) state.

    For instances with requires_input=False, canonical_position is fully
    determined by substrate-locks (Lawvere, branches).
    For instances with requires_input=True, canonical_position=None at
    frozen state; live_position computed via compute_coupling_point_live().
    """
    return CouplingPointState(
        coupling_name=name,
        coupled_frames=coupled_frames,
        n_frames=len(coupled_frames),
        coupling_type=coupling_type,
        substrate_card=substrate_card,
        is_substrate_derived_intersection=is_substrate_derived,
        independent_canonical_uses=independent_canonical_uses,
        is_stable_while_constituents_hold=is_stable,
        canonical_position=canonical_position,
        live_position=None,
        requires_input=requires_input,
        enumerated_cardinality=enumerated_cardinality,
    )


def compute_coupling_point_live(
    base: CouplingPointState,
    live_position: dict,
) -> CouplingPointState:
    """Populate live_position for an input-dependent coupling-point.

    For instances with requires_input=False, calling this is a substrate-
    error (live_position is undefined for substrate-frozen couplings).

    Substrate-honest behavior: ValueError if base.requires_input is False.
    """
    if not base.requires_input:
        raise ValueError(
            f"{base.coupling_name} is substrate-frozen (requires_input=False); "
            "live_position is undefined for this coupling-point class"
        )
    return CouplingPointState(
        coupling_name=base.coupling_name,
        coupled_frames=base.coupled_frames,
        n_frames=base.n_frames,
        coupling_type=base.coupling_type,
        substrate_card=base.substrate_card,
        is_substrate_derived_intersection=base.is_substrate_derived_intersection,
        independent_canonical_uses=base.independent_canonical_uses,
        is_stable_while_constituents_hold=base.is_stable_while_constituents_hold,
        canonical_position=base.canonical_position,
        live_position=live_position,
        requires_input=base.requires_input,
        enumerated_cardinality=base.enumerated_cardinality,
    )


def passes_anchor_class_3_criteria(state: CouplingPointState) -> dict:
    """Substrate-discipline check per test_coupling_points_20260516.py CP6.

    Anchor-class-3 admission criteria:
      (a) substrate-derived intersection — required
      (b) independent canonical use — at least one evidence-pointer
      (c) stable while constituents hold — required

    Returns dict with per-criterion pass/fail + overall verdict.
    """
    a = state.is_substrate_derived_intersection
    b = len(state.independent_canonical_uses) >= 1
    c = state.is_stable_while_constituents_hold
    return {
        'criterion_a_substrate_derived': a,
        'criterion_b_independent_canonical_use': b,
        'criterion_c_stable_while_constituents_hold': c,
        'overall_admits_to_anchor_class_3': a and b and c,
    }


def describe_coupling_point(state: CouplingPointState) -> str:
    pos_str = (
        f"canonical={state.canonical_position}"
        if state.canonical_position is not None
        else f"live={state.live_position} (requires_input={state.requires_input})"
    )
    return (
        f"Coupling-point: {state.coupling_name}\n"
        f"  Coupled frames ({state.n_frames}): {' × '.join(state.coupled_frames)}\n"
        f"  Type: {state.coupling_type}"
        f"{' (enumerated cardinality ' + str(state.enumerated_cardinality) + ')' if state.enumerated_cardinality else ''}\n"
        f"  Position: {pos_str}\n"
        f"  Substrate card: {state.substrate_card}\n"
        f"  Anchor-class-3 criteria: {passes_anchor_class_3_criteria(state)}\n"
    )
