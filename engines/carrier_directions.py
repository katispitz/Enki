"""
Carrier axis-direction-class registry — Enki.

3 direction-classes per cube geometry. Each class = 2 antipodal-pairs sharing
an axis-direction = 4 parallel cube edges. Each class covers ALL 8 PE planets.

| Direction | Antipodal pairs        | 4 edges                    |
|-----------|------------------------|----------------------------|
| z-axis    | E01-E04, E09-E12       | E01, E04, E09, E12         |
| y-axis    | E02-E07, E06-E11       | E02, E07, E06, E11         |
| x-axis    | E03-E10, E05-E08       | E03, E10, E05, E08         |
"""
from __future__ import annotations
from typing import Optional

from cube_edges import DIRECTION_GROUPS, EDGE_AXIS, edge_state
from carrier_pairs import pair_state
from _carrier_direction_engine import (
    CarrierDirectionState, compute_carrier_direction_state
)


def direction_state(direction: str,
                    planet_lons: Optional[dict] = None) -> CarrierDirectionState:
    """Compute direction-class state.

    planet_lons (optional): {planet_name: lon_deg}. When supplied, retrieves
    longitudes for each edge's planet-pair and computes live state. When None,
    all edges/pairs frozen.
    """
    pairs = DIRECTION_GROUPS[direction]
    states = []
    for pair_a, pair_b in [pairs]:
        # Each `pair` in DIRECTION_GROUPS is a tuple (edge_a, edge_b) — but loop
        # structure here is iterating over the 2 antipodal pairs in this direction.
        pass

    # Iterate 2 antipodal pairs in this direction
    pair_states_dicts = []
    for edge_a, edge_b in pairs:
        if planet_lons is None:
            ps = pair_state(edge_a, edge_b)
        else:
            from cube_edges import EDGE_PLANET_PAIRS
            pa = EDGE_PLANET_PAIRS[edge_a]
            pb = EDGE_PLANET_PAIRS[edge_b]
            ps = pair_state(
                edge_a, edge_b,
                planet_lons.get(pa[0]), planet_lons.get(pa[1]),
                planet_lons.get(pb[0]), planet_lons.get(pb[1]),
            )
        pair_states_dicts.append(ps.to_dict())

    return compute_carrier_direction_state(
        direction, pair_states_dicts[0], pair_states_dicts[1],
    )


def all_frozen() -> list:
    return [direction_state(d).to_dict() for d in ['x', 'y', 'z']]


if __name__ == '__main__':
    print("CARRIER DIRECTION-CLASS REGISTRY (3 axis-direction groups)\n")
    for state in all_frozen():
        print(f"  {state['direction']}-axis:")
        print(f"    pairs: {state['pair_ids']}")
        print(f"    edges: {state['edge_ids']}")
        print(f"    planets ({len(state['all_planets'])}): {state['all_planets']}")
        print()
