"""
Erichthonius bridge engine — Enki.

Substrate position (per Nammu canon §M.5 V2.5 LOCK, card 3de9d703):
  Bridge:               Erichthonius
  Icosidodec midpoint:  midpt(V4, V8)
  Parent vertices:      V4 (Athena/Saturn seat) ↔ V8 (Hephaestus/Uranus seat)
  Parent planet pair:   Saturn × Uranus
  Shell:                R=φ (icosidodec)

Mythologically: Erichthonius = born of Hephaestus's seed + Athena (without
contact; substrate-honest: emergence at midpoint between their vertices).

Shared shape: ~/Enki/engines/_bridge_engine.py
"""
from __future__ import annotations
from typing import Optional

from _bridge_engine import BridgeState, compute_bridge_state, describe_bridge


BRIDGE_NAME       = 'Erichthonius'
ICOSIDODEC_ANCHOR = 'midpt(V4, V8)'
PARENT_VERTICES   = ('V4', 'V8')
PARENT_PLANETS    = ('Saturn', 'Uranus')
SUBSTRATE_CARD    = '3de9d703'

__canonical__ = {
    'function_class':     'planet-aspect-activate',
    'functional_tier':    'primitive',
    'compositional_axis': 'spatial',
    'residency_id':       'bridge-erichthonius-midptV4V8',
    'canon_citation':     'canon §M.5 V2.5 LOCK card 3de9d703',
    'status':             'canonical',
}


def bridge_state(saturn_lon: Optional[float] = None,
                 uranus_lon: Optional[float] = None) -> BridgeState:
    return compute_bridge_state(
        BRIDGE_NAME, ICOSIDODEC_ANCHOR, PARENT_VERTICES, PARENT_PLANETS, SUBSTRATE_CARD,
        saturn_lon, uranus_lon,
    )


def describe() -> str:
    return describe_bridge(BRIDGE_NAME, ICOSIDODEC_ANCHOR, PARENT_VERTICES,
                           PARENT_PLANETS, SUBSTRATE_CARD)


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('SAMPLE: Saturn + Uranus at exact conjunction (both 280°):')
    print(json.dumps(bridge_state(280.0, 280.0).to_dict(), indent=2))
