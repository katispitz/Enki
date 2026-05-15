"""
Chaos ↔ Tartarus antipodal pair — Enki.

Second cosmogonic axis: Earth/Virgo (Mercury × Pluto) ↔ Water/Scorpio (Mars × Neptune).

Canon §26 V2.5 T1.1-REVISED Hesiod-coherent antipodal lock:
  - Chaos    : MQF1 / Mercury × Pluto / Virgo   / card 2f2bd039
  - Tartarus : MQF5 / Mars × Neptune  / Scorpio / card f76168b6

Shared shape: ~/Enki/engines/_pair_engine.py
"""
from __future__ import annotations
from typing import Optional

import primordial_chaos    as _chaos
import primordial_tartarus as _tartarus
from _pair_engine import PairState, compute_pair_state, describe_pair


PAIR_NAME         = ('Chaos', 'Tartarus')
CUBE_FACE_PAIR    = ('MQF1', 'MQF5')

__canonical__ = {
    'function_class':     'polarity-define',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'primordial-pair-chaos-tartarus',
    'canon_citation':     'canon §M.5 antipodal-pair / cards 2f2bd039+f76168b6',
    'status':             'canonical',
}
EARTH_ZODIAC      = 'Virgo'
WATER_ZODIAC      = 'Scorpio'
EARTH_PLANET_PAIR = ('Mercury', 'Pluto')
WATER_PLANET_PAIR = ('Mars', 'Neptune')
EARTH_CARD        = '2f2bd039'
WATER_CARD        = 'f76168b6'


def pair_state(mercury_lon: Optional[float] = None,
               pluto_lon:   Optional[float] = None,
               mars_lon:    Optional[float] = None,
               neptune_lon: Optional[float] = None) -> PairState:
    earth_axis = _chaos.axis_state(mercury_lon, pluto_lon)
    water_axis = _tartarus.axis_state(mars_lon, neptune_lon)
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
    print('SAMPLE: both axes at exact conjunction (Chaos @ 165°, Tartarus @ 225°):')
    print(json.dumps(pair_state(165.0, 165.0, 225.0, 225.0).to_dict(), indent=2))
