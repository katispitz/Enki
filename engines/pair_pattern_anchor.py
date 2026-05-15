"""
F4 PATTERN ↔ F7 ANCHOR — inner-oct lateral antipodal pair.

Air-Father ↔ Earth-Mother lateral axis.
F4 planets: Mercury, Moon, Mars. F7 planets: Venus, Saturn, Jupiter.
Vertex union: V2+V4+V5 ∪ V1+V3+V6 = all 6 sign-rulership vertices.
"""
from __future__ import annotations
from typing import Optional

import face_f4_pattern as _f4
import face_f7_anchor  as _f7
from _inner_oct_pair_engine import (
    InnerOctPairState, compute_inner_oct_pair_state, describe_inner_oct_pair
)


PAIR_NAME = ('PATTERN', 'ANCHOR')

__canonical__ = {
    'function_class':     'polarity-define',
    'functional_tier':    'first-composition',
    'compositional_axis': 'spatial',
    'residency_id':       'inner-oct-pair-pattern-anchor',
    'canon_citation':     'canon §10 (inner-oct faces) / F4↔F7 lateral pair',
    'status':             'canonical',
}


def pair_state(mercury_lon: Optional[float] = None,
               moon_lon:    Optional[float] = None,
               mars_lon:    Optional[float] = None,
               venus_lon:   Optional[float] = None,
               saturn_lon:  Optional[float] = None,
               jupiter_lon: Optional[float] = None) -> InnerOctPairState:
    f4_state = _f4.face_state(mercury_lon, moon_lon, mars_lon)
    f7_state = _f7.face_state(venus_lon, saturn_lon, jupiter_lon)
    return compute_inner_oct_pair_state(f4_state, f7_state)


def describe() -> str:
    return describe_inner_oct_pair(
        'F4', 'F7', 'PATTERN', 'ANCHOR',
        ('lateral', 'lateral'), ('Air', 'Earth'), ('Father', 'Mother'),
    )


if __name__ == '__main__':
    print(describe())
