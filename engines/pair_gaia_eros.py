"""
Gaia ↔ Eros-primordial antipodal pair — Enki.

First cosmogonic axis: Earth/Taurus (Venus × Pluto) ↔ Water/Pisces (Jupiter × Neptune).

Canon §26 V2.5 T1.1-REVISED Hesiod-coherent antipodal lock:
  - Gaia            : MQF0 / Venus × Pluto    / Taurus   / card a64c8127
  - Eros-primordial : MQF4 / Jupiter × Neptune / Pisces  / card 524fdee6

Cube-face antipode + zodiac antipode (Taurus ↔ Pisces are not strict 180°
opposition; they are antipode-by-pair-grouping under the Pluto/Neptune dyad
partition, NOT zodiac-180°-antipode. Substrate-honest distinction.)

Shared shape: ~/Enki/engines/_pair_engine.py
"""
from __future__ import annotations
from typing import Optional

import primordial_gaia as _gaia
import primordial_eros as _eros
from _pair_engine import PairState, compute_pair_state, describe_pair


PAIR_NAME         = ('Gaia', 'Eros-primordial')
CUBE_FACE_PAIR    = ('MQF0', 'MQF4')

__canonical__ = {
    'function_class':     'polarity-define',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'primordial-pair-gaia-eros',
    'canon_citation':     'canon §M.5 antipodal-pair / cards a64c8127+524fdee6',
    'status':             'canonical',
}
EARTH_ZODIAC      = 'Taurus'
WATER_ZODIAC      = 'Pisces'
EARTH_PLANET_PAIR = ('Venus', 'Pluto')
WATER_PLANET_PAIR = ('Jupiter', 'Neptune')
EARTH_CARD        = 'a64c8127'
WATER_CARD        = '524fdee6'


def pair_state(venus_lon:   Optional[float] = None,
               pluto_lon:   Optional[float] = None,
               jupiter_lon: Optional[float] = None,
               neptune_lon: Optional[float] = None) -> PairState:
    """Compute the Gaia-Eros pair-level state.

    All four lons supplied → live pair state.
    All four None → frozen pair (substrate-locked definition).
    Mixed → ValueError (substrate-honest reject).
    """
    earth_axis = _gaia.axis_state(venus_lon, pluto_lon)
    water_axis = _eros.axis_state(jupiter_lon, neptune_lon)
    return compute_pair_state(
        PAIR_NAME, CUBE_FACE_PAIR,
        EARTH_ZODIAC, WATER_ZODIAC,
        EARTH_CARD, WATER_CARD,
        earth_axis, water_axis,
    )


def describe() -> str:
    return describe_pair(
        PAIR_NAME, CUBE_FACE_PAIR,
        EARTH_ZODIAC, WATER_ZODIAC,
        EARTH_PLANET_PAIR, WATER_PLANET_PAIR,
        EARTH_CARD, WATER_CARD,
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('FROZEN:')
    print(json.dumps(pair_state().to_dict(), indent=2))
    print()
    print('SAMPLE: both axes at exact conjunction (Gaia: Venus+Pluto @ 60°, Eros: Jupiter+Neptune @ 345°):')
    print(json.dumps(pair_state(60.0, 60.0, 345.0, 345.0).to_dict(), indent=2))
    print()
    print('SAMPLE: Earth-dominant (Gaia exact, Eros quiet):')
    print(json.dumps(pair_state(60.0, 60.0, 0.0, 60.0).to_dict(), indent=2))
