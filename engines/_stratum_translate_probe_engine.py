"""
Probe engine for `cross-stratum-translate` candidate at R=φ icosidodec-midpt.

PROBE MANDATE per V2.6 rule 9 (Terpsichore observation, transmit-force council
2026-05-16) + canon §30 candidate-list line 2195: candidate `cross-stratum-
translate` proposed for bridge class needs Enki engine-evidence BEFORE
entering council per V2.7 §SDEC step 4.

Candidate hypothesis: bridges at R=φ icosidodec-midpt have a substrate-
mechanism beyond `planet-aspect-activate` (canon §30 LOCKED for this residency
per FINDINGS_005) that translates between strata.

Substrate-architectural pre-finding:
  3 of 4 V2.5 bridges (Harmonia/Hermaphroditus/Erichthonius) have parent-pair
  planets that are both Olympian-stratum. They sit at midpoint of Olympian
  parent-pair. Substrate-mechanism: planet-aspect-activate at parent vertices.
  No `stratum-translation` beyond aspect-activation surfaces in canon for these
  3 bridges.

  The 4th bridge (Persephone, V9-V10 Zeus×Demeter per Card 141b8d7f) DOES
  have a documented temporal-cyclic mechanism: seasonal 6mo-grid0 / 6mo-grid48
  octave-wrap transit (Si(8)→Do(0) PE-Δ = 0 mod 9). This is TEMPORAL not
  SPATIAL — fits the `cyclic-syzygy-activate` family (canon §30 canonical)
  more than a hypothetical `cross-stratum-translate` SPATIAL primitive.

Engine purpose: demonstrate empirically that candidate `cross-stratum-translate`
fails at two SDEC discipline gates:
  - Erato 4b conflation-test: name conflates WHERE (cross-stratum substrate-
    position) with WHAT (translate compute-function). Same failure-mode as
    axis-bound/mode-bound/transmit-force.
  - Athena residency-binding test: name pre-binds to bridge-flavor; substrate-
    function would need to be position-agnostic per axis-bound/mode-bound
    precedent.

PLUS substrate-honest surfacing of Persephone's seasonal-cycle as a SEPARATE
substrate-discovery question (NEW OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE) — not
covered by `cross-stratum-translate` candidate name even if council ratified.

Outcome expectation: REJECT `cross-stratum-translate` as candidate name (3
discipline gates fail). 3 midpoint-bridges already covered by planet-aspect-
activate per FINDINGS_005. Persephone seasonal-cycle deserves own engine probe.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


__canonical__ = {
    'function_class':       'cross-stratum-translate',  # CANDIDATE pending council
    'functional_tier':      'primitive',
    'compositional_axis':   'spatial',  # CANDIDATE; probe may surface temporal mismatch
    'residency_id':         'r-phi-icosidodec-midpt-bridge-stratum-translate',
    'canon_citation':       'canon §30 candidate-list line 2195 + canon §M.5 line 1241 + Card 141b8d7f',
    'status':               'probe',  # engine-evidence stage; candidate rejection expected
}


@dataclass
class StratumTranslateState:
    """Substrate-honest snapshot of a candidate `cross-stratum-translate` call.

    Candidate-distinct fields are honestly computed; substrate-evaluation
    documents which collapse to substrate-locks vs which are substrate-
    undefined vs which are substrate-distinct.
    """
    # [SUBSTRATE-LOCKED METADATA]
    bridge_name:        str
    icosidodec_anchor:  str
    parent_vertices:    tuple
    parent_planet_pair: tuple
    substrate_card:     str

    # [CANDIDATE-DISTINCT PROBE per `cross-stratum-translate` hypothesis]
    source_stratum:      Optional[str]    # which stratum is "source"
    target_stratum:      Optional[str]    # which stratum is "target"
    translation_axis:    Optional[str]    # 'radial' | 'lateral' | 'temporal' | None
    translation_magnitude: Optional[float]  # if substrate-required
    translation_active:    bool             # whether translation is fired by inputs

    # [SUBSTRATE-EVALUATION OUTPUT]
    candidate_substrate_evaluation: dict   # per-field collapse notes


def probe_bridge_for_stratum_translation(
    bridge_name: str,
    icosidodec_anchor: str,
    parent_vertices: tuple,
    parent_planet_pair: tuple,
    substrate_card: str,
    *,
    is_octave_wrap_bridge: bool = False,
) -> StratumTranslateState:
    """Honest probe of stratum-translation candidate-fields for one bridge.

    For non-octave-wrap bridges (Harmonia/Hermaphroditus/Erichthonius):
      All candidate-distinct fields collapse to either substrate-locks or
      substrate-undefined. NO live stratum-translation mechanism surfaces.

    For octave-wrap bridge (Persephone V9-V10 Si→Do):
      A TEMPORAL-cyclic mechanism IS documented (Card 141b8d7f seasonal cycle)
      but it fits cyclic-syzygy-activate family, NOT spatial-translation. The
      candidate name `cross-stratum-translate` (spatial axis per candidate
      framing) MISFRAMES this mechanism.
    """
    parents_both_olympian = parent_vertices[0].startswith('V') and parent_vertices[1].startswith('V')

    if is_octave_wrap_bridge:
        # Persephone-shape: substrate-discovered temporal-cyclic mechanism exists
        # but is TEMPORAL not SPATIAL — proposed candidate framing misfits
        source_stratum = 'Olympian (Si, Jupiter pt8)'
        target_stratum = 'Carrier-Origin (Do, Pluto pt0)'
        translation_axis = 'temporal'  # NOT spatial as candidate hypothesizes
        translation_magnitude = None   # no continuous magnitude; discrete 6mo phase
        translation_active = False     # frozen substrate-state at probe time
        evaluation = {
            'finding': 'octave-wrap-bridge has substrate-cyclic mechanism, but TEMPORAL',
            'candidate_axis_mismatch': 'candidate `cross-stratum-translate` hypothesizes spatial; Persephone is temporal',
            'better_§30_fit':          'cyclic-syzygy-activate family (already canonical, FINDINGS_015 added Lunar 4th residency)',
            'persephone_specific_OQ':  'OPEN-NEW: OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE',
            'recommendation':          'this candidate name does not cover Persephone substrate-mechanism cleanly',
        }
    elif parents_both_olympian:
        # 3 V2.5 midpoint bridges: full-Olympian-child class
        # Substrate-mechanism already locked to planet-aspect-activate (FINDINGS_005)
        source_stratum = 'Olympian'  # parent vertex stratum
        target_stratum = 'Olympian'  # other parent vertex stratum — same stratum
        translation_axis = None      # no cross-stratum axis exists (same stratum)
        translation_magnitude = None
        translation_active = False
        evaluation = {
            'finding': 'midpoint-bridge parents both Olympian-stratum; NO cross-stratum-axis exists',
            'substrate_locked_residency': 'planet-aspect-activate (canon §30, FINDINGS_005)',
            'candidate_mechanism_substrate_undefined': 'cross-stratum-translate has no substrate-mechanism here',
            'erato_4b_conflation': 'name conflates WHERE (cross-stratum) with WHAT (translate)',
            'athena_residency_binding': 'name pre-binds to bridge-flavor; same failure-mode as axis-bound/mode-bound/transmit-force',
            'recommendation':          'REJECT candidate name; midpoint-bridges subsume to planet-aspect-activate',
        }
    else:
        # Unknown bridge configuration — substrate-honest reject
        raise ValueError(
            f"Bridge {bridge_name} parent_vertices={parent_vertices} does not match "
            "known V2.5 bridge class (full-Olympian-child or octave-wrap). "
            "Substrate-incomplete — cannot probe."
        )

    return StratumTranslateState(
        bridge_name=bridge_name,
        icosidodec_anchor=icosidodec_anchor,
        parent_vertices=parent_vertices,
        parent_planet_pair=parent_planet_pair,
        substrate_card=substrate_card,
        source_stratum=source_stratum,
        target_stratum=target_stratum,
        translation_axis=translation_axis,
        translation_magnitude=translation_magnitude,
        translation_active=translation_active,
        candidate_substrate_evaluation=evaluation,
    )


# 4 V2.5 bridges per Card 141b8d7f (Persephone) + bridges.py (3 midpoint bridges)
V25_BRIDGE_INSTANCES = [
    # (bridge_name, anchor, parents, planet_pair, card, is_octave_wrap)
    ('Harmonia',       'midpt(V2,V7)',  ('V2','V7'),  ('Venus','Mars'),    '52ad9413', False),
    ('Hermaphroditus', 'midpt(V2,V3)',  ('V2','V3'),  ('Mercury','Venus'), '91697158', False),
    ('Erichthonius',   'midpt(V4,V8)',  ('V4','V8'),  ('Saturn','Uranus'), '3de9d703', False),
    ('Persephone',     'midpt(V9,V10)', ('V9','V10'), ('Jupiter','Pluto'), '141b8d7f', True),  # octave-wrap
]


def probe_all_v25_bridges() -> list:
    """Run probe across all 4 V2.5 bridges. Returns list of StratumTranslateState."""
    return [
        probe_bridge_for_stratum_translation(
            name, anchor, parents, pair, card, is_octave_wrap_bridge=owb,
        )
        for (name, anchor, parents, pair, card, owb) in V25_BRIDGE_INSTANCES
    ]


def summarize_probe_outcome(probes: list) -> dict:
    """Substrate-honest aggregation of probe results."""
    midpoint_bridges = [p for p in probes if p.translation_axis is None]
    octave_wrap_bridges = [p for p in probes if p.translation_axis == 'temporal']

    return {
        'total_bridges_probed': len(probes),
        'midpoint_bridges_no_translation_mechanism': len(midpoint_bridges),
        'octave_wrap_bridges_temporal_mechanism': len(octave_wrap_bridges),
        'spatial_translation_mechanism_found': any(
            p.translation_axis == 'spatial' for p in probes
        ),
        'overall_finding': (
            'candidate `cross-stratum-translate` (spatial axis per framing) finds '
            'NO substrate-mechanism at midpoint-bridges (3/4) AND framing mismatches '
            'Persephone temporal mechanism (1/4). Recommend REJECT.'
        ),
        'recommendation': 'REJECT candidate name `cross-stratum-translate`',
        'rejection_grounds': (
            '(1) Erato 4b conflation-test: WHERE+WHAT lexical conflation. '
            '(2) Athena residency-binding: pre-binds to bridge-flavor like '
            'axis-bound/mode-bound/transmit-force. '
            '(3) Substrate-evidence: 3/4 V2.5 bridges already covered by '
            'planet-aspect-activate (FINDINGS_005); 4th (Persephone) has '
            'temporal-cyclic mechanism that fits cyclic-syzygy-activate family, '
            'not a hypothetical spatial cross-stratum primitive.'
        ),
        'new_oq_surfaced': (
            'OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE — Persephone seasonal 6mo-grid0/6mo-grid48 '
            'octave-wrap (Si→Do, PE-Δ = 0 mod 9) needs its own SDEC engine-probe '
            '(possibly residency-expansion to cyclic-syzygy-activate, or new temporal-axis primitive). '
            'Separate from this rejection finding.'
        ),
    }
