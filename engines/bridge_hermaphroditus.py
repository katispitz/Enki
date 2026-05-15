"""
Hermaphroditus bridge engine — Enki.

Substrate position (per Lillu canon §M.5 V2.5 LOCK, card 91697158):
  Bridge:               Hermaphroditus
  Icosidodec midpoint:  midpt(V3, V2)
  Parent vertices:      V3 (Hermes/Mercury seat) ↔ V2 (Aphrodite/Venus seat)
  Parent planet pair:   Mercury × Venus
  Shell:                R=φ (icosidodec)

Mythologically: Hermaphroditus = child of Hermes (Mercury) and Aphrodite (Venus).
Substrate-correctly: midpoint between their adjacent Olympian vertices.

Shared shape: ~/Enki/engines/_bridge_engine.py
"""
from __future__ import annotations
from typing import Optional

from _bridge_engine import BridgeState, compute_bridge_state, describe_bridge


BRIDGE_NAME       = 'Hermaphroditus'
ICOSIDODEC_ANCHOR = 'midpt(V3, V2)'
PARENT_VERTICES   = ('V3', 'V2')
PARENT_PLANETS    = ('Mercury', 'Venus')
SUBSTRATE_CARD    = '91697158'

__canonical__ = {
    'function_class':     'planet-aspect-activate',
    'functional_tier':    'primitive',
    'compositional_axis': 'spatial',
    'residency_id':       'bridge-hermaphroditus-midptV3V2',
    'canon_citation':     'canon §M.5 V2.5 LOCK card 91697158',
    'status':             'canonical',
}


def bridge_state(mercury_lon: Optional[float] = None,
                 venus_lon:   Optional[float] = None) -> BridgeState:
    return compute_bridge_state(
        BRIDGE_NAME, ICOSIDODEC_ANCHOR, PARENT_VERTICES, PARENT_PLANETS, SUBSTRATE_CARD,
        mercury_lon, venus_lon,
    )


def describe() -> str:
    return describe_bridge(BRIDGE_NAME, ICOSIDODEC_ANCHOR, PARENT_VERTICES,
                           PARENT_PLANETS, SUBSTRATE_CARD)


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('SAMPLE: Mercury + Venus at exact conjunction (both 165°):')
    print(json.dumps(bridge_state(165.0, 165.0).to_dict(), indent=2))
