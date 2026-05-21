"""
Eros (primordial) axis engine — Enki.

NOT to be confused with Olympian-era Eros (son of Aphrodite). This is the
PRIMORDIAL Eros — Hesiod-line first-generation deity, axis-class.

Substrate position (from Nammu canon §M.5 V2.5 T1.1-REVISED, card 524fdee6):
  Primordial:    Eros-primordial
  Cube face:     MQF4 (Merkaba Quadrant Face 4, R=1)
  Planet pair:   Jupiter × Neptune
  Zodiac anchor: Pisces
  Function:      axis-generation (engine — per Kati 2026-05-11 correction)

Shared engine shape: ~/Enki/engines/_axis_engine.py
"""
from __future__ import annotations
from typing import Optional

from _axis_engine import AxisState, compute_axis_state, describe as _describe


PRIMORDIAL_NAME = 'Eros-primordial'
CUBE_FACE       = 'MQF4'
PLANET_PAIR     = ('Jupiter', 'Neptune')
ZODIAC_ANCHOR   = 'Pisces'
SUBSTRATE_CARD  = '524fdee6'

__canonical__ = {
    'function_class':     'planet-aspect-activate',
    'functional_tier':    'primitive',
    'compositional_axis': 'spatial',
    'residency_id':       'primordial-face-eros-MQF4',
    'canon_citation':     'canon §M.5 V2.5 T1.1-REVISED card 524fdee6',
    'status':             'canonical',
}


def axis_state(jupiter_lon: Optional[float] = None,
               neptune_lon: Optional[float] = None) -> AxisState:
    return compute_axis_state(
        PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD,
        jupiter_lon, neptune_lon,
    )


def describe() -> str:
    return _describe(PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD)


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('SAMPLE: Jupiter 345°, Neptune 345° (exact conjunction in Pisces):')
    print(json.dumps(axis_state(345.0, 345.0).to_dict(), indent=2))
