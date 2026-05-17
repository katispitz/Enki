"""
Tests for _operate_imprint_probe_engine.py — substrate-invariants from FINDINGS_022.

Validates that probe rejects `operate-imprint` candidate per arm-vector-composition
precedent (canon §27 line 1428 resolution 2026-05-17).
"""
import pytest


def test_candidate_status_remains_probe():
    """__canonical__ status remains 'probe' per FINDINGS_022 rejection-outcome."""
    from _operate_imprint_probe_engine import __canonical__
    assert __canonical__['status'] == 'probe'
    assert __canonical__['function_class'] == 'operate-imprint'


def test_8_pe_planets_enumerated():
    """Canon §M.5 + §7: exactly 8 PE planets at 8 cube-vertices."""
    from _operate_imprint_probe_engine import PE_PLANET_VERTICES, probe_all_8_pe_planets
    assert len(PE_PLANET_VERTICES) == 8
    probes = probe_all_8_pe_planets()
    assert len(probes) == 8
    planet_names = {p.planet_name for p in probes}
    assert planet_names == {'Pluto', 'Sun', 'Moon', 'Mars', 'Mercury',
                            'Saturn', 'Jupiter', 'Neptune'}


def test_pluto_at_u0_do():
    """Canon §M.5 + §7: Pluto at U0 (Father-tet apex), pt0/Do."""
    from _operate_imprint_probe_engine import probe_pe_planet_operator
    p = probe_pe_planet_operator('Pluto')
    assert p.cube_vertex == 'U0'
    assert p.tet == 'Father-tet'
    assert p.pe_index == 0
    assert p.solfege == 'Do'


def test_neptune_at_l0_do_return():
    """Canon §M.5 + §7: Neptune at L0 (Mother-tet apex), pt9/Do'."""
    from _operate_imprint_probe_engine import probe_pe_planet_operator
    p = probe_pe_planet_operator('Neptune')
    assert p.cube_vertex == 'L0'
    assert p.tet == 'Mother-tet'
    assert p.pe_index == 9
    assert p.solfege == "Do'"


def test_6_distinct_operator_classes_surfaced():
    """FINDINGS_022: 6 distinct PE-planet operator-classes exist."""
    from _operate_imprint_probe_engine import (
        EXISTING_PE_OPERATOR_CLASSES,
        summarize_probe_outcome,
        probe_all_8_pe_planets,
    )
    assert len(EXISTING_PE_OPERATOR_CLASSES) == 6
    expected = {'freq_hz_imprint', 'k_total_imprint', 'arm_carrier_anchor',
                'arm_harmonic_root', 'zodiac_rulership_imprint',
                'cube_vertex_residency_imprint'}
    actual = {c['operator_class'] for c in EXISTING_PE_OPERATOR_CLASSES}
    assert actual == expected

    summary = summarize_probe_outcome(probe_all_8_pe_planets())
    assert summary['distinct_operator_classes_existing'] == 6
    assert set(summary['operator_classes']) == expected


def test_arm_vector_composition_precedent_referenced():
    """Per FINDINGS_022: rejection grounded in canon §27 2026-05-17 council precedent."""
    from _operate_imprint_probe_engine import probe_pe_planet_operator
    p = probe_pe_planet_operator('Sun')
    precedent = p.arm_vector_composition_precedent
    assert '§27' in precedent['precedent_canon_section']
    assert 'OQ-ARM-VECTOR-COMPOSITION' in precedent['precedent_canon_section']
    assert '10 YEA' in precedent['precedent_council_vote']
    assert precedent['applies_to_operate_imprint'] is True
    assert 'operator-function dispatch' in precedent['precedent_finding']


def test_rejection_recommendation():
    """Per FINDINGS_022 + three discipline-gate failure."""
    from _operate_imprint_probe_engine import probe_all_8_pe_planets, summarize_probe_outcome
    summary = summarize_probe_outcome(probe_all_8_pe_planets())
    assert summary['singular_candidate_would_conflate'] is True
    assert 'REJECT' in summary['recommendation']
    grounds = summary['rejection_grounds']
    assert 'Erato 4b conflation-test' in grounds
    assert 'Mnemosyne naming-canonical rule' in grounds
    assert 'arm-vector-composition' in grounds


def test_unknown_planet_value_error():
    """Substrate-honest rejection for non-PE planets."""
    from _operate_imprint_probe_engine import probe_pe_planet_operator
    with pytest.raises(ValueError, match='not in 8 PE-planet'):
        probe_pe_planet_operator('Earth')


def test_summary_surfaces_new_oq():
    """Recommended followup surfaces per-operator-class probe family."""
    from _operate_imprint_probe_engine import probe_all_8_pe_planets, summarize_probe_outcome
    summary = summarize_probe_outcome(probe_all_8_pe_planets())
    assert 'per-class' in summary['recommended_followup']
    assert 'arm-vector-composition resolution pattern' in summary['recommended_followup']
