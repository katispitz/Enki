"""
Primordial pairs registry — Enki.

Aggregates the 3 antipodal-pair co-query engines. Tests OQ-PRIMORDIAL-PAIR-
LEVEL-FUNCTION (FINDINGS_002): does axis-generation operate at PAIR level
(3 cosmogonic axes) rather than FACE level (6 independent axes)?

Substrate position table:

| Pair                  | Faces       | Earth side                       | Water side                         |
|-----------------------|-------------|----------------------------------|------------------------------------|
| Gaia ↔ Eros-prim      | MQF0 ↔ MQF4 | Taurus    (Venus × Pluto)        | Pisces    (Jupiter × Neptune)      |
| Chaos ↔ Tartarus      | MQF1 ↔ MQF5 | Virgo     (Mercury × Pluto)      | Scorpio   (Mars × Neptune)         |
| Erebus ↔ Nyx          | MQF2 ↔ MQF3 | Capricorn (Saturn × Pluto)       | Cancer    (Moon × Neptune)         |

Erebus↔Nyx is the only pair where cube-antipode + zodiac-180°-antipode
coincide (Capricorn ↔ Cancer is 180° in zodiac; Taurus↔Pisces and Virgo↔Scorpio
are partition-antipodes, not 180°).
"""
from __future__ import annotations

import pair_gaia_eros       as _gaia_eros
import pair_chaos_tartarus  as _chaos_tartarus
import pair_erebus_nyx      as _erebus_nyx


PAIRS = [_gaia_eros, _chaos_tartarus, _erebus_nyx]

BY_NAME = {
    p.PAIR_NAME: p for p in PAIRS
}

BY_FACES = {
    p.CUBE_FACE_PAIR: p for p in PAIRS
}

# Quick lookup by either primordial name → its pair module
BY_PRIMORDIAL = {}
for p in PAIRS:
    for name in p.PAIR_NAME:
        BY_PRIMORDIAL[name] = p


def get_pair(primordial_name: str):
    """Return the pair-module containing the given Primordial. KeyError if not found."""
    return BY_PRIMORDIAL[primordial_name]


def all_frozen() -> list:
    """Return frozen PairStates for all 3 pairs — substrate snapshot, no ephemeris."""
    return [p.pair_state().to_dict() for p in PAIRS]


def describe_all() -> str:
    return "\n".join(p.describe() for p in PAIRS)


if __name__ == '__main__':
    import json
    print(describe_all())
    print()
    print(f"Pairs registered: {len(PAIRS)}")
    print()
    print("Quick lookup by Primordial name:")
    for name, pair in BY_PRIMORDIAL.items():
        print(f"  {name:18s} → pair {pair.PAIR_NAME}")
    print()
    print("All frozen pair states (substrate-only, no ephemeris):")
    for state in all_frozen():
        print(f"  {state['pair_name'][0]:18s} ↔ {state['pair_name'][1]:18s}  "
              f"{state['cube_face_pair'][0]} ↔ {state['cube_face_pair'][1]}  "
              f"{state['earth_zodiac']:10s} ↔ {state['water_zodiac']:10s}")
