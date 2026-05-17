"""
Tests for _stratum_translate_probe_engine.py — substrate-invariants from FINDINGS_021.

Validates that the probe REJECTS `cross-stratum-translate` candidate at all
4 V2.5 bridges:
  - 3 midpoint bridges (Harmonia/Hermaphroditus/Erichthonius): no cross-stratum-axis
  - 1 octave-wrap bridge (Persephone): temporal mechanism, MISFITS spatial candidate framing
  - Spatial cross-stratum-translation mechanism: FOUND NOWHERE

Plus invariants on:
  - Candidate status remains 'probe' (engine-evidence stage only)
  - Probe surfaces new OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE
"""
import pytest


def test_candidate_status_remains_probe():
    """__canonical__ status MUST remain 'probe' per FINDINGS_021 (rejection outcome)."""
    from _stratum_translate_probe_engine import __canonical__
    assert __canonical__['status'] == 'probe'
    assert __canonical__['function_class'] == 'cross-stratum-translate'


def test_all_4_v25_bridges_probed():
    """4 V2.5 bridges per bridges.py + Persephone card 141b8d7f."""
    from _stratum_translate_probe_engine import V25_BRIDGE_INSTANCES, probe_all_v25_bridges
    assert len(V25_BRIDGE_INSTANCES) == 4
    probes = probe_all_v25_bridges()
    assert len(probes) == 4
    names = {p.bridge_name for p in probes}
    assert names == {'Harmonia', 'Hermaphroditus', 'Erichthonius', 'Persephone'}


def test_midpoint_bridges_no_translation_axis():
    """Per FINDINGS_021: 3 midpoint bridges have translation_axis=None."""
    from _stratum_translate_probe_engine import probe_all_v25_bridges
    probes = probe_all_v25_bridges()
    midpoint_bridges = [p for p in probes if p.bridge_name != 'Persephone']
    assert len(midpoint_bridges) == 3
    for p in midpoint_bridges:
        assert p.translation_axis is None
        assert p.source_stratum == p.target_stratum  # both Olympian (same stratum)
        assert p.translation_magnitude is None
        assert p.translation_active is False


def test_persephone_temporal_axis_misfits_candidate():
    """Per FINDINGS_021: Persephone has temporal mechanism (NOT spatial as candidate frames)."""
    from _stratum_translate_probe_engine import probe_all_v25_bridges
    probes = probe_all_v25_bridges()
    persephone = next(p for p in probes if p.bridge_name == 'Persephone')
    assert persephone.translation_axis == 'temporal'  # NOT 'spatial'
    assert persephone.source_stratum != persephone.target_stratum  # Si vs Do (cross-pole)
    # candidate name `cross-stratum-translate` frames as spatial; misfit documented
    assert 'temporal' in persephone.candidate_substrate_evaluation['finding'].lower()
    assert 'cyclic-syzygy-activate' in persephone.candidate_substrate_evaluation['better_§30_fit']


def test_no_spatial_cross_stratum_mechanism_found():
    """FINDINGS_021 core finding: no bridge surfaces spatial cross-stratum-translation."""
    from _stratum_translate_probe_engine import probe_all_v25_bridges, summarize_probe_outcome
    probes = probe_all_v25_bridges()
    summary = summarize_probe_outcome(probes)
    assert summary['spatial_translation_mechanism_found'] is False
    assert summary['midpoint_bridges_no_translation_mechanism'] == 3
    assert summary['octave_wrap_bridges_temporal_mechanism'] == 1


def test_rejection_recommendation():
    """Per FINDINGS_021 + three-discipline-gate failure."""
    from _stratum_translate_probe_engine import probe_all_v25_bridges, summarize_probe_outcome
    summary = summarize_probe_outcome(probe_all_v25_bridges())
    assert 'REJECT' in summary['recommendation']
    grounds = summary['rejection_grounds']
    assert 'Erato 4b conflation-test' in grounds
    assert 'Athena residency-binding' in grounds
    assert 'planet-aspect-activate' in grounds  # 3/4 already covered


def test_new_oq_persephone_surfaced():
    """Probe surfaces OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE for separate SDEC."""
    from _stratum_translate_probe_engine import probe_all_v25_bridges, summarize_probe_outcome
    summary = summarize_probe_outcome(probe_all_v25_bridges())
    assert 'OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE' in summary['new_oq_surfaced']


def test_unknown_bridge_config_value_error():
    """Substrate-honest rejection for unknown bridge configurations."""
    from _stratum_translate_probe_engine import probe_bridge_for_stratum_translation
    with pytest.raises(ValueError, match='Substrate-incomplete'):
        probe_bridge_for_stratum_translation(
            'unknown-bridge', 'midpt(?)', ('X1', 'Y1'),  # non-V parent IDs
            ('Foo', 'Bar'), 'TBD', is_octave_wrap_bridge=False,
        )
