"""
F3 DESIRE ↔ F5 SYNTHESIS — inner-oct lateral antipodal pair.

Air-Father ↔ Earth-Mother lateral axis.
F3 planets: Venus, Moon, Jupiter. F5 planets: Mercury, Saturn, Mars.
Vertex union: V1+V4+V6 ∪ V2+V3+V5 = all 6 sign-rulership vertices.
"""
from __future__ import annotations
from typing import Optional

import face_f3_desire    as _f3
import face_f5_synthesis as _f5
from _inner_oct_pair_engine import (
    InnerOctPairState, compute_inner_oct_pair_state, describe_inner_oct_pair
)


PAIR_NAME = ('DESIRE', 'SYNTHESIS')

__canonical__ = {
    'function_class':     'polarity-define',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-pair-desire-synthesis',
    'canon_citation':     'canon §10 (inner-oct faces) / F3↔F5 lateral pair',
    'status':             'canonical',
}


def pair_state(venus_lon:   Optional[float] = None,
               moon_lon:    Optional[float] = None,
               jupiter_lon: Optional[float] = None,
               mercury_lon: Optional[float] = None,
               saturn_lon:  Optional[float] = None,
               mars_lon:    Optional[float] = None) -> InnerOctPairState:
    f3_state = _f3.face_state(venus_lon, moon_lon, jupiter_lon)
    f5_state = _f5.face_state(mercury_lon, saturn_lon, mars_lon)
    return compute_inner_oct_pair_state(f3_state, f5_state)


def describe() -> str:
    return describe_inner_oct_pair(
        'F3', 'F5', 'DESIRE', 'SYNTHESIS',
        ('lateral', 'lateral'), ('Air', 'Earth'), ('Father', 'Mother'),
    )


if __name__ == '__main__':
    print(describe())
