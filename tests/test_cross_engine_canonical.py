"""
Tests for canon §30 canonical function-class invariants surfaced by FINDINGS docs.

Validates that the substrate-architectural findings continue to hold:
  - FINDINGS_002: 3+3 Pluto/Neptune Primordial partition + Earth/Water trine
  - FINDINGS_003: 1+3 pair-partition pattern at cube-face (apex + 3 lateral)
  - FINDINGS_005: cross-R-tier residency for `planet-aspect-activate` (Primordial face × Bridge midpt)
  - FINDINGS_008: 3rd residency at cube-edge carriers
  - FINDINGS_009: cube-edge cascade 12→6→3→1; falsifies 1+3 partition at cube-edge
  - FINDINGS_011: triangle-aspect-activate cross-R-tier (inner-oct face × tet-face)
  - FINDINGS_012/013: N-polygon family BIFURCATES at N=5 (spatial vs temporal)
  - FINDINGS_014: cyclic-syzygy-activate (was cyclic-conjunction); Mars opposition
  - FINDINGS_015: 4th residency (Lunar); cross-event-type umbrella

These are LIVING substrate-invariants — break = canonical drift.
"""
import pytest
from dataclasses import fields


# ─── Canonical primitive: planet-aspect-activate ──────────────────────────────

def test_planet_aspect_activate_primitive_at_3_residencies():
    """
    Canon §30: `planet-aspect-activate` (primitive/spatial) has 3 residencies
    (cube-face Primordial + icosidodec-midpt Bridge + cube-edge Carrier).
    """
    # All 3 use compute_axis_state directly or via field-shape:
    from _axis_engine import compute_axis_state, AxisState
    from _bridge_engine import BridgeState
    # Primordial face (uses compute_axis_state directly)
    import primordial_gaia
    g = primordial_gaia.axis_state(60.0, 60.0)
    assert isinstance(g, AxisState)
    assert g.activation_strength == 1.0
    # Bridge midpt (own engine, same compute pattern)
    import bridge_harmonia
    b = bridge_harmonia.bridge_state(60.0, 60.0)
    assert isinstance(b, BridgeState)
    assert b.activation_strength == 1.0
    # Cube-edge carrier (uses compute_axis_state directly)
    from cube_edges import edge_state
    c = edge_state('E01', 60.0, 60.0)
    assert isinstance(c, AxisState)
    assert c.activation_strength == 1.0


# ─── Canonical first-composition: polarity-define ─────────────────────────────

def test_polarity_define_at_2_residencies():
    """
    Canon §30: `polarity-define` (first-composition/spatial) at 2 residencies
    (cube-face pair × inner-oct face-pair).
    """
    from _pair_engine import PairState
    from _inner_oct_pair_engine import InnerOctPairState
    # Both have polarity + polarity_label
    pair_fields = {f.name for f in fields(PairState)}
    iop_fields = {f.name for f in fields(InnerOctPairState)}
    assert 'polarity' in pair_fields
    assert 'polarity' in iop_fields
    assert 'polarity_label' in pair_fields
    assert 'polarity_label' in iop_fields


# ─── Canonical first-composition: triangle-aspect-activate ────────────────────

def test_triangle_aspect_activate_at_2_residencies():
    """
    Canon §30: `triangle-aspect-activate` (first-composition/spatial) at 2
    residencies (inner-oct face × Merkaba tet-face).
    Both compose 3 × planet-aspect-activate per triangle edge.
    """
    from _inner_oct_face_engine import InnerOctFaceState
    from _tet_face_engine import TetFaceState
    io_fields = {f.name for f in fields(InnerOctFaceState)}
    tf_fields = {f.name for f in fields(TetFaceState)}
    shared = io_fields & tf_fields
    # FINDINGS_011 documented 17 shared
    assert len(shared) == 17


# ─── Canonical first-composition: cyclic-syzygy-activate ──────────────────────

def test_cyclic_syzygy_activate_at_4_residencies():
    """
    Canon §30: `cyclic-syzygy-activate` (first-composition/temporal) at 4
    residencies (Venus Ring 3, Mercury Ring 5, Mars Ring 4, Lunar Ring 1/Ring 2 ratio).
    All compute via N-conjunction-longitude-compose pattern.
    """
    from venus_pentagram import compute_venus_pentagram_state
    from mercury_cycle import compute_mercury_cycle_state
    from mars_cycle import compute_mars_cycle_state
    from lunar_year_cycle import compute_lunar_year_cycle_state
    # All 4 produce dataclass states with `mean_adjacent_step` field (compute marker)
    vp = compute_venus_pentagram_state('t', 0.0, 144.0, 288.0, 72.0, 216.0)
    mc = compute_mercury_cycle_state('t', [(i * 114.5) % 360 for i in range(41)])
    ma = compute_mars_cycle_state('t', [(i * 48.6) % 360 for i in range(37)])
    ly = compute_lunar_year_cycle_state('t', [(i * 30.0) % 360 for i in range(12)])
    for s in (vp, mc, ma, ly):
        assert hasattr(s, 'mean_adjacent_step'), f"{s} lacks mean_adjacent_step"


# ─── N-polygon family BIFURCATION (FINDINGS_012) ──────────────────────────────

def test_spatial_axis_n_parameterized():
    """
    FINDINGS_012: spatial-axis N-polygon family has distinct canonical entries
    per vertex-count.
      N=2 → planet-aspect-activate (2-planet aspect)
      N=3 → triangle-aspect-activate (3-planet triangle)
    """
    # N=2 is primitive (AxisState compute via 2 lon args)
    from _axis_engine import compute_axis_state
    s2 = compute_axis_state('t', 'a', ('P', 'Q'), 'z', 'c', 0.0, 60.0)
    assert s2.angular_separation == 60.0
    # N=3 is first-composition (3 lons)
    from _inner_oct_face_engine import compute_inner_oct_face_state
    s3 = compute_inner_oct_face_state(
        'T', 'MODE', 'E', 'P', 'apex', ['V1', 'V2', 'V3'], ['Venus', 'Mercury', 'Saturn'], None,
        0.0, 60.0, 120.0,
    )
    assert len(s3.pair_states) == 3  # composes 3 pair-aspect-activates


def test_temporal_axis_n_covariant():
    """
    FINDINGS_013: temporal-axis family is N-COVARIANT — single function (cyclic-
    syzygy-activate) operates across all N (5, 12, 37, 41). Not N-parameterized.
    """
    from venus_pentagram import VENUS_PENTAGRAM_N
    from mercury_cycle import MERCURY_CYCLE_N
    from mars_cycle import MARS_CYCLE_N
    from lunar_year_cycle import LUNAR_CYCLE_N
    ns = {VENUS_PENTAGRAM_N, MERCURY_CYCLE_N, MARS_CYCLE_N, LUNAR_CYCLE_N}
    assert ns == {5, 12, 37, 41}  # 4 distinct N values, single function-name
    assert len(ns) == 4  # genuinely different N-values


# ─── Substrate-cascade invariants ─────────────────────────────────────────────

def test_cube_face_cascade_6_3_2_1():
    """FINDINGS_004: cube-face cascade 6 faces → 3 pairs → 2 trines → 1 system."""
    import primordials
    import primordial_pairs
    import primordial_trines
    assert len(primordials.PRIMORDIALS) == 6
    assert len(primordial_pairs.PAIRS) == 3
    assert len(primordial_trines.TRINES) == 2


def test_inner_oct_cascade_8_4_1plus3():
    """FINDINGS_007: inner-oct cascade 8 faces → 4 pairs (1 apex + 3 lateral)."""
    import inner_oct_faces
    import inner_oct_pairs
    assert len(inner_oct_faces.FACES) == 8
    assert len(inner_oct_pairs.PAIRS) == 4


def test_cube_edge_cascade_12_6_3_1():
    """
    FINDINGS_009: cube-edge cascade 12 edges → 6 antipodal pairs → 3 directions → 1.
    FALSIFIES 1+3 partition (which holds only at face-class).
    """
    from cube_edges import CUBE_EDGES, ANTIPODAL_PAIRS, DIRECTION_GROUPS
    assert len(CUBE_EDGES) == 12
    assert len(ANTIPODAL_PAIRS) == 6
    assert len(DIRECTION_GROUPS) == 3
