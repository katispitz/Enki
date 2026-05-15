"""
Tests for Primordial pair/trine/system cascade composition.

Per FINDINGS_002+003+004:
  6 face → 3 antipodal pairs → 2 trines → 1 system cascade structure.
  Antipodal pairs: Gaia↔Eros-prim, Chaos↔Tartarus, Erebus↔Nyx.
  Each pair = 1 Pluto-side + 1 Neptune-side (crosses partition).
"""
import pytest
import pair_gaia_eros
import pair_chaos_tartarus
import pair_erebus_nyx
import primordial_pairs
import trine_pluto_axis
import trine_neptune_axis
import primordial_trines
import primordial_system


PAIR_MODULES = [
    (pair_gaia_eros,      ('Gaia', 'Eros-primordial'), ('MQF0', 'MQF4')),
    (pair_chaos_tartarus, ('Chaos', 'Tartarus'),       ('MQF1', 'MQF5')),
    (pair_erebus_nyx,     ('Erebus', 'Nyx'),           ('MQF2', 'MQF3')),
]


@pytest.mark.parametrize('mod,pair_name,face_pair', PAIR_MODULES)
def test_pair_substrate_locks(mod, pair_name, face_pair):
    assert mod.PAIR_NAME == pair_name
    assert mod.CUBE_FACE_PAIR == face_pair


@pytest.mark.parametrize('mod,pair_name,face_pair', PAIR_MODULES)
def test_pair_frozen(mod, pair_name, face_pair):
    s = mod.pair_state()
    d = s.to_dict()
    assert tuple(d['pair_name']) == pair_name
    assert d['both_active'] is None  # frozen


def test_pair_both_conjunction_balanced():
    """Both faces firing conjunction → balanced polarity."""
    # Gaia-Eros: Venus×Pluto + Jupiter×Neptune
    s = pair_gaia_eros.pair_state(60.0, 60.0, 345.0, 345.0)
    d = s.to_dict()
    assert d['both_active'] is True
    assert d['co_activation'] == 1.0
    assert d['polarity'] == 0.0
    assert d['polarity_label'] == 'balanced'


def test_pair_earth_dominant():
    """Earth-side firing, Water-side quiet → earth-dominant polarity."""
    # Gaia conj (60/60), Eros at non-aspect (0/90)
    s = pair_gaia_eros.pair_state(60.0, 60.0, 0.0, 90.0)
    d = s.to_dict()
    # 0-90 = square = 90° = activation 1, but Eros wants exact aspect
    # check it's NOT balanced
    # Actually 0-90 fires square at 1.0 → both_active = True
    # Let me pick clear earth-only:
    s2 = pair_gaia_eros.pair_state(60.0, 60.0, 0.0, 7.0)  # 7° apart no aspect
    d2 = s2.to_dict()
    assert d2['both_active'] is False
    assert d2['polarity_label'] in ('Gaia-dominant', 'earth-dominant', 'SOURCE-dominant')  # earth-side dominant


def test_registry_3_pairs():
    assert len(primordial_pairs.PAIRS) == 3


def test_registry_lookup_by_primordial_name():
    p = primordial_pairs.get_pair('Gaia')
    assert p.PAIR_NAME == ('Gaia', 'Eros-primordial')
    p2 = primordial_pairs.get_pair('Nyx')
    assert p2.PAIR_NAME == ('Erebus', 'Nyx')


def test_antipodal_pairs_each_cross_pluto_neptune():
    """FINDINGS_002: every antipodal pair has 1 Pluto-side + 1 Neptune-side."""
    for p in primordial_pairs.PAIRS:
        assert p.EARTH_CARD != p.WATER_CARD
        assert 'Pluto' in p.EARTH_PLANET_PAIR
        assert 'Neptune' in p.WATER_PLANET_PAIR


def test_trine_pluto_axis():
    assert trine_pluto_axis.OUTER_ANCHOR == 'Pluto'
    assert trine_pluto_axis.ELEMENT == 'Earth'
    assert trine_pluto_axis.PRIMORDIALS == ['Gaia', 'Chaos', 'Erebus']


def test_trine_neptune_axis():
    assert trine_neptune_axis.OUTER_ANCHOR == 'Neptune'
    assert trine_neptune_axis.ELEMENT == 'Water'
    assert trine_neptune_axis.PRIMORDIALS == ['Nyx', 'Eros-primordial', 'Tartarus']


def test_pluto_trine_live_partial_input_raises():
    """Mixed frozen/live (some lons supplied, others None) → ValueError."""
    with pytest.raises(ValueError):
        trine_pluto_axis.trine_state(60.0, None, 280.0, 100.0)


def test_system_cascade_full_composition():
    """primordial_system composes 6 faces + 3 pairs + 2 trines → 1 system."""
    state = primordial_system.system_state(
        venus_lon=60.0, mercury_lon=60.0, saturn_lon=60.0, pluto_lon=60.0,
        moon_lon=200.0, jupiter_lon=200.0, mars_lon=200.0, neptune_lon=200.0,
    )
    d = state.to_dict()
    # All Pluto-side conj at 60°, all Neptune-side conj at 200° → 6/6 active
    assert d['active_face_count'] == 6
    assert d['all_quiet'] is False
    # All firing at full activation, even balance
    assert d['whole_cube_activation'] == 6.0


def test_system_frozen():
    s = primordial_system.system_state().to_dict()
    assert s['whole_cube_activation'] is None
    assert s['active_face_count'] is None
