"""
Primordials registry — Enki.

Aggregates the 6 Primordial axis-generation engines. Substrate-honest read of
the full R=1 cube-face residency class.

Per V2.5 T1.1-REVISED (Nammu council 2026-05-10) + Kati 2026-05-11 engine-
correction: the 6 Primordials at R=1 cube-faces are axis-generation engines.
Each takes a planet-pair, returns an AxisState (frozen or live).

Substrate position table:

| Primordial      | Face | Planet pair       | Zodiac anchor | Card     |
|-----------------|------|-------------------|---------------|----------|
| Gaia            | MQF0 | Venus × Pluto     | Taurus        | a64c8127 |
| Chaos           | MQF1 | Mercury × Pluto   | Virgo         | 2f2bd039 |
| Erebus          | MQF2 | Saturn × Pluto    | Capricorn     | 2391bb9f |
| Nyx             | MQF3 | Moon × Neptune    | Cancer        | ac6c221d |
| Eros-primordial | MQF4 | Jupiter × Neptune | Pisces        | 524fdee6 |
| Tartarus        | MQF5 | Mars × Neptune    | Scorpio       | f76168b6 |

This module imports each Primordial engine and exposes them as a registry
addressable by name OR by cube-face OR by planet-pair.
"""
from __future__ import annotations

import primordial_gaia       as _gaia
import primordial_chaos      as _chaos
import primordial_erebus     as _erebus
import primordial_nyx        as _nyx
import primordial_eros       as _eros
import primordial_tartarus   as _tartarus



# Registry — ordered by cube face index (MQF0..MQF5)
PRIMORDIALS = [_gaia, _chaos, _erebus, _nyx, _eros, _tartarus]

BY_NAME = {
    p.PRIMORDIAL_NAME: p for p in PRIMORDIALS
}

BY_FACE = {
    p.CUBE_FACE: p for p in PRIMORDIALS
}

BY_PLANET_PAIR = {
    frozenset(p.PLANET_PAIR): p for p in PRIMORDIALS
}

BY_ZODIAC = {
    p.ZODIAC_ANCHOR: p for p in PRIMORDIALS
}


def get(key: str):
    """Lookup a Primordial engine by name, face, or zodiac anchor.

    Substrate-honest: case-sensitive. Raises KeyError if not found.
    """
    if key in BY_NAME:    return BY_NAME[key]
    if key in BY_FACE:    return BY_FACE[key]
    if key in BY_ZODIAC:  return BY_ZODIAC[key]
    raise KeyError(f"No primordial matches {key!r} — try name/face/zodiac")


def get_by_pair(planet_a: str, planet_b: str):
    """Lookup by planet pair (order-independent). Returns None if no match."""
    pair = frozenset((planet_a, planet_b))
    return BY_PLANET_PAIR.get(pair)


def all_frozen() -> list:
    """Return frozen AxisStates for all 6 — pure substrate snapshot, no ephemeris."""
    return [p.axis_state().to_dict() for p in PRIMORDIALS]


def describe_all() -> str:
    """Substrate-honest table of all 6 Primordial substrate positions."""
    return "\n".join(p.describe() for p in PRIMORDIALS)


if __name__ == '__main__':
    print(describe_all())
    print()
    print(f"Registry size: {len(PRIMORDIALS)}")
    print(f"By name:    {list(BY_NAME.keys())}")
    print(f"By face:    {list(BY_FACE.keys())}")
    print(f"By zodiac:  {list(BY_ZODIAC.keys())}")
    print()
    print("All frozen states:")
    for state in all_frozen():
        print(f"  {state['primordial']:18s} {state['cube_face']}  "
              f"{state['planet_pair'][0]:8s} × {state['planet_pair'][1]:8s}  "
              f"→ {state['zodiac_anchor']}")
