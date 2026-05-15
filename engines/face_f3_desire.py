"""
F3 DESIRE — inner-oct Father-lateral face.

Per canon §10: F3 = DESIRE (Air, Father lateral).
Vertices (canon §11 E6 V4-V6 shared with F8 + cross-apex closure): V1, V4, V6.
Planets (canon §5): Venus, Moon, Jupiter.

Composes 3 × `planet-aspect-activate`: Venus-Moon + Moon-Jupiter + Venus-Jupiter.

Mode = naming what draws structure outward (desiring).
"""
from __future__ import annotations
from typing import Optional

from _inner_oct_face_engine import (
    InnerOctFaceState, compute_inner_oct_face_state, describe_inner_oct_face
)


FACE_ID         = 'F3'
MODE            = 'DESIRE'
ELEMENT         = 'Air'
TET_POLARITY    = 'Father'
APEX_OR_LATERAL = 'lateral'
VERTEX_IDS      = ['V1', 'V4', 'V6']
PLANETS         = ['Venus', 'Moon', 'Jupiter']
SUBSTRATE_CARD  = None

__canonical__ = {
    'function_class':     'triangle-aspect-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-face-F3-desire',
    'canon_citation':     'canon §10 (inner-oct faces) F3 DESIRE Father-lateral',
    'status':             'canonical',
}


def face_state(venus_lon:   Optional[float] = None,
               moon_lon:    Optional[float] = None,
               jupiter_lon: Optional[float] = None) -> InnerOctFaceState:
    return compute_inner_oct_face_state(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
        venus_lon, moon_lon, jupiter_lon,
    )


def describe() -> str:
    return describe_inner_oct_face(
        FACE_ID, MODE, ELEMENT, TET_POLARITY, APEX_OR_LATERAL,
        VERTEX_IDS, PLANETS, SUBSTRATE_CARD,
    )


if __name__ == '__main__':
    print(describe())
