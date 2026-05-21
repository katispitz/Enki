"""
Shared inner-octahedron face engine — R=1/√3 archetype mode-class.

Per Nammu canon §10 (INNER OCTAHEDRON FACES) + §5 (vertex planet assignments).
8 archetype-mode faces (F1-F8), each a triangle of 3 vertex-planets.

Substrate-emergent factoring: inner-oct face function COMPOSES from the
canonical primitive `planet-aspect-activate` (canon §30, graduated 2026-05-12).
Each face computes 3 pairwise planet-aspect-activate calls (one per triangle
edge) plus mode-level aggregation.

This validates the canonical promotion pattern — once a primitive function
graduates, higher-level engines compose it without re-implementing physics.

Substrate-locked face → vertex → planet mapping (from canon §5 + §10 + §11):

| Face | Mode      | Element | Tet     | Vertices    | Planets                  |
|------|-----------|---------|---------|-------------|--------------------------|
| F1   | SOURCE    | Fire    | Father  | V1,V2,V3    | Venus, Mercury, Saturn   |
| F2   | FEEDBACK  | Earth   | Mother  | V1,V2,V4    | Venus, Mercury, Moon     |
| F3   | DESIRE    | Air     | Father  | V1,V4,V6    | Venus, Moon, Jupiter     |
| F4   | PATTERN   | Air     | Father  | V2,V4,V5    | Mercury, Moon, Mars      |
| F5   | SYNTHESIS | Earth   | Mother  | V2,V3,V5    | Mercury, Saturn, Mars    |
| F6   | RESOURCE  | Air     | Father  | V3,V5,V6    | Saturn, Mars, Jupiter    |
| F7   | ANCHOR    | Earth   | Mother  | V1,V3,V6    | Venus, Saturn, Jupiter   |
| F8   | VOID      | Water   | Mother  | V4,V5,V6    | Moon, Mars, Jupiter      |

Each vertex appears in exactly 4 faces (oct property). No face contains
both members of any antipodal vertex pair (V1↔V5, V2↔V6, V3↔V4) per
canon §5. Antipodal-pair structure: F1↔F8, F2↔F6, F3↔F5, F4↔F7.

Inner-oct face function (candidate `mode-bound`, canon §30 status:
candidate-single-residency at R=1/√3): each face emits an aggregate mode-
activation derived from its 3 pairwise planet-aspect-activations. This is
the FIRST residency for `mode-bound`; cross-R-tier confirmation pending.

Substrate-discipline:
  - Composes canonical `planet-aspect-activate` (canon §30) via _axis_engine
  - No new aspect detection; reuses substrate-derived 5-aspect set + 6° orb
  - NULL-honest where ephemeris partial across the 3 planets
  - Emits multiple aggregations (substrate-honest; consumer chooses)
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional

from _axis_engine import compute_axis_state


@dataclass
class InnerOctFaceState:
    """Substrate-honest snapshot of an inner-oct face's archetype-mode activation.

    Composed from 3 planet-aspect-activate pairs (one per triangle edge).
    Pair sub-states preserved for substrate-cascade transparency.
    """
    # Permanent definition (always known)
    face_id:           str              # F1..F8
    mode:              str              # SOURCE / FEEDBACK / etc
    element:           str              # Fire / Air / Earth / Water
    tet_polarity:      str              # Father / Mother
    apex_or_lateral:   str              # apex / lateral
    vertex_ids:        list             # [V1, V2, V3] etc — 3 inner-oct vertices
    planets:           list             # [Venus, Mercury, Saturn] etc — 3 planets
    substrate_card:    Optional[str]    # canonical lock card if available (most TBD)
    shell:             str              # '1/√3' (inner-oct shell)

    # Live state (3 pair sub-activations + mode-level aggregations)
    pair_states:       list             # [AxisState.to_dict(), ...] × 3 — one per edge
    edges:             list             # ordered edge labels e.g. ['Venus-Mercury','Mercury-Saturn','Venus-Saturn']

    # Aggregated mode-level metrics (NULL when all 3 pairs frozen)
    active_pair_count: Optional[int]    # 0..3 — how many edges in orb
    coherence:         Optional[bool]   # all 3 active
    resonance:         Optional[bool]   # ≥2 active
    presence:          Optional[bool]   # ≥1 active
    min_activation:    Optional[float]
    max_activation:    Optional[float]
    mean_activation:   Optional[float]
    sum_activation:    Optional[float]
    dominant_edge:     Optional[str]    # which edge strongest

    def to_dict(self) -> dict:
        d = asdict(self)
        return d


def compute_inner_oct_face_state(
    face_id: str, mode: str, element: str, tet_polarity: str,
    apex_or_lateral: str, vertex_ids: list, planets: list,
    substrate_card: Optional[str],
    planet_lon_a: Optional[float] = None,
    planet_lon_b: Optional[float] = None,
    planet_lon_c: Optional[float] = None,
) -> InnerOctFaceState:
    """Compute live inner-oct face state.

    Inputs are 3 planet longitudes in same order as `planets` list (e.g., for
    F1 with planets=[Venus, Mercury, Saturn]: planet_lon_a=Venus, _b=Mercury,
    _c=Saturn).

    All 3 None → frozen state (substrate-locks only).
    All 3 supplied → live state with 3 pair-activations + mode aggregation.
    Mixed → ValueError (substrate-honest reject).
    """
    lons = [planet_lon_a, planet_lon_b, planet_lon_c]
    if all(l is None for l in lons):
        # Frozen state
        pair_states = [
            compute_axis_state(face_id, f"inner-oct-{face_id}",
                               (planets[i], planets[j]), f"{element}/{mode}",
                               substrate_card or "TBD", None, None).to_dict()
            for i, j in [(0, 1), (1, 2), (0, 2)]
        ]
        edges = [f"{planets[i]}-{planets[j]}" for i, j in [(0, 1), (1, 2), (0, 2)]]
        return InnerOctFaceState(
            face_id=face_id, mode=mode, element=element, tet_polarity=tet_polarity,
            apex_or_lateral=apex_or_lateral, vertex_ids=vertex_ids, planets=planets,
            substrate_card=substrate_card, shell='1/√3',
            pair_states=pair_states, edges=edges,
            active_pair_count=None, coherence=None, resonance=None, presence=None,
            min_activation=None, max_activation=None, mean_activation=None,
            sum_activation=None, dominant_edge=None,
        )

    if any(l is None for l in lons):
        raise ValueError(
            f"Inner-oct face {face_id} requires all 3 planet longitudes or none — "
            "partial input is substrate-incomplete"
        )

    # Live state — compose 3 pair-aspect-activates
    pairs = [(0, 1), (1, 2), (0, 2)]
    pair_states = []
    edges = []
    activations = []
    for i, j in pairs:
        ax = compute_axis_state(
            face_id, f"inner-oct-{face_id}",
            (planets[i], planets[j]), f"{element}/{mode}",
            substrate_card or "TBD",
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
    if max_act > 0.0:
        dom_edge = edges[activations.index(max_act)]
    else:
        dom_edge = None

    return InnerOctFaceState(
        face_id=face_id, mode=mode, element=element, tet_polarity=tet_polarity,
        apex_or_lateral=apex_or_lateral, vertex_ids=vertex_ids, planets=planets,
        substrate_card=substrate_card, shell='1/√3',
        pair_states=pair_states, edges=edges,
        active_pair_count=active_count,
        coherence=(active_count == 3),
        resonance=(active_count >= 2),
        presence=(active_count >= 1),
        min_activation=min_act, max_activation=max_act,
        mean_activation=mean_act, sum_activation=sum_act,
        dominant_edge=dom_edge,
    )


def describe_inner_oct_face(face_id: str, mode: str, element: str,
                            tet_polarity: str, apex_or_lateral: str,
                            vertex_ids: list, planets: list,
                            substrate_card: Optional[str]) -> str:
    return (
        f"Inner-oct face: {face_id} ({mode})\n"
        f"Position:       {apex_or_lateral} ({tet_polarity}-tet, {element})\n"
        f"Vertices:       {' + '.join(vertex_ids)}\n"
        f"Planets:        {' + '.join(planets)}\n"
        f"Shell:          R=1/√3 (inner-octahedron)\n"
        f"Substrate card: {substrate_card or 'TBD (inner-oct face cards not yet locked individually)'}\n"
        f"Function-class candidate: mode-bound (candidate-single-residency, canon §30 — awaiting cross-R-tier confirmation)\n"
        f"Composition:    composes 3 × `planet-aspect-activate` (canonical, canon §30) per triangle edge\n"
    )
