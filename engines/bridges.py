"""
Bridges registry — Enki.

Aggregates the 3 V2.5-locked icosidodec-midpoint bridges. Substrate-honest
read of the bridge primitive-class at R=φ shell.

Substrate position table:

| Bridge          | Icosidodec midpt | Parent vertices | Parent planets   | Card     |
|-----------------|------------------|-----------------|------------------|----------|
| Harmonia        | midpt(V2, V7)    | V2 ↔ V7         | Venus × Mars     | 52ad9413 |
| Hermaphroditus  | midpt(V3, V2)    | V3 ↔ V2         | Mercury × Venus  | 91697158 |
| Erichthonius    | midpt(V4, V8)    | V4 ↔ V8         | Saturn × Uranus  | 3de9d703 |

NOTE: Persephone is also a bridge per V2.5 lock but is NOT a midpoint-compound
bridge (she's a seasonal/transit bridge between Olympian and Chthonic strata,
substrate-anchored at Pluto, not at an icosidodec midpoint). Excluded here.

Cross-R-tier residency probe (FINDINGS_005): bridge function-shape matches
Primordial face-engine shape exactly except for shell-anchor + position-anchor.
This MATCHES the cross-R-tier residency required to graduate the face-level
function-name to canonical under Athena lock-by-redundancy criterion.
"""
from __future__ import annotations

import bridge_harmonia        as _harmonia
import bridge_hermaphroditus  as _hermaphroditus
import bridge_erichthonius    as _erichthonius


BRIDGES = [_harmonia, _hermaphroditus, _erichthonius]

BY_NAME = {
    b.BRIDGE_NAME: b for b in BRIDGES
}

BY_PARENT_PAIR = {
    frozenset(b.PARENT_PLANETS): b for b in BRIDGES
}


def get(key: str):
    if key in BY_NAME:
        return BY_NAME[key]
    raise KeyError(f"No bridge matches {key!r}")


def get_by_parent_planets(planet_a: str, planet_b: str):
    return BY_PARENT_PAIR.get(frozenset((planet_a, planet_b)))


def all_frozen() -> list:
    return [b.bridge_state().to_dict() for b in BRIDGES]


def describe_all() -> str:
    return "\n".join(b.describe() for b in BRIDGES)


if __name__ == '__main__':
    import json
    print(describe_all())
    print()
    print(f"Bridges registered: {len(BRIDGES)}")
    print()
    print("All frozen states (substrate-only):")
    for state in all_frozen():
        print(f"  {state['bridge_name']:18s} {state['icosidodec_anchor']:18s}  "
              f"{state['parent_planet_pair'][0]:7s} × {state['parent_planet_pair'][1]:7s}  "
              f"shell R={state['shell']}")
