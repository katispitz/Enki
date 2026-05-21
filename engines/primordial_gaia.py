"""
Gaia primordial axis engine — Enki.

Substrate position (from Nammu canon §M.5 V2.5 T1.1-REVISED, card a64c8127):
  Primordial:    Gaia
  Cube face:     MQF0 (Merkaba Quadrant Face 0, R=1)
  Planet pair:   Venus × Pluto
  Zodiac anchor: Taurus
  Function:      axis-generation (engine — per Kati 2026-05-11 correction)

Shared engine shape: ~/Enki/engines/_axis_engine.py
"""
from __future__ import annotations
from typing import Optional

from _axis_engine import AxisState, compute_axis_state, describe as _describe


PRIMORDIAL_NAME = 'Gaia'
CUBE_FACE       = 'MQF0'
PLANET_PAIR     = ('Venus', 'Pluto')
ZODIAC_ANCHOR   = 'Taurus'
SUBSTRATE_CARD  = 'a64c8127'

# Per placement_rules.md V2.7 §ENGINE-SCHEMA DISCIPLINE
__canonical__ = {
    'function_class':     'planet-aspect-activate',
    'functional_tier':    'primitive',
    'compositional_axis': 'spatial',
    'residency_id':       'primordial-face-gaia-MQF0',
    'canon_citation':     'canon §M.5 V2.5 T1.1-REVISED card a64c8127',
    'status':             'canonical',
}


def axis_state(venus_lon: Optional[float] = None,
               pluto_lon: Optional[float] = None) -> AxisState:
    return compute_axis_state(
        PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD,
        venus_lon, pluto_lon,
    )


def describe() -> str:
    return _describe(PRIMORDIAL_NAME, CUBE_FACE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD)


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('FROZEN:')
    print(json.dumps(axis_state().to_dict(), indent=2))
    print()
    print('SAMPLE: Venus + Pluto exact conjunction at 270° (Capricorn 0°):')
    print(json.dumps(axis_state(270.0, 270.0).to_dict(), indent=2))
    print()
    print('SAMPLE: Venus 30°, Pluto 210° (opposition):')
    print(json.dumps(axis_state(30.0, 210.0).to_dict(), indent=2))
    print()
    print('SAMPLE: Venus 0°, Pluto 122° (trine, 2° orb):')
    print(json.dumps(axis_state(0.0, 122.0).to_dict(), indent=2))
