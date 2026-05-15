"""
Shared carrier direction-class engine — 3 axis-direction groups.

Each axis-direction (x/y/z) has 4 parallel cube edges = 2 antipodal pairs.
Substrate-emergent: each direction-class covers ALL 8 PE planets via 4 edges
(2 from each pair, each pair = 4 planets, full union = 8).

This is a NEW substrate-class cardinality at cube-edge cascade: direction-3
sits between pair-6 and system-1 in the cascade. Tests whether 1+3 partition
holds at cube-edge level (per OQ-1-PLUS-3-PARTITION-UNIVERSAL).
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class CarrierDirectionState:
    """Substrate-honest snapshot of an axis-direction class (4 cube edges)."""
    direction:        str               # 'x' / 'y' / 'z'
    pair_ids:         list              # ['E01-E04', 'E09-E12']
    edge_ids:         list              # 4 edges
    all_planets:      list              # all 8 PE planets (full set)

    pair_a_state:     Optional[dict]
    pair_b_state:     Optional[dict]

    both_pairs_active: Optional[bool]
    direction_sum:    Optional[float]   # sum across 4 edges
    direction_mean:   Optional[float]
    direction_max:    Optional[float]
    dominant_pair:    Optional[str]

    def to_dict(self) -> dict:
        return asdict(self)


def compute_carrier_direction_state(
    direction: str, pair_a_state: dict, pair_b_state: dict,
) -> CarrierDirectionState:
    """Build direction-state from 2 carrier-pair-state dicts.

    Both frozen or both live (cascade per-frozen-flag check propagates from
    edge-level via pair-level).
    """
    edge_ids = (
        pair_a_state['edge_ids'] + pair_b_state['edge_ids']
    )
    # Collect planets from edge states (avoid duplicates via set)
    pa_pls = pair_a_state['planet_pairs']
    pb_pls = pair_b_state['planet_pairs']
    all_planets = sorted({p for pair in pa_pls + pb_pls for p in pair})
    pair_ids = [pair_a_state['pair_id'], pair_b_state['pair_id']]

    # Frozen check: pair_a_state['sum_activation'] is None when frozen
    a_frozen = pair_a_state['sum_activation'] is None
    b_frozen = pair_b_state['sum_activation'] is None
    if a_frozen and b_frozen:
        return CarrierDirectionState(
            direction=direction, pair_ids=pair_ids, edge_ids=edge_ids,
            all_planets=all_planets,
            pair_a_state=pair_a_state, pair_b_state=pair_b_state,
            both_pairs_active=None, direction_sum=None,
            direction_mean=None, direction_max=None, dominant_pair=None,
        )

    aa = pair_a_state['sum_activation'] or 0.0
    bb = pair_b_state['sum_activation'] or 0.0
    both = bool(pair_a_state['both_active']) and bool(pair_b_state['both_active'])
    dsum = aa + bb
    dmean = dsum / 2.0  # mean of pair-sums
    dmax = max(aa, bb)
    if aa > bb:
        dom = pair_a_state['pair_id']
    elif bb > aa:
        dom = pair_b_state['pair_id']
    else:
        dom = None

    return CarrierDirectionState(
        direction=direction, pair_ids=pair_ids, edge_ids=edge_ids,
        all_planets=all_planets,
        pair_a_state=pair_a_state, pair_b_state=pair_b_state,
        both_pairs_active=both, direction_sum=dsum,
        direction_mean=dmean, direction_max=dmax, dominant_pair=dom,
    )
