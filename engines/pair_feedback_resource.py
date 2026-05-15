"""
F2 FEEDBACK ↔ F6 RESOURCE — inner-oct lateral antipodal pair.

Earth-Mother ↔ Air-Father lateral axis.
F2 planets: Venus, Mercury, Moon. F6 planets: Saturn, Mars, Jupiter.
Vertex union: V1+V2+V4 ∪ V3+V5+V6 = all 6 sign-rulership vertices.
"""
from __future__ import annotations
from typing import Optional

import face_f2_feedback as _f2
import face_f6_resource as _f6
from _inner_oct_pair_engine import (
    InnerOctPairState, compute_inner_oct_pair_state, describe_inner_oct_pair
)


PAIR_NAME = ('FEEDBACK', 'RESOURCE')

__canonical__ = {
    'function_class':     'polarity-define',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-pair-feedback-resource',
    'canon_citation':     'canon §10 (inner-oct faces) / F2↔F6 lateral pair',
    'status':             'canonical',
}


def pair_state(venus_lon:   Optional[float] = None,
               mercury_lon: Optional[float] = None,
               moon_lon:    Optional[float] = None,
               saturn_lon:  Optional[float] = None,
               mars_lon:    Optional[float] = None,
               jupiter_lon: Optional[float] = None) -> InnerOctPairState:
    f2_state = _f2.face_state(venus_lon, mercury_lon, moon_lon)
    f6_state = _f6.face_state(saturn_lon, mars_lon, jupiter_lon)
    return compute_inner_oct_pair_state(f2_state, f6_state)


def describe() -> str:
    return describe_inner_oct_pair(
        'F2', 'F6', 'FEEDBACK', 'RESOURCE',
        ('lateral', 'lateral'), ('Earth', 'Air'), ('Mother', 'Father'),
    )


if __name__ == '__main__':
    print(describe())
