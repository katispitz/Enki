"""
Tests for 8 inner-oct face engines (R=1/√3) + 4 antipodal pairs.

Per canon §10 + §11 (face/edge enumeration) + §5 (vertex planet assignments).

FINDINGS_007 key invariant: NO face contains both members of any antipodal-
vertex pair (V1↔V5, V2↔V6, V3↔V4). Substrate-error-prone enumeration; F5+F7
were corrected via this constraint during build.

Antipodal pairs: F1↔F8 (apex), F2↔F6, F3↔F5, F4↔F7 (vertex-complement).
"""
import pytest
import face_f1_source
import face_f2_feedback
import face_f3_desire
import face_f4_pattern
import face_f5_synthesis
import face_f6_resource
import face_f7_anchor
import face_f8_void
import inner_oct_faces
import pair_source_void
import pair_feedback_resource
import pair_desire_synthesis
import pair_pattern_anchor
import inner_oct_pairs


FACE_MODULES = [
    (face_f1_source,    'F1', 'SOURCE',    'Fire',  'Father', 'apex',    ['V1', 'V2', 'V3'], ['Venus', 'Mercury', 'Saturn']),
    (face_f2_feedback,  'F2', 'FEEDBACK',  'Earth', 'Mother', 'lateral', ['V1', 'V2', 'V4'], ['Venus', 'Mercury', 'Moon']),
    (face_f3_desire,    'F3', 'DESIRE',    'Air',   'Father', 'lateral', ['V1', 'V4', 'V6'], ['Venus', 'Moon', 'Jupiter']),
    (face_f4_pattern,   'F4', 'PATTERN',   'Air',   'Father', 'lateral', ['V2', 'V4', 'V5'], ['Mercury', 'Moon', 'Mars']),
    (face_f5_synthesis, 'F5', 'SYNTHESIS', 'Earth', 'Mother', 'lateral', ['V2', 'V3', 'V5'], ['Mercury', 'Saturn', 'Mars']),
    (face_f6_resource,  'F6', 'RESOURCE',  'Air',   'Father', 'lateral', ['V3', 'V5', 'V6'], ['Saturn', 'Mars', 'Jupiter']),
    (face_f7_anchor,    'F7', 'ANCHOR',    'Earth', 'Mother', 'lateral', ['V1', 'V3', 'V6'], ['Venus', 'Saturn', 'Jupiter']),
    (face_f8_void,      'F8', 'VOID',      'Water', 'Mother', 'apex',    ['V4', 'V5', 'V6'], ['Moon', 'Mars', 'Jupiter']),
]


# Antipodal vertex pairs per canon §5 (V1↔V5 Venus-Mars / V2↔V6 Mercury-Jupiter / V3↔V4 Saturn-Moon)
ANTIPODAL_VERTICES = [('V1', 'V5'), ('V2', 'V6'), ('V3', 'V4')]


@pytest.mark.parametrize('mod,fid,mode,elem,tet,al,verts,planets', FACE_MODULES)
def test_face_substrate_locks(mod, fid, mode, elem, tet, al, verts, planets):
    assert mod.FACE_ID == fid
    assert mod.MODE == mode
    assert mod.ELEMENT == elem
    assert mod.TET_POLARITY == tet
    assert mod.APEX_OR_LATERAL == al
    assert mod.VERTEX_IDS == verts
    assert mod.PLANETS == planets


@pytest.mark.parametrize('mod,fid,mode,elem,tet,al,verts,planets', FACE_MODULES)
def test_face_antipodal_vertex_exclusion(mod, fid, mode, elem, tet, al, verts, planets):
    """
    FINDINGS_007 invariant: no inner-oct face contains both members of any
    antipodal-vertex pair. F5 + F7 had this bug pre-correction.
    """
    vert_set = set(verts)
    for a, b in ANTIPODAL_VERTICES:
        assert not (a in vert_set and b in vert_set), \
            f"Face {fid} violates antipode-exclusion: contains {a} AND {b}"


@pytest.mark.parametrize('mod,fid,mode,elem,tet,al,verts,planets', FACE_MODULES)
def test_face_frozen(mod, fid, mode, elem, tet, al, verts, planets):
    s = mod.face_state()
    assert s.face_id == fid
    assert s.shell == '1/√3'
    assert s.active_pair_count is None  # frozen


@pytest.mark.parametrize('mod,fid,mode,elem,tet,al,verts,planets', FACE_MODULES)
def test_face_live_all_conjunction(mod, fid, mode, elem, tet, al, verts, planets):
    """All 3 planets at same longitude → all 3 edges conjunction → coherence."""
    s = mod.face_state(100.0, 100.0, 100.0)
    assert s.active_pair_count == 3
    assert s.coherence is True
    assert s.resonance is True
    assert s.presence is True
    assert s.mean_activation == 1.0


def test_each_vertex_in_exactly_4_faces():
    """Octahedron invariant: each vertex incident to 4 faces."""
    vertex_count = {}
    for mod, _fid, _m, _e, _t, _al, verts, _p in FACE_MODULES:
        for v in verts:
            vertex_count[v] = vertex_count.get(v, 0) + 1
    for v in ['V1', 'V2', 'V3', 'V4', 'V5', 'V6']:
        assert vertex_count[v] == 4, f"Vertex {v} in {vertex_count[v]} faces, expected 4"


def test_registry_8_faces():
    assert len(inner_oct_faces.FACES) == 8


def test_tet_polarity_partition_4_plus_4():
    """4 Father-tet faces + 4 Mother-tet faces."""
    assert len(inner_oct_faces.BY_TET['Father']) == 4
    assert len(inner_oct_faces.BY_TET['Mother']) == 4


def test_element_distribution():
    """1 Fire (F1) + 3 Air (F3/F4/F6) + 3 Earth (F2/F5/F7) + 1 Water (F8)."""
    assert len(inner_oct_faces.BY_ELEMENT['Fire']) == 1
    assert len(inner_oct_faces.BY_ELEMENT['Air']) == 3
    assert len(inner_oct_faces.BY_ELEMENT['Earth']) == 3
    assert len(inner_oct_faces.BY_ELEMENT['Water']) == 1


PAIR_MODULES = [
    (pair_source_void,         ('SOURCE', 'VOID')),
    (pair_feedback_resource,   ('FEEDBACK', 'RESOURCE')),
    (pair_desire_synthesis,    ('DESIRE', 'SYNTHESIS')),
    (pair_pattern_anchor,      ('PATTERN', 'ANCHOR')),
]


@pytest.mark.parametrize('mod,pair_name', PAIR_MODULES)
def test_inner_oct_pair_substrate(mod, pair_name):
    assert mod.PAIR_NAME == pair_name


def test_inner_oct_pairs_registry_4():
    assert len(inner_oct_pairs.PAIRS) == 4


def test_antipodal_pair_vertex_union_covers_all_6():
    """
    FINDINGS_007 finding: each antipodal pair's vertex union = all 6 inner-oct
    vertices (different from cube pairs which cover only 4 of 8).
    """
    all_verts = {'V1', 'V2', 'V3', 'V4', 'V5', 'V6'}
    pair_pairs = [
        ('SOURCE', 'VOID'),
        ('FEEDBACK', 'RESOURCE'),
        ('DESIRE', 'SYNTHESIS'),
        ('PATTERN', 'ANCHOR'),
    ]
    for mode_a, mode_b in pair_pairs:
        face_a = inner_oct_faces.BY_MODE[mode_a]
        face_b = inner_oct_faces.BY_MODE[mode_b]
        union = set(face_a.VERTEX_IDS) | set(face_b.VERTEX_IDS)
        assert union == all_verts, \
            f"Antipodal pair {mode_a}↔{mode_b} doesn't cover all 6 verts: got {union}"
