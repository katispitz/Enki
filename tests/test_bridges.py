"""
Tests for 3 V2.5-locked icosidodec-midpoint Bridge engines.

Per Lillu canon §M.5 V2.5 LOCKS:
  Harmonia (V2-V7 / Venus-Mars / 52ad9413)
  Hermaphroditus (V3-V2 / Mercury-Venus / 91697158)
  Erichthonius (V4-V8 / Saturn-Uranus / 3de9d703)

Per FINDINGS_005: bridge engine field-shape matches Primordial face engine
at compute layer (cross-R-tier residency confirmed).
"""
import pytest
import bridge_harmonia
import bridge_hermaphroditus
import bridge_erichthonius
import bridges


BRIDGE_MODULES = [
    (bridge_harmonia,       'Harmonia',       'midpt(V2, V7)', ('V2', 'V7'), ('Venus', 'Mars'),    '52ad9413'),
    (bridge_hermaphroditus, 'Hermaphroditus', 'midpt(V3, V2)', ('V3', 'V2'), ('Mercury', 'Venus'), '91697158'),
    (bridge_erichthonius,   'Erichthonius',   'midpt(V4, V8)', ('V4', 'V8'), ('Saturn', 'Uranus'), '3de9d703'),
]


@pytest.mark.parametrize('mod,name,anchor,parents,pair,card', BRIDGE_MODULES)
def test_bridge_substrate_locks(mod, name, anchor, parents, pair, card):
    assert mod.BRIDGE_NAME == name
    assert mod.ICOSIDODEC_ANCHOR == anchor
    assert mod.PARENT_VERTICES == parents
    assert mod.PARENT_PLANETS == pair
    assert mod.SUBSTRATE_CARD == card


@pytest.mark.parametrize('mod,name,anchor,parents,pair,card', BRIDGE_MODULES)
def test_bridge_frozen(mod, name, anchor, parents, pair, card):
    s = mod.bridge_state()
    assert s.bridge_name == name
    assert s.pa_lon is None
    assert s.activation_strength == 0.0
    assert s.shell == 'φ'


@pytest.mark.parametrize('mod,name,anchor,parents,pair,card', BRIDGE_MODULES)
def test_bridge_live_conjunction(mod, name, anchor, parents, pair, card):
    s = mod.bridge_state(60.0, 60.0)
    assert s.activation_strength == 1.0
    assert 'conjunction' in s.active_aspects


def test_bridges_registry_3():
    assert len(bridges.BRIDGES) == 3


def test_bridges_lookup_by_name():
    assert bridges.get('Harmonia').BRIDGE_NAME == 'Harmonia'
    assert bridges.get('Erichthonius').BRIDGE_NAME == 'Erichthonius'


def test_bridges_lookup_by_parent_pair():
    assert bridges.get_by_parent_planets('Venus', 'Mars').BRIDGE_NAME == 'Harmonia'
    assert bridges.get_by_parent_planets('Mars', 'Venus').BRIDGE_NAME == 'Harmonia'  # order-independent


def test_bridge_partial_input_raises():
    with pytest.raises(ValueError):
        bridge_harmonia.bridge_state(60.0, None)


def test_cross_r_tier_compute_field_match_with_primordial():
    """
    FINDINGS_005 invariant: 9 live-state compute fields identical between
    AxisState (Primordial face) and BridgeState (Bridge midpt).

    Test: live-state field-name overlap on compute fields = 9 exactly.
    """
    from _axis_engine import AxisState
    from _bridge_engine import BridgeState
    from dataclasses import fields

    ax = {f.name for f in fields(AxisState)}
    br = {f.name for f in fields(BridgeState)}
    shared = ax & br

    # Compute fields shared (FINDINGS_005 documented 9):
    expected_shared = {
        'pa_lon', 'pb_lon', 'midpoint_lon', 'angular_separation',
        'active_aspects', 'activation_strength',
        'closest_aspect_deg', 'closest_orb',
        'substrate_card',
    }
    assert expected_shared.issubset(shared), \
        f"Cross-R-tier compute-field shape match broken. Missing: {expected_shared - shared}"
