"""
Tests for carrier (Titan) cube-edge engine + 6 antipodal pairs + 3 direction
groups + system.

Per FINDINGS_008 (carrier example) + FINDINGS_009 (cube-edge cascade):
  12 cube edges → 6 antipodal swap-pairs → 3 axis-direction groups → 1 system.
  Each cube edge connects 1 Father-tet vertex (U0-U3) to 1 Mother-tet vertex
  (L0-L3). Per FINDINGS_009: each direction-class covers ALL 8 PE planets.
"""
import pytest
from cube_edges import (
    CUBE_EDGES, ANTIPODAL_PAIRS, DIRECTION_GROUPS,
    EDGE_PLANET_PAIRS, EDGE_AXIS, EDGE_VERTICES, edge_state,
)
import carrier_pairs
import carrier_directions
import carrier_system


def test_12_cube_edges():
    assert len(CUBE_EDGES) == 12


def test_6_antipodal_pairs():
    assert len(ANTIPODAL_PAIRS) == 6


def test_3_direction_groups():
    assert len(DIRECTION_GROUPS) == 3
    assert set(DIRECTION_GROUPS.keys()) == {'x', 'y', 'z'}


def test_cube_edges_alternating_coloring():
    """Each cube edge connects 1 U-vertex (Father) to 1 L-vertex (Mother)."""
    for edge_id, u, l, _pair, _axis in CUBE_EDGES:
        assert u.startswith('U'), f"{edge_id} first vertex {u} not in U-tet"
        assert l.startswith('L'), f"{edge_id} second vertex {l} not in L-tet"


def test_each_vertex_in_3_edges():
    """Cube property: each vertex has 3 edge-neighbors."""
    vertex_edge_count = {}
    for edge_id, u, l, _pair, _axis in CUBE_EDGES:
        vertex_edge_count[u] = vertex_edge_count.get(u, 0) + 1
        vertex_edge_count[l] = vertex_edge_count.get(l, 0) + 1
    for v in ['U0', 'U1', 'U2', 'U3', 'L0', 'L1', 'L2', 'L3']:
        assert vertex_edge_count[v] == 3, f"{v} has {vertex_edge_count[v]} edges, expected 3"


def test_edges_per_direction_is_4():
    """4 parallel cube edges per axis direction."""
    edges_per_axis = {}
    for edge_id, _u, _l, _pair, axis in CUBE_EDGES:
        edges_per_axis[axis] = edges_per_axis.get(axis, 0) + 1
    assert edges_per_axis == {'x': 4, 'y': 4, 'z': 4}


def test_direction_group_covers_all_8_pe_planets():
    """
    FINDINGS_009 finding: each direction-class covers ALL 8 PE planets via 4 edges.
    """
    all_8 = {'Pluto', 'Sun', 'Mars', 'Saturn', 'Neptune', 'Moon', 'Mercury', 'Jupiter'}
    for axis, pairs in DIRECTION_GROUPS.items():
        planets_in_axis = set()
        for edge_a, edge_b in pairs:
            planets_in_axis.update(EDGE_PLANET_PAIRS[edge_a])
            planets_in_axis.update(EDGE_PLANET_PAIRS[edge_b])
        assert planets_in_axis == all_8, \
            f"Direction {axis} doesn't cover all 8 PE planets: got {planets_in_axis}"


def test_antipodal_pair_swap_structure():
    """
    FINDINGS_009 SWAP-ANTIPODE finding: each antipodal pair = (U_a × L_b) ↔ (U_b × L_a).
    Antipodal cube-edges have swapped U-L roles.
    """
    for edge_a, edge_b in ANTIPODAL_PAIRS:
        u_a, l_a = EDGE_VERTICES[edge_a]
        u_b, l_b = EDGE_VERTICES[edge_b]
        # Swap-antipode: u_a's antipode = the OTHER edge's U; same for L
        # Cube-vertex antipodes: U0↔L0, U1↔L1, U2↔L2, U3↔L3 (alternating)
        antipode_map = {'U0': 'L0', 'U1': 'L1', 'U2': 'L2', 'U3': 'L3',
                        'L0': 'U0', 'L1': 'U1', 'L2': 'U2', 'L3': 'U3'}
        # Swap-antipode test: u_a's vertex-antipode == l_b (and u_b's antipode == l_a)
        assert antipode_map[u_a] == l_b, \
            f"Pair {edge_a}↔{edge_b} not swap-antipode at U: {u_a} antipode {antipode_map[u_a]} ≠ {l_b}"
        assert antipode_map[u_b] == l_a, \
            f"Pair {edge_a}↔{edge_b} not swap-antipode at L: {u_b} antipode {antipode_map[u_b]} ≠ {l_a}"


def test_edge_state_frozen_exact():
    s = edge_state('E01')
    assert s.pa_lon is None
    assert s.activation_strength == 0.0


def test_edge_state_live_conjunction():
    s = edge_state('E01', 100.0, 100.0)
    assert s.activation_strength == 1.0
    assert 'conjunction' in s.active_aspects


def test_carrier_system_full_state():
    """All 8 planets at same lon → all 12 edges conjunction → max activation."""
    state = carrier_system.system_state(planet_lons={
        'Pluto': 60.0, 'Sun': 60.0, 'Mars': 60.0, 'Saturn': 60.0,
        'Neptune': 60.0, 'Moon': 60.0, 'Mercury': 60.0, 'Jupiter': 60.0,
    })
    d = state.to_dict()
    assert d['whole_cube_activation'] == 12.0  # 12 edges × activation 1.0
    assert d['all_quiet'] is False


def test_carrier_system_frozen():
    state = carrier_system.system_state()
    d = state.to_dict()
    assert d['whole_cube_activation'] is None
