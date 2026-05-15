"""
Shared carrier antipodal-edge-pair engine — R=1 cube-edge antipodes.

Each antipodal cube-edge pair has SWAP-ANTIPODE structure:
  Edge A: U_a × L_b
  Edge B: U_b × L_a  (vertex antipodes swapped)

Example: E01 U0×L1 (Pluto×Moon) ↔ E04 U1×L0 (Sun×Neptune).
  U0↔L0 are cube-vertex antipodes; U1↔L1 are cube-vertex antipodes.
  Edges connect U_a × NON-antipodal L. Antipodal edge has swapped vertices.

Composes 2 cube-edge AxisStates (canonical `planet-aspect-activate` per edge)
+ pair-level derived metrics.

Substrate-discipline: pair-state captures 4 planets across 2 swap-antipode
edges. Different substrate-semantics from Primordial cube-face pair (which
captured cosmogonic-axis polarity) — these capture cube-edge axis-direction
sharing.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional

from _axis_engine import AxisState


@dataclass
class CarrierPairState:
    """Substrate-honest snapshot of an antipodal cube-edge pair."""
    # Permanent definition
    pair_id:          str                # e.g. 'E01-E04'
    edge_ids:         tuple              # ('E01', 'E04')
    axis:             str                # 'x' / 'y' / 'z'
    planet_pairs:     tuple              # ((Pluto,Moon), (Sun,Neptune))
    all_planets:      list               # 4 planets across both edges

    # Live state
    edge_a_state:     Optional[dict]     # AxisState.to_dict() for edge A
    edge_b_state:     Optional[dict]
    both_active:      Optional[bool]
    co_activation:    Optional[float]    # min — both must fire
    sum_activation:   Optional[float]    # additive total
    polarity:         Optional[float]    # (a-b)/sum
    dominant_edge:    Optional[str]
    polarity_label:   Optional[str]

    def to_dict(self) -> dict:
        d = asdict(self)
        d['edge_ids']     = list(self.edge_ids)
        d['planet_pairs'] = [list(p) for p in self.planet_pairs]
        return d


def _polarity_label(a_act: float, b_act: float, edge_a: str, edge_b: str) -> str:
    if a_act == 0.0 and b_act == 0.0:
        return 'quiet'
    diff = a_act - b_act
    if abs(diff) < 0.1:
        return 'balanced'
    return f'{edge_a}-dominant' if diff > 0 else f'{edge_b}-dominant'


def compute_carrier_pair_state(
    edge_a_id: str,
    edge_b_id: str,
    axis: str,
    edge_a_state: AxisState,
    edge_b_state: AxisState,
) -> CarrierPairState:
    """Build a carrier-pair-state from two cube-edge AxisStates."""
    a_frozen = edge_a_state.pa_lon is None
    b_frozen = edge_b_state.pa_lon is None
    if a_frozen != b_frozen:
        raise ValueError(
            f"Carrier pair ({edge_a_id}, {edge_b_id}) requires both edges frozen "
            "OR both live — asymmetric input is substrate-incomplete"
        )

    pair_id = f'{edge_a_id}-{edge_b_id}'
    pp = (edge_a_state.planet_pair, edge_b_state.planet_pair)
    all_pl = list(edge_a_state.planet_pair) + list(edge_b_state.planet_pair)
    a_d = edge_a_state.to_dict()
    b_d = edge_b_state.to_dict()

    if a_frozen and b_frozen:
        return CarrierPairState(
            pair_id=pair_id, edge_ids=(edge_a_id, edge_b_id), axis=axis,
            planet_pairs=pp, all_planets=all_pl,
            edge_a_state=a_d, edge_b_state=b_d,
            both_active=None, co_activation=None, sum_activation=None,
            polarity=None, dominant_edge=None, polarity_label=None,
        )

    aa = edge_a_state.activation_strength
    bb = edge_b_state.activation_strength
    both = (aa > 0.0) and (bb > 0.0)
    co = min(aa, bb)
    summ = aa + bb
    pol = (aa - bb) / max(summ, 1e-9) if summ > 0 else 0.0
    label = _polarity_label(aa, bb, edge_a_id, edge_b_id)
    if aa > bb:
        dom = edge_a_id
    elif bb > aa:
        dom = edge_b_id
    else:
        dom = None

    return CarrierPairState(
        pair_id=pair_id, edge_ids=(edge_a_id, edge_b_id), axis=axis,
        planet_pairs=pp, all_planets=all_pl,
        edge_a_state=a_d, edge_b_state=b_d,
        both_active=both, co_activation=co, sum_activation=summ,
        polarity=pol, dominant_edge=dom, polarity_label=label,
    )
