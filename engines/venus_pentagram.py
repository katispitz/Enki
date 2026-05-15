"""
Venus pentagram engine — temporal-composition probe.

Substrate-canonical (Lillu canon §23b OQ-RINGS-06): Venus pt3 / X3 / Ring 3 =
**5 inferior conjunctions over 2880 tithis ≈ 8 years**. The 5 conjunctions
trace a pentagram in the zodiac — 5 positions separated by ~144° each (the
pentagram angle), drifting only ~2°/cycle.

Per canon line 982: "Venus activates the φ-shell (dodecahedron / 5 Merkabas)."
Per canon line 930: "65 = 5×13 (Venus pentagram step × Neptune ring integer)."
Per canon line 983: "5 (Venus pentagram) × 13 (Mercury/Ring 5) = 65 is a
φ-family product. Not coincidence."

This engine substantiates Kati's substrate-insight (2026-05-12): pentagon at
N=5 is Venus-cyclic TEMPORAL composition, NOT spatial multi-planet
composition. Different shape than triangle-aspect-activate (3 different
planets at 1 time) and planet-aspect-activate (2 different planets at 1
time). N-polygon family BIFURCATES at N=5.

Function shape:
  - Input: 5 Venus inferior-conjunction longitudes (chronologically ordered
    over one 8-year cycle)
  - Output: pentagram-state (5 vertex positions + angular separation
    pattern + closure check + drift measurement)

Substrate-discipline notes:
  - This is NOT pentagon-aspect-activate (which would have been 5 different
    planets at dodec-face vertices). That candidate STAYS substrate-pending
    on T1.4 (20 ico face / dodec vert class meaning OPEN).
  - Venus pentagram IS substrate-locked at canon §23b OQ-RINGS-06.
  - Different function-class candidate: `venus-pentagram-activate` (temporal,
    1-planet-5-samples) OR `temporal-pentagram-activate` (shell-agnostic
    temporal-composition name).
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


# Substrate constants per canon §23b OQ-RINGS-06
__canonical__ = {
    'function_class':     'cyclic-syzygy-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'temporal',
    'residency_id':       'venus-ring3-pentagram',
    'canon_citation':     'canon §23b OQ-RINGS-06 / Venus Ring 3 / 5 inferior-conjunction syzygies / 2880t / 8yr',
    'status':             'canonical',
}


VENUS_RING_TITHIS    = 2880          # 8 years = 2880 tithis (canon §23b)
VENUS_PENTAGRAM_N    = 5             # 5 inferior conjunctions per cycle
PENTAGRAM_STEP_DEG   = 360.0 / 5     # 72° between pentagram vertices (not 144°)
                                     # NOTE: 144° = adjacent pentagram-star vertex
                                     # 72° = sequential pentagram-vertex
                                     # Both substrate-meaningful per pentagram structure
PENTAGRAM_ADJ_STEP   = 144.0         # adjacent inferior-conjunction step in zodiac
                                     # (Venus retrograde causes apparent backward step)


@dataclass
class VenusPentagramState:
    """Substrate-honest snapshot of a Venus pentagram cycle.

    5 inferior-conjunction longitudes over 8 years, traced angular structure.
    """
    # Permanent definition (always known)
    cycle_id:           str              # identifier for this 8-year cycle
    canonical_steps:    int              # 5 per canon
    cycle_tithis:       int              # 2880 per canon §23b OQ-RINGS-06
    pentagram_step_deg: float            # 72° (closure step)
    adjacent_step_deg:  float            # 144° (zodiac-apparent step between conjunctions)

    # Live state (NULL when no longitudes supplied)
    longitudes:         Optional[list]   # 5 Venus lons at inferior conjunctions, ordered
    pairwise_separations: Optional[list] # 4 separations between consecutive conjunctions
    closure_separation: Optional[float]  # separation from 5th back to 1st (closure check)
    mean_adjacent_step: Optional[float]  # avg of 4 adjacent steps (should approach 144°)
    drift_deg:          Optional[float]  # how much the pentagram has shifted from ideal
                                         # (drift = mean_adjacent_step - 144° expected)
    pentagram_closure:  Optional[bool]   # True if cycle closes within drift tolerance
    drift_tolerance:    float = 6.0      # V2.6 G4 ignition orb — closure within 6°

    def to_dict(self) -> dict:
        return asdict(self)


def _angular_step(a: float, b: float) -> float:
    """Forward-going step from a to b modulo 360 (always 0..360)."""
    step = (b - a) % 360.0
    return step


def compute_venus_pentagram_state(
    cycle_id: str,
    lon1: Optional[float] = None,
    lon2: Optional[float] = None,
    lon3: Optional[float] = None,
    lon4: Optional[float] = None,
    lon5: Optional[float] = None,
) -> VenusPentagramState:
    """Compute Venus pentagram state from 5 chronologically-ordered conjunction longitudes.

    All 5 None → frozen state (substrate-locks only).
    All 5 supplied → live pentagram-state with closure check.
    Mixed → ValueError (substrate-honest reject — partial pentagram is incomplete).
    """
    lons = [lon1, lon2, lon3, lon4, lon5]
    if all(l is None for l in lons):
        return VenusPentagramState(
            cycle_id=cycle_id,
            canonical_steps=VENUS_PENTAGRAM_N,
            cycle_tithis=VENUS_RING_TITHIS,
            pentagram_step_deg=PENTAGRAM_STEP_DEG,
            adjacent_step_deg=PENTAGRAM_ADJ_STEP,
            longitudes=None, pairwise_separations=None,
            closure_separation=None, mean_adjacent_step=None,
            drift_deg=None, pentagram_closure=None,
        )

    if any(l is None for l in lons):
        raise ValueError(
            f"Venus pentagram {cycle_id} requires all 5 conjunction longitudes "
            "or none — partial input is substrate-incomplete (cycle not closed)"
        )

    # Adjacent steps between consecutive conjunctions (4 forward steps)
    seps = [_angular_step(lons[i], lons[i + 1]) for i in range(4)]
    # Closure step from 5th back to 1st (wrapping a full cycle)
    closure_step = _angular_step(lons[4], lons[0])

    mean_step = sum(seps) / 4.0
    drift = mean_step - PENTAGRAM_ADJ_STEP
    closure = (
        abs(drift) <= 6.0
        and abs(closure_step - PENTAGRAM_ADJ_STEP) <= 6.0
    )

    return VenusPentagramState(
        cycle_id=cycle_id,
        canonical_steps=VENUS_PENTAGRAM_N,
        cycle_tithis=VENUS_RING_TITHIS,
        pentagram_step_deg=PENTAGRAM_STEP_DEG,
        adjacent_step_deg=PENTAGRAM_ADJ_STEP,
        longitudes=lons,
        pairwise_separations=seps,
        closure_separation=closure_step,
        mean_adjacent_step=mean_step,
        drift_deg=drift,
        pentagram_closure=closure,
    )


def describe() -> str:
    return (
        "VENUS PENTAGRAM ENGINE (temporal-composition probe)\n"
        f"Substrate-canonical (canon §23b OQ-RINGS-06): Venus pt3 / X3 / Ring 3\n"
        f"  - {VENUS_PENTAGRAM_N} inferior conjunctions per cycle\n"
        f"  - {VENUS_RING_TITHIS} tithis (8 years) per cycle\n"
        f"  - {PENTAGRAM_ADJ_STEP}° apparent zodiac step between consecutive conjunctions\n"
        f"  - {PENTAGRAM_STEP_DEG}° pentagram-closure step (5 × 72° = 360°)\n"
        f"  - φ-shell activation: 'Venus activates the φ-shell (dodecahedron / 5 Merkabas)'\n"
        f"  - 65-octave product: 5 (Venus pentagram) × 13 (Mercury Ring 5) = 65 φ-family\n"
        f"\n"
        f"Function-class CANDIDATE: `venus-pentagram-activate` (temporal-composition,\n"
        f"  1-planet × 5-time-samples) — qualitatively DIFFERENT from planet-aspect-activate\n"
        f"  (2-planet) and triangle-aspect-activate (3-planet) which are spatial-compositions.\n"
        f"\n"
        f"Substrate finding (FINDINGS_012): N-polygon aspect-activate family BIFURCATES\n"
        f"  at N=5. Pentagon-N has TWO substrate-honest interpretations:\n"
        f"    (a) Spatial: 5 different planets at 5 dodec-face vertices (T1.4 OPEN, no\n"
        f"        canon-lock for dodec-vertex planet residency)\n"
        f"    (b) Temporal: 1 planet (Venus) × 5 time-samples (CANON-LOCKED §23b OQ-RINGS-06)\n"
        f"\n"
        f"Reading (b) is the only substrate-canonical N=5 instance.\n"
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('FROZEN STATE (no longitudes):')
    print(json.dumps(compute_venus_pentagram_state('cycle_frozen').to_dict(), indent=2))
    print()
    # Sample: ideal pentagram — 5 conjunctions at 144° apparent steps starting at 0°
    print('SAMPLE: IDEAL PENTAGRAM (0°, 144°, 288°, 72°, 216° → closure 360°):')
    state = compute_venus_pentagram_state(
        'ideal_cycle',
        0.0, 144.0, 288.0, 72.0, 216.0,
    )
    d = state.to_dict()
    print(f"  longitudes: {d['longitudes']}")
    print(f"  pairwise_separations: {d['pairwise_separations']}")
    print(f"  closure_separation: {d['closure_separation']}")
    print(f"  mean_adjacent_step: {d['mean_adjacent_step']:.2f}°")
    print(f"  drift_deg: {d['drift_deg']:.2f}°")
    print(f"  pentagram_closure: {d['pentagram_closure']}")
