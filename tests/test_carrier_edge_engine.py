"""
Tests for _carrier_edge_engine.py — substrate-invariants from FINDINGS_019.

Validates that the cube-edge carrier engine:
  - Frozen state NULL-honest across all fields
  - Live-compute fields IDENTICAL to AxisState + BridgeState for same input
    (shape-match outcome (a) per transmit-force conflation-test council 2026-05-16)
  - Partial-input ValueError (NULL-honest reject)
  - Candidate-distinct probe fields evaluate per FINDINGS_019 documented behavior
  - Canonical activation = 1.0 at ideal-input
  - Substrate-locked metadata categories preserved
"""
import math
import pytest
from dataclasses import fields


# ─── Substrate-locks / canon-constant invariants ──────────────────────────────

def test_substrate_locks_match_canon():
    """Canon §3 R=1 + canon §1 cube edge length = 2/√3."""
    from _carrier_edge_engine import SUBSTRATE_R_SHELL, CUBE_EDGE_LENGTH, ORB_IGNITION_DEG
    assert SUBSTRATE_R_SHELL == 1.0  # canon §3
    assert math.isclose(CUBE_EDGE_LENGTH, 2.0 / math.sqrt(3.0))  # canon §1 derivation
    assert ORB_IGNITION_DEG == 6.0  # V2.6 G4 two-tier-orb canon


def test_canonical_declaration_matches_30():
    """__canonical__ matches canon §30 entry for planet-aspect-activate."""
    from _carrier_edge_engine import __canonical__
    assert __canonical__['function_class'] == 'planet-aspect-activate'
    assert __canonical__['functional_tier'] == 'primitive'
    assert __canonical__['compositional_axis'] == 'spatial'
    assert __canonical__['status'] == 'canonical'


# ─── Frozen-state NULL-honesty ────────────────────────────────────────────────

def test_frozen_state_null_honest():
    """No ephemeris input → frozen state, all live fields NULL/0.0."""
    from _carrier_edge_engine import frozen_carrier_edge
    fr = frozen_carrier_edge(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD'
    )
    # Substrate-locks populated
    assert fr.carrier_name == 'cube-edge-E01'
    assert fr.cube_edge == 'E01'
    assert fr.u_vertex == 'U0'
    assert fr.l_vertex == 'L1'
    assert fr.edge_axis == 'z'
    assert fr.planet_pair == ('Pluto', 'Moon')
    assert fr.shell == 1.0
    # Live fields NULL
    assert fr.pa_lon is None
    assert fr.pb_lon is None
    assert fr.midpoint_lon is None
    assert fr.angular_separation is None
    assert fr.active_aspects == []
    assert fr.activation_strength == 0.0
    assert fr.closest_aspect_deg is None
    assert fr.closest_orb is None
    # Candidate-distinct probe fields NULL in frozen state
    assert fr.flow_direction is None
    assert fr.edge_integrated_magnitude is None
    assert fr.carrier_modulation_phase is None


def test_partial_input_value_error():
    """One longitude given, one None → ValueError (NULL-honest reject)."""
    from _carrier_edge_engine import compute_carrier_edge_state
    with pytest.raises(ValueError, match='substrate-incomplete'):
        compute_carrier_edge_state(
            'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD',
            120.0, None,
        )
    with pytest.raises(ValueError, match='substrate-incomplete'):
        compute_carrier_edge_state(
            'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD',
            None, 120.0,
        )


# ─── Canonical activation at ideal input ──────────────────────────────────────

def test_exact_conjunction_canonical_activation():
    """PA=PB → exact conjunction → activation_strength = 1.0."""
    from _carrier_edge_engine import compute_carrier_edge_state
    s = compute_carrier_edge_state(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD',
        120.0, 120.0,
    )
    assert s.activation_strength == 1.0
    assert s.angular_separation == 0.0
    assert 'conjunction' in s.active_aspects
    assert s.closest_aspect_deg == 0


def test_no_aspect_no_activation():
    """Outside 6° orb of any canonical aspect → activation 0.0, no aspects."""
    from _carrier_edge_engine import compute_carrier_edge_state
    s = compute_carrier_edge_state(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD',
        0.0, 37.0,
    )
    assert s.activation_strength == 0.0
    assert s.active_aspects == []


# ─── Shape-match invariant (FINDINGS_019 outcome (a)) ─────────────────────────

def test_live_compute_shape_match_axis_engine():
    """
    FINDINGS_019 outcome (a) invariant: live-compute fields IDENTICAL between
    CarrierEdgeState and AxisState given same input.
    """
    from _axis_engine import compute_axis_state
    from _carrier_edge_engine import compute_carrier_edge_state
    PA, PB = 100.0, 220.0  # asymmetric input near trine (sep ~120)
    axis = compute_axis_state('Gaia', 'MQF0', ('Venus', 'Pluto'), 'Taurus', 'card123', PA, PB)
    carrier = compute_carrier_edge_state(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD', PA, PB
    )
    live_fields = [
        'pa_lon', 'pb_lon', 'midpoint_lon', 'angular_separation',
        'active_aspects', 'activation_strength',
        'closest_aspect_deg', 'closest_orb',
    ]
    for f in live_fields:
        assert getattr(axis, f) == getattr(carrier, f), (
            f"Live-compute field {f} mismatch: axis={getattr(axis, f)!r} "
            f"carrier={getattr(carrier, f)!r}"
        )


def test_live_compute_shape_match_bridge_engine():
    """Live-compute fields IDENTICAL between CarrierEdgeState and BridgeState."""
    from _bridge_engine import compute_bridge_state
    from _carrier_edge_engine import compute_carrier_edge_state
    PA, PB = 45.0, 135.0  # exact square
    bridge = compute_bridge_state(
        'Harmonia', 'midpt(V2,V7)', ('V2', 'V7'), ('Venus', 'Mars'), 'card456', PA, PB
    )
    carrier = compute_carrier_edge_state(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD', PA, PB
    )
    live_fields = [
        'pa_lon', 'pb_lon', 'midpoint_lon', 'angular_separation',
        'active_aspects', 'activation_strength',
        'closest_aspect_deg', 'closest_orb',
    ]
    for f in live_fields:
        assert getattr(bridge, f) == getattr(carrier, f), (
            f"Live-compute field {f} mismatch: bridge={getattr(bridge, f)!r} "
            f"carrier={getattr(carrier, f)!r}"
        )


# ─── Candidate-distinct probe-field invariants per FINDINGS_019 ───────────────

def test_flow_direction_substrate_vestigial():
    """
    FINDINGS_019 invariant: flow_direction differs when PA/PB swapped,
    but activation_strength stays IDENTICAL — confirming flow_direction is
    live-derivable but NOT consumed by canonical compute (substrate-vestigial).
    """
    from _carrier_edge_engine import compute_carrier_edge_state
    u_leads = compute_carrier_edge_state(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD', 120.0, 180.0
    )
    l_leads = compute_carrier_edge_state(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD', 180.0, 120.0
    )
    # Canonical activation symmetric on |sep|
    assert u_leads.activation_strength == l_leads.activation_strength
    assert u_leads.angular_separation == l_leads.angular_separation
    # Flow direction asymmetric (live-derivable)
    assert u_leads.flow_direction == 'U→L'
    assert l_leads.flow_direction == 'L→U'


def test_flow_direction_symmetric_at_conjunction():
    """At PA == PB, flow_direction = 'symmetric' (no signed arc)."""
    from _carrier_edge_engine import compute_carrier_edge_state
    s = compute_carrier_edge_state(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD', 200.0, 200.0
    )
    assert s.flow_direction == 'symmetric'


def test_edge_integrated_magnitude_substrate_redundant():
    """
    FINDINGS_019 invariant: edge_integrated_magnitude == activation_strength
    × CUBE_EDGE_LENGTH. Pure algebraic transform of canonical compute by
    substrate-locked constant — substrate-redundant.
    """
    from _carrier_edge_engine import compute_carrier_edge_state, CUBE_EDGE_LENGTH
    s = compute_carrier_edge_state(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD', 0.0, 0.0
    )
    assert math.isclose(s.edge_integrated_magnitude,
                        s.activation_strength * CUBE_EDGE_LENGTH)


def test_carrier_modulation_phase_substrate_undefined():
    """
    FINDINGS_019 invariant: carrier_modulation_phase has no independent compute
    from canonical 2-planet input. Returns activation-mirror (≥0) or NULL.
    """
    from _carrier_edge_engine import compute_carrier_edge_state
    # No aspect → NULL
    s_none = compute_carrier_edge_state(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD', 0.0, 37.0
    )
    assert s_none.carrier_modulation_phase is None
    # Active aspect → mirrors activation_strength
    s_active = compute_carrier_edge_state(
        'cube-edge-E01', 'E01', 'U0', 'L1', 'z', ('Pluto', 'Moon'), 'TBD', 0.0, 0.0
    )
    assert s_active.carrier_modulation_phase == s_active.activation_strength


# ─── Field-category partition invariant (SDEC step 3) ─────────────────────────

def test_field_categories_partition():
    """
    SDEC step 3 partition: CarrierEdgeState has 8 substrate-locked metadata
    fields + 8 live-compute fields + 3 candidate-distinct probe fields = 19.
    """
    from _carrier_edge_engine import CarrierEdgeState
    all_fields = {f.name for f in fields(CarrierEdgeState)}
    substrate_locked = {'carrier_name', 'cube_edge', 'u_vertex', 'l_vertex',
                        'edge_axis', 'planet_pair', 'substrate_card', 'shell'}
    live_compute = {'pa_lon', 'pb_lon', 'midpoint_lon', 'angular_separation',
                    'active_aspects', 'activation_strength',
                    'closest_aspect_deg', 'closest_orb'}
    candidate_distinct = {'flow_direction', 'edge_integrated_magnitude',
                          'carrier_modulation_phase'}
    expected = substrate_locked | live_compute | candidate_distinct
    assert all_fields == expected, (
        f"Field set drift — extra: {all_fields - expected}, "
        f"missing: {expected - all_fields}"
    )
    assert len(all_fields) == 19
