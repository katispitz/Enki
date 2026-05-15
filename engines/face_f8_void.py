"""
F8 VOID — inner-oct Mother-apex face.

Per canon §10: F8 = VOID (Water, Mother apex).
Vertices (canon §11 E4+E5+E6 union): V4, V5, V6.
Planets (canon §5): Moon, Mars, Jupiter.

Composes 3 × `planet-aspect-activate`: Moon-Mars + Mars-Jupiter + Moon-Jupiter.

Mode = naming what dissolves to make room (voiding).
Antipode of F1 SOURCE.
"""
from __future__ import annotations
from typing import Optional

from _inner_oct_face_engine import (
    InnerOctFaceState, compute_inner_oct_face_state, describe_inner_oct_face
)


FACE_ID         = 'F8'
MODE            = 'VOID'
ELEMENT         = 'Water'
TET_POLARITY    = 'Mother'
APEX_OR_LATERAL = 'apex'
VERTEX_IDS      = ['V4', 'V5', 'V6']
PLANETS         = ['Moon', 'Mars', 'Jupiter']
SUBSTRATE_CARD  = None

__canonical__ = {
    'function_class':     'triangle-aspect-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-face-F8-void',
    'canon_citation':     'canon §10 (inner-oct faces) F8 VOID Mother-apex',
    'status':             'canonical',
}


def face_state(moon_lon:    Optional[float] = None,
               mars_lon:    Optional[float] = None,
               jupiter_lon: Optional[float] = None) -> InnerOctFaceState:
    return compute_inner_oct_face_state(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
        moon_lon, mars_lon, jupiter_lon,
    )


def describe() -> str:
    return describe_inner_oct_face(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
    )


if __name__ == '__main__':
    print(describe())
