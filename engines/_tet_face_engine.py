"""
Shared Merkaba tet-face engine — 8 tet-faces at R=1.

Per canon §M.5 + canon_quick_ref: "Merkaba = Outer Cube. 8V / 12E / 6F or 8 tet-faces.
Same circumsphere." The 8 tet-faces split into:
  - 4 Father-tet faces (Pluto/Sun/Mars/Saturn vertices)
  - 4 Mother-tet faces (Neptune/Moon/Mercury/Jupiter vertices)

Each tet-face is a TRIANGLE with 3 vertex-corner planets (3 of the 4 tet-vertices).
Tetrahedron has 4 vertices and 4 triangular faces; each face omits 1 vertex.

Face enumeration:
  Father-tet faces (each face's 3 vertices = full {U0,U1,U2,U3} minus one):
    TF1 = {U0, U1, U2}  (omits U3 Saturn) — Pluto, Sun, Mars
    TF2 = {U0, U1, U3}  (omits U2 Mars)   — Pluto, Sun, Saturn
    TF3 = {U0, U2, U3}  (omits U1 Sun)    — Pluto, Mars, Saturn
    TF4 = {U1, U2, U3}  (omits U0 Pluto)  — Sun, Mars, Saturn

  Mother-tet faces (each face's 3 vertices = full {L0,L1,L2,L3} minus one):
    TF5 = {L0, L1, L2}  (omits L3 Jupiter) — Neptune, Moon, Mercury
    TF6 = {L0, L1, L3}  (omits L2 Mercury) — Neptune, Moon, Jupiter
    TF7 = {L0, L2, L3}  (omits L1 Moon)    — Neptune, Mercury, Jupiter
    TF8 = {L1, L2, L3}  (omits L0 Neptune) — Moon, Mercury, Jupiter

Function: composes 3 × `planet-aspect-activate` (canonical, canon §30) per face,
one per triangle edge. Same compute shape as inner-oct face engine — tests
cross-R-tier residency for `mode-bound` candidate (or shell-agnostic
`triangle-aspect-activate` candidate per FINDINGS_011 conflation-test).

Substrate-incomplete: per-face archetype-mode label NOT canon-locked (canon §M.5
identifies the 8 tet-faces as Father/Mother polarity, but doesn't lock individual
mode-class per face). This engine builds SHAPE without inventing per-face modes.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional

from _axis_engine import compute_axis_state


@dataclass
class TetFaceState:
    """Substrate-honest snapshot of a Merkaba tet-face.

    Composed from 3 planet-aspect-activate pairs (one per triangle edge).
    """
    # Permanent definition (always known)
    face_id:           str              # TF1..TF8
    tet_polarity:      str              # Father / Mother
    omitted_vertex:    str              # the 4th tet-vertex this face omits
    vertex_ids:        list             # 3 vertex IDs (U0-U3 or L0-L3)
    planets:           list             # 3 planet names
    shell:             str              # '1' (Merkaba cube-vertex shell)
    substrate_card:    Optional[str]    # TBD per canon §M.5 tet-face individual locks

    # Live state (3 pair sub-activations + face-level aggregations)
    pair_states:       list             # AxisState.to_dict() × 3
    edges:             list             # ordered edge labels

    # Aggregated metrics (NULL when all 3 pairs frozen)
    active_pair_count: Optional[int]
    coherence:         Optional[bool]
    resonance:         Optional[bool]
    presence:          Optional[bool]
    min_activation:    Optional[float]
    max_activation:    Optional[float]
    mean_activation:   Optional[float]
    sum_activation:    Optional[float]
    dominant_edge:     Optional[str]

    def to_dict(self) -> dict:
        return asdict(self)


def compute_tet_face_state(
    face_id: str, tet_polarity: str, omitted_vertex: str,
    vertex_ids: list, planets: list, substrate_card: Optional[str],
    planet_lon_a: Optional[float] = None,
    planet_lon_b: Optional[float] = None,
    planet_lon_c: Optional[float] = None,
) -> TetFaceState:
    """Compute live tet-face state.

    Inputs are 3 planet longitudes in same order as `planets` list.

    All 3 None → frozen state (substrate-locks only).
    All 3 supplied → live state with 3 pair-activations + face aggregation.
    Mixed → ValueError (substrate-honest reject).
    """
    lons = [planet_lon_a, planet_lon_b, planet_lon_c]
    if all(l is None for l in lons):
        pair_states = [
            compute_axis_state(face_id, f'tet-face-{face_id}',
                               (planets[i], planets[j]), f'{tet_polarity}-tet',
                               substrate_card or 'TBD', None, None).to_dict()
            for i, j in [(0, 1), (1, 2), (0, 2)]
        ]
        edges = [f"{planets[i]}-{planets[j]}" for i, j in [(0, 1), (1, 2), (0, 2)]]
        return TetFaceState(
            face_id=face_id, tet_polarity=tet_polarity,
            omitted_vertex=omitted_vertex,
            vertex_ids=vertex_ids, planets=planets,
            shell='1', substrate_card=substrate_card,
            pair_states=pair_states, edges=edges,
            active_pair_count=None, coherence=None, resonance=None,
            presence=None, min_activation=None, max_activation=None,
            mean_activation=None, sum_activation=None, dominant_edge=None,
        )

    if any(l is None for l in lons):
        raise ValueError(
            f"Tet-face {face_id} requires all 3 planet longitudes or none — "
            "partial input is substrate-incomplete"
        )

    pairs = [(0, 1), (1, 2), (0, 2)]
    pair_states = []
    edges = []
    activations = []
    for i, j in pairs:
        ax = compute_axis_state(
            face_id, f'tet-face-{face_id}',
            (planets[i], planets[j]), f'{tet_polarity}-tet',
            substrate_card or 'TBD',
            lons[i], lons[j],
        )
        pair_states.append(ax.to_dict())
        edges.append(f"{planets[i]}-{planets[j]}")
        activations.append(ax.activation_strength)

    active_count = sum(1 for x in activations if x > 0.0)
    min_act = min(activations)
    max_act = max(activations)
    mean_act = sum(activations) / 3.0
    sum_act = sum(activations)
    dom_edge = edges[activations.index(max_act)] if max_act > 0 else None

    return TetFaceState(
        face_id=face_id, tet_polarity=tet_polarity,
        omitted_vertex=omitted_vertex,
        vertex_ids=vertex_ids, planets=planets,
        shell='1', substrate_card=substrate_card,
        pair_states=pair_states, edges=edges,
        active_pair_count=active_count,
        coherence=(active_count == 3),
        resonance=(active_count >= 2),
        presence=(active_count >= 1),
        min_activation=min_act, max_activation=max_act,
        mean_activation=mean_act, sum_activation=sum_act,
        dominant_edge=dom_edge,
    )


def describe_tet_face(face_id: str, tet_polarity: str, omitted_vertex: str,
                      vertex_ids: list, planets: list,
                      substrate_card: Optional[str]) -> str:
    return (
        f"Merkaba tet-face: {face_id}\n"
        f"Tet polarity:   {tet_polarity}\n"
        f"Omits vertex:   {omitted_vertex}\n"
        f"Vertices:       {' + '.join(vertex_ids)}\n"
        f"Planets:        {' + '.join(planets)}\n"
        f"Shell:          R=1 (Merkaba cube-vertex shell)\n"
        f"Substrate card: {substrate_card or 'TBD (per-face mode-class NOT canon-locked)'}\n"
        f"Function-class candidate: `mode-bound` (cross-R-tier 2nd residency probe) OR\n"
        f"  `triangle-aspect-activate` (shell-agnostic 3-planet compose shape)\n"
        f"Composition:    composes 3 × `planet-aspect-activate` (canonical, canon §30)\n"
    )
