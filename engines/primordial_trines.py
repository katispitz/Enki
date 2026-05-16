"""
Primordial trines registry — Enki.

Aggregates the 2 outer-planet-anchored trine engines. Substantiates OQ-PLUTO-
NEPTUNE-PARTITION (FINDINGS_002+003): the 6 Primordials organize into 2 trines
of 3, partitioned by outer-planet anchor.

| Trine        | Anchor   | Element | Faces           | Members                          |
|--------------|----------|---------|-----------------|----------------------------------|
| Pluto-axis   | Pluto    | Earth   | MQF0/1/2        | Gaia + Chaos + Erebus            |
| Neptune-axis | Neptune  | Water   | MQF3/4/5        | Nyx + Eros-primordial + Tartarus |

This is a NEW primitive-class at the same R=1 shell, cardinality 2 (lower than
pair-class cardinality 3 and face-class cardinality 6). Substrate-cascade:

  face-class (6)  ⇒  pair-class (3, antipodal)  ⇒  trine-class (2, outer-anchored)

Three primitive-class levels at R=1 shell, each with distinct function-name
candidates pending council ratification.
"""
from __future__ import annotations

import trine_pluto_axis    as _pluto_trine
import trine_neptune_axis  as _neptune_trine


TRINES = [_pluto_trine, _neptune_trine]

BY_NAME = {
    t.TRINE_NAME: t for t in TRINES
}

BY_ANCHOR = {
    t.OUTER_ANCHOR: t for t in TRINES
}

BY_ELEMENT = {
    t.ELEMENT: t for t in TRINES
}

# Quick lookup by Primordial name → its trine module
BY_PRIMORDIAL = {}
for t in TRINES:
    for name in t.PRIMORDIALS:
        BY_PRIMORDIAL[name] = t


def get_trine(primordial_name: str):
    """Return the trine-module containing the given Primordial."""
    return BY_PRIMORDIAL[primordial_name]


def all_frozen() -> list:
    return [t.trine_state().to_dict() for t in TRINES]


def describe_all() -> str:
    return "\n\n".join(t.describe() for t in TRINES)


if __name__ == '__main__':
    print(describe_all())
    print()
    print(f"Trines registered: {len(TRINES)}")
    print()
    print("Quick lookup by Primordial name:")
    for name, trine in BY_PRIMORDIAL.items():
        print(f"  {name:18s} → trine {trine.TRINE_NAME!r}")
    print()
    print("All frozen trine snapshots:")
    for state in all_frozen():
        print(f"  {state['trine_name']:14s} {state['outer_anchor']:8s} {state['element']:5s} "
              f"{state['cube_faces']}  {state['zodiac_signs']}")
