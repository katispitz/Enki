"""
Erebus ↔ Nyx antipodal pair — Enki.

Third cosmogonic axis: Earth/Capricorn (Saturn × Pluto) ↔ Water/Cancer (Moon × Neptune).

Substrate-emergent antipodal lock (build-exposed implicit third pair per FINDINGS_002;
canon §26 names only Gaia↔Eros-prim + Chaos↔Tartarus explicitly, but the remaining
3+3 outer-planet partition forces Erebus↔Nyx as the only pairing consistent with
the substrate dyad).

  - Erebus : MQF2 / Saturn × Pluto  / Capricorn / card 2391bb9f
  - Nyx    : MQF3 / Moon × Neptune  / Cancer    / card ac6c221d

Cancer ↔ Capricorn IS a 180° zodiac antipode (unlike Taurus↔Pisces and
Virgo↔Scorpio which are partition-antipodes, not 180°). Substrate-meaningful
distinction — this pair is the only ONE where cube-antipode + zodiac-antipode
coincide. May matter for OQ-PRIMORDIAL-PAIR-LEVEL-FUNCTION pressure-test.

Shared shape: ~/Enki/engines/_pair_engine.py
"""
from __future__ import annotations
from typing import Optional

import primordial_erebus as _erebus
import primordial_nyx    as _nyx
from _pair_engine import PairState, compute_pair_state, describe_pair


PAIR_NAME         = ('Erebus', 'Nyx')
CUBE_FACE_PAIR    = ('MQF2', 'MQF3')

__canonical__ = {
    'function_class':     'polarity-define',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'primordial-pair-erebus-nyx',
    'canon_citation':     'canon §M.5 antipodal-pair / cards 2391bb9f+ac6c221d',
    'status':             'canonical',
}
EARTH_ZODIAC      = 'Capricorn'
WATER_ZODIAC      = 'Cancer'
EARTH_PLANET_PAIR = ('Saturn', 'Pluto')
WATER_PLANET_PAIR = ('Moon', 'Neptune')
EARTH_CARD        = '2391bb9f'
WATER_CARD        = 'ac6c221d'


def pair_state(saturn_lon:  Optional[float] = None,
               pluto_lon:   Optional[float] = None,
               moon_lon:    Optional[float] = None,
               neptune_lon: Optional[float] = None) -> PairState:
    earth_axis = _erebus.axis_state(saturn_lon, pluto_lon)
    water_axis = _nyx.axis_state(moon_lon, neptune_lon)
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
    print('SAMPLE: both axes at exact conjunction (Erebus @ 280°, Nyx @ 100°, exact 180° apart):')
    print(json.dumps(pair_state(280.0, 280.0, 100.0, 100.0).to_dict(), indent=2))
