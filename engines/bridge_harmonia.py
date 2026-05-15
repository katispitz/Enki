"""
Harmonia bridge engine — Enki.

Substrate position (per Lillu canon §M.5 V2.5 LOCK, card 52ad9413):
  Bridge:               Harmonia
  Icosidodec midpoint:  midpt(V2, V7)
  Parent vertices:      V2 (Aphrodite/Venus seat) ↔ V7 (Ares/Mars seat)
  Parent planet pair:   Venus × Mars
  Shell:                R=φ (icosidodec)
  Function class probe: cross-R-tier residency test for face-level function

Mythologically: Harmonia = daughter of Aphrodite (Venus) and Ares (Mars).
Substrate-correctly: the icosidodec midpoint BETWEEN their olympian vertices.

Shared shape: ~/Enki/engines/_bridge_engine.py
"""
from __future__ import annotations
from typing import Optional

from _bridge_engine import BridgeState, compute_bridge_state, describe_bridge


BRIDGE_NAME       = 'Harmonia'
ICOSIDODEC_ANCHOR = 'midpt(V2, V7)'
PARENT_VERTICES   = ('V2', 'V7')
PARENT_PLANETS    = ('Venus', 'Mars')
SUBSTRATE_CARD    = '52ad9413'

__canonical__ = {
    'function_class':     'planet-aspect-activate',
    'functional_tier':    'primitive',
    'compositional_axis': 'spatial',
    'residency_id':       'bridge-harmonia-midptV2V7',
    'canon_citation':     'canon §M.5 V2.5 LOCK card 52ad9413',
    'status':             'canonical',
}


def bridge_state(venus_lon: Optional[float] = None,
                 mars_lon:  Optional[float] = None) -> BridgeState:
    return compute_bridge_state(
        BRIDGE_NAME, ICOSIDODEC_ANCHOR, PARENT_VERTICES, PARENT_PLANETS, SUBSTRATE_CARD,
        venus_lon, mars_lon,
    )


def describe() -> str:
    return describe_bridge(BRIDGE_NAME, ICOSIDODEC_ANCHOR, PARENT_VERTICES,
                           PARENT_PLANETS, SUBSTRATE_CARD)


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('FROZEN:')
    print(json.dumps(bridge_state().to_dict(), indent=2))
    print()
    print('SAMPLE: Venus + Mars at exact conjunction (both 60°):')
    print(json.dumps(bridge_state(60.0, 60.0).to_dict(), indent=2))
