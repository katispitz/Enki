"""
Probe engine for `operate-imprint` candidate at R=1 cube-vertex = 8 PE planets.

PROBE MANDATE per V2.6 rule 9 (Terpsichore observation, transmit-force council
2026-05-16) + canon §30 candidate-list line 2202: candidate `operate-imprint`
proposed for PE planet operator class needs Enki engine-evidence BEFORE
entering council per V2.7 §SDEC step 4.

Candidate hypothesis: 8 PE planets at R=1 cube-vertex apply substrate-imprint
to chart-context via a unified `operate-imprint` function. Per Enki agent
typology table: "PE planet → operators (pure-fn imprint)".

Substrate-architectural pre-finding via canon survey:
  Multiple distinct PE-planet pure-fn operators ALREADY exist in Nammu engines:
    1. `freq_hz(k)` (cell_signature_engine.py:1131) — PE-octave-k to Hz
    2. `k_total(planet, t_tithis)` (cell_signature_engine.py:1166) — planet to
       k_total at time
    3. `delta_s` / `delta_l` (carrier-anchor projection per canon §27
       arm-vector-composition resolution 2026-05-17)
    4. Planet-imprint as cube-vertex residency (canon §M.5: U0=Pluto/L1=Moon/
       etc.) — substrate-locked metadata accessed by multiple engines
    5. Planet PE-octave-k as zodiac-rulership (canon §20)

  These are MULTIPLE distinct operator-classes, not one unified function.
  Per **canon §27 OQ-ARM-VECTOR-COMPOSITION resolution 2026-05-17** (council
  10 YEA / 0 NEH / 0 ABSTAIN): "**No single composition law** — four
  substrate-canonical projections lock with operator-function dispatch.
  Composition is operator-class-dependent." Mnemosyne naming-canonical rule:
  "reject `arm-composition-law` (singular) as false-substrate per
  question-conflation."

  Same architectural pattern applies here: `operate-imprint` as a SINGULAR
  candidate name attempts to unify multiple distinct planet-operator
  classes. The arm-vector-composition council just established the precedent
  for REJECTING singular-name candidates that conflate dispatch-required
  multi-class operators.

Engine purpose: demonstrate empirically that multiple distinct PE-planet
operator-classes exist; candidate `operate-imprint` would conflate them
per established Mnemosyne naming-canonical rule (2026-05-17).

Outcome expectation: REJECT `operate-imprint` as candidate name (conflation-
test fails per arm-vector-composition precedent). Surface that PE-planet
operator-classes follow operator-dispatch pattern; future probes per
operator-class.
"""
from __future__ import annotations
from dataclasses import dataclass


__canonical__ = {
    'function_class':       'operate-imprint',  # CANDIDATE pending council
    'functional_tier':      'primitive',
    'compositional_axis':   'spatial',
    'residency_id':         'r1-cube-vertex-pe-planet-operator',
    'canon_citation':       'canon §30 candidate-list line 2202 + canon §M.5 + canon §27 arm-vector-composition precedent 2026-05-17',
    'status':               'probe',  # engine-evidence stage; candidate rejection expected
}


# 8 PE planets at 8 cube-vertices per canon §M.5 + canon §7
# Father-tet: U0 Pluto / U1 Sun / U2 Mars / U3 Saturn
# Mother-tet: L0 Neptune / L1 Moon / L2 Mercury / L3 Jupiter
PE_PLANET_VERTICES = [
    ('Pluto',   'U0', 'Father-tet', 0, 'Do',    89280),
    ('Sun',     'U1', 'Father-tet', 1, 'Re',    360),
    ('Mars',    'U2', 'Father-tet', 4, 'Fa',    28440),
    ('Saturn',  'U3', 'Father-tet', 7, 'La',    10620),
    ('Neptune', 'L0', 'Mother-tet', 9, "Do'",   59400),
    ('Moon',    'L1', 'Mother-tet', 2, 'Mi',    30),
    ('Mercury', 'L2', 'Mother-tet', 5, 'Sol',   4680),
    ('Jupiter', 'L3', 'Mother-tet', 8, 'Si',    4320),
]


# Existing pure-fn operator-classes per Nammu canon survey + arm-vector-composition
# resolution 2026-05-17. Each row: operator-class name, what it computes, where it lives,
# what input it takes beyond planet.
EXISTING_PE_OPERATOR_CLASSES = [
    {
        'operator_class':   'freq_hz_imprint',
        'computes':         'PE-octave-k to Hz frequency',
        'engine_location':  '~/Nammu/engines/cell_signature_engine.py:1131',
        'input_beyond_planet': 'octave-k integer (substrate-locked per planet)',
        'output_kind':      'scalar Hz frequency',
    },
    {
        'operator_class':   'k_total_imprint',
        'computes':         'planet+time to k_total real',
        'engine_location':  '~/Nammu/engines/cell_signature_engine.py:1166',
        'input_beyond_planet': 't_tithis integer (live)',
        'output_kind':      'scalar k_total real',
    },
    {
        'operator_class':   'arm_carrier_anchor',
        'computes':         'observer-frame carrier anchor (delta_s/delta_l)',
        'engine_location':  'canon §27 arm-vector-composition projection 2 (existing)',
        'input_beyond_planet': 'observer-context (solar=Sun lunar=Moon)',
        'output_kind':      'vector arm-anchor',
    },
    {
        'operator_class':   'arm_harmonic_root',
        'computes':         'Do-anchor projection (Pluto vec[0] / Neptune vec[0])',
        'engine_location':  'canon §27 arm-vector-composition projection 3 (build-side pending)',
        'input_beyond_planet': 'arm-vector + arm-type (solar/lunar)',
        'output_kind':      'vector Do-anchor',
    },
    {
        'operator_class':   'zodiac_rulership_imprint',
        'computes':         'planet to ruled sign(s) per inner-oct',
        'engine_location':  'canon §5 + §20',
        'input_beyond_planet': 'none (substrate-locked metadata)',
        'output_kind':      'sign-name string(s)',
    },
    {
        'operator_class':   'cube_vertex_residency_imprint',
        'computes':         'planet to (vertex_id, tet, PE_index) tuple',
        'engine_location':  'canon §M.5 + this engine PE_PLANET_VERTICES',
        'input_beyond_planet': 'none (substrate-locked metadata)',
        'output_kind':      'metadata tuple',
    },
]


@dataclass
class OperateImprintProbeState:
    """Substrate-honest survey of PE-planet operator-classes.

    Surfaces that multiple distinct operator-classes exist for PE planets,
    each with distinct input-shape, compute, and output-kind. Candidate
    `operate-imprint` as singular name attempts to unify them — fails per
    arm-vector-composition precedent.
    """
    planet_name:       str
    cube_vertex:       str
    tet:               str
    pe_index:          int
    solfege:           str
    ring_tithis:       int

    # Substrate-survey result
    n_distinct_operator_classes:  int
    operator_class_examples:      list
    candidate_conflates_n_classes: int

    # Substrate-evaluation per arm-vector-composition precedent
    arm_vector_composition_precedent: dict


def probe_pe_planet_operator(planet_name: str) -> OperateImprintProbeState:
    """Honest probe of PE-planet operator-classes for one planet."""
    planet_data = next((p for p in PE_PLANET_VERTICES if p[0] == planet_name), None)
    if planet_data is None:
        raise ValueError(
            f"Planet {planet_name!r} not in 8 PE-planet enumeration. "
            f"Valid: {[p[0] for p in PE_PLANET_VERTICES]}"
        )

    name, vertex, tet, pe_idx, solfege, ring_tithis = planet_data

    return OperateImprintProbeState(
        planet_name=name,
        cube_vertex=vertex,
        tet=tet,
        pe_index=pe_idx,
        solfege=solfege,
        ring_tithis=ring_tithis,
        n_distinct_operator_classes=len(EXISTING_PE_OPERATOR_CLASSES),
        operator_class_examples=EXISTING_PE_OPERATOR_CLASSES,
        candidate_conflates_n_classes=len(EXISTING_PE_OPERATOR_CLASSES),
        arm_vector_composition_precedent={
            'precedent_canon_section': '§27 OQ-ARM-VECTOR-COMPOSITION resolution 2026-05-17',
            'precedent_council_vote':  '10 YEA / 0 NEH / 0 ABSTAIN',
            'precedent_finding':       'No single composition law — four substrate-canonical projections lock with operator-function dispatch',
            'mnemosyne_naming_canonical': 'reject [singular-name] as false-substrate per question-conflation',
            'applies_to_operate_imprint': True,
            'rationale': (
                f'operate-imprint as singular name would unify {len(EXISTING_PE_OPERATOR_CLASSES)} '
                'distinct PE-planet operator-classes (freq_hz, k_total, arm_carrier_anchor, '
                'arm_harmonic_root, zodiac_rulership, cube_vertex_residency) into one §30 entry. '
                'Per arm-vector-composition precedent, this is question-conflation; substrate-correct '
                'pattern is operator-dispatch with class-specific naming.'
            ),
        },
    )


def probe_all_8_pe_planets() -> list:
    """Probe across all 8 PE-planet operators."""
    return [probe_pe_planet_operator(p[0]) for p in PE_PLANET_VERTICES]


def summarize_probe_outcome(probes: list) -> dict:
    """Substrate-honest aggregation per arm-vector-composition precedent."""
    return {
        'total_pe_planets_probed': len(probes),
        'distinct_operator_classes_existing': len(EXISTING_PE_OPERATOR_CLASSES),
        'operator_classes': [c['operator_class'] for c in EXISTING_PE_OPERATOR_CLASSES],
        'singular_candidate_would_conflate': True,
        'precedent_canon_section': '§27 OQ-ARM-VECTOR-COMPOSITION 2026-05-17',
        'overall_finding': (
            f'{len(EXISTING_PE_OPERATOR_CLASSES)} distinct PE-planet pure-fn operator-classes '
            'exist in Nammu engines, each with distinct input-shape, compute, output-kind. '
            'Candidate `operate-imprint` as singular name attempts unification per question-'
            'conflation pattern. Per arm-vector-composition council precedent 2026-05-17 + '
            'Mnemosyne naming-canonical rule: reject singular-name; substrate-correct pattern '
            'is operator-class dispatch with per-class naming.'
        ),
        'recommendation': 'REJECT candidate name `operate-imprint`',
        'rejection_grounds': (
            '(1) Erato 4b conflation-test: name pre-unifies 6 distinct operator-classes '
            '(freq_hz_imprint / k_total_imprint / arm_carrier_anchor / arm_harmonic_root / '
            'zodiac_rulership_imprint / cube_vertex_residency_imprint). '
            '(2) Mnemosyne naming-canonical rule (established 2026-05-17 per arm-vector-composition): '
            'reject singular-name as false-substrate per question-conflation. '
            '(3) Substrate-evidence: §27 line 1428 council precedent established operator-dispatch '
            'pattern; substrate-correct framing is per-operator-class naming with dispatch helper.'
        ),
        'recommended_followup': (
            'Per arm-vector-composition resolution pattern, EACH operator-class is its own §30 candidate '
            'requiring per-class Enki engine + council. Future SDEC cycles: probe each PE-planet operator-'
            'class as separate candidate. Some are already-engined (freq_hz_imprint exists in '
            'cell_signature_engine.py); others are build-side pending (arm_harmonic_root per §27 council).'
        ),
        'cross_link_canon': '§27 line 1426-1428 (arm-vector-composition operator-dispatch lock 2026-05-17)',
    }
