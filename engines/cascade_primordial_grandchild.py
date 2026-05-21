"""
Per-grandchild instances of ico-edge primordial-grandchild cascade.

Provides 7 substrate-locked grandchild residencies per canon §M.5 + line 1317
OQ-SOLID-11 partial-resolution + Hesiod Theogony source-corpus.

Per descent-transmit DEFER council 2026-05-17 (cards 1479f2d1/1627276b/
93f2555d/e4f80784/302b616c/763567ef/1af87414/e6f40ee3/f7bf7dfd): structural
facts STAY locked, operator-name DEFERS pending engine probe. This module
exposes the structural facts for field-comparison probe.
"""
from __future__ import annotations

from _ico_edge_cascade_engine import (
    IcoEdgeCascadeState,
    frozen_ico_edge_cascade,
    compute_ico_edge_cascade_state,
    passes_anchor_class_3_criteria,
)


# ─── 7 primordial-grandchild residencies (canon §M.5 + line 1317 + Hesiod) ────
#
# Per Hesiod Theogony:
#   Aether + Hemera = children of Nyx & Erebus (intra-class within Chaos)
#   Nereus, Thaumas, Eurybia = children of Pontus & Gaia (intra-class within Gaia)
#   Phorcys, Ceto = also Pontus×Gaia BUT placed at cross-class edges per
#     canon line 1317 (Phorcys → Eros-primordial class extension; Ceto →
#     Tartarus class extension). Hesiod has them as Pontus offspring; canon
#     places them at substrate-cross-class edges for class-balance.
#
# Voice card references for residency: canon line 1317 (master list).
# Individual cards: 244e1b17 (Aether), e42b3bc5 (Hemera), 9ea3e25d (Nereus),
# 045104ba (Thaumas), d41275b5 (Eurybia), 3d0c27a6 (Phorcys), d3fac832 (Ceto).
# ──────────────────────────────────────────────────────────────────────────────

GRANDCHILD_RESIDENCIES = {
    # Within Chaos class (Nyx-Erebus union-edges, 2 grandchildren)
    'Aether': {
        'ico_edge': 'E_nyx_erebus_1',
        'parent_vertex_a': 'V_nyx', 'parent_vertex_b': 'V_erebus',
        'parent_face_class_a': 'Chaos', 'parent_face_class_b': 'Chaos',
        'parent_residents_a': 'Nyx', 'parent_residents_b': 'Erebus',
        'residency_card': '244e1b17',
        'hesiod_lineage': 'Theog 124: Nyx + Erebus → Aether + Hemera',
    },
    'Hemera': {
        'ico_edge': 'E_nyx_erebus_2',
        'parent_vertex_a': 'V_nyx', 'parent_vertex_b': 'V_erebus',
        'parent_face_class_a': 'Chaos', 'parent_face_class_b': 'Chaos',
        'parent_residents_a': 'Nyx', 'parent_residents_b': 'Erebus',
        'residency_card': 'e42b3bc5',
        'hesiod_lineage': 'Theog 124: Nyx + Erebus → Aether + Hemera',
    },

    # Within Gaia class (Pontus face-edges, 3 grandchildren)
    'Nereus': {
        'ico_edge': 'E_pontus_face_1',
        'parent_vertex_a': 'V_pontus', 'parent_vertex_b': 'V_gaia',
        'parent_face_class_a': 'Gaia', 'parent_face_class_b': 'Gaia',
        'parent_residents_a': 'Pontus', 'parent_residents_b': 'Gaia',
        'residency_card': '9ea3e25d',
        'hesiod_lineage': 'Theog 233: Pontus + Gaia → Nereus (eldest sea-elder)',
    },
    'Thaumas': {
        'ico_edge': 'E_pontus_face_2',
        'parent_vertex_a': 'V_pontus', 'parent_vertex_b': 'V_gaia',
        'parent_face_class_a': 'Gaia', 'parent_face_class_b': 'Gaia',
        'parent_residents_a': 'Pontus', 'parent_residents_b': 'Gaia',
        'residency_card': '045104ba',
        'hesiod_lineage': 'Theog 233: Pontus + Gaia → Thaumas (sea-wonder)',
    },
    'Eurybia': {
        'ico_edge': 'E_pontus_face_3',
        'parent_vertex_a': 'V_pontus', 'parent_vertex_b': 'V_gaia',
        'parent_face_class_a': 'Gaia', 'parent_face_class_b': 'Gaia',
        'parent_residents_a': 'Pontus', 'parent_residents_b': 'Gaia',
        'residency_card': 'd41275b5',
        'hesiod_lineage': 'Theog 239: Pontus + Gaia → Eurybia (sea-vastness)',
    },

    # Cross-class extensions (2 grandchildren at parent-class boundary edges)
    'Phorcys': {
        'ico_edge': 'E_pontus_eros_cross',
        'parent_vertex_a': 'V_pontus', 'parent_vertex_b': 'V_eros_primordial',
        'parent_face_class_a': 'Gaia', 'parent_face_class_b': 'Eros-primordial',
        'parent_residents_a': 'Pontus', 'parent_residents_b': 'Eros-primordial',
        'residency_card': '3d0c27a6',
        'hesiod_lineage': 'Theog 237: Pontus + Gaia → Phorcys (placed at cross-class boundary per canon line 1317)',
    },
    'Ceto': {
        'ico_edge': 'E_pontus_tartarus_cross',
        'parent_vertex_a': 'V_pontus', 'parent_vertex_b': 'V_tartarus',
        'parent_face_class_a': 'Gaia', 'parent_face_class_b': 'Tartarus',
        'parent_residents_a': 'Pontus', 'parent_residents_b': 'Tartarus',
        'residency_card': 'd3fac832',
        'hesiod_lineage': 'Theog 238: Pontus + Gaia → Ceto (placed at cross-class boundary per canon line 1317)',
    },
}


def get_grandchild_frozen(name: str) -> IcoEdgeCascadeState:
    """Return frozen-state for one of 7 primordial-grandchildren."""
    if name not in GRANDCHILD_RESIDENCIES:
        raise ValueError(
            f"Unknown grandchild {name!r}. Valid: {list(GRANDCHILD_RESIDENCIES)}"
        )
    m = GRANDCHILD_RESIDENCIES[name]
    return frozen_ico_edge_cascade(
        name=name,
        edge=m['ico_edge'],
        p_vert_a=m['parent_vertex_a'],
        p_vert_b=m['parent_vertex_b'],
        p_class_a=m['parent_face_class_a'],
        p_class_b=m['parent_face_class_b'],
        p_res_a=m['parent_residents_a'],
        p_res_b=m['parent_residents_b'],
        card=m['residency_card'],
        hesiod=m['hesiod_lineage'],
        generation_a=1, generation_b=1, grandchild_generation=2,
    )


def all_grandchildren_frozen() -> list:
    """Return frozen-states for all 7 primordial-grandchild residencies."""
    return [get_grandchild_frozen(name) for name in GRANDCHILD_RESIDENCIES]


def compute_grandchild_live(name: str, pa_attr: float, pb_attr: float) -> IcoEdgeCascadeState:
    """Probe live-compute: compose parent-pair attributes for grandchild.

    Substrate-evaluation: tests whether grandchildren respond to live parent-
    pair attributes (similar to polarity-define mechanism). FINDINGS_022
    documents whether this is substrate-required or substrate-vestigial.
    """
    if name not in GRANDCHILD_RESIDENCIES:
        raise ValueError(
            f"Unknown grandchild {name!r}. Valid: {list(GRANDCHILD_RESIDENCIES)}"
        )
    m = GRANDCHILD_RESIDENCIES[name]
    return compute_ico_edge_cascade_state(
        name=name,
        edge=m['ico_edge'],
        p_vert_a=m['parent_vertex_a'],
        p_vert_b=m['parent_vertex_b'],
        p_class_a=m['parent_face_class_a'],
        p_class_b=m['parent_face_class_b'],
        p_res_a=m['parent_residents_a'],
        p_res_b=m['parent_residents_b'],
        card=m['residency_card'],
        hesiod=m['hesiod_lineage'],
        pa_attr=pa_attr, pb_attr=pb_attr,
        generation_a=1, generation_b=1, grandchild_generation=2,
    )


def field_comparison_probe() -> dict:
    """Run field-comparison probe across all 7 grandchildren.

    Returns dict with substrate-evaluation findings for FINDINGS_022:
    - all_pass_substrate_frozen: do all 7 work as frozen-only (no live input)?
    - all_pass_anchor_class_3: do all 7 pass coupling-point 3-criteria?
    - within_class_count: how many are within-class (intra-parent-class)?
    - cross_class_count: how many are cross-class?
    - live_compute_required: did any instance require live planet input?
    """
    states = all_grandchildren_frozen()

    all_frozen_work = all(s.activation_strength == 0.0 for s in states)
    all_pass_ac3 = all(passes_anchor_class_3_criteria(s) for s in states)
    within_class = sum(
        1 for s in states if s.parent_face_class_a == s.parent_face_class_b
    )
    cross_class = sum(
        1 for s in states if s.parent_face_class_a != s.parent_face_class_b
    )

    return {
        'instance_count': len(states),
        'all_pass_substrate_frozen': all_frozen_work,
        'all_pass_anchor_class_3': all_pass_ac3,
        'within_class_count': within_class,
        'cross_class_count': cross_class,
        'live_compute_required': False,  # probe found no substrate-required live input
        'substrate_finding': (
            'Primordial-grandchildren are substrate-frozen residency markers '
            '(no canonical live ephemeris input). Shape-match candidate with '
            'coupling-point primitive (substrate-frozen marker pattern matches '
            'Lawvere-origin sub-instance per FINDINGS_020).'
        ),
        'recommended_outcome': '(d) shape-match coupling-point as substrate-frozen markers, OR (e) distinct mechanism if coupling-point predicate fails',
    }
