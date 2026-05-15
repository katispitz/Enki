"""
Inner-oct antipodal-pair registry — Enki.

4 antipodal pairs per inner-oct vertex-complement (R=1/√3):

| Pair name           | Face IDs | Element pair  | Tet pair        | Apex/lateral set |
|---------------------|----------|---------------|-----------------|------------------|
| SOURCE ↔ VOID       | F1 ↔ F8  | Fire ↔ Water  | Father ↔ Mother | apex ↔ apex      |
| FEEDBACK ↔ RESOURCE | F2 ↔ F6  | Earth ↔ Air   | Mother ↔ Father | lateral ↔ lateral|
| DESIRE ↔ SYNTHESIS  | F3 ↔ F5  | Air ↔ Earth   | Father ↔ Mother | lateral ↔ lateral|
| PATTERN ↔ ANCHOR    | F4 ↔ F7  | Air ↔ Earth   | Father ↔ Mother | lateral ↔ lateral|

Substrate-emergent: each antipodal pair's vertex union covers ALL 6
sign-rulership vertices (3 + 3). Different from cube pair-class where each
pair covers only 4 of 8 cube vertices.

Pattern across pairs:
  - 1 apex-pair (F1↔F8) with Fire-Water + Father-Mother element-polarity
  - 3 lateral-pairs each with Air-Earth element-polarity (different combos)
"""
from __future__ import annotations

import pair_source_void       as _p18
import pair_feedback_resource as _p26
import pair_desire_synthesis  as _p35
import pair_pattern_anchor    as _p47


PAIRS = [_p18, _p26, _p35, _p47]

BY_NAME = {p.PAIR_NAME: p for p in PAIRS}


def get(pair_name: tuple):
    return BY_NAME[pair_name]


def all_frozen() -> list:
    return [p.pair_state().to_dict() for p in PAIRS]


def describe_all() -> str:
    return "\n".join(p.describe() for p in PAIRS)


if __name__ == '__main__':
    print(describe_all())
    print()
    print(f"Inner-oct antipodal pairs registered: {len(PAIRS)}")
    print()
    print("All frozen pair states:")
    for state in all_frozen():
        print(f"  {state['pair_name'][0]:10s} ↔ {state['pair_name'][1]:10s}  "
              f"{state['face_ids'][0]} ↔ {state['face_ids'][1]}  "
              f"{state['apex_or_lateral_set'][0]} ↔ {state['apex_or_lateral_set'][1]}  "
              f"{state['element_pair'][0]:5s} ↔ {state['element_pair'][1]:5s}")
