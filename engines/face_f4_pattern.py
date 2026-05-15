"""
F4 PATTERN — inner-oct Father-lateral face.

Per canon §10: F4 = PATTERN (Air, Father lateral).
Vertices (canon §11 E4 V4-V5 shared with F8): V2, V4, V5.
Planets (canon §5): Mercury, Moon, Mars.

Composes 3 × `planet-aspect-activate`: Mercury-Moon + Moon-Mars + Mercury-Mars.

Mode = recognizing form across the arc (patterning).
"""
from __future__ import annotations
from typing import Optional

from _inner_oct_face_engine import (
    InnerOctFaceState, compute_inner_oct_face_state, describe_inner_oct_face
)


FACE_ID         = 'F4'
MODE            = 'PATTERN'
ELEMENT         = 'Air'
TET_POLARITY    = 'Father'
APEX_OR_LATERAL = 'lateral'
VERTEX_IDS      = ['V2', 'V4', 'V5']
PLANETS         = ['Mercury', 'Moon', 'Mars']
SUBSTRATE_CARD  = None

__canonical__ = {
    'function_class':     'triangle-aspect-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-face-F4-pattern',
    'canon_citation':     'canon §10 (inner-oct faces) F4 PATTERN Father-lateral',
    'status':             'canonical',
}


def face_state(mercury_lon: Optional[float] = None,
               moon_lon:    Optional[float] = None,
               mars_lon:    Optional[float] = None) -> InnerOctFaceState:
    return compute_inner_oct_face_state(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
        mercury_lon, moon_lon, mars_lon,
    )


def describe() -> str:
    return describe_inner_oct_face(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
    )


if __name__ == '__main__':
    print(describe())
