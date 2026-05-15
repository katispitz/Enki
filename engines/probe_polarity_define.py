"""
Cross-R-tier residency probe for `polarity-define` function-name candidate.

Tests whether the cube-face pair-class function (cube Primordial pair-engine)
also operates at inner-oct face-pair-class (inner-oct pair-engine). Cross-R-tier
match would graduate `polarity-define` from candidate-single-residency-class
to canonical via Athena lock-by-redundancy criterion.

Two candidate pair-class function-shapes:
  - PairState (cube-face primordial pair) — 3 instances at R=1 cube-face-pair
    (Gaia-Eros / Chaos-Tartarus / Erebus-Nyx)
  - InnerOctPairState (inner-oct face pair) — 4 instances at R=1/√3
    face-pair (Source-Void / Feedback-Resource / Desire-Synthesis / Pattern-Anchor)

Comparison axes:
  (a) Field-by-field overlap — do both emit polarity, polarity_label,
      activation aggregates with same semantics?
  (b) Compute pattern — both compose 2 face-states + emit pair-level metrics?
  (c) Input shape — both take TWO LOWER-LEVEL FACE STATES as composition input?
  (d) Substrate-semantics — do they polarize SAME kind of substrate-state, or
      different kinds (cosmogonic-axis vs archetype-mode)?
"""
from __future__ import annotations
from dataclasses import fields

from _pair_engine import PairState
from _inner_oct_pair_engine import InnerOctPairState


def field_names(cls) -> set:
    return {f.name for f in fields(cls)}


def compare_shapes() -> dict:
    """Field-by-field overlap analysis."""
    cube_pair_fields = field_names(PairState)
    inner_oct_pair_fields = field_names(InnerOctPairState)
    shared = cube_pair_fields & inner_oct_pair_fields
    cube_only = cube_pair_fields - inner_oct_pair_fields
    oct_only = inner_oct_pair_fields - cube_pair_fields

    return {
        'cube_pair_field_count': len(cube_pair_fields),
        'inner_oct_pair_field_count': len(inner_oct_pair_fields),
        'shared_fields': sorted(shared),
        'cube_only_fields': sorted(cube_only),
        'inner_oct_only_fields': sorted(oct_only),
    }


def core_polarity_fields() -> set:
    """Fields semantically related to polarity-emission specifically."""
    return {'polarity', 'polarity_label', 'dominant_face'}


def analyze_polarity_overlap() -> dict:
    """Check if core polarity fields exist in both dataclasses."""
    core = core_polarity_fields()
    cube = field_names(PairState)
    oct  = field_names(InnerOctPairState)
    return {
        'core_polarity_fields': sorted(core),
        'in_cube_pair': sorted(core & cube),
        'in_inner_oct_pair': sorted(core & oct),
        'shared_core': sorted(core & cube & oct),
        'all_match': core.issubset(cube) and core.issubset(oct),
    }


def substrate_semantic_distinction() -> dict:
    """What does each pair-class actually polarize?"""
    return {
        'cube_face_pair': {
            'inputs': '2 Primordial face-engines (each = direct planet-aspect-activate of cosmogonic planet-pair)',
            'polarizes': 'Earth-Pluto-axis vs Water-Neptune-axis cosmogonic-arm activation',
            'pair_planet_coverage': '4 of 8 cube-vertex planets per pair',
            'antipode_relationship': 'cosmogonic-pair antipode (Hesiod-line antipodal locks)',
        },
        'inner_oct_face_pair': {
            'inputs': '2 inner-oct face-engines (each = composition of 3 planet-aspect-activate on triangle edges)',
            'polarizes': 'archetype-mode-A vs archetype-mode-B (e.g., SOURCE-vs-VOID, FEEDBACK-vs-RESOURCE)',
            'pair_planet_coverage': 'ALL 6 sign-rulership planets per pair (vertex-complement union)',
            'antipode_relationship': 'octahedral vertex-complement antipode (geometric, not Hesiod)',
        },
    }


def conflation_analysis() -> dict:
    """Apply Erato rule 4b: does `polarity-define` name conflate distinct functions?"""
    return {
        'compute_pattern': {
            'description': 'Both: compose 2 lower-level face-states + emit polarity, polarity_label, dominant_face, activation aggregates',
            'shape_match': True,
            'shell_specificity': False,  # operates at multiple shells (R=1 + R=1/√3)
        },
        'substrate_semantics': {
            'description': 'Different inputs (cosmogonic-axis-arm vs archetype-mode), different antipode-meaning (Hesiod-cosmogonic vs octahedral-geometric)',
            'semantic_match': False,
            'conflation_risk': 'MEDIUM — same compute, different substrate-meaning',
        },
        'recommendation': (
            'Cross-R-tier residency MATCHES on compute-shape (necessary for canonical). '
            'But substrate-semantics DIFFER — cube pair polarizes COSMOGONIC AXES while inner-oct pair '
            'polarizes ARCHETYPE MODES. Conflation risk per Erato rule 4b: medium. '
            'Council should determine whether: '
            '(a) `polarity-define` is shell-agnostic (compute-shape canonical despite semantic difference) '
            '— OR — '
            '(b) split into `cosmogonic-polarity-define` (cube pair) + `mode-polarity-define` (inner-oct pair) '
            '— OR — '
            '(c) `polarity-define` graduates as canonical because the META-FUNCTION '
            '"compose 2 face-states + emit polarity" is itself shell-agnostic, regardless of what '
            'the face-states represent.'
        ),
    }


if __name__ == '__main__':
    import json
    print("CROSS-R-TIER RESIDENCY PROBE: `polarity-define`\n")
    print("="*70)
    print()
    print("(a) FIELD-BY-FIELD SHAPE COMPARISON:")
    print(json.dumps(compare_shapes(), indent=2))
    print()
    print("(b) CORE POLARITY-FIELD OVERLAP:")
    print(json.dumps(analyze_polarity_overlap(), indent=2))
    print()
    print("(c) SUBSTRATE-SEMANTIC DISTINCTION:")
    print(json.dumps(substrate_semantic_distinction(), indent=2))
    print()
    print("(d) CONFLATION-TEST ANALYSIS:")
    print(json.dumps(conflation_analysis(), indent=2))
