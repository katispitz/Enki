"""
Shared inner-oct antipodal-pair engine — R=1/√3 archetype-mode pairs.

4 antipodal pairs per inner-oct vertex-complement:
  F1 SOURCE     ↔ F8 VOID       (apex pair)
  F2 FEEDBACK   ↔ F6 RESOURCE
  F3 DESIRE     ↔ F5 SYNTHESIS
  F4 PATTERN    ↔ F7 ANCHOR

Each pair's two faces have COMPLEMENTARY vertex sets (no shared vertex) and
TOGETHER cover ALL 6 sign-rulership vertices. So each antipodal pair captures
the FULL inner-oct vertex-planet set internally. Substrate-emergent finding
distinct from cube pair-class (where each pair only covers 4 of 8 planets).

Composes from inner-oct face engine (which composes from canonical
`planet-aspect-activate` × 3). No new physics; only composition.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional

from _inner_oct_face_engine import InnerOctFaceState


@dataclass
class InnerOctPairState:
    """Substrate-honest snapshot of an inner-oct antipodal face-pair."""
    # Permanent (always known)
    pair_name:           tuple              # (face_a_mode, face_b_mode)
    face_ids:            tuple              # (F_a, F_b)
    apex_or_lateral_set: tuple              # ('apex', 'apex') for F1-F8; ('lateral', 'lateral') for others
    element_pair:        tuple              # ('Fire', 'Water') etc
    tet_polarity_pair:   tuple              # ('Father', 'Mother') etc
    vertex_union:        list               # all 6 vertices (covered by the pair)
    planet_union:        list               # all 6 sign-rulership planets

    # Live state
    face_a_state:        Optional[dict]     # InnerOctFaceState.to_dict()
    face_b_state:        Optional[dict]

    # Pair-level derived (NULL when frozen)
    both_face_coherent:  Optional[bool]     # both faces have coherence=True
    either_face_active:  Optional[bool]     # at least one face presence=True
    pair_active_pair_count: Optional[int]   # sum of active pairs across both faces (0..6 edges)
    polarity:            Optional[float]    # face_a mean - face_b mean, signed
    polarity_label:      Optional[str]      # quiet/balanced/<mode_a>-dominant/<mode_b>-dominant
    dominant_face:       Optional[str]      # face_id with higher mean_activation

    def to_dict(self) -> dict:
        d = asdict(self)
        d['pair_name']           = list(self.pair_name)
        d['face_ids']            = list(self.face_ids)
        d['apex_or_lateral_set'] = list(self.apex_or_lateral_set)
        d['element_pair']        = list(self.element_pair)
        d['tet_polarity_pair']   = list(self.tet_polarity_pair)
        return d


def _polarity_label(face_a_mode: str, face_b_mode: str,
                    a_mean: float, b_mean: float) -> str:
    if a_mean == 0.0 and b_mean == 0.0:
        return 'quiet'
    diff = a_mean - b_mean
    if abs(diff) < 0.1:
        return 'balanced'
    return f"{face_a_mode}-dominant" if diff > 0 else f"{face_b_mode}-dominant"


def compute_inner_oct_pair_state(
    face_a: InnerOctFaceState,
    face_b: InnerOctFaceState,
) -> InnerOctPairState:
    """Build a pair-state from two inner-oct face states."""
    a_frozen = face_a.active_pair_count is None
    b_frozen = face_b.active_pair_count is None

    if a_frozen != b_frozen:
        raise ValueError(
            f"Inner-oct pair ({face_a.face_id}, {face_b.face_id}) requires both "
            "faces frozen OR both live — asymmetric input is substrate-incomplete"
        )

    pair_name = (face_a.mode, face_b.mode)
    face_ids  = (face_a.face_id, face_b.face_id)
    apex_lat  = (face_a.apex_or_lateral, face_b.apex_or_lateral)
    element_pair = (face_a.element, face_b.element)
    tet_pair  = (face_a.tet_polarity, face_b.tet_polarity)
    vertex_union = sorted(set(face_a.vertex_ids) | set(face_b.vertex_ids))
    planet_union = sorted(set(face_a.planets) | set(face_b.planets))

    a_d = face_a.to_dict()
    b_d = face_b.to_dict()

    if a_frozen and b_frozen:
        return InnerOctPairState(
            pair_name=pair_name, face_ids=face_ids,
            apex_or_lateral_set=apex_lat, element_pair=element_pair,
            tet_polarity_pair=tet_pair,
            vertex_union=vertex_union, planet_union=planet_union,
            face_a_state=a_d, face_b_state=b_d,
            both_face_coherent=None, either_face_active=None,
            pair_active_pair_count=None,
            polarity=None, polarity_label=None, dominant_face=None,
        )

    a_mean = face_a.mean_activation
    b_mean = face_b.mean_activation
    both_coh = bool(face_a.coherence and face_b.coherence)
    either_active = bool(face_a.presence or face_b.presence)
    total_active = (face_a.active_pair_count or 0) + (face_b.active_pair_count or 0)
    sum_means = a_mean + b_mean
    if sum_means > 0:
        polarity = (a_mean - b_mean) / max(sum_means, 1e-9)
    else:
        polarity = 0.0
    label = _polarity_label(face_a.mode, face_b.mode, a_mean, b_mean)
    if a_mean > b_mean:
        dom = face_a.face_id
    elif b_mean > a_mean:
        dom = face_b.face_id
    else:
        dom = None

    return InnerOctPairState(
        pair_name=pair_name, face_ids=face_ids,
        apex_or_lateral_set=apex_lat, element_pair=element_pair,
        tet_polarity_pair=tet_pair,
        vertex_union=vertex_union, planet_union=planet_union,
        face_a_state=a_d, face_b_state=b_d,
        both_face_coherent=both_coh, either_face_active=either_active,
        pair_active_pair_count=total_active,
        polarity=polarity, polarity_label=label, dominant_face=dom,
    )


def describe_inner_oct_pair(
    face_a_id: str, face_b_id: str, mode_a: str, mode_b: str,
    apex_or_lateral_set: tuple, element_pair: tuple, tet_pair: tuple,
) -> str:
    return (
        f"Inner-oct antipodal pair: {face_a_id} {mode_a} ↔ {face_b_id} {mode_b}\n"
        f"Apex/lateral: {apex_or_lateral_set[0]} ↔ {apex_or_lateral_set[1]}\n"
        f"Elements:     {element_pair[0]} ↔ {element_pair[1]}\n"
        f"Tet polarity: {tet_pair[0]} ↔ {tet_pair[1]}\n"
        f"Composes 2 × inner-oct-face engines (each composing 3 × planet-aspect-activate).\n"
        f"Function-class candidate: TBD (inner-oct pair-level; substrate-emergent).\n"
    )
