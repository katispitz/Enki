"""
Carrier antipodal-edge pairs registry — Enki.

6 antipodal cube-edge pairs enumerated from cube_edges.ANTIPODAL_PAIRS.

| Pair        | Axis | Planet pair A    | Planet pair B    |
|-------------|------|------------------|------------------|
| E01-E04     | z    | Pluto-Moon       | Sun-Neptune      |
| E09-E12     | z    | Mars-Jupiter     | Saturn-Mercury   |
| E02-E07     | y    | Pluto-Mercury    | Mars-Neptune     |
| E06-E11     | y    | Sun-Jupiter      | Saturn-Moon      |
| E03-E10     | x    | Pluto-Jupiter    | Saturn-Neptune   |
| E05-E08     | x    | Sun-Mercury      | Mars-Moon        |

Each pair is a SWAP-ANTIPODE: cube-edge antipodes have swapped U-L vertex
endpoints, capturing 4 planets in a polarity-inversion relationship.
"""
from __future__ import annotations
from typing import Optional

from cube_edges import (
    ANTIPODAL_PAIRS, EDGE_AXIS, edge_state
)
from _carrier_pair_engine import CarrierPairState, compute_carrier_pair_state


def pair_state(edge_a_id: str, edge_b_id: str,
               planet_a1_lon: Optional[float] = None,
               planet_a2_lon: Optional[float] = None,
               planet_b1_lon: Optional[float] = None,
               planet_b2_lon: Optional[float] = None) -> CarrierPairState:
    """Compute pair-state for a named antipodal cube-edge pair.

    planet_*_lon are passed positionally for the planet-pairs at edges A and B.
    """
    axis = EDGE_AXIS[edge_a_id]
    es_a = edge_state(edge_a_id, planet_a1_lon, planet_a2_lon)
    es_b = edge_state(edge_b_id, planet_b1_lon, planet_b2_lon)
    return compute_carrier_pair_state(edge_a_id, edge_b_id, axis, es_a, es_b)


def all_frozen() -> list:
    return [pair_state(a, b).to_dict() for a, b in ANTIPODAL_PAIRS]


if __name__ == '__main__':
    print("CARRIER ANTIPODAL-PAIRS REGISTRY (6 pairs)\n")
    for state in all_frozen():
        edges = state['edge_ids']
        pps   = state['planet_pairs']
        axis  = state['axis']
        print(f"  {edges[0]}↔{edges[1]}  axis={axis}  "
              f"({pps[0][0]}-{pps[0][1]}) ↔ ({pps[1][0]}-{pps[1][1]})")
