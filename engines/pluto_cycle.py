"""
Pluto cycle engine — Ring 0 sign-ingress (4th cyclic-sign-ingress-activate residency).

Substrate-canonical (Nammu canon §23b line 945):
  Pluto / pt0 / Do / Ring 0 = 89280t / ~248yr / "Pluto outer-orbit carrier (integer×30 ✓)"

Per canon §23b OQ-RINGS-04 RESOLVED + Earth-Pluto-Ring0 retraction 2026-05-11:
Pluto promoted to Ring 0 (was Earth/pt0/1t — retracted as inconsistent overlay).
Pluto sidereal ≈ 248yr → 12 sign-ingresses per Ring cycle, ~20.7yr/sign.

Note: Pluto's orbit is highly elliptical + inclined (heliocentric). For
substrate-engine purposes, ZODIAC SIGN-INGRESS is canonically the 12-sign
traversal per sidereal cycle (uniform 30° apparent step in ecliptic longitude
projection). Sign-ingress event timing varies non-uniformly due to orbital
eccentricity, but the CANONICAL 12-sign-cardinality holds substrate-honestly.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


__canonical__ = {
    'function_class':     'cyclic-sign-ingress-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'temporal',
    'residency_id':       'pluto-ring0-cycle',
    'canon_citation':     'canon §23b line 945 OQ-RINGS-04 / Pluto Ring 0 / 12 sign-ingresses / 89280t / ~248yr',
    'status':             'canonical',
}


PLUTO_RING_TITHIS    = 89280         # ~248 years per canon §23b line 945
PLUTO_SIDEREAL_N     = 12            # 12 zodiac signs per Ring 0
PLUTO_SIGN_STEP      = 30.0          # 360° / 12 exact
EVENT_TYPE           = 'sign-ingress'


@dataclass
class PlutoCycleState:
    cycle_id:            str
    canonical_steps:     int
    cycle_tithis:        int
    adjacent_step_deg:   float
    event_type:          str
    longitudes:          Optional[list]
    pairwise_separations: Optional[list]
    mean_adjacent_step:  Optional[float]
    drift_deg:           Optional[float]
    closure:             Optional[bool]
    drift_tolerance:     float = 6.0

    def to_dict(self) -> dict:
        return asdict(self)


def _angular_step(a: float, b: float) -> float:
    return (b - a) % 360.0


def compute_pluto_cycle_state(
    cycle_id: str,
    longitudes: Optional[list] = None,
) -> PlutoCycleState:
    if longitudes is None:
        return PlutoCycleState(
            cycle_id=cycle_id,
            canonical_steps=PLUTO_SIDEREAL_N,
            cycle_tithis=PLUTO_RING_TITHIS,
            adjacent_step_deg=PLUTO_SIGN_STEP,
            event_type=EVENT_TYPE,
            longitudes=None, pairwise_separations=None,
            mean_adjacent_step=None, drift_deg=None, closure=None,
        )
    if len(longitudes) != PLUTO_SIDEREAL_N:
        raise ValueError(
            f"Pluto cycle {cycle_id} requires exactly {PLUTO_SIDEREAL_N} "
            f"sign-ingress longitudes, got {len(longitudes)}. Substrate-incomplete."
        )
    seps = [_angular_step(longitudes[i], longitudes[i + 1]) for i in range(PLUTO_SIDEREAL_N - 1)]
    mean_step = sum(seps) / len(seps)
    drift = mean_step - PLUTO_SIGN_STEP
    closure = abs(drift) <= 6.0
    return PlutoCycleState(
        cycle_id=cycle_id,
        canonical_steps=PLUTO_SIDEREAL_N,
        cycle_tithis=PLUTO_RING_TITHIS,
        adjacent_step_deg=PLUTO_SIGN_STEP,
        event_type=EVENT_TYPE,
        longitudes=longitudes,
        pairwise_separations=seps,
        mean_adjacent_step=mean_step,
        drift_deg=drift,
        closure=closure,
    )


def describe() -> str:
    return (
        f"PLUTO CYCLE ENGINE (Ring 0, 4th cyclic-sign-ingress-activate residency)\n"
        f"Substrate-canonical (canon §23b line 945, OQ-RINGS-04 RESOLVED): Pluto pt0 / Do / Ring 0\n"
        f"  - {PLUTO_SIDEREAL_N} sign-ingresses per Ring cycle\n"
        f"  - {PLUTO_RING_TITHIS} tithis (~248yr) per cycle\n"
        f"  - {PLUTO_SIGN_STEP}° exact zodiac step per sign-ingress\n"
        f"  - 'Pluto outer-orbit carrier' framing (canon §23b)\n"
    )


if __name__ == '__main__':
    print(describe())
    ideal = [(i * PLUTO_SIGN_STEP) % 360.0 for i in range(PLUTO_SIDEREAL_N)]
    s = compute_pluto_cycle_state('ideal', ideal).to_dict()
    print(f"\nIDEAL CYCLE: closure={s['closure']}, drift={s['drift_deg']:.4f}°, mean={s['mean_adjacent_step']:.2f}°")
