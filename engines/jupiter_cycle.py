"""
Jupiter cycle engine — Ring 8 sign-ingress probe (peer to Saturn Ring 7).

Substrate-canonical (Lillu canon §23b line 954):
  Jupiter / pt8 / Si / Ring 8 = 4320t / 12yr / "Zodiac circuit (1yr/sign × 12)"

Same shape as Saturn Ring 7 (FINDINGS_016): N=12 sign-ingresses per Ring cycle,
30° step per sign. Different period (12yr vs Saturn 29.5yr), different planet,
but SAME substrate-mechanism (zodiac-boundary crossing).

Tests cross-R-tier residency for cyclic-sign-ingress-activate candidate
function-class. If shape MATCHES Saturn at compute level → 2 independent
residencies → Athena lock-by-redundancy MET → canonical promotion ready.

Substrate-pattern recurrence:
  Saturn Ring 7: 12 sign-ingresses / 29.5yr / 30° step
  Jupiter Ring 8: 12 sign-ingresses / 12yr / 30° step
  Both: outer planet, slow orbital, ~1 sign/year traversal rate
  Both: sign-ingress event-type (NOT syzygy)
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


__canonical__ = {
    'function_class':     'cyclic-sign-ingress-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'temporal',
    'residency_id':       'jupiter-ring8-cycle',
    'canon_citation':     'canon §23b line 954 / Jupiter Ring 8 / 12 sign-ingresses / 4320t / 12yr',
    'status':             'canonical',
}


JUPITER_RING_TITHIS  = 4320          # 12 years per canon §23b line 954
JUPITER_SIDEREAL_N   = 12            # 12 zodiac signs per Ring 8
JUPITER_SIGN_STEP    = 30.0          # 360° / 12 = exact 30° per sign-ingress
EVENT_TYPE           = 'sign-ingress'


@dataclass
class JupiterCycleState:
    """Jupiter cycle state — sidereal sign-ingress (parallel to Saturn)."""
    cycle_id:            str
    canonical_steps:     int               # 12
    cycle_tithis:        int               # 4320
    adjacent_step_deg:   float             # 30.0°
    event_type:          str               # 'sign-ingress'

    longitudes:          Optional[list]    # 12 sign-ingress lons
    pairwise_separations: Optional[list]   # 11 separations
    mean_adjacent_step:  Optional[float]
    drift_deg:           Optional[float]
    closure:             Optional[bool]
    drift_tolerance:     float = 6.0

    def to_dict(self) -> dict:
        return asdict(self)


def _angular_step(a: float, b: float) -> float:
    return (b - a) % 360.0


def compute_jupiter_cycle_state(
    cycle_id: str,
    longitudes: Optional[list] = None,
) -> JupiterCycleState:
    if longitudes is None:
        return JupiterCycleState(
            cycle_id=cycle_id,
            canonical_steps=JUPITER_SIDEREAL_N,
            cycle_tithis=JUPITER_RING_TITHIS,
            adjacent_step_deg=JUPITER_SIGN_STEP,
            event_type=EVENT_TYPE,
            longitudes=None, pairwise_separations=None,
            mean_adjacent_step=None, drift_deg=None, closure=None,
        )

    if len(longitudes) != JUPITER_SIDEREAL_N:
        raise ValueError(
            f"Jupiter cycle {cycle_id} requires exactly {JUPITER_SIDEREAL_N} "
            f"sign-ingress longitudes, got {len(longitudes)}. Substrate-incomplete."
        )

    seps = [_angular_step(longitudes[i], longitudes[i + 1]) for i in range(JUPITER_SIDEREAL_N - 1)]
    mean_step = sum(seps) / len(seps)
    drift = mean_step - JUPITER_SIGN_STEP
    closure = abs(drift) <= 6.0

    return JupiterCycleState(
        cycle_id=cycle_id,
        canonical_steps=JUPITER_SIDEREAL_N,
        cycle_tithis=JUPITER_RING_TITHIS,
        adjacent_step_deg=JUPITER_SIGN_STEP,
        event_type=EVENT_TYPE,
        longitudes=longitudes,
        pairwise_separations=seps,
        mean_adjacent_step=mean_step,
        drift_deg=drift,
        closure=closure,
    )


def describe() -> str:
    return (
        "JUPITER CYCLE ENGINE (Ring 8, sidereal sign-ingress, peer to Saturn Ring 7)\n"
        f"Substrate-canonical (canon §23b line 954): Jupiter pt8 / Si / Ring 8\n"
        f"  - {JUPITER_SIDEREAL_N} sign-ingresses per Ring cycle\n"
        f"  - {JUPITER_RING_TITHIS} tithis (~12yr) per cycle\n"
        f"  - {JUPITER_SIGN_STEP}° exact zodiac step per sign-ingress\n"
        f"  - Event type: SIGN-INGRESS (zodiac-boundary crossing)\n"
        f"\n"
        f"Cross-R-tier residency probe for `cyclic-sign-ingress-activate`:\n"
        f"  Saturn Ring 7 (FINDINGS_016) — 1st residency.\n"
        f"  Jupiter Ring 8 (THIS) — 2nd residency candidate.\n"
        f"  Both share: N=12 sign-ingresses, 30° step, same event-type.\n"
        f"  Differ: period (12yr vs 29.5yr), planet (Jupiter vs Saturn).\n"
        f"\n"
        f"If shape MATCHES → Athena lock-by-redundancy MET → canonical promotion.\n"
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()
    ideal_lons = [(i * JUPITER_SIGN_STEP) % 360.0 for i in range(JUPITER_SIDEREAL_N)]
    print(f'SAMPLE: IDEAL CYCLE ({JUPITER_SIDEREAL_N} sign-ingresses at exact {JUPITER_SIGN_STEP}° steps):')
    s = compute_jupiter_cycle_state('ideal', ideal_lons)
    d = s.to_dict()
    print(f"  canonical_steps: {d['canonical_steps']}")
    print(f"  cycle_tithis: {d['cycle_tithis']}")
    print(f"  event_type: {d['event_type']}")
    print(f"  mean_adjacent_step: {d['mean_adjacent_step']:.2f}°")
    print(f"  drift_deg: {d['drift_deg']:.4f}°")
    print(f"  closure: {d['closure']}")
