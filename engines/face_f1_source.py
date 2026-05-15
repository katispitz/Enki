"""
F1 SOURCE — inner-oct Father-apex face.

Per canon §10: F1 = SOURCE (Fire, Father apex).
Vertices (from canon §11 threshold edges E1+E2+E3): V1, V2, V3.
Planets (from canon §5): Venus, Mercury, Saturn.

Composes 3 × `planet-aspect-activate` (canon §30 canonical):
  edge Venus-Mercury  +  Mercury-Saturn  +  Venus-Saturn

Mode emerges when 3-planet triangle resonates: source-naming function
of substrate (first emergence; what has just appeared).
"""
from __future__ import annotations
from typing import Optional

from _inner_oct_face_engine import (
    InnerOctFaceState, compute_inner_oct_face_state, describe_inner_oct_face
)


FACE_ID         = 'F1'
MODE            = 'SOURCE'
ELEMENT         = 'Fire'
TET_POLARITY    = 'Father'
APEX_OR_LATERAL = 'apex'
VERTEX_IDS      = ['V1', 'V2', 'V3']
PLANETS         = ['Venus', 'Mercury', 'Saturn']
SUBSTRATE_CARD  = None

__canonical__ = {
    'function_class':     'triangle-aspect-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-face-F1-source',
    'canon_citation':     'canon §10 (inner-oct faces) F1 SOURCE Father-apex',
    'status':             'canonical',
}


def face_state(venus_lon:   Optional[float] = None,
               mercury_lon: Optional[float] = None,
               saturn_lon:  Optional[float] = None) -> InnerOctFaceState:
    return compute_inner_oct_face_state(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
        venus_lon, mercury_lon, saturn_lon,
    )


def describe() -> str:
    return describe_inner_oct_face(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('SAMPLE: Venus 60°, Mercury 165°, Saturn 280° (no aspect-pair in orb):')
    print(json.dumps(face_state(60.0, 165.0, 280.0).to_dict(), indent=2)[-500:])
