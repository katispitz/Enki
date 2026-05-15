"""
Tests for _axis_engine.py — canonical `planet-aspect-activate` primitive
(canon §30, functional_tier=primitive, compositional_axis=spatial).

Verifies:
  - Frozen state (substrate-locks only, NULL live fields)
  - Live state at substrate-aspect angles (0/60/90/120/180)
  - Orb behavior (linear activation across 6° ignition orb V2.6 G4)
  - Partial input → ValueError (substrate-honest reject)
  - Wrap-around midpoint calculation
"""
import pytest
from _axis_engine import (
    AxisState, compute_axis_state, SUBSTRATE_ASPECTS, ORB_IGNITION_DEG,
)


def test_frozen_axis_returns_null_live_fields():
    s = compute_axis_state('TestEngine', 'TestAnchor', ('Venus', 'Pluto'),
                           'TestZodiac', 'TestCard', None, None)
    assert s.primordial == 'TestEngine'
    assert s.cube_face == 'TestAnchor'
    assert s.planet_pair == ('Venus', 'Pluto')
    assert s.zodiac_anchor == 'TestZodiac'
    assert s.substrate_card == 'TestCard'
    # Live fields NULL when frozen
    assert s.pa_lon is None
    assert s.pb_lon is None
    assert s.midpoint_lon is None
    assert s.angular_separation is None
    assert s.active_aspects == []
    assert s.activation_strength == 0.0


def test_exact_conjunction_fires_with_activation_1():
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 60.0, 60.0)
    assert s.angular_separation == 0.0
    assert 'conjunction' in s.active_aspects
    assert s.activation_strength == 1.0


def test_exact_opposition_fires():
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 30.0, 210.0)
    assert s.angular_separation == 180.0
    assert 'opposition' in s.active_aspects
    assert s.activation_strength == 1.0


def test_exact_trine_fires():
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 0.0, 120.0)
    assert s.angular_separation == 120.0
    assert 'trine' in s.active_aspects
    assert s.activation_strength == 1.0


def test_exact_square_fires():
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 0.0, 90.0)
    assert 'square' in s.active_aspects
    assert s.activation_strength == 1.0


def test_exact_sextile_fires():
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 0.0, 60.0)
    assert 'sextile' in s.active_aspects
    assert s.activation_strength == 1.0


def test_outside_orb_no_activation():
    # 7° from any aspect (e.g., 7° from sextile 60°) → outside 6° orb
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 0.0, 67.0)
    assert s.active_aspects == []
    assert s.activation_strength == 0.0


def test_orb_linear_decay_within_orb():
    # 3° from conjunction → activation = 1 - 3/6 = 0.5
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 0.0, 3.0)
    assert 'conjunction' in s.active_aspects
    assert abs(s.activation_strength - 0.5) < 1e-9


def test_partial_input_raises():
    with pytest.raises(ValueError):
        compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 60.0, None)
    with pytest.raises(ValueError):
        compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', None, 60.0)


def test_midpoint_short_arc():
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 0.0, 60.0)
    assert s.midpoint_lon == 30.0


def test_midpoint_wraps_at_360():
    # Venus at 350°, Pluto at 10° — midpoint should be 0° (wrap)
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 350.0, 10.0)
    assert s.midpoint_lon == 0.0


def test_substrate_aspects_are_5_first_principles():
    """V2.6 substrate aspects = 0/60/90/120/180 (canon §15 + §20)."""
    degs = {deg for _name, deg, _why in SUBSTRATE_ASPECTS}
    assert degs == {0, 60, 90, 120, 180}


def test_orb_is_6_per_v26_g4():
    """V2.6 G4 ignition orb = 6° (grid-cell width)."""
    assert ORB_IGNITION_DEG == 6.0


def test_to_dict_returns_json_safe_planet_pair():
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 60.0, 60.0)
    d = s.to_dict()
    assert d['planet_pair'] == ['Venus', 'Pluto']  # list, not tuple


def test_closest_aspect_when_in_orb():
    s = compute_axis_state('E', 'A', ('Venus', 'Pluto'), 'Z', 'C', 0.0, 122.0)
    assert s.closest_aspect_deg == 120
    assert s.closest_orb == 2.0


def test_dataclass_fields_count():
    """AxisState is the universal 2-planet engine output (FINDINGS_008)."""
    from dataclasses import fields
    assert len(fields(AxisState)) == 13
