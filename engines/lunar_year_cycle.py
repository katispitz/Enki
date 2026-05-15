"""
Lunar year cycle engine — 4th residency for cyclic-syzygy-activate.

Substrate-derivable from canon §23b ring ratios:
  Ring 1 Solar = 360t (1 solar year, canon §23b OQ-RINGS-05)
  Ring 2 Lunar = 30t (1 synodic month, canon §23b OQ-RINGS-05)
  Ring 1 / Ring 2 = 360 / 30 = 12 → N=12 synodic-syzygies per solar year

Event-type: NEW-MOON SYZYGY (sun-earth-moon aligned, moon between earth and sun).
Same syzygy umbrella that covers Venus/Mercury inferior conjunctions + Mars
oppositions. Different planet (Moon), different syzygy-flavor (sun-moon
conjunction = new moon).

Adjacent step in zodiac between consecutive new moons:
  Sun's apparent zodiac advance per synodic month (30 tithis × 12°/tithi)... wait
  Per canon: 1 tithi advance = 12° of moon-sun phase (full synodic cycle = 360°).
  But that's PHASE not zodiac longitude.
  Zodiac-longitude step: Sun advances 360° in 360t (Ring 1 solar year)
  → in 1 synodic month (30t), Sun advances 360 × 30/360 = 30°
  → consecutive new moons in zodiac are ~30° apart.
  Closure: 12 × 30° = 360° ✓ EXACT closure.

Substrate-canonical N=12 + period 360t + adjacent step 30°.

Note: tighter cycles available (Saros 18.03yr, Metonic 19yr, etc.) but require
nodal/anomalistic month tracking. Solar-year synodic cycle is the cleanest
substrate-derived Lunar N-cycle from canon §23b ring-ratios alone.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


__canonical__ = {
    'function_class':     'cyclic-syzygy-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'temporal',
    'residency_id':       'lunar-ring1-ring2-derived-cycle',
    'canon_citation':     'canon §23b OQ-RINGS-05 / derived N = Ring 1 / Ring 2 = 360/30 / 12 new-moon syzygies / 360t / 1yr',
    'status':             'canonical',
}


LUNAR_YEAR_TITHIS    = 360            # Ring 1 solar year per canon §23b OQ-RINGS-05
LUNAR_CYCLE_N        = 12             # Ring 1 / Ring 2 = 360 / 30 = 12 synodics per year
LUNAR_ADJ_STEP_DEG   = 30.0           # 360° / 12 = exact 30° per new-moon step in zodiac
EVENT_TYPE           = 'new-moon-syzygy'  # sun-earth-moon syzygy (conjunction flavor)


@dataclass
class LunarYearCycleState:
    """Substrate-honest snapshot of 1 solar year of new-moon syzygies."""
    cycle_id:            str
    canonical_steps:     int               # 12
    cycle_tithis:        int               # 360
    adjacent_step_deg:   float             # 30°
    event_type:          str               # 'new-moon-syzygy'

    longitudes:          Optional[list]    # 12 new-moon lons, ordered
    pairwise_separations: Optional[list]   # 11 separations
    mean_adjacent_step:  Optional[float]
    drift_deg:           Optional[float]
    closure:             Optional[bool]
    drift_tolerance:     float = 6.0

    def to_dict(self) -> dict:
        return asdict(self)


def _angular_step(a: float, b: float) -> float:
    return (b - a) % 360.0


def compute_lunar_year_cycle_state(
    cycle_id: str,
    longitudes: Optional[list] = None,
) -> LunarYearCycleState:
    if longitudes is None:
        return LunarYearCycleState(
            cycle_id=cycle_id,
            canonical_steps=LUNAR_CYCLE_N,
            cycle_tithis=LUNAR_YEAR_TITHIS,
            adjacent_step_deg=LUNAR_ADJ_STEP_DEG,
            event_type=EVENT_TYPE,
            longitudes=None, pairwise_separations=None,
            mean_adjacent_step=None, drift_deg=None, closure=None,
        )

    if len(longitudes) != LUNAR_CYCLE_N:
        raise ValueError(
            f"Lunar year cycle {cycle_id} requires exactly {LUNAR_CYCLE_N} "
            f"new-moon longitudes, got {len(longitudes)}. Substrate-incomplete."
        )

    seps = [_angular_step(longitudes[i], longitudes[i + 1]) for i in range(LUNAR_CYCLE_N - 1)]
    mean_step = sum(seps) / len(seps)
    drift = mean_step - LUNAR_ADJ_STEP_DEG
    closure = abs(drift) <= 6.0

    return LunarYearCycleState(
        cycle_id=cycle_id,
        canonical_steps=LUNAR_CYCLE_N,
        cycle_tithis=LUNAR_YEAR_TITHIS,
        adjacent_step_deg=LUNAR_ADJ_STEP_DEG,
        event_type=EVENT_TYPE,
        longitudes=longitudes,
        pairwise_separations=seps,
        mean_adjacent_step=mean_step,
        drift_deg=drift,
        closure=closure,
    )


def describe() -> str:
    return (
        "LUNAR YEAR CYCLE (12 new-moon syzygies per solar year)\n"
        f"Substrate-derivable from canon §23b ring ratios:\n"
        f"  Ring 1 Solar (360t) / Ring 2 Lunar (30t) = {LUNAR_CYCLE_N}\n"
        f"  - {LUNAR_CYCLE_N} new-moon syzygies per cycle\n"
        f"  - {LUNAR_YEAR_TITHIS} tithis (~1 solar year) per cycle\n"
        f"  - {LUNAR_ADJ_STEP_DEG}° EXACT zodiac step between consecutive new-moons\n"
        f"  - 12 × 30° = 360° exact closure\n"
        f"  - Event type: NEW-MOON SYZYGY (sun-earth-moon conjunction)\n"
        f"\n"
        f"4th residency probe for `cyclic-syzygy-activate` (canon §30 canonical):\n"
        f"  - Venus Ring 3: 5 inferior-conjunction syzygies / 8yr ✓\n"
        f"  - Mercury Ring 5: 41 inferior-conjunction syzygies / 13yr ✓\n"
        f"  - Mars Ring 4: 37 opposition syzygies / 79yr ✓\n"
        f"  - Lunar Ring 1/Ring 2: 12 new-moon syzygies / 1yr (THIS PROBE)\n"
        f"\n"
        f"If shape MATCHES: cyclic-syzygy-activate has 4 independent residencies\n"
        f"across all syzygy event-types (inferior conjunction + opposition +\n"
        f"new-moon conjunction). Confirms `syzygy` umbrella spans full event-set.\n"
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('FROZEN STATE:')
    print(json.dumps(compute_lunar_year_cycle_state('cycle_frozen').to_dict(), indent=2)[:400])
    print('...')
    print()
    # Sample: ideal cycle starting at vernal equinox 0°
    ideal_lons = [(i * LUNAR_ADJ_STEP_DEG) % 360.0 for i in range(LUNAR_CYCLE_N)]
    print(f'SAMPLE: IDEAL CYCLE ({LUNAR_CYCLE_N} new-moons at exact {LUNAR_ADJ_STEP_DEG}° steps):')
    state = compute_lunar_year_cycle_state('ideal_cycle', ideal_lons)
    d = state.to_dict()
    print(f"  canonical_steps: {d['canonical_steps']}")
    print(f"  cycle_tithis: {d['cycle_tithis']}")
    print(f"  event_type: {d['event_type']}")
    print(f"  mean_adjacent_step: {d['mean_adjacent_step']:.2f}°")
    print(f"  drift_deg: {d['drift_deg']:.4f}°")
    print(f"  closure: {d['closure']}")
    print(f"  separations (first 5): {[round(s,2) for s in d['pairwise_separations'][:5]]}")
