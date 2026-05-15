"""
Cube edges enumeration — Enki.

12 Merkaba cube edges at R=1 shell. Each cube edge connects ONE Father-tet
vertex (U0-U3) to ONE Mother-tet vertex (L0-L3) per cube's alternating-
vertex-coloring property.

Substrate-derivation (canon §1 + §3 + §7):
  Cube vertices at (±1/√3, ±1/√3, ±1/√3) when R=1.
  Father-tet: U0=(+,+,+), U1=(-,-,+), U2=(-,+,-), U3=(+,-,-)
  Mother-tet: L0=(-,-,-), L1=(+,+,-), L2=(+,-,+), L3=(-,+,+)
  Cube-adjacent vertices differ in EXACTLY 1 coordinate.
  Each vertex has 3 cube-edge neighbors (all in opposite tet).
  Total: 8 × 3 / 2 = 12 cube edges. ✓

Per canon §7 planet mapping:
  U0=Pluto, U1=Sun, U2=Mars, U3=Saturn (Father-tet)
  L0=Neptune, L1=Moon, L2=Mercury, L3=Jupiter (Mother-tet)

Each cube edge → planet-pair → function = `planet-aspect-activate` (canonical,
canon §30, graduated 2026-05-12).

SUBSTRATE-INCOMPLETE: per-Titan-to-cube-edge mapping is OPEN per Lillu BOARD
T1.3. The 12 edges are canon-locked by GEOMETRY (vertex-pair + planet-pair);
Titan figure-name assignment is substrate-pending. Cards/Titan names NOT
included in this enumeration.
"""
from __future__ import annotations
from typing import Optional

from _axis_engine import compute_axis_state, AxisState


# 12 cube edges enumerated by Merkaba vertex-coordinate analysis.
# Direction = which axis the edge is parallel to (x/y/z).
# Each entry: (edge_id, u_vertex, l_vertex, planet_pair, axis)
CUBE_EDGES = [
    # z-axis edges (parallel to z; vary in z, fixed x,y)
    ('E01', 'U0', 'L1', ('Pluto',   'Moon'),    'z'),   # (+,+,+)↔(+,+,-)
    ('E04', 'U1', 'L0', ('Sun',     'Neptune'), 'z'),   # (-,-,+)↔(-,-,-)
    ('E09', 'U2', 'L3', ('Mars',    'Jupiter'), 'z'),   # (-,+,-)↔(-,+,+)
    ('E12', 'U3', 'L2', ('Saturn',  'Mercury'), 'z'),   # (+,-,-)↔(+,-,+)
    # y-axis edges (parallel to y; vary in y, fixed x,z)
    ('E02', 'U0', 'L2', ('Pluto',   'Mercury'), 'y'),   # (+,+,+)↔(+,-,+)
    ('E07', 'U2', 'L0', ('Mars',    'Neptune'), 'y'),   # (-,+,-)↔(-,-,-)
    ('E06', 'U1', 'L3', ('Sun',     'Jupiter'), 'y'),   # (-,-,+)↔(-,+,+)
    ('E11', 'U3', 'L1', ('Saturn',  'Moon'),    'y'),   # (+,-,-)↔(+,+,-)
    # x-axis edges (parallel to x; vary in x, fixed y,z)
    ('E03', 'U0', 'L3', ('Pluto',   'Jupiter'), 'x'),   # (+,+,+)↔(-,+,+)
    ('E10', 'U3', 'L0', ('Saturn',  'Neptune'), 'x'),   # (+,-,-)↔(-,-,-)
    ('E05', 'U1', 'L2', ('Sun',     'Mercury'), 'x'),   # (-,-,+)↔(+,-,+)
    ('E08', 'U2', 'L1', ('Mars',    'Moon'),    'x'),   # (-,+,-)↔(+,+,-)
]


# Antipodal-pair lookup (each edge has 1 parallel edge across cube center)
# Derived from coordinate analysis: edge at (sign_a, sign_b) for fixed-coords
# is antipodal to edge at (-sign_a, -sign_b).
ANTIPODAL_PAIRS = [
    # z-axis pairs
    ('E01', 'E04'),  # (+,+,*) ↔ (-,-,*)
    ('E09', 'E12'),  # (-,+,*) ↔ (+,-,*)
    # y-axis pairs
    ('E02', 'E07'),  # (+,*,+) ↔ (-,*,-)
    ('E06', 'E11'),  # (-,*,+) ↔ (+,*,-)
    # x-axis pairs
    ('E03', 'E10'),  # (*,+,+) ↔ (*,-,-)
    ('E05', 'E08'),  # (*,-,+) ↔ (*,+,-)
]


# Direction-class groups (3 axes × 2 antipodal pairs each = 6 pairs)
DIRECTION_GROUPS = {
    'z': [('E01', 'E04'), ('E09', 'E12')],
    'y': [('E02', 'E07'), ('E06', 'E11')],
    'x': [('E03', 'E10'), ('E05', 'E08')],
}


# Edge ID → planet-pair lookup
EDGE_PLANET_PAIRS = {edge[0]: edge[3] for edge in CUBE_EDGES}
# Edge ID → axis lookup
EDGE_AXIS = {edge[0]: edge[4] for edge in CUBE_EDGES}
# Edge ID → vertex-pair lookup
EDGE_VERTICES = {edge[0]: (edge[1], edge[2]) for edge in CUBE_EDGES}


def edge_state(edge_id: str,
               planet_a_lon: Optional[float] = None,
               planet_b_lon: Optional[float] = None) -> AxisState:
    """Compute state for a cube edge given planet-pair longitudes.

    Reuses canonical `planet-aspect-activate` (compute_axis_state). Same function
    as Primordial face engines; substrate-position is cube-edge instead of cube-face.
    """
    u_v, l_v = EDGE_VERTICES[edge_id]
    pair     = EDGE_PLANET_PAIRS[edge_id]
    axis     = EDGE_AXIS[edge_id]
    return compute_axis_state(
        f'cube-edge-{edge_id}',           # engine name
        f'{edge_id}({u_v}-{l_v}, {axis}-axis)',  # position anchor
        pair, f'{axis}-axis carrier', 'TBD',     # planet_pair, context, card
        planet_a_lon, planet_b_lon,
    )


def all_frozen_edges() -> list:
    """Return frozen AxisStates for all 12 cube edges."""
    return [edge_state(e[0]).to_dict() for e in CUBE_EDGES]


if __name__ == '__main__':
    print("CUBE EDGE ENUMERATION (12 Merkaba cube edges, R=1)")
    print(f"\nTotal edges: {len(CUBE_EDGES)}")
    print(f"Total antipodal pairs: {len(ANTIPODAL_PAIRS)}")
    print(f"Total direction groups: {len(DIRECTION_GROUPS)}")
    print()
    print("By edge:")
    for edge_id, u, l, pair, axis in CUBE_EDGES:
        print(f"  {edge_id}  {u}↔{l}  {pair[0]:8s} × {pair[1]:8s}  {axis}-axis")
    print()
    print("Antipodal pairs:")
    for a, b in ANTIPODAL_PAIRS:
        pa = EDGE_PLANET_PAIRS[a]
        pb = EDGE_PLANET_PAIRS[b]
        ax = EDGE_AXIS[a]
        print(f"  {a}↔{b}  ({pa[0]}-{pa[1]}) ↔ ({pb[0]}-{pb[1]})  {ax}-axis")
    print()
    print("Direction groups (axis-class):")
    for axis, pairs in DIRECTION_GROUPS.items():
        edges = [e for pair in pairs for e in pair]
        print(f"  {axis}-axis ({len(pairs)} pairs, {len(edges)} edges): {edges}")
