"""
Saturn cycle engine — Ring 7 probe + Moon-synodic-mirror investigation.

Substrate-canonical (Nammu canon §23b line 953):
  Saturn / pt7 / La / Ring 7 = 10620t / 29.5yr / "Full orbital / Moon-synodic mirror"

Two substrate-meaningful cycle-types to investigate:
  (1) **Sidereal orbital** — Saturn completes ~1 zodiac circuit per Ring 7
      (29.46yr Saturn sidereal ≈ 29.5yr Ring 7). Event = sign-ingress
      (Saturn enters new zodiac sign). N=12 sign-ingresses per Saturn ring.
  (2) **Synodic oppositions** — sun-Saturn opposition occurs ~once per
      1.035yr synodic (Saturn synodic ≈ 378d). N ≈ 28.5 oppositions per
      Saturn ring cycle (NOT clean integer; opposition cycle doesn't close
      cleanly).

Moon-synodic-mirror investigation (canon line 953):
  Saturn period = 29.5 years
  Lunar synodic period = 29.5 days
  Ratio: same numerical value, different time unit (years vs days)
  Tithi ratio: 10620t / 30t = 354 ≈ 1 solar year (360t)
  Substrate-pattern: Saturn-tithis ÷ Lunar-tithis ≈ Solar-tithis-per-year

This is substrate-emergent fractal across time-units:
  - 1 lunar synodic month → 1 Saturn orbital year (numerical mirror)
  - 30t Ring 2 → 30t × 354 = 10620t Ring 7
  - 354 ≈ Ring 1 Solar year (close to 360t)

The "mirror" is substrate-numerical-fact, NOT an active compute. No engine
operation derives from it directly — it's a structural observation in canon.

Function-class candidates from Saturn probe:
  (a) cyclic-syzygy-activate at N=28-29 oppositions — DOESN'T FIT (non-integer)
  (b) cyclic-sign-ingress-activate at N=12 — NEW function-class candidate
      (outer planet zodiac-traversal, 1 sign-per-year cycle)
  (c) substrate-mirror — descriptor, not function

This engine builds (b) sign-ingress shape + documents the substrate-mirror.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


__canonical__ = {
    'function_class':     'cyclic-sign-ingress-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'temporal',
    'residency_id':       'saturn-ring7-cycle',
    'canon_citation':     'canon §23b line 953 / Saturn Ring 7 / 12 sign-ingresses / 10620t / 29.5yr',
    'status':             'canonical',
}


SATURN_RING_TITHIS  = 10620         # 29.5 years per canon §23b line 953
SATURN_SIDEREAL_N   = 12            # 12 zodiac signs traversed per Ring 7
SATURN_SIGN_STEP    = 30.0          # 360° / 12 = exact 30° per sign-ingress
EVENT_TYPE          = 'sign-ingress'  # Saturn enters new zodiac sign

# Substrate-mirror constants (canon §23b numerical observation)
LUNAR_SYNODIC_TITHIS = 30           # Ring 2
SOLAR_YEAR_TITHIS    = 360          # Ring 1
MIRROR_RATIO         = SATURN_RING_TITHIS / LUNAR_SYNODIC_TITHIS  # 354
MIRROR_RATIO_FRAC    = MIRROR_RATIO / SOLAR_YEAR_TITHIS           # 0.983 ≈ 1


@dataclass
class SaturnCycleState:
    """Saturn cycle state — sidereal sign-ingress interpretation."""
    cycle_id:            str
    canonical_steps:     int               # 12 sign-ingresses per Ring 7
    cycle_tithis:        int               # 10620
    adjacent_step_deg:   float             # 30.0° per sign
    event_type:          str               # 'sign-ingress'

    longitudes:          Optional[list]    # 12 sign-ingress lons, ordered
    pairwise_separations: Optional[list]   # 11 separations
    mean_adjacent_step:  Optional[float]
    drift_deg:           Optional[float]
    closure:             Optional[bool]
    drift_tolerance:     float = 6.0

    # Substrate-mirror disclosure (canon line 953)
    moon_synodic_mirror_ratio: float = MIRROR_RATIO       # 354
    moon_synodic_mirror_in_solar_years: float = MIRROR_RATIO_FRAC  # ~0.983

    def to_dict(self) -> dict:
        return asdict(self)


def _angular_step(a: float, b: float) -> float:
    return (b - a) % 360.0


def compute_saturn_cycle_state(
    cycle_id: str,
    longitudes: Optional[list] = None,
) -> SaturnCycleState:
    """Compute Saturn cycle state from 12 sign-ingress longitudes (1 per zodiac sign)."""
    if longitudes is None:
        return SaturnCycleState(
            cycle_id=cycle_id,
            canonical_steps=SATURN_SIDEREAL_N,
            cycle_tithis=SATURN_RING_TITHIS,
            adjacent_step_deg=SATURN_SIGN_STEP,
            event_type=EVENT_TYPE,
            longitudes=None, pairwise_separations=None,
            mean_adjacent_step=None, drift_deg=None, closure=None,
        )

    if len(longitudes) != SATURN_SIDEREAL_N:
        raise ValueError(
            f"Saturn cycle {cycle_id} requires exactly {SATURN_SIDEREAL_N} "
            f"sign-ingress longitudes, got {len(longitudes)}. Substrate-incomplete."
        )

    seps = [_angular_step(longitudes[i], longitudes[i + 1]) for i in range(SATURN_SIDEREAL_N - 1)]
    mean_step = sum(seps) / len(seps)
    drift = mean_step - SATURN_SIGN_STEP
    closure = abs(drift) <= 6.0

    return SaturnCycleState(
        cycle_id=cycle_id,
        canonical_steps=SATURN_SIDEREAL_N,
        cycle_tithis=SATURN_RING_TITHIS,
        adjacent_step_deg=SATURN_SIGN_STEP,
        event_type=EVENT_TYPE,
        longitudes=longitudes,
        pairwise_separations=seps,
        mean_adjacent_step=mean_step,
        drift_deg=drift,
        closure=closure,
    )


def describe() -> str:
    return (
        "SATURN CYCLE ENGINE (Ring 7, sidereal sign-ingress cycle)\n"
        f"Substrate-canonical (canon §23b line 953): Saturn pt7 / La / Ring 7\n"
        f"  - {SATURN_SIDEREAL_N} sign-ingresses per Ring cycle (1 sign-per-year × 12yr)\n"
        f"  - {SATURN_RING_TITHIS} tithis (~29.5yr) per cycle\n"
        f"  - {SATURN_SIGN_STEP}° exact zodiac step per sign-ingress\n"
        f"  - Event type: SIGN-INGRESS (zodiac-boundary crossing)\n"
        f"\n"
        f"  NEW function-class candidate (NOT cyclic-syzygy-activate):\n"
        f"  Substrate-pressure-test: sign-ingress is NOT a syzygy event\n"
        f"  (not sun-earth-planet alignment, just planet crossing sign boundary).\n"
        f"  Different mechanism than cyclic-syzygy-activate.\n"
        f"  Candidate: `cyclic-sign-ingress-activate` (NEW function-class)\n"
        f"\n"
        f"  Substrate-mirror disclosure (canon line 953):\n"
        f"  - Saturn 29.5yr orbital ≈ Lunar 29.5d synodic (numerical mirror)\n"
        f"  - Ratio: {SATURN_RING_TITHIS}t / {LUNAR_SYNODIC_TITHIS}t = {MIRROR_RATIO}\n"
        f"  - 354 ≈ 1 solar year ({SOLAR_YEAR_TITHIS}t, 1.7% off)\n"
        f"  - Substrate-numerical-FACT not active substrate-function. Descriptor.\n"
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('FROZEN STATE:')
    print(json.dumps(compute_saturn_cycle_state('cycle_frozen').to_dict(), indent=2)[:400])
    print('...')
    print()
    ideal_lons = [(i * SATURN_SIGN_STEP) % 360.0 for i in range(SATURN_SIDEREAL_N)]
    print(f'SAMPLE: IDEAL CYCLE ({SATURN_SIDEREAL_N} sign-ingresses at exact {SATURN_SIGN_STEP}° steps):')
    s = compute_saturn_cycle_state('ideal', ideal_lons)
    d = s.to_dict()
    print(f"  canonical_steps: {d['canonical_steps']}")
    print(f"  cycle_tithis: {d['cycle_tithis']}")
    print(f"  event_type: {d['event_type']}")
    print(f"  mean_adjacent_step: {d['mean_adjacent_step']:.2f}°")
    print(f"  drift_deg: {d['drift_deg']:.4f}°")
    print(f"  closure: {d['closure']}")
    print(f"  moon_synodic_mirror_ratio: {d['moon_synodic_mirror_ratio']}")
    print(f"  moon_synodic_mirror_in_solar_years: {d['moon_synodic_mirror_in_solar_years']:.3f}")
