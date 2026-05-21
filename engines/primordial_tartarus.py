"""
Tartarus primordial axis engine — Enki.

Substrate position (from Nammu canon §M.5 V2.5 T1.1-REVISED, card f76168b6):
  Primordial:    Tartarus
  Cube face:     MQF5 (Merkaba Quadrant Face 5, R=1)
  Planet pair:   Mars × Neptune
  Zodiac anchor: Scorpio
  Function:      axis-generation (engine — per Kati 2026-05-11 correction)

Shared engine shape: ~/Enki/engines/_axis_engine.py
"""
from __future__ import annotations
from typing import Optional

from _axis_engine import AxisState, compute_axis_state, describe as _describe


PRIMORDIAL_NAME = 'Tartarus'
CUBE_FACE       = 'MQF5'
PLANET_PAIR     = ('Mars', 'Neptune')
ZODIAC_ANCHOR   = 'Scorpio'
SUBSTRATE_CARD  = 'f76168b6'

__canonical__ = {
    'function_class':     'planet-aspect-activate',
    'functional_tier':    'primitive',
    'compositional_axis': 'spatial',
    'residency_id':       'primordial-face-tartarus-MQF5',
    'canon_citation':     'canon §M.5 V2.5 T1.1-REVISED card f76168b6',
    'status':             'canonical',
}


def axis_state(mars_lon: Optional[float] = None,
               neptune_lon: Optional[float] = None) -> AxisState:
    return compute_axis_state(
        PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD,
        mars_lon, neptune_lon,
    )


def describe() -> str:
    return _describe(PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD)


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('SAMPLE: Mars 230°, Neptune 230° (exact conjunction in Scorpio):')
    print(json.dumps(axis_state(230.0, 230.0).to_dict(), indent=2))
