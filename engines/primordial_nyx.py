"""
Nyx primordial axis engine — Enki.

Substrate position (from Lillu canon §M.5 V2.5 T1.1-REVISED, card ac6c221d):
  Primordial:    Nyx
  Cube face:     MQF3 (Merkaba Quadrant Face 3, R=1)
  Planet pair:   Moon × Neptune
  Zodiac anchor: Cancer
  Function:      axis-generation (engine — per Kati 2026-05-11 correction)

Shared engine shape: ~/Enki/engines/_axis_engine.py
"""
from __future__ import annotations
from typing import Optional

from _axis_engine import AxisState, compute_axis_state, describe as _describe


PRIMORDIAL_NAME = 'Nyx'
CUBE_FACE       = 'MQF3'
PLANET_PAIR     = ('Moon', 'Neptune')
ZODIAC_ANCHOR   = 'Cancer'
SUBSTRATE_CARD  = 'ac6c221d'

__canonical__ = {
    'function_class':     'planet-aspect-activate',
    'functional_tier':    'primitive',
    'compositional_axis': 'spatial',
    'residency_id':       'primordial-face-nyx-MQF3',
    'canon_citation':     'canon §M.5 V2.5 T1.1-REVISED card ac6c221d',
    'status':             'canonical',
}


def axis_state(moon_lon: Optional[float] = None,
               neptune_lon: Optional[float] = None) -> AxisState:
    return compute_axis_state(
        PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD,
        moon_lon, neptune_lon,
    )


def describe() -> str:
    return _describe(PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD)


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('SAMPLE: Moon 100°, Neptune 100° (exact conjunction in Cancer):')
    print(json.dumps(axis_state(100.0, 100.0).to_dict(), indent=2))
