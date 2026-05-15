"""
Merkaba tet-faces registry — Enki.

8 triangular faces inscribed in Merkaba cube (R=1):
  4 Father-tet (Pluto/Sun/Mars/Saturn vertex set)
  4 Mother-tet (Neptune/Moon/Mercury/Jupiter vertex set)

Each face = 3 of the 4 tet-vertices (omits 1). Same compute pattern as
inner-oct face engine — cross-R-tier residency probe for `mode-bound` (or
shell-agnostic `triangle-aspect-activate`) candidate function.

Per canon §M.5 + canon_quick_ref: substrate-position locked at face-class
level (Father/Mother polarity). Per-face individual archetype-mode labels NOT
canon-locked.
"""
from __future__ import annotations
from typing import Optional

from _tet_face_engine import (
    TetFaceState, compute_tet_face_state, describe_tet_face
)


# 8 tet-faces: 4 Father + 4 Mother. Each: (face_id, polarity, omitted_vertex, vertex_ids, planets).
TET_FACES = [
    # Father-tet faces — each omits one of {U0,U1,U2,U3}
    ('TF1', 'Father', 'U3', ['U0', 'U1', 'U2'], ['Pluto', 'Sun', 'Mars']),
    ('TF2', 'Father', 'U2', ['U0', 'U1', 'U3'], ['Pluto', 'Sun', 'Saturn']),
    ('TF3', 'Father', 'U1', ['U0', 'U2', 'U3'], ['Pluto', 'Mars', 'Saturn']),
    ('TF4', 'Father', 'U0', ['U1', 'U2', 'U3'], ['Sun', 'Mars', 'Saturn']),
    # Mother-tet faces — each omits one of {L0,L1,L2,L3}
    ('TF5', 'Mother', 'L3', ['L0', 'L1', 'L2'], ['Neptune', 'Moon', 'Mercury']),
    ('TF6', 'Mother', 'L2', ['L0', 'L1', 'L3'], ['Neptune', 'Moon', 'Jupiter']),
    ('TF7', 'Mother', 'L1', ['L0', 'L2', 'L3'], ['Neptune', 'Mercury', 'Jupiter']),
    ('TF8', 'Mother', 'L0', ['L1', 'L2', 'L3'], ['Moon', 'Mercury', 'Jupiter']),
]


def face_state(face_id: str,
               planet_lon_a: Optional[float] = None,
               planet_lon_b: Optional[float] = None,
               planet_lon_c: Optional[float] = None) -> TetFaceState:
    """Compute tet-face state for a named face. Substrate-locks fetched from TET_FACES."""
    entry = next((f for f in TET_FACES if f[0] == face_id), None)
    if entry is None:
        raise KeyError(f"Unknown tet-face {face_id!r}")
    fid, polarity, omitted, vertices, planets = entry
    return compute_tet_face_state(
        fid, polarity, omitted, vertices, planets, None,
        planet_lon_a, planet_lon_b, planet_lon_c,
    )


def all_frozen() -> list:
    return [face_state(e[0]).to_dict() for e in TET_FACES]


def describe_all() -> str:
    out = []
    for fid, polarity, omitted, vertices, planets in TET_FACES:
        out.append(describe_tet_face(fid, polarity, omitted, vertices, planets, None))
    return "\n".join(out)


if __name__ == '__main__':
    print(describe_all())
    print()
    print(f"Tet-faces registered: {len(TET_FACES)}")
    print()
    print("By tet polarity:")
    fathers = [f for f in TET_FACES if f[1] == 'Father']
    mothers = [f for f in TET_FACES if f[1] == 'Mother']
    print(f"  Father (4): {[f[0] for f in fathers]} (planets from {{Pluto,Sun,Mars,Saturn}})")
    print(f"  Mother (4): {[f[0] for f in mothers]} (planets from {{Neptune,Moon,Mercury,Jupiter}})")
    print()
    print("All frozen states:")
    for state in all_frozen():
        print(f"  {state['face_id']} {state['tet_polarity']:6s} omit={state['omitted_vertex']}  "
              f"{state['vertex_ids']} → {state['planets']}")
