"""
Erebus primordial axis engine — Enki.

Substrate position (from Nammu canon §M.5 V2.5 T1.1-REVISED, card 2391bb9f):
  Primordial:    Erebus
  Cube face:     MQF2 (Merkaba Quadrant Face 2, R=1)
  Planet pair:   Saturn × Pluto
  Zodiac anchor: Capricorn
  Function:      axis-generation (engine — per Kati 2026-05-11 correction)

Shared engine shape: ~/Enki/engines/_axis_engine.py
"""
from __future__ import annotations
from typing import Optional

from _axis_engine import AxisState, compute_axis_state, describe as _describe


PRIMORDIAL_NAME = 'Erebus'
CUBE_FACE       = 'MQF2'
PLANET_PAIR     = ('Saturn', 'Pluto')
ZODIAC_ANCHOR   = 'Capricorn'
SUBSTRATE_CARD  = '2391bb9f'

__canonical__ = {
    'function_class':     'planet-aspect-activate',
    'functional_tier':    'primitive',
    'compositional_axis': 'spatial',
    'residency_id':       'primordial-face-erebus-MQF2',
    'canon_citation':     'canon §M.5 V2.5 T1.1-REVISED card 2391bb9f',
    'status':             'canonical',
}


def axis_state(saturn_lon: Optional[float] = None,
               pluto_lon: Optional[float] = None) -> AxisState:
    return compute_axis_state(
        PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD,
        saturn_lon, pluto_lon,
    )


def describe() -> str:
    return _describe(PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD)


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('SAMPLE: Saturn 280°, Pluto 280° (exact conjunction in Capricorn):')
    print(json.dumps(axis_state(280.0, 280.0).to_dict(), indent=2))
