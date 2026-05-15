"""
Inner-octahedron faces registry — Enki.

Aggregates the 8 archetype-mode faces at R=1/√3 inner-oct shell.

Per canon §10 (locked) + §5 (vertex planets) + §11 (edge boundaries):

| Face | Mode      | Element | Tet     | Apex/Lateral | Vertices | Planets                  |
|------|-----------|---------|---------|--------------|----------|--------------------------|
| F1   | SOURCE    | Fire    | Father  | apex         | V1,V2,V3 | Venus, Mercury, Saturn   |
| F2   | FEEDBACK  | Earth   | Mother  | lateral      | V1,V2,V4 | Venus, Mercury, Moon     |
| F3   | DESIRE    | Air     | Father  | lateral      | V1,V4,V6 | Venus, Moon, Jupiter     |
| F4   | PATTERN   | Air     | Father  | lateral      | V2,V4,V5 | Mercury, Moon, Mars      |
| F5   | SYNTHESIS | Earth   | Mother  | lateral      | V2,V3,V5 | Mercury, Saturn, Mars    |
| F6   | RESOURCE  | Air     | Father  | lateral      | V3,V5,V6 | Saturn, Mars, Jupiter    |
| F7   | ANCHOR    | Earth   | Mother  | lateral      | V1,V3,V6 | Venus, Saturn, Jupiter   |
| F8   | VOID      | Water   | Mother  | apex         | V4,V5,V6 | Moon, Mars, Jupiter      |

Antipodal pairs (vertex-complement, per oct symmetry):
  F1 SOURCE     ↔ F8 VOID       (apex pair, Fire ↔ Water)
  F2 FEEDBACK   ↔ F6 RESOURCE   (Earth ↔ Air, Mother-lateral ↔ Father-lateral)
  F3 DESIRE     ↔ F5 SYNTHESIS  (Air ↔ Earth, Father-lateral ↔ Mother-lateral)
  F4 PATTERN   ↔ F7 ANCHOR     (Air ↔ Earth, Father-lateral ↔ Mother-lateral)

Cascade structure (per FINDINGS_007):
  face-class  (cardinality 8) — 8 archetype modes
  pair-class  (cardinality 4) — 4 antipodal pairs (1 apex + 3 lateral)
  partition   (cardinality 2) — apex-pair × lateral-pair-set
  system      (cardinality 1) — full inner-oct

Different from cube cascade (6→3→2→1). Inner-oct cascade is 8→4→1+3→1.
"""
from __future__ import annotations

import face_f1_source     as _f1
import face_f2_feedback   as _f2
import face_f3_desire     as _f3
import face_f4_pattern    as _f4
import face_f5_synthesis  as _f5
import face_f6_resource   as _f6
import face_f7_anchor     as _f7
import face_f8_void       as _f8


FACES = [_f1, _f2, _f3, _f4, _f5, _f6, _f7, _f8]

BY_FACE_ID = {f.FACE_ID: f for f in FACES}
BY_MODE    = {f.MODE: f    for f in FACES}
BY_TET = {
    'Father': [f for f in FACES if f.TET_POLARITY == 'Father'],
    'Mother': [f for f in FACES if f.TET_POLARITY == 'Mother'],
}
BY_ELEMENT = {}
for f in FACES:
    BY_ELEMENT.setdefault(f.ELEMENT, []).append(f)


def get(face_id_or_mode: str):
    if face_id_or_mode in BY_FACE_ID:
        return BY_FACE_ID[face_id_or_mode]
    if face_id_or_mode in BY_MODE:
        return BY_MODE[face_id_or_mode]
    raise KeyError(f"No inner-oct face matches {face_id_or_mode!r}")


def all_frozen() -> list:
    return [f.face_state().to_dict() for f in FACES]


def describe_all() -> str:
    return "\n".join(f.describe() for f in FACES)


if __name__ == '__main__':
    print(describe_all())
    print()
    print(f"Inner-oct faces registered: {len(FACES)}")
    print()
    print("By tet polarity:")
    print(f"  Father (4): {[f.FACE_ID for f in BY_TET['Father']]} = {[f.MODE for f in BY_TET['Father']]}")
    print(f"  Mother (4): {[f.FACE_ID for f in BY_TET['Mother']]} = {[f.MODE for f in BY_TET['Mother']]}")
    print()
    print("By element:")
    for elem, faces in BY_ELEMENT.items():
        print(f"  {elem:6s}: {[f.FACE_ID for f in faces]}")
    print()
    print("All frozen states:")
    for state in all_frozen():
        print(f"  {state['face_id']} {state['mode']:10s} {state['apex_or_lateral']:7s} "
              f"({state['tet_polarity']}, {state['element']}) "
              f"{state['vertex_ids']} → {state['planets']}")
