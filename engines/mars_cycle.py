"""
Mars 37-opposition cycle engine — temporal-cyclic substrate-pressure-test.

Substrate-canonical (Nammu canon §23b line 950): Mars / pt4 / Fa / Ring 4 =
**37 opposition resonance over 28440t (~79yr)**.

Critical distinction from Venus/Mercury inferior-conjunction cycles:
  - Venus + Mercury are INFERIOR planets (inside Earth's orbit) — their cyclic
    event is INFERIOR CONJUNCTION (planet between Earth and Sun).
  - Mars is an OUTER planet (outside Earth's orbit) — its cyclic event is
    OPPOSITION (planet opposite Sun in sky, Earth between Sun and Mars).
  - Same temporal-cyclic structure (1 planet × N time-samples) but DIFFERENT
    alignment-event type.

Tests substrate-pressure-question (FINDINGS_014): does the canonical
`cyclic-conjunction-activate` (graduated 2026-05-12, ratified at Venus + Mercury
inferior-conjunctions) extend to Mars oppositions? If shape MATCHES at compute
level (despite event-type difference), the umbrella concept "conjunction" needs
broadening to "alignment" or "syzygy" (sun-earth-planet aligned, regardless of
which side planet is on).

Substrate-data per canon §23b OQ-RINGS-09:
  - N = 37 oppositions per Ring cycle
  - Period = 28440 tithis = ~79 years
  - Mars synodic period ≈ 779.96 days ≈ 2.135 Earth-years
  - Adjacent zodiac step ≈ 48.6° between consecutive oppositions
    (Earth advances 2.135 revs per Mars synodic = 408.6° net; minus 360° = 48.6°)
  - 37 oppositions × 48.6° = 1798° mod 360° ≈ -2° closure drift over 79yr

Function shape:
  - Input: 37 Mars opposition longitudes (chronologically ordered over ~79yr)
  - Output: cycle-closure state (pairwise separations + drift + closure check)
  - Same compute pattern as venus_pentagram + mercury_cycle
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


__canonical__ = {
    'function_class':     'cyclic-syzygy-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'temporal',
    'residency_id':       'mars-ring4-cycle',
    'canon_citation':     'canon §23b line 950 / Mars Ring 4 / 37 opposition syzygies / 28440t / 79yr',
    'status':             'canonical',
}


MARS_RING_TITHIS    = 28440          # ~79 years per canon §23b line 950
MARS_CYCLE_N        = 37             # 37 oppositions per Ring cycle
# Adjacent step: Earth's apparent advance per Mars synodic minus 360°
# Mars synodic / Earth year = 779.96 / 365.25 = 2.135
# Earth advance = 2.135 × 360° = 769° → net = 409° → mod 360 = 49°
# Substrate-precise: 28440 / 37 / (365.25 × adj_step_per_year_factor) ...
# Direct: zodiac fraction per opposition = (mars_synodic - earth_year) / earth_year × 360°
# ≈ (779.96 - 365.25)/365.25 × 360° = 1.135 × 360° = 408.6° mod 360° = 48.6°
MARS_ADJ_STEP_DEG   = 48.6
EVENT_TYPE          = 'opposition'    # vs 'inferior_conjunction' for Venus/Mercury


@dataclass
class MarsCycleState:
    """Substrate-honest snapshot of a Mars 37-opposition cycle."""
    cycle_id:            str
    canonical_steps:     int               # 37
    cycle_tithis:        int               # 28440
    adjacent_step_deg:   float             # ≈48.6°
    event_type:          str               # 'opposition' (substrate-event distinction)

    longitudes:          Optional[list]    # 37 Mars opposition lons, ordered
    pairwise_separations: Optional[list]   # 36 separations
    mean_adjacent_step:  Optional[float]
    drift_deg:           Optional[float]
    closure:             Optional[bool]
    drift_tolerance:     float = 6.0       # V2.6 G4 ignition orb

    def to_dict(self) -> dict:
        return asdict(self)


def _angular_step(a: float, b: float) -> float:
    return (b - a) % 360.0


def compute_mars_cycle_state(
    cycle_id: str,
    longitudes: Optional[list] = None,
) -> MarsCycleState:
    """Compute Mars cycle state from 37 chronologically-ordered opposition longitudes."""
    if longitudes is None:
        return MarsCycleState(
            cycle_id=cycle_id,
            canonical_steps=MARS_CYCLE_N,
            cycle_tithis=MARS_RING_TITHIS,
            adjacent_step_deg=MARS_ADJ_STEP_DEG,
            event_type=EVENT_TYPE,
            longitudes=None, pairwise_separations=None,
            mean_adjacent_step=None, drift_deg=None, closure=None,
        )

    if len(longitudes) != MARS_CYCLE_N:
        raise ValueError(
            f"Mars cycle {cycle_id} requires exactly {MARS_CYCLE_N} opposition "
            f"longitudes, got {len(longitudes)}. Substrate-incomplete."
        )

    seps = [_angular_step(longitudes[i], longitudes[i + 1]) for i in range(MARS_CYCLE_N - 1)]
    mean_step = sum(seps) / len(seps)
    drift = mean_step - MARS_ADJ_STEP_DEG
    closure = abs(drift) <= 6.0

    return MarsCycleState(
        cycle_id=cycle_id,
        canonical_steps=MARS_CYCLE_N,
        cycle_tithis=MARS_RING_TITHIS,
        adjacent_step_deg=MARS_ADJ_STEP_DEG,
        event_type=EVENT_TYPE,
        longitudes=longitudes,
        pairwise_separations=seps,
        mean_adjacent_step=mean_step,
        drift_deg=drift,
        closure=closure,
    )


def describe() -> str:
    return (
        "MARS 37-OPPOSITION CYCLE (temporal-cyclic, outer-planet OPPOSITION event-type)\n"
        f"Substrate-canonical (canon §23b Ring 4): Mars pt4 / Fa\n"
        f"  - {MARS_CYCLE_N} oppositions per Ring cycle\n"
        f"  - {MARS_RING_TITHIS} tithis (~79yr) per cycle\n"
        f"  - ~{MARS_ADJ_STEP_DEG}° apparent zodiac step between consecutive oppositions\n"
        f"  - Event type: OPPOSITION (sun-earth-mars alignment, mars opposite sun)\n"
        f"\n"
        f"Substrate-pressure-test on `cyclic-conjunction-activate` (canonical canon §30):\n"
        f"  Mars oppositions are NOT inferior conjunctions. If shape MATCHES at compute\n"
        f"  level → 3rd temporal-cyclic residency confirms umbrella interpretation.\n"
        f"  But name '`cyclic-CONJUNCTION-activate`' may be too narrow → broadening\n"
        f"  required to `cyclic-alignment-activate` or `cyclic-syzygy-activate`.\n"
        f"\n"
        f"  Two readings (FINDINGS_014):\n"
        f"  (a) Strict-conjunction: cyclic-conjunction-activate ONLY for inferior planets;\n"
        f"      Mars needs separate function-name (e.g., `cyclic-opposition-activate`).\n"
        f"  (b) Umbrella-alignment: Mnemosyne 2026-05-12 reading — 'conjunction' as\n"
        f"      umbrella superclass covering all alignment-cycle events. Mars fits.\n"
        f"  (c) Broaden-canonical: rename `cyclic-conjunction-activate` → \n"
        f"      `cyclic-alignment-activate` (more substrate-honest umbrella).\n"
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('FROZEN STATE:')
    print(json.dumps(compute_mars_cycle_state('cycle_frozen').to_dict(), indent=2)[:500])
    print('...')
    print()
    # Sample: ideal Mars cycle — 37 lons at 48.6° steps
    ideal_lons = [(i * MARS_ADJ_STEP_DEG) % 360.0 for i in range(MARS_CYCLE_N)]
    print(f'SAMPLE: IDEAL CYCLE ({MARS_CYCLE_N} oppositions at exact {MARS_ADJ_STEP_DEG}° steps):')
    state = compute_mars_cycle_state('ideal_cycle', ideal_lons)
    d = state.to_dict()
    print(f"  canonical_steps: {d['canonical_steps']}")
    print(f"  cycle_tithis: {d['cycle_tithis']}")
    print(f"  event_type: {d['event_type']}")
    print(f"  mean_adjacent_step: {d['mean_adjacent_step']:.2f}°")
    print(f"  drift_deg: {d['drift_deg']:.4f}°")
    print(f"  closure: {d['closure']}")
    print(f"  separations (first 5): {[round(s,2) for s in d['pairwise_separations'][:5]]}")
