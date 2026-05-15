"""
Neptune-axis trine — Enki.

3 Primordials anchored by Neptune, all 3 zodiac-anchored in Water-trine signs:
  - Nyx       : MQF3 / Moon × Neptune    / Cancer
  - Eros-prim : MQF4 / Jupiter × Neptune / Pisces
  - Tartarus  : MQF5 / Mars × Neptune    / Scorpio

Substrate-honest: Neptune is the SHARED anchor; the other planet (Moon /
Jupiter / Mars) is the FACE-distinct identifier per Primordial. Water element
trine (Cancer/Pisces/Scorpio) is the zodiac-quality signature.

Shared shape: ~/Enki/engines/_trine_engine.py
"""
from __future__ import annotations
from typing import Optional

import primordial_nyx      as _nyx
import primordial_eros     as _eros
import primordial_tartarus as _tartarus
from _trine_engine import TrineState, compute_trine_state, describe_trine


TRINE_NAME      = 'Neptune-axis'
OUTER_ANCHOR    = 'Neptune'
ELEMENT         = 'Water'
PRIMORDIALS     = ['Nyx', 'Eros-primordial', 'Tartarus']
CUBE_FACES      = ['MQF3', 'MQF4', 'MQF5']
ZODIAC_SIGNS    = ['Cancer', 'Pisces', 'Scorpio']
SUBSTRATE_CARDS = ['ac6c221d', '524fdee6', 'f76168b6']


def trine_state(moon_lon:    Optional[float] = None,
                jupiter_lon: Optional[float] = None,
                mars_lon:    Optional[float] = None,
                neptune_lon: Optional[float] = None) -> TrineState:
    """Compute Neptune-axis trine state.

    Neptune is the SHARED anchor — supplied once, threaded into all 3 engines.
    """
    states = [
        _nyx.axis_state(moon_lon, neptune_lon),
        _eros.axis_state(jupiter_lon, neptune_lon),
        _tartarus.axis_state(mars_lon, neptune_lon),
    ]
    return compute_trine_state(TRINE_NAME, OUTER_ANCHOR, ELEMENT, states)


def describe() -> str:
    return describe_trine(
        TRINE_NAME, OUTER_ANCHOR, ELEMENT,
        PRIMORDIALS, CUBE_FACES, ZODIAC_SIGNS, SUBSTRATE_CARDS,
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('SAMPLE: Neptune @ 345° + Moon @ 100° (Nyx ≠ conj), Jupiter @ 345° (Eros exact conj), Mars @ 165° (Tartarus 180° opp):')
    print(json.dumps(trine_state(100.0, 345.0, 165.0, 345.0).to_dict(), indent=2)[-900:])
