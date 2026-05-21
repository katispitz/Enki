"""
Chaos primordial axis engine — Enki.

Substrate position (from Nammu canon §M.5 V2.5 T1.1-REVISED, card 2f2bd039):
  Primordial:    Chaos
  Cube face:     MQF1 (Merkaba Quadrant Face 1, R=1)
  Planet pair:   Mercury × Pluto
  Zodiac anchor: Virgo
  Function:      axis-generation (engine — per Kati 2026-05-11 correction)

Shared engine shape: ~/Enki/engines/_axis_engine.py
"""
from __future__ import annotations
from typing import Optional

from _axis_engine import AxisState, compute_axis_state, describe as _describe


PRIMORDIAL_NAME = 'Chaos'
CUBE_FACE       = 'MQF1'
PLANET_PAIR     = ('Mercury', 'Pluto')
ZODIAC_ANCHOR   = 'Virgo'
SUBSTRATE_CARD  = '2f2bd039'

__canonical__ = {
    'function_class':     'planet-aspect-activate',
    'functional_tier':    'primitive',
    'compositional_axis': 'spatial',
    'residency_id':       'primordial-face-chaos-MQF1',
    'canon_citation':     'canon §M.5 V2.5 T1.1-REVISED card 2f2bd039',
    'status':             'canonical',
}


def axis_state(mercury_lon: Optional[float] = None,
               pluto_lon: Optional[float] = None) -> AxisState:
    return compute_axis_state(
        PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD,
        mercury_lon, pluto_lon,
    )


def describe() -> str:
    return _describe(PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD)


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('SAMPLE: Mercury 165°, Pluto 165° (exact conjunction in Virgo):')
    print(json.dumps(axis_state(165.0, 165.0).to_dict(), indent=2))
