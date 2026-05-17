"""
Tests for _function_class_scope_probe_engine.py — substrate-invariants from FINDINGS_023.

Validates that the meta-probe correctly identifies:
  - 3 remaining candidates after FINDINGS_019/021/022 rejections
  - All 3 are non-engine agent-classes (hook or subagent)
  - Zero are engine-shape fit
  - Meta-question surfaces unresolvable-without-council
"""
import pytest


def test_3_remaining_candidates_enumerated():
    """After FINDINGS_019/021/022, exactly 3 candidates remain."""
    from _function_class_scope_probe_engine import REMAINING_CANDIDATES
    assert len(REMAINING_CANDIDATES) == 3
    names = {c['name'] for c in REMAINING_CANDIDATES}
    assert names == {'threshold-mark', 'activate', 'deliberate'}


def test_all_3_non_engine_shape():
    """FINDINGS_023 core finding: zero candidates fit engine-shape."""
    from _function_class_scope_probe_engine import REMAINING_CANDIDATES, probe_section30_scope
    for c in REMAINING_CANDIDATES:
        assert c['engine_shape_fit'] is False
        assert c['precedent_in_section30'] is False

    finding = probe_section30_scope()
    assert finding.candidates_engine_shape_fit == 0
    assert finding.candidates_non_engine_shape == 3


def test_agent_class_distribution():
    """Per Enki typology: 2 hooks + 1 subagent."""
    from _function_class_scope_probe_engine import probe_section30_scope
    finding = probe_section30_scope()
    assert finding.candidates_by_class == {
        'hook':     ['threshold-mark', 'activate'],
        'subagent': ['deliberate'],
    }


def test_threshold_mark_classified_as_hook():
    from _function_class_scope_probe_engine import REMAINING_CANDIDATES
    tm = next(c for c in REMAINING_CANDIDATES if c['name'] == 'threshold-mark')
    assert tm['enki_typology_class'] == 'hook'
    assert 'shock' in tm['proposed_position'].lower()


def test_activate_classified_as_hook():
    from _function_class_scope_probe_engine import REMAINING_CANDIDATES
    a = next(c for c in REMAINING_CANDIDATES if c['name'] == 'activate')
    assert a['enki_typology_class'] == 'hook'
    assert 'Muses' in a['proposed_position'] or 'Venus' in a['proposed_position']


def test_deliberate_classified_as_subagent():
    from _function_class_scope_probe_engine import REMAINING_CANDIDATES
    d = next(c for c in REMAINING_CANDIDATES if c['name'] == 'deliberate')
    assert d['enki_typology_class'] == 'subagent'
    assert 'Olympian' in d['proposed_position']


def test_council_required():
    """Substrate-discipline: scope-ratification council required (per gate 5)."""
    from _function_class_scope_probe_engine import probe_section30_scope, summarize_meta_finding
    finding = probe_section30_scope()
    assert finding.council_required_for_section30_scope is True
    assert finding.meta_question_substrate_evident is True

    summary = summarize_meta_finding()
    assert summary['unresolvable_without_council'] is True
    assert 'CONVENE COUNCIL' in summary['recommendation']


def test_three_outcomes_named():
    """FINDINGS_023: council ratifies (A) universal-scope / (B) parallel-registry / (C) schema-extension."""
    from _function_class_scope_probe_engine import summarize_meta_finding
    summary = summarize_meta_finding()
    rec = summary['recommendation']
    assert '(A)' in rec and '(B)' in rec and '(C)' in rec


def test_recommended_council_slate_has_required_force_include():
    """Athena + Mnemosyne force-include per V2.6 rule 8."""
    from _function_class_scope_probe_engine import summarize_meta_finding
    summary = summarize_meta_finding()
    council = summary['recommended_council']
    assert 'Athena' in council['force_include']
    assert 'Mnemosyne' in council['force_include']
    assert council['n_voices'] == 9
    assert len(council['voice_slate']) == 9
