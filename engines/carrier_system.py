"""
Carrier system composition — Enki.

Full substrate-cascade composition of the carrier primitive-class at R=1
cube-edges. Combines 3 primitive-class levels:

  edge-class      (cardinality 12) — individual cube edges
  pair-class      (cardinality 6)  — antipodal cube-edge pairs (swap-antipode)
  direction-class (cardinality 3)  — axis-direction groups (x/y/z)
  system          (cardinality 1)  — full Merkaba cube

Cascade: 12 → 6 → 3 → 1 (different from cube-face 6→3→2→1 and inner-oct 8→4→2→1).

Tests OQ-1-PLUS-3-PARTITION-UNIVERSAL: at cube-edge cascade, direction-class
is 3-way (x/y/z), NOT 1+3. Substrate finding: 1+3 partition is NOT universal
across primitive-types within the same shell.

System-level metrics derived from cascade composition.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional

from carrier_directions import direction_state


@dataclass
class CarrierSystemState:
    """Full carrier-cascade snapshot."""
    edge_count:       int = 12
    pair_count:       int = 6
    direction_count:  int = 3

    direction_x:      Optional[dict] = None
    direction_y:      Optional[dict] = None
    direction_z:      Optional[dict] = None

    whole_cube_activation: Optional[float] = None
    active_pair_count:     Optional[int] = None      # how many of 6 pairs have both_active
    dominant_direction:    Optional[str] = None
    direction_sums:        Optional[dict] = None     # {x: sum, y: sum, z: sum}
    all_quiet:             Optional[bool] = None

    def to_dict(self) -> dict:
        return asdict(self)


def system_state(planet_lons: Optional[dict] = None) -> CarrierSystemState:
    """Compute full carrier-cascade state.

    planet_lons (optional): {planet_name: lon_deg} for all 8 PE planets. None
    yields frozen substrate-locks. Live state computes all 12 edges + 6 pairs
    + 3 directions and emits system-level metrics.
    """
    dx = direction_state('x', planet_lons)
    dy = direction_state('y', planet_lons)
    dz = direction_state('z', planet_lons)
    dx_d = dx.to_dict()
    dy_d = dy.to_dict()
    dz_d = dz.to_dict()

    frozen = dx_d['direction_sum'] is None
    if frozen:
        return CarrierSystemState(
            direction_x=dx_d, direction_y=dy_d, direction_z=dz_d,
        )

    sums = {
        'x': dx_d['direction_sum'] or 0.0,
        'y': dy_d['direction_sum'] or 0.0,
        'z': dz_d['direction_sum'] or 0.0,
    }
    whole = sum(sums.values())
    # Active-pair count: count pairs across 3 directions where both_active=True
    active_pairs = 0
    for d in (dx_d, dy_d, dz_d):
        if d['pair_a_state']['both_active']: active_pairs += 1
        if d['pair_b_state']['both_active']: active_pairs += 1
    if whole > 0:
        dom = max(sums, key=sums.get)
    else:
        dom = None

    return CarrierSystemState(
        direction_x=dx_d, direction_y=dy_d, direction_z=dz_d,
        whole_cube_activation=whole,
        active_pair_count=active_pairs,
        dominant_direction=dom,
        direction_sums=sums,
        all_quiet=(whole == 0.0),
    )


def describe() -> str:
    return (
        "CARRIER SYSTEM (R=1 cube-edge residency class)\n"
        "  Three primitive-class levels composed:\n"
        "    edge-class       cardinality 12 — individual cube edges\n"
        "    pair-class       cardinality 6  — antipodal swap-pairs\n"
        "    direction-class  cardinality 3  — axis-direction groups (x/y/z)\n"
        "\n"
        "  Cascade: 12 → 6 → 3 → 1.\n"
        "  Substrate-emergent: each direction-class covers ALL 8 PE planets via 4 edges.\n"
        "\n"
        "  Per-class function:\n"
        "    edge:      planet-aspect-activate (CANONICAL §30)\n"
        "    pair:      swap-antipode-coactivation (candidate, conflation-test pending)\n"
        "    direction: axis-direction-aggregation (candidate)\n"
        "    system:    cube-edge-saturate (candidate)\n"
        "\n"
        "  SUBSTRATE-INCOMPLETE: per-Titan figure-name assignment for 12 edges OPEN\n"
        "  per Nammu BOARD T1.3. This module enumerates geometry-locked positions.\n"
    )


if __name__ == '__main__':
    print(describe())
    # Sample live: all 8 PE planets at conjunction-spread (no aspect)
    print('SAMPLE LIVE STATE (all 8 planets in single zodiac quadrant):')
    state = system_state(planet_lons={
        'Pluto':   270.0,  # Capricorn 0°
        'Sun':     280.0,
        'Mars':    290.0,
        'Saturn':  300.0,
        'Neptune': 330.0,
        'Moon':    340.0,
        'Mercury': 350.0,
        'Jupiter': 0.0,
    })
    d = state.to_dict()
    print(f"  whole_cube_activation: {d['whole_cube_activation']:.3f}")
    print(f"  active_pair_count:     {d['active_pair_count']}/6")
    print(f"  dominant_direction:    {d['dominant_direction']}")
    print(f"  direction_sums:        {d['direction_sums']}")
    print(f"  all_quiet:             {d['all_quiet']}")
    print()
    print('Direction breakdown:')
    for axis_key, d_key in [('x', 'direction_x'), ('y', 'direction_y'), ('z', 'direction_z')]:
        ds = d[d_key]
        print(f"  {axis_key}-axis: sum={ds['direction_sum']:.3f}, "
              f"pairs both_active=({ds['pair_a_state']['both_active']}, {ds['pair_b_state']['both_active']})")
