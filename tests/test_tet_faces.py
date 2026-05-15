"""
Tests for 8 Merkaba tet-face engines (R=1).

Per FINDINGS_011 cross-R-tier residency probe: tet-face engine field-shape
matches inner-oct face engine at compute layer. Substantiated triangle-aspect-
activate canonical promotion (canon §30).

8 tet-faces: 4 Father-tet (omit U0..U3) + 4 Mother-tet (omit L0..L3).
Each face = 3-of-4 tet vertices, omits 1.
"""
import pytest
import tet_faces
from _tet_face_engine import TetFaceState


EXPECTED_TET_FACES = [
    ('TF1', 'Father', 'U3', ['U0', 'U1', 'U2'], ['Pluto', 'Sun', 'Mars']),
    ('TF2', 'Father', 'U2', ['U0', 'U1', 'U3'], ['Pluto', 'Sun', 'Saturn']),
    ('TF3', 'Father', 'U1', ['U0', 'U2', 'U3'], ['Pluto', 'Mars', 'Saturn']),
    ('TF4', 'Father', 'U0', ['U1', 'U2', 'U3'], ['Sun', 'Mars', 'Saturn']),
    ('TF5', 'Mother', 'L3', ['L0', 'L1', 'L2'], ['Neptune', 'Moon', 'Mercury']),
    ('TF6', 'Mother', 'L2', ['L0', 'L1', 'L3'], ['Neptune', 'Moon', 'Jupiter']),
    ('TF7', 'Mother', 'L1', ['L0', 'L2', 'L3'], ['Neptune', 'Mercury', 'Jupiter']),
    ('TF8', 'Mother', 'L0', ['L1', 'L2', 'L3'], ['Moon', 'Mercury', 'Jupiter']),
]


def test_registry_8_tet_faces():
    assert len(tet_faces.TET_FACES) == 8


def test_tet_faces_match_expected():
    actual = [(fid, p, o, v, pl) for fid, p, o, v, pl in tet_faces.TET_FACES]
    assert actual == EXPECTED_TET_FACES


def test_4_father_4_mother():
    fathers = [f for f in tet_faces.TET_FACES if f[1] == 'Father']
    mothers = [f for f in tet_faces.TET_FACES if f[1] == 'Mother']
    assert len(fathers) == 4
    assert len(mothers) == 4


@pytest.mark.parametrize('face_id,polarity,omitted,vertices,planets', EXPECTED_TET_FACES)
def test_tet_face_frozen(face_id, polarity, omitted, vertices, planets):
    s = tet_faces.face_state(face_id)
    assert s.face_id == face_id
    assert s.tet_polarity == polarity
    assert s.omitted_vertex == omitted
    assert s.vertex_ids == vertices
    assert s.planets == planets
    assert s.shell == '1'
    assert s.active_pair_count is None  # frozen


@pytest.mark.parametrize('face_id,polarity,omitted,vertices,planets', EXPECTED_TET_FACES)
def test_tet_face_live_all_conjunction(face_id, polarity, omitted, vertices, planets):
    s = tet_faces.face_state(face_id, 100.0, 100.0, 100.0)
    assert s.coherence is True
    assert s.active_pair_count == 3


def test_unknown_face_raises():
    with pytest.raises(KeyError):
        tet_faces.face_state('TFXX')


def test_each_tet_vertex_in_3_faces():
    """Tetrahedron invariant: each vertex incident to 3 of 4 faces (omitted once)."""
    father_count = {}
    mother_count = {}
    for fid, polarity, omitted, vertices, planets in tet_faces.TET_FACES:
        for v in vertices:
            if polarity == 'Father':
                father_count[v] = father_count.get(v, 0) + 1
            else:
                mother_count[v] = mother_count.get(v, 0) + 1
    for v in ['U0', 'U1', 'U2', 'U3']:
        assert father_count[v] == 3, f"Father vertex {v} in {father_count[v]} faces, expected 3"
    for v in ['L0', 'L1', 'L2', 'L3']:
        assert mother_count[v] == 3, f"Mother vertex {v} in {mother_count[v]} faces, expected 3"


def test_cross_r_tier_shape_with_inner_oct():
    """
    FINDINGS_011 invariant: 17 of 20 fields shared between InnerOctFaceState
    and TetFaceState. Compute fields identical; differences are metadata.
    """
    from _inner_oct_face_engine import InnerOctFaceState
    from dataclasses import fields
    io = {f.name for f in fields(InnerOctFaceState)}
    tf = {f.name for f in fields(TetFaceState)}
    shared = io & tf
    # FINDINGS_011 documented 17 shared
    assert len(shared) == 17, f"Expected 17 shared fields, got {len(shared)}"
    # Compute fields must be in shared
    compute_required = {
        'active_pair_count', 'coherence', 'resonance', 'presence',
        'min_activation', 'max_activation', 'mean_activation', 'sum_activation',
        'dominant_edge', 'pair_states', 'edges',
        'face_id', 'planets', 'vertex_ids', 'tet_polarity', 'shell',
        'substrate_card',
    }
    assert compute_required.issubset(shared), \
        f"Missing compute fields in shared: {compute_required - shared}"
