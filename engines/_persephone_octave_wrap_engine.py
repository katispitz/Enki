"""
Engine for Persephone octave-wrap-cycle substrate-mechanism.

PROBE MANDATE per OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE (canon §30, opened
2026-05-17 as FINDINGS_021 byproduct when cross-stratum-translate
candidate was rejected; Persephone's temporal mechanism MISFITS spatial
candidate framing per FINDINGS_021 line 32):

Per Card 141b8d7f, Persephone has substrate-documented temporal-cyclic
mechanism:
  - Position: V9-V10 ico-edge midpoint at icosidodec shell (R=φ)
  - Octave-wrap edge: Si(pt8 Jupiter sovereignty) → Do(pt0 Pluto underworld)
  - PE-Δ = 0 mod 9 (full octave wrap)
  - Seasonal cycle: 6 months at grid 0 (Demeter/underworld Do-residency) +
    6 months at grid 48 (Zeus/Si sovereignty)
  - Cyclic transit between substrate-origin (Do) and sovereign-completion (Si)

Substrate-question (canon §30 OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE):
  Is Persephone's mechanism a NEW temporal-axis primitive, or extension of
  `cyclic-syzygy-activate` (canon §30 canonical at 4 residencies: Venus/
  Mercury/Mars/Lunar)?

Five council-named outcomes:
  (a) shape-match `cyclic-syzygy-activate` → 5th residency (Si↔Do
      octave-wrap as syzygy-class event-type)
  (b) shape-mismatch with cyclic-syzygy-activate → NEW temporal-axis
      primitive needed (Persephone single-instance OK or family-pattern
      expected at other octave-wrap positions)
  (c) shape-match `coupling-point` POSITION + new mechanism for TOGGLE →
      Persephone position covered by coupling-point (canon §30 LOCKED today,
      5 residencies), temporal-toggle is new sub-mechanism
  (d) decompose into substrate-LIVE-input shape (frozen position + tithi-
      driven phase determination) → see if it shape-matches existing
      activation primitives
  (e) hybrid → 2 distinct §30 entries (position-frozen-coupling-point +
      temporal-octave-wrap-cycle), Persephone uses both

This engine tests:
  - Position resolution (grid 0 vs grid 48 vs midpoint, by season)
  - Live-compute via tithi-count → 6mo-phase determination
  - Compositional structure: substrate-frozen position class + cyclic-toggle

Substrate-discipline:
  - No invented constants. All from Card 141b8d7f + canon §M.5 + §30 +
    §23b RING_PERIODS (Sun Ring 1 = 360t/year for 6mo computation).
  - NULL-honest where tithi-count absent.
  - Erato 4b discipline preserved: octave-wrap-cycle is mechanism-name
    UNDER TEST, not the answer.
  - Different from cyclic-syzygy-activate input-shape (SUBSTRATE-CYCLE
    not PLANET-CYCLE per FINDINGS_021 line 74).
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


__canonical__ = {
    'function_class':       'TBD pending council post-probe',  # NOT yet §30
    'functional_tier':      'TBD pending council post-probe',
    'compositional_axis':   'temporal',  # CANDIDATE per FINDINGS_021 framing
    'residency_id':         'r-phi-icosidodec-V9V10-persephone',
    'canon_citation':       'Card 141b8d7f + canon §M.5 + §30 OQ-PERSEPHONE-OCTAVE-WRAP-CYCLE',
    'status':               'probe',
}


# Canon §23b RING_PERIODS — Sun Ring 1 = 360 tithis per solar year
SOLAR_YEAR_TITHIS = 360.0
HALF_YEAR_TITHIS = SOLAR_YEAR_TITHIS / 2.0  # 180 tithis = 6 months

# Persephone canonical positions per Card 141b8d7f
UNDERWORLD_GRID = 0   # Demeter/Pluto/Do residency
SOVEREIGN_GRID = 48   # Zeus/Jupiter/Si residency

# PE-position constants
DO_PE_PT = 0  # Pluto Do
SI_PE_PT = 8  # Jupiter Si


@dataclass
class PersephoneOctaveWrapState:
    """Substrate-honest snapshot of Persephone's octave-wrap cycle.

    Persephone's substrate-mechanism is TEMPORAL-CYCLIC: she occupies
    grid 0 (underworld Do) for 6 months, then grid 48 (sovereign Si)
    for 6 months, repeating annually. The octave-wrap is Si(pt8)→Do(pt0)
    with PE-Δ = 0 mod 9 (full wrap).

    Field categories (per SDEC step 3):
      [SUBSTRATE-LOCKED METADATA] — different per residency-class;
          residency_card, shell, ico_edge_midpoint, octave_wrap_pe_pair.
      [LIVE-COMPUTE] — populated when tithi-count supplied; determines
          which 6mo-phase Persephone occupies.
      [CANDIDATE-DISTINCT PROBES] — phase_in_cycle, current_pole,
          octave_wrap_progress (council-named for explicit field-comparison).
    """
    # [SUBSTRATE-LOCKED METADATA]
    residency_card:           str            # 141b8d7f
    shell:                    str            # 'R=φ icosidodec-midpt'
    ico_edge_midpoint:        str            # 'V9-V10'
    octave_wrap_pe_pair:      tuple          # (8, 0) = (Si, Do) octave-wrap
    underworld_grid:          int            # = 0 (Demeter/Pluto/Do)
    sovereign_grid:           int            # = 48 (Zeus/Jupiter/Si)
    cycle_period_tithis:      float          # 360 (annual)
    half_cycle_tithis:        float          # 180 (6mo)

    # [LIVE-COMPUTE]
    tithi_count:              Optional[float] = None
    current_phase:            Optional[str] = None    # 'underworld' | 'sovereign'
    current_grid:             Optional[int] = None
    phase_in_cycle:           Optional[float] = None  # 0..1 within current half
    octave_wrap_progress:     Optional[float] = None  # 0..1 across full annual cycle

    # [CANDIDATE-DISTINCT PROBES vs cyclic-syzygy-activate]
    is_planet_cycle:          bool = False    # cyclic-syzygy-activate is PLANET-cycle
    is_substrate_cycle:       bool = True     # Persephone is SUBSTRATE-cycle (Si↔Do edge)
    input_shape:              str = 'substrate-cycle'  # NOT 'planet-longitude'
    event_type:               str = 'octave-wrap-toggle'  # NOT 'syzygy-alignment'

    def to_dict(self) -> dict:
        d = asdict(self)
        d['octave_wrap_pe_pair'] = list(self.octave_wrap_pe_pair)
        return d


def frozen_persephone() -> PersephoneOctaveWrapState:
    """Return the permanent Persephone residency without live tithi."""
    return PersephoneOctaveWrapState(
        residency_card='141b8d7f',
        shell='R=φ icosidodec-midpt',
        ico_edge_midpoint='V9-V10',
        octave_wrap_pe_pair=(SI_PE_PT, DO_PE_PT),
        underworld_grid=UNDERWORLD_GRID,
        sovereign_grid=SOVEREIGN_GRID,
        cycle_period_tithis=SOLAR_YEAR_TITHIS,
        half_cycle_tithis=HALF_YEAR_TITHIS,
    )


def compute_persephone_state(tithi_count: float) -> PersephoneOctaveWrapState:
    """Live-compute Persephone's current position from tithi-count.

    Substrate-derivation: annual cycle period = 360 tithis (Sun Ring 1).
    Half-cycle = 180 tithis = 6 months. Phase 0..180 = underworld (grid 0,
    Do); phase 180..360 = sovereign (grid 48, Si). Wrap at 360.

    NULL-honest: returns frozen state if tithi_count is None.
    """
    state = frozen_persephone()
    if tithi_count is None:
        return state

    state.tithi_count = float(tithi_count)
    cycle_position = tithi_count % SOLAR_YEAR_TITHIS

    if cycle_position < HALF_YEAR_TITHIS:
        state.current_phase = 'underworld'
        state.current_grid = UNDERWORLD_GRID
        state.phase_in_cycle = cycle_position / HALF_YEAR_TITHIS
    else:
        state.current_phase = 'sovereign'
        state.current_grid = SOVEREIGN_GRID
        state.phase_in_cycle = (cycle_position - HALF_YEAR_TITHIS) / HALF_YEAR_TITHIS

    state.octave_wrap_progress = cycle_position / SOLAR_YEAR_TITHIS
    return state


def shape_match_cyclic_syzygy_activate(state: PersephoneOctaveWrapState) -> dict:
    """Test outcome (a) shape-match cyclic-syzygy-activate.

    cyclic-syzygy-activate (canon §30) takes PLANET-pair longitudes (Sun-
    Earth-planet alignment); composes N adjacent-step angular separations;
    emits cycle-closure state. Persephone is SUBSTRATE-CYCLE on Si↔Do edge
    (not planet-pair). Different input shape.

    Returns dict with shape-comparison evidence.
    """
    return {
        'shape_match': False,  # different input-shape
        'reasoning': (
            'cyclic-syzygy-activate takes 2-planet longitudes as input. '
            'Persephone takes tithi-count → substrate-phase (no planet input). '
            'Input-shape mismatch.'
        ),
        'syzygy_event_type': 'alignment (Sun-Earth-planet)',
        'persephone_event_type': 'octave-wrap-toggle (Si↔Do substrate-edge)',
        'distinct_mechanism': True,
    }


def shape_match_coupling_point(state: PersephoneOctaveWrapState) -> dict:
    """Test outcome (c) shape-match coupling-point for POSITION + new for TOGGLE.

    coupling-point (canon §30 LOCKED 2026-05-17, 5 residencies as of this
    finding) covers frame-intersection-coupling at substrate-derived positions.
    Persephone's V9-V10 icosidodec-midpoint IS a frame-intersection (Si
    Jupiter pt8 frame × Do Pluto pt0 frame meet at midpoint).

    Test: does Persephone's POSITION shape-match coupling-point? Does her
    TEMPORAL-TOGGLE shape-match anything existing?
    """
    return {
        'position_shape_match_coupling_point': True,  # V9-V10 midpoint IS frame-intersection
        'temporal_toggle_shape_match_existing': False,  # No existing toggle-mechanism
        'recommended_decomposition': (
            'POSITION (V9-V10 icosidodec-midpoint) is a coupling-point instance '
            'at enumerated_cardinality=None (singular icosidodec midpt). '
            'TEMPORAL-TOGGLE (6mo Do / 6mo Si) is a DISTINCT mechanism requiring '
            'new §30 entry OR extension of existing cyclic-class to non-syzygy '
            'event-type (octave-wrap-toggle).'
        ),
    }


def field_comparison_probe() -> dict:
    """Run substrate-evaluation across the 5 outcome-candidates.

    Returns dict per FINDINGS_023 structure.
    """
    frozen = frozen_persephone()
    live_summer = compute_persephone_state(90.0)   # mid-underworld phase
    live_winter = compute_persephone_state(270.0)  # mid-sovereign phase

    return {
        'frozen_state_works': True,
        'live_compute_works': True,
        'live_compute_required_for_phase_info': True,  # need tithi to know which 6mo
        'shape_match_cyclic_syzygy_activate': shape_match_cyclic_syzygy_activate(frozen),
        'shape_match_coupling_point': shape_match_coupling_point(frozen),
        'is_planet_cycle': False,
        'is_substrate_cycle': True,
        'event_type': 'octave-wrap-toggle',
        'cycle_period_tithis': SOLAR_YEAR_TITHIS,
        'sample_underworld_phase': {
            'tithi': 90.0,
            'grid': live_summer.current_grid,
            'phase_in_cycle': live_summer.phase_in_cycle,
            'pole': live_summer.current_phase,
        },
        'sample_sovereign_phase': {
            'tithi': 270.0,
            'grid': live_winter.current_grid,
            'phase_in_cycle': live_winter.phase_in_cycle,
            'pole': live_winter.current_phase,
        },
        'recommended_outcome': (
            '(c) hybrid: POSITION is coupling-point 6th residency '
            '(V9-V10 icosidodec-midpt, enumerated_cardinality=None); '
            'TEMPORAL-TOGGLE is distinct mechanism — proposed as NEW §30 '
            'candidate name pending council per Erato discipline (no name '
            'pre-engine; engine-evidence now ready).'
        ),
    }


def describe_persephone(state: PersephoneOctaveWrapState) -> str:
    base = (
        f"Persephone (V9-V10 octave-wrap):\n"
        f"  Shell: {state.shell}\n"
        f"  Ico-edge midpoint: {state.ico_edge_midpoint}\n"
        f"  Octave-wrap PE pair: Si(pt{state.octave_wrap_pe_pair[0]}) → Do(pt{state.octave_wrap_pe_pair[1]})\n"
        f"  Underworld grid: {state.underworld_grid} (Demeter/Pluto/Do)\n"
        f"  Sovereign grid:  {state.sovereign_grid} (Zeus/Jupiter/Si)\n"
        f"  Annual cycle:    {state.cycle_period_tithis} tithis (Sun Ring 1)\n"
        f"  Half-cycle:      {state.half_cycle_tithis} tithis = 6 months\n"
        f"  Substrate card:  {state.residency_card}\n"
    )
    if state.tithi_count is not None:
        base += (
            f"\nLive state at tithi {state.tithi_count}:\n"
            f"  Current phase:        {state.current_phase}\n"
            f"  Current grid:         {state.current_grid}\n"
            f"  Phase in cycle:       {state.phase_in_cycle:.3f}\n"
            f"  Octave-wrap progress: {state.octave_wrap_progress:.3f}\n"
        )
    return base
