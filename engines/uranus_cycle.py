"""
Uranus cycle engine — Ring 6 sign-ingress (3rd cyclic-sign-ingress-activate residency).

Substrate-canonical (Lillu canon §23b line 952):
  Uranus / pt6 / X6 / Ring 6 = 30240t / 84yr / "Full zodiac circuit (7yr/sign × 12)"

Same shape as Saturn Ring 7 + Jupiter Ring 8 sign-ingress cycles. Different
period (84yr — much slower outer planet), same N=12 zodiac-cardinality.

Substrate-pattern: outer planet zodiac-traversal cycle. Adjacent step 30°
(exact, by zodiac-sign cardinality).
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


__canonical__ = {
    'function_class':     'cyclic-sign-ingress-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'temporal',
    'residency_id':       'uranus-ring6-cycle',
    'canon_citation':     'canon §23b line 952 / Uranus Ring 6 / 12 sign-ingresses / 30240t / 84yr',
    'status':             'canonical',
}


URANUS_RING_TITHIS   = 30240         # 84 years per canon §23b line 952
URANUS_SIDEREAL_N    = 12            # 12 zodiac signs per Ring 6
URANUS_SIGN_STEP     = 30.0          # 360° / 12 exact
EVENT_TYPE           = 'sign-ingress'


@dataclass
class UranusCycleState:
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


def compute_uranus_cycle_state(
    cycle_id: str,
    longitudes: Optional[list] = None,
) -> UranusCycleState:
    if longitudes is None:
        return UranusCycleState(
            cycle_id=cycle_id,
            canonical_steps=URANUS_SIDEREAL_N,
            cycle_tithis=URANUS_RING_TITHIS,
            adjacent_step_deg=URANUS_SIGN_STEP,
            event_type=EVENT_TYPE,
            longitudes=None, pairwise_separations=None,
            mean_adjacent_step=None, drift_deg=None, closure=None,
        )
    if len(longitudes) != URANUS_SIDEREAL_N:
        raise ValueError(
            f"Uranus cycle {cycle_id} requires exactly {URANUS_SIDEREAL_N} "
            f"sign-ingress longitudes, got {len(longitudes)}. Substrate-incomplete."
        )
    seps = [_angular_step(longitudes[i], longitudes[i + 1]) for i in range(URANUS_SIDEREAL_N - 1)]
    mean_step = sum(seps) / len(seps)
    drift = mean_step - URANUS_SIGN_STEP
    closure = abs(drift) <= 6.0
    return UranusCycleState(
        cycle_id=cycle_id,
        canonical_steps=URANUS_SIDEREAL_N,
        cycle_tithis=URANUS_RING_TITHIS,
        adjacent_step_deg=URANUS_SIGN_STEP,
        event_type=EVENT_TYPE,
        longitudes=longitudes,
        pairwise_separations=seps,
        mean_adjacent_step=mean_step,
        drift_deg=drift,
        closure=closure,
    )


def describe() -> str:
    return (
        f"URANUS CYCLE ENGINE (Ring 6, 3rd cyclic-sign-ingress-activate residency)\n"
        f"Substrate-canonical (canon §23b line 952): Uranus pt6 / X6 / Ring 6\n"
        f"  - {URANUS_SIDEREAL_N} sign-ingresses per Ring cycle\n"
        f"  - {URANUS_RING_TITHIS} tithis (~84yr) per cycle\n"
        f"  - {URANUS_SIGN_STEP}° exact zodiac step per sign-ingress\n"
        f"  - Event type: sign-ingress (zodiac-boundary crossing, outer-planet family)\n"
    )


if __name__ == '__main__':
    print(describe())
    ideal = [(i * URANUS_SIGN_STEP) % 360.0 for i in range(URANUS_SIDEREAL_N)]
    s = compute_uranus_cycle_state('ideal', ideal).to_dict()
    print(f"\nIDEAL CYCLE: closure={s['closure']}, drift={s['drift_deg']:.4f}°, mean={s['mean_adjacent_step']:.2f}°")
