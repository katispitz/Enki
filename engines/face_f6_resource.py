"""
F6 RESOURCE — inner-oct Father-lateral face.

Per canon §10: F6 = RESOURCE (Air, Father lateral).
Vertices (canon §11 E5 V5-V6 shared with F8): V3, V5, V6.
Planets (canon §5): Saturn, Mars, Jupiter.

Composes 3 × `planet-aspect-activate`: Saturn-Mars + Mars-Jupiter + Saturn-Jupiter.

Mode = naming what fuels the cycle (resourcing).
"""
from __future__ import annotations
from typing import Optional

from _inner_oct_face_engine import (
    InnerOctFaceState, compute_inner_oct_face_state, describe_inner_oct_face
)


FACE_ID         = 'F6'
MODE            = 'RESOURCE'
ELEMENT         = 'Air'
TET_POLARITY    = 'Father'
APEX_OR_LATERAL = 'lateral'
VERTEX_IDS      = ['V3', 'V5', 'V6']
PLANETS         = ['Saturn', 'Mars', 'Jupiter']
SUBSTRATE_CARD  = None

__canonical__ = {
    'function_class':     'triangle-aspect-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-face-F6-resource',
    'canon_citation':     'canon §10 (inner-oct faces) F6 RESOURCE Father-lateral',
    'status':             'canonical',
}


def face_state(saturn_lon:  Optional[float] = None,
               mars_lon:    Optional[float] = None,
               jupiter_lon: Optional[float] = None) -> InnerOctFaceState:
    return compute_inner_oct_face_state(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
        saturn_lon, mars_lon, jupiter_lon,
    )


def describe() -> str:
    return describe_inner_oct_face(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
    )


if __name__ == '__main__':
    print(describe())
