"""
Tests for _coupling_point_engine.py + 4 instance modules.

Validates FINDINGS_020 substrate-invariants for OQ-BRANCH-COUPLING-ENGINE
engine-evidence:
  - All 4 instance-classes admit to anchor-class-3 via 3-criteria predicate test
  - Substrate-locked metadata (n_frames, coupling_type, requires_input,
    enumerated_cardinality) varies as documented
  - Substrate-frozen instances (Lawvere, branches) reject compute_coupling_point_live
  - 12-branch enumeration cardinality enforced (canon §15d)
  - Polarity-pairing rule per Card E (canon §15d) preserved per branch
  - Wade-Giles + Pinyin dual-spelling per Mnemosyne discipline 2026-05-17
  - Substrate-frozen branches yield identical canonical_position regardless of call

This test suite captures the engine-evidence per V2.6 rule 9 (Terpsichore
observation) BEFORE council ratification, so future drift is detectable.
"""
import pytest
from dataclasses import fields


# ─── Anchor-class-3 admission criteria (CP6 invariant carried into Enki) ──────

def test_all_4_instances_admit_to_anchor_class_3():
    """All 4 instance-classes pass 3-criteria predicate test per FINDINGS_020."""
    from _coupling_point_engine import passes_anchor_class_3_criteria
    from coupling_rising_sign import rising_sign_frozen
    from coupling_lunar_node import lunar_nodes_frozen
    from coupling_lawvere_origin import lawvere_origin
    from coupling_branch import branch_coupling

    instances = [
        rising_sign_frozen(),
        lunar_nodes_frozen(),
        lawvere_origin(),
        *(branch_coupling(i) for i in range(12)),
    ]
    for state in instances:
        crit = passes_anchor_class_3_criteria(state)
        assert crit['overall_admits_to_anchor_class_3'], (
            f"{state.coupling_name} fails 3-criteria predicate test: {crit}"
        )


def test_3_criteria_individually_held():
    """Per-criterion evidence held across all instances per FINDINGS_020."""
    from _coupling_point_engine import passes_anchor_class_3_criteria
    from coupling_rising_sign import rising_sign_frozen
    from coupling_lunar_node import lunar_nodes_frozen
    from coupling_lawvere_origin import lawvere_origin
    from coupling_branch import branch_coupling

    for state in [rising_sign_frozen(), lunar_nodes_frozen(), lawvere_origin(),
                  branch_coupling(0), branch_coupling(11)]:
        crit = passes_anchor_class_3_criteria(state)
        assert crit['criterion_a_substrate_derived']
        assert crit['criterion_b_independent_canonical_use']
        assert crit['criterion_c_stable_while_constituents_hold']


# ─── Compute-shape-distinct invariants per FINDINGS_020 ───────────────────────

def test_n_frames_distinction():
    """branches couple 4 frames; 3 references couple 2 each (FINDINGS_020)."""
    from coupling_rising_sign import rising_sign_frozen
    from coupling_lunar_node import lunar_nodes_frozen
    from coupling_lawvere_origin import lawvere_origin
    from coupling_branch import branch_coupling

    assert rising_sign_frozen().n_frames == 2
    assert lunar_nodes_frozen().n_frames == 2
    assert lawvere_origin().n_frames == 2
    for i in range(12):
        assert branch_coupling(i).n_frames == 4, (
            f"branch {i} should couple 4 frames per Card 8d8887a1"
        )


def test_coupling_type_distinction():
    """coupling_type varies: singular / pair-180 / enumerated-N (FINDINGS_020)."""
    from coupling_rising_sign import rising_sign_frozen
    from coupling_lunar_node import lunar_nodes_frozen
    from coupling_lawvere_origin import lawvere_origin
    from coupling_branch import branch_coupling

    assert rising_sign_frozen().coupling_type == 'singular'
    assert lunar_nodes_frozen().coupling_type == 'pair-180'
    assert lawvere_origin().coupling_type == 'singular'
    assert branch_coupling(0).coupling_type == 'enumerated-N'


def test_requires_input_distinction():
    """requires_input: True for rising-sign/lunar-nodes; False for Lawvere/branches."""
    from coupling_rising_sign import rising_sign_frozen
    from coupling_lunar_node import lunar_nodes_frozen
    from coupling_lawvere_origin import lawvere_origin
    from coupling_branch import branch_coupling

    assert rising_sign_frozen().requires_input is True
    assert lunar_nodes_frozen().requires_input is True
    assert lawvere_origin().requires_input is False
    for i in range(12):
        assert branch_coupling(i).requires_input is False


def test_enumerated_cardinality_distinction():
    """branches alone have enumerated_cardinality=12; references singular/2."""
    from coupling_rising_sign import rising_sign_frozen
    from coupling_lunar_node import lunar_nodes_frozen
    from coupling_lawvere_origin import lawvere_origin
    from coupling_branch import branch_coupling

    assert rising_sign_frozen().enumerated_cardinality is None
    assert lunar_nodes_frozen().enumerated_cardinality == 2
    assert lawvere_origin().enumerated_cardinality is None
    assert branch_coupling(0).enumerated_cardinality == 12


# ─── Substrate-frozen partial-input rejection (NULL-honest) ───────────────────

def test_substrate_frozen_rejects_live_compute():
    """compute_coupling_point_live on substrate-frozen instance → ValueError."""
    from _coupling_point_engine import compute_coupling_point_live
    from coupling_lawvere_origin import lawvere_origin
    from coupling_branch import branch_coupling

    with pytest.raises(ValueError, match='substrate-frozen'):
        compute_coupling_point_live(lawvere_origin(), {'fake': 'input'})
    with pytest.raises(ValueError, match='substrate-frozen'):
        compute_coupling_point_live(branch_coupling(0), {'fake': 'input'})


# ─── Branch enumeration (canon §15d 12-fold) ─────────────────────────────────

def test_branch_enumeration_cardinality():
    """Exactly 12 branches; index out-of-bound rejected (substrate-enforced)."""
    from coupling_branch import branch_coupling, all_12_branches, BRANCHES

    assert len(BRANCHES) == 12
    assert len(all_12_branches()) == 12
    for i in range(12):
        b = branch_coupling(i)
        assert b.enumerated_cardinality == 12

    with pytest.raises(ValueError, match='substrate-enforced cardinality'):
        branch_coupling(12)
    with pytest.raises(ValueError, match='substrate-enforced cardinality'):
        branch_coupling(-1)


def test_branch_substrate_frozen_repeatability():
    """Substrate-frozen branches yield identical canonical_position across calls."""
    from coupling_branch import branch_coupling

    for i in range(12):
        a = branch_coupling(i)
        b = branch_coupling(i)
        assert a.canonical_position == b.canonical_position
        assert a.coupled_frames == b.coupled_frames


# ─── Polarity-pairing rule per Card E (canon §15d) ────────────────────────────

def test_yang_branches_pair_only_yang_stems():
    """Card E: yang stems pair only yang branches (polarity-locked)."""
    from coupling_branch import BRANCHES

    YANG_STEMS = {'Jiǎ', 'Bǐng', 'Wù', 'Gēng', 'Rén'}
    YIN_STEMS  = {'Yǐ', 'Dīng', 'Jǐ', 'Xīn', 'Guǐ'}

    for (pinyin, _wg, _beast, polarity, _compass, _hs, _he, _elem, stem_yang, stem_yin) in BRANCHES:
        if polarity == 'yang' and stem_yang is not None:
            assert stem_yang in YANG_STEMS, (
                f"Yang branch {pinyin} paired with non-yang stem {stem_yang}"
            )
            assert stem_yin is None, (
                f"Yang branch {pinyin} has yin-stem pairing: {stem_yin}"
            )
        if polarity == 'yin' and stem_yin is not None:
            assert stem_yin in YIN_STEMS, (
                f"Yin branch {pinyin} paired with non-yin stem {stem_yin}"
            )
            assert stem_yang is None, (
                f"Yin branch {pinyin} has yang-stem pairing: {stem_yang}"
            )


def test_xu_hai_no_stem_in_cycle_1():
    """Canon §15d: Xū and Hài lack cycle-1 stem (stem-cycle restarts at Jiǎ + branch 11)."""
    from coupling_branch import branch_coupling

    xu = branch_coupling(10)
    assert xu.canonical_position['pinyin'] == 'Xū'
    assert xu.canonical_position['cyclic_stem_pair'] is None
    assert xu.canonical_position['elemental_wu_xing'] is None

    hai = branch_coupling(11)
    assert hai.canonical_position['pinyin'] == 'Hài'
    assert hai.canonical_position['cyclic_stem_pair'] is None
    assert hai.canonical_position['elemental_wu_xing'] is None


def test_wade_giles_pinyin_dual_spelling():
    """Mnemosyne discipline 2026-05-17: both spellings preserved per branch."""
    from coupling_branch import branch_coupling, BRANCHES

    for i, (pinyin, wg, *_) in enumerate(BRANCHES):
        b = branch_coupling(i)
        assert b.canonical_position['pinyin'] == pinyin
        assert b.canonical_position['wade_giles'] == wg


# ─── Cardinal-direction substrate alignment per Universal Order p.221 ─────────

def test_cardinal_branch_alignments():
    """Canon §15d / source-anchor Card fc2d1d3b: cardinal direction alignments."""
    from coupling_branch import branch_by_pinyin

    # E = sunrise (Mǎo); S = noon (Wǔ); W = sunset (Yǒu); N = midnight (Zǐ)
    assert branch_by_pinyin('Zǐ').canonical_position['spatial_compass']  == 'N'
    assert branch_by_pinyin('Mǎo').canonical_position['spatial_compass'] == 'E'
    assert branch_by_pinyin('Wǔ').canonical_position['spatial_compass']  == 'S'
    assert branch_by_pinyin('Yǒu').canonical_position['spatial_compass'] == 'W'


# ─── Rising-sign live compute ─────────────────────────────────────────────────

def test_rising_sign_live_kati_natal():
    """ASC=45.5° → rising-sign idx=1 (Taurus), per canon §22."""
    from coupling_rising_sign import rising_sign_live

    rs = rising_sign_live(45.5)
    assert rs.live_position['zodiac_segment_idx'] == 1
    assert rs.live_position['zodiac_segment_name'] == 'Taurus'
    assert rs.requires_input is True


def test_rising_sign_normalization():
    """ASC values outside [0, 360) normalize correctly."""
    from coupling_rising_sign import rising_sign_live

    rs = rising_sign_live(405.5)  # = 45.5
    assert rs.live_position['zodiac_segment_idx'] == 1


# ─── Lunar-nodes live compute (CP4 invariant) ─────────────────────────────────

def test_lunar_nodes_180_degree_invariant():
    """CP4: Rahu/Ketu always 180° apart per orbital-plane × ecliptic geometry."""
    from coupling_lunar_node import lunar_nodes_live

    for rahu_test in [0.0, 45.0, 90.0, 180.0, 270.0, 359.9]:
        ln = lunar_nodes_live(rahu_test)
        diff = abs((ln.live_position['ketu_lon'] - ln.live_position['rahu_lon']) % 360 - 180)
        assert diff < 1e-9, f"Rahu={rahu_test}: separation drift {diff}"


# ─── Lawvere-origin substrate-locked invariant ────────────────────────────────

def test_lawvere_origin_is_substrate_zero():
    """Canon line 1275: Lawvere fixed point at (0,0,0) Merkaba center."""
    from coupling_lawvere_origin import lawvere_origin

    lv = lawvere_origin()
    assert lv.canonical_position['x'] == 0.0
    assert lv.canonical_position['y'] == 0.0
    assert lv.canonical_position['z'] == 0.0
    assert lv.requires_input is False


# ─── Canonical declaration status ─────────────────────────────────────────────

def test_canonical_status_remains_probe():
    """__canonical__ status MUST remain 'probe' until council ratification (gate 5)."""
    from _coupling_point_engine import __canonical__

    assert __canonical__['status'] == 'probe', (
        "Per FINDINGS_020 / SDEC step 5 / V2.7 §VALIDATION DISCIPLINE: status "
        "must remain 'probe' until council ratifies anchor-class-3 promotion to §30. "
        "If this test fails, council must have convened — update FINDINGS_020 + this test."
    )


def test_canonical_function_class_is_candidate():
    """function_class is candidate name pending council; Erato 4b may rename."""
    from _coupling_point_engine import __canonical__

    assert __canonical__['function_class'] == 'coupling-point-anchor'  # CANDIDATE
