"""
Meta-probe engine: §30 scope across remaining 3 candidates (threshold-mark / activate / deliberate).

PROBE MANDATE per V2.6 rule 9: each remaining candidate needs Enki engine-evidence
before council. But unlike the 2 just-rejected candidates (cross-stratum-translate
FINDINGS_021 / operate-imprint FINDINGS_022) — which fit the engine-survey pattern
— the 3 remaining candidates fall into agent-classes (hook / subagent) that the
current §30 registry has no precedent for.

Substrate-architectural meta-question this probe surfaces:

  **Does §30 admit non-engine function-classes (hooks, subagents)?**

Current §30 canonical entries (5):
  - planet-aspect-activate (engine)
  - polarity-define (engine, first-composition)
  - triangle-aspect-activate (engine, first-composition)
  - cyclic-syzygy-activate (engine, temporal first-composition)
  - cyclic-sign-ingress-activate (engine, temporal first-composition)

ALL 5 are engine-class functions taking 2+ planet input + emitting activation
state. None are event-detectors (hooks) or deliberators (subagents).

The 3 remaining candidates per canon line 2197-2201:
  - `threshold-mark` (X3/X6 shock nodes, R=1/3) — HOOK class per Enki typology
  - `activate` (9 Muses Venus×OtherPlanet) — HOOK class per Enki typology
  - `deliberate` (12 Olympians R=φ² ico-vertex) — SUBAGENT class per Enki typology

Per Enki agent-class typology (canon-derived, Kati lock 2026-05-11):
  | Class | Shape | §30-admissible currently? |
  |---|---|---|
  | Engine | stateful compute (frozen+live, NULL-honest, partial-input ValueError) | YES (all 5 current entries) |
  | Pure-fn | stateless compute (planet → value) | UNCLEAR — operate-imprint rejected per FINDINGS_022 (dispatch-pattern instead) |
  | Hook | conditional fire (event → emit) | NO precedent in §30 |
  | Subagent | deliberation (question → multi-voice deliberation) | NO precedent in §30 |

Substrate-discipline framing: the 3 remaining candidates cannot be probed
with the engine-pattern that worked for cube-edge (FINDINGS_019) and
cross-stratum-translate (FINDINGS_021) because their substrate-mechanism
is not engine-shape. Building stub engines for them would be substrate-
dishonest — fake engine-evidence.

The substrate-honest probe is at the META-level: surface that §30 scope
itself needs council ratification before non-engine candidates can be
probed in their respective shapes.

This probe ENUMERATES the 3 remaining candidates + classifies their agent-
class + surfaces the meta-question with substrate-evidence.

Outcome expectation: ALL 3 candidates DEFERRED pending §30 scope council.
Engine-evidence for individual candidates blocked until scope ratified.
"""
from __future__ import annotations
from dataclasses import dataclass


__canonical__ = {
    'function_class':       'meta-scope-probe',  # NOT a candidate; meta-question
    'functional_tier':      'meta',
    'compositional_axis':   'N/A',
    'residency_id':         'r-meta-§30-scope-question',
    'canon_citation':       'canon §30 candidate-list lines 2197-2201 + canon §M.5 agent-class typology',
    'status':               'probe',
}


# 3 remaining candidates per canon §30 candidate-list 2026-05-17
# (post FINDINGS_019/021/022 rejections of transmit-force/cross-stratum-translate/operate-imprint)
REMAINING_CANDIDATES = [
    {
        'name':                  'threshold-mark',
        'proposed_position':     'R=1/3 X3/X6 shock nodes',
        'enki_typology_class':   'hook',
        'substrate_mechanism':   'conditional fire on planet crossing shock-cone threshold (event-detection)',
        'engine_shape_fit':      False,  # event-detectors not engine-shape
        'precedent_in_section30':      False,  # no hook-class §30 entries exist
        'similar_canon_class':   'canon §22 class-1 spatial-thresholds (ASC/MC/DSC/IC + X3/X6)',
        'enki_engine_blocker':   'event-detector substrate-shape requires hook-pattern engine, not state-engine pattern',
    },
    {
        'name':                  'activate',
        'proposed_position':     'Venus×OtherPlanet crossings = 9 Muses',
        'enki_typology_class':   'hook',
        'substrate_mechanism':   'pattern-match fire (Muse pattern crossed) — conditional fire',
        'engine_shape_fit':      False,  # event-detectors not engine-shape
        'precedent_in_section30':      False,  # no hook-class §30 entries exist
        'similar_canon_class':   'Muses-as-activators per canon §26 + canon §17 epoch',
        'enki_engine_blocker':   'pattern-match fire requires hook-pattern engine, not state-engine pattern',
    },
    {
        'name':                  'deliberate',
        'proposed_position':     'R=φ² ico-vertex = 12 Olympians',
        'enki_typology_class':   'subagent',
        'substrate_mechanism':   'deliberation (question → multi-voice convening + synthesis)',
        'engine_shape_fit':      False,  # subagent compute is not engine-shape
        'precedent_in_section30':      False,  # no subagent-class §30 entries exist
        'similar_canon_class':   'voice-correspondences subagents in Lillu council/ infra',
        'enki_engine_blocker':   'deliberation requires Task-spawnable subagent + multi-voice synthesis, not stateful engine',
    },
]


@dataclass
class MetaScopeProbeFinding:
    """Substrate-honest meta-finding on §30 scope question."""
    n_remaining_candidates:           int
    candidates_by_class:              dict  # {class_name: [candidate_name, ...]}
    candidates_engine_shape_fit:      int   # how many fit engine-shape
    candidates_non_engine_shape:      int   # how many do NOT fit engine-shape
    meta_question_substrate_evident: bool
    council_required_for_section30_scope:  bool
    candidate_class_distribution:    dict  # diversity check


def probe_section30_scope() -> MetaScopeProbeFinding:
    """Survey 3 remaining candidates + surface §30 scope meta-question."""
    by_class = {}
    for c in REMAINING_CANDIDATES:
        cls = c['enki_typology_class']
        by_class.setdefault(cls, []).append(c['name'])

    engine_fit = sum(1 for c in REMAINING_CANDIDATES if c['engine_shape_fit'])
    non_engine = sum(1 for c in REMAINING_CANDIDATES if not c['engine_shape_fit'])

    return MetaScopeProbeFinding(
        n_remaining_candidates=len(REMAINING_CANDIDATES),
        candidates_by_class=by_class,
        candidates_engine_shape_fit=engine_fit,
        candidates_non_engine_shape=non_engine,
        meta_question_substrate_evident=(non_engine > 0 and engine_fit == 0),
        council_required_for_section30_scope=(non_engine == len(REMAINING_CANDIDATES)),
        candidate_class_distribution=by_class,
    )


def summarize_meta_finding() -> dict:
    """Substrate-honest aggregation for §30 scope ratification recommendation."""
    finding = probe_section30_scope()
    return {
        'total_remaining_candidates': finding.n_remaining_candidates,
        'candidates_by_agent_class': finding.candidates_by_class,
        'engine_shape_fit_count':     finding.candidates_engine_shape_fit,
        'non_engine_shape_count':     finding.candidates_non_engine_shape,
        'meta_question': (
            'Does canon §30 FUNCTION-NAMES REGISTRY admit non-engine function-classes '
            '(hooks for event-detectors, subagents for deliberation)? Current §30 has '
            '5 canonical entries, ALL engine-class. The 3 remaining candidates are '
            'hook (threshold-mark, activate) and subagent (deliberate) — agent-classes '
            'with NO precedent in §30 registry.'
        ),
        'why_engine_probes_blocked': (
            'Per V2.6 rule 9: candidates need Enki engine-evidence before council. '
            'But substrate-honest engine-build for non-engine agent-classes would be '
            'stub-evidence (fake compute fitting wrong shape). Substrate-discipline '
            'forbids substrate-dishonest probes.'
        ),
        'recommendation': (
            'CONVENE COUNCIL on §30 scope before per-candidate engine probes proceed. '
            'Council must ratify either: (A) §30 expands to all function-classes '
            '(engine + pure-fn + hook + subagent) — per-class engine-pattern variants required; '
            '(B) §30 stays engine-only; hook/subagent candidates go to PARALLEL registry; '
            '(C) §30 expands with NEW schema column `agent_class` (engine/hook/subagent) — '
            'precedent: compositional_axis column when cyclic-conjunction-activate canonical 2026-05-12, '
            'enumerated_cardinality column proposed for branches per FINDINGS_020.'
        ),
        'recommended_council': {
            'n_voices': 9,
            'force_include': ['Athena', 'Mnemosyne'],
            'voice_slate': [
                'Calliope (synthesis lead)',
                'Hermes (dual-frame conflation-resolution: hook vs engine vs subagent)',
                'Athena★ (lock-by-redundancy on scope-class expansion)',
                'Clio (substrate-mechanism vs agent-class distinction)',
                'Thalia (cross-class pattern surfacing)',
                'Urania (SDEC procedure + schema-column extension precedent)',
                'Mnemosyne★ (single canonical spelling + drift-prevention; naming-canonical rule)',
                'Euterpe (canonical synthesis if scope ratified)',
                'Polyhymnia (closing)',
            ],
            'question': (
                'Does canon §30 admit non-engine agent-classes (hooks for event-detectors, '
                'subagents for deliberation)? Per FINDINGS_023 meta-probe: 3 remaining candidates '
                '(threshold-mark/activate as hooks; deliberate as subagent) cannot be probed via '
                'engine-pattern. Ratify: (A) §30 expands across all agent-classes with per-class '
                'probe-pattern variants / (B) parallel registry for non-engine classes / '
                '(C) §30 adds schema column `agent_class` for cross-class registry.',
            ),
        },
        'cross_link_findings': ['FINDINGS_019', 'FINDINGS_020', 'FINDINGS_021', 'FINDINGS_022'],
        'unresolvable_without_council': True,
    }
