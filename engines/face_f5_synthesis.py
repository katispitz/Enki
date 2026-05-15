"""
F5 SYNTHESIS — inner-oct Mother-lateral face.

Per canon §10: F5 = SYNTHESIS (Earth, Mother lateral).
Vertices (canon §11 E2 V2-V3 shared with F1 + antipode-complement closure): V2, V3, V5.
Planets (canon §5): Mercury, Saturn, Mars.

Composes 3 × `planet-aspect-activate`: Mercury-Saturn + Saturn-Mars + Mercury-Mars.

Mode = binding disparate strands into coherence (synthesizing).
"""
from __future__ import annotations
from typing import Optional

from _inner_oct_face_engine import (
    InnerOctFaceState, compute_inner_oct_face_state, describe_inner_oct_face
)


FACE_ID         = 'F5'
MODE            = 'SYNTHESIS'
ELEMENT         = 'Earth'
TET_POLARITY    = 'Mother'
APEX_OR_LATERAL = 'lateral'
VERTEX_IDS      = ['V2', 'V3', 'V5']
PLANETS         = ['Mercury', 'Saturn', 'Mars']
SUBSTRATE_CARD  = None

__canonical__ = {
    'function_class':     'triangle-aspect-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-face-F5-synthesis',
    'canon_citation':     'canon §10 (inner-oct faces) F5 SYNTHESIS Mother-lateral',
    'status':             'canonical',
}


def face_state(mercury_lon: Optional[float] = None,
               saturn_lon:  Optional[float] = None,
               mars_lon:    Optional[float] = None) -> InnerOctFaceState:
    return compute_inner_oct_face_state(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
        mercury_lon, saturn_lon, mars_lon,
    )


def describe() -> str:
    return describe_inner_oct_face(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
    )


if __name__ == '__main__':
    print(describe())
