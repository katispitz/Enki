"""
Tests for 6 Primordial face engines + registry.

Per V2.5 T1.1-REVISED (Lillu canon §M.5) substrate-locks:
  Gaia@MQF0/Venus×Pluto/Taurus/a64c8127
  Chaos@MQF1/Mercury×Pluto/Virgo/2f2bd039
  Erebus@MQF2/Saturn×Pluto/Capricorn/2391bb9f
  Nyx@MQF3/Moon×Neptune/Cancer/ac6c221d
  Eros-prim@MQF4/Jupiter×Neptune/Pisces/524fdee6
  Tartarus@MQF5/Mars×Neptune/Scorpio/f76168b6

Each engine = thin wrapper composing `_axis_engine.compute_axis_state` with
substrate-locked params.
"""
import pytest
import primordial_gaia
import primordial_chaos
import primordial_erebus
import primordial_nyx
import primordial_eros
import primordial_tartarus
import primordials


PRIMORDIAL_MODULES = [
    (primordial_gaia,     'Gaia',            'MQF0', ('Venus', 'Pluto'),     'Taurus',    'a64c8127'),
    (primordial_chaos,    'Chaos',           'MQF1', ('Mercury', 'Pluto'),   'Virgo',     '2f2bd039'),
    (primordial_erebus,   'Erebus',          'MQF2', ('Saturn', 'Pluto'),    'Capricorn', '2391bb9f'),
    (primordial_nyx,      'Nyx',             'MQF3', ('Moon', 'Neptune'),    'Cancer',    'ac6c221d'),
    (primordial_eros,     'Eros-primordial', 'MQF4', ('Jupiter', 'Neptune'), 'Pisces',    '524fdee6'),
    (primordial_tartarus, 'Tartarus',        'MQF5', ('Mars', 'Neptune'),    'Scorpio',   'f76168b6'),
]


@pytest.mark.parametrize('mod,name,face,pair,zodiac,card', PRIMORDIAL_MODULES)
def test_primordial_substrate_locks(mod, name, face, pair, zodiac, card):
    """Each Primordial has canon-locked substrate position."""
    assert mod.PRIMORDIAL_NAME == name
    assert mod.CUBE_FACE == face
    assert mod.PLANET_PAIR == pair
    assert mod.ZODIAC_ANCHOR == zodiac
    assert mod.SUBSTRATE_CARD == card


@pytest.mark.parametrize('mod,name,face,pair,zodiac,card', PRIMORDIAL_MODULES)
def test_primordial_frozen_state(mod, name, face, pair, zodiac, card):
    """Frozen state returns substrate-locks with NULL live fields."""
    s = mod.axis_state()
    assert s.primordial == name
    assert s.cube_face == face
    assert s.planet_pair == pair
    assert s.zodiac_anchor == zodiac
    assert s.substrate_card == card
    assert s.pa_lon is None
    assert s.activation_strength == 0.0


@pytest.mark.parametrize('mod,name,face,pair,zodiac,card', PRIMORDIAL_MODULES)
def test_primordial_live_conjunction(mod, name, face, pair, zodiac, card):
    """Each Primordial fires conjunction when both planets at same lon."""
    s = mod.axis_state(100.0, 100.0)
    assert s.activation_strength == 1.0
    assert 'conjunction' in s.active_aspects


def test_registry_has_6_primordials():
    assert len(primordials.PRIMORDIALS) == 6


def test_registry_by_name_lookups():
    g = primordials.get('Gaia')
    assert g.PRIMORDIAL_NAME == 'Gaia'
    n = primordials.get('Nyx')
    assert n.PRIMORDIAL_NAME == 'Nyx'


def test_registry_by_face_lookups():
    assert primordials.get('MQF0').PRIMORDIAL_NAME == 'Gaia'
    assert primordials.get('MQF5').PRIMORDIAL_NAME == 'Tartarus'


def test_registry_by_zodiac_lookups():
    assert primordials.get('Taurus').PRIMORDIAL_NAME == 'Gaia'
    assert primordials.get('Pisces').PRIMORDIAL_NAME == 'Eros-primordial'


def test_registry_by_planet_pair():
    assert primordials.get_by_pair('Venus', 'Pluto').PRIMORDIAL_NAME == 'Gaia'
    assert primordials.get_by_pair('Pluto', 'Venus').PRIMORDIAL_NAME == 'Gaia'  # order-independent
    assert primordials.get_by_pair('Mars', 'Neptune').PRIMORDIAL_NAME == 'Tartarus'


def test_pluto_neptune_partition_via_registry():
    """FINDINGS_002 finding: 3 Pluto-anchored + 3 Neptune-anchored Primordials."""
    pluto_anchored = [p for p in primordials.PRIMORDIALS
                      if 'Pluto' in p.PLANET_PAIR]
    neptune_anchored = [p for p in primordials.PRIMORDIALS
                        if 'Neptune' in p.PLANET_PAIR]
    assert len(pluto_anchored) == 3
    assert len(neptune_anchored) == 3
    pluto_names = {p.PRIMORDIAL_NAME for p in pluto_anchored}
    neptune_names = {p.PRIMORDIAL_NAME for p in neptune_anchored}
    assert pluto_names == {'Gaia', 'Chaos', 'Erebus'}
    assert neptune_names == {'Nyx', 'Eros-primordial', 'Tartarus'}


def test_earth_water_zodiac_partition():
    """FINDINGS_002: Pluto-anchored = Earth trine, Neptune-anchored = Water trine."""
    earth_signs = {'Taurus', 'Virgo', 'Capricorn'}
    water_signs = {'Cancer', 'Pisces', 'Scorpio'}
    pluto_zodiacs = {p.ZODIAC_ANCHOR for p in primordials.PRIMORDIALS if 'Pluto' in p.PLANET_PAIR}
    neptune_zodiacs = {p.ZODIAC_ANCHOR for p in primordials.PRIMORDIALS if 'Neptune' in p.PLANET_PAIR}
    assert pluto_zodiacs == earth_signs
    assert neptune_zodiacs == water_signs


def test_all_face_ids_unique():
    faces = [p.CUBE_FACE for p in primordials.PRIMORDIALS]
    assert len(set(faces)) == 6
    assert set(faces) == {'MQF0', 'MQF1', 'MQF2', 'MQF3', 'MQF4', 'MQF5'}
