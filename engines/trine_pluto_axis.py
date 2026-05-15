"""
Pluto-axis trine — Enki.

3 Primordials anchored by Pluto, all 3 zodiac-anchored in Earth-trine signs:
  - Gaia    : MQF0 / Venus × Pluto    / Taurus
  - Chaos   : MQF1 / Mercury × Pluto  / Virgo
  - Erebus  : MQF2 / Saturn × Pluto   / Capricorn

Substrate-honest: Pluto is the SHARED anchor; the other planet (Venus / Mercury /
Saturn) is the FACE-distinct identifier per Primordial. Earth element trine
(Taurus/Virgo/Capricorn) is the zodiac-quality signature.

Shared shape: ~/Enki/engines/_trine_engine.py
"""
from __future__ import annotations
from typing import Optional

import primordial_gaia   as _gaia
import primordial_chaos  as _chaos
import primordial_erebus as _erebus
from _trine_engine import TrineState, compute_trine_state, describe_trine


TRINE_NAME      = 'Pluto-axis'
OUTER_ANCHOR    = 'Pluto'
ELEMENT         = 'Earth'
PRIMORDIALS     = ['Gaia', 'Chaos', 'Erebus']
CUBE_FACES      = ['MQF0', 'MQF1', 'MQF2']
ZODIAC_SIGNS    = ['Taurus', 'Virgo', 'Capricorn']
SUBSTRATE_CARDS = ['a64c8127', '2f2bd039', '2391bb9f']


def trine_state(venus_lon:   Optional[float] = None,
                mercury_lon: Optional[float] = None,
                saturn_lon:  Optional[float] = None,
                pluto_lon:   Optional[float] = None) -> TrineState:
    """Compute Pluto-axis trine state.

    Pluto is the SHARED anchor — supplied once, threaded into all 3 face engines.
    All 4 lons supplied → live state. All 4 None → frozen state.
    Partial input → ValueError (cascades from face-engines).
    """
    states = [
        _gaia.axis_state(venus_lon, pluto_lon),
        _chaos.axis_state(mercury_lon, pluto_lon),
        _erebus.axis_state(saturn_lon, pluto_lon),
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
    print('FROZEN:')
    print(json.dumps(trine_state().to_dict(), indent=2)[:500])
    print('...')
    print()
    print('SAMPLE: Pluto @ 270° + Venus @ 270° (Gaia exact conj), Mercury @ 165° (Chaos quincunx ≈ 105°, not in 6° orb), Saturn @ 90° (Erebus 180° opp):')
    print(json.dumps(trine_state(270.0, 165.0, 90.0, 270.0).to_dict(), indent=2)[-800:])
