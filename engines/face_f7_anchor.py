"""
F7 ANCHOR — inner-oct Mother-lateral face.

Per canon §10: F7 = ANCHOR (Earth, Mother lateral).
Vertices (canon §11 E3 V1-V3 shared with F1 + antipode-complement closure): V1, V3, V6.
Planets (canon §5): Venus, Saturn, Jupiter.

Composes 3 × `planet-aspect-activate`: Venus-Saturn + Saturn-Jupiter + Venus-Jupiter.

Mode = holding ground while the structure moves (anchoring).
"""
from __future__ import annotations
from typing import Optional

from _inner_oct_face_engine import (
    InnerOctFaceState, compute_inner_oct_face_state, describe_inner_oct_face
)


FACE_ID         = 'F7'
MODE            = 'ANCHOR'
ELEMENT         = 'Earth'
TET_POLARITY    = 'Mother'
APEX_OR_LATERAL = 'lateral'
VERTEX_IDS      = ['V1', 'V3', 'V6']
PLANETS         = ['Venus', 'Saturn', 'Jupiter']
SUBSTRATE_CARD  = None

__canonical__ = {
    'function_class':     'triangle-aspect-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-face-F7-anchor',
    'canon_citation':     'canon §10 (inner-oct faces) F7 ANCHOR Mother-lateral',
    'status':             'canonical',
}


def face_state(venus_lon:   Optional[float] = None,
               saturn_lon:  Optional[float] = None,
               jupiter_lon: Optional[float] = None) -> InnerOctFaceState:
    return compute_inner_oct_face_state(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
        venus_lon, saturn_lon, jupiter_lon,
    )


def describe() -> str:
    return describe_inner_oct_face(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
    )


if __name__ == '__main__':
    print(describe())
