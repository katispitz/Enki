"""
F2 FEEDBACK — inner-oct Mother-lateral face.

Per canon §10: F2 = FEEDBACK (Earth, Mother lateral).
Vertices (canon §11 E1 V1-V2 shared with F1 + cross-apex closure): V1, V2, V4.
Planets (canon §5): Venus, Mercury, Moon.

Composes 3 × `planet-aspect-activate`: Venus-Mercury + Mercury-Moon + Venus-Moon.

Mode = returning motion back to its origin (feedback-reflecting).
"""
from __future__ import annotations
from typing import Optional

from _inner_oct_face_engine import (
    InnerOctFaceState, compute_inner_oct_face_state, describe_inner_oct_face
)


FACE_ID         = 'F2'
MODE            = 'FEEDBACK'
ELEMENT         = 'Earth'
TET_POLARITY    = 'Mother'
APEX_OR_LATERAL = 'lateral'
VERTEX_IDS      = ['V1', 'V2', 'V4']
PLANETS         = ['Venus', 'Mercury', 'Moon']
SUBSTRATE_CARD  = None

__canonical__ = {
    'function_class':     'triangle-aspect-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-face-F2-feedback',
    'canon_citation':     'canon §10 (inner-oct faces) F2 FEEDBACK Mother-lateral',
    'status':             'canonical',
}


def face_state(venus_lon:   Optional[float] = None,
               mercury_lon: Optional[float] = None,
               moon_lon:    Optional[float] = None) -> InnerOctFaceState:
    return compute_inner_oct_face_state(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
        venus_lon, mercury_lon, moon_lon,
    )


def describe() -> str:
    return describe_inner_oct_face(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
    )


if __name__ == '__main__':
    print(describe())
