"""
F1 SOURCE ↔ F8 VOID — inner-oct apex antipodal pair.

Fire-Father ↔ Water-Mother axis (the primary inner-oct polarity).
Vertex union: V1+V2+V3 ∪ V4+V5+V6 = all 6 sign-rulership vertices.
Planet union: all 6 sign-rulership planets.

Composes from 2 face engines (each composing 3 × planet-aspect-activate).
"""
from __future__ import annotations
from typing import Optional

import face_f1_source as _f1
import face_f8_void   as _f8
from _inner_oct_pair_engine import (
    InnerOctPairState, compute_inner_oct_pair_state, describe_inner_oct_pair
)


PAIR_NAME = ('SOURCE', 'VOID')

__canonical__ = {
    'function_class':     'polarity-define',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-pair-source-void',
    'canon_citation':     'canon §10 (inner-oct faces) + §M.5 / F1↔F8 apex pair',
    'status':             'canonical',
}


def pair_state(venus_lon:   Optional[float] = None,
               mercury_lon: Optional[float] = None,
               saturn_lon:  Optional[float] = None,
               moon_lon:    Optional[float] = None,
               mars_lon:    Optional[float] = None,
               jupiter_lon: Optional[float] = None) -> InnerOctPairState:
    f1_state = _f1.face_state(venus_lon, mercury_lon, saturn_lon)
    f8_state = _f8.face_state(moon_lon, mars_lon, jupiter_lon)
    return compute_inner_oct_pair_state(f1_state, f8_state)


def describe() -> str:
    return describe_inner_oct_pair(
        'F1', 'F8', 'SOURCE', 'VOID',
        ('apex', 'apex'), ('Fire', 'Water'), ('Father', 'Mother'),
    )


if __name__ == '__main__':
    print(describe())
