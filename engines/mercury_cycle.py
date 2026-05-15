"""
Mercury 41-conjunction cycle engine — temporal-composition probe (peer to Venus pentagram).

Substrate-canonical (Lillu canon §23b OQ-RINGS-07 + line 951 + line 987):
  Mercury / pt5 / Sol / Ring 5 = 41 inferior conjunctions over 4680t (~13yr).

Per canon line 966:
  "OQ-RINGS-07 RESOLVED — 4680t attribution. Mechanism test: Mercury's 41
  inferior conjunctions generate the 13yr closure → primary driver."

Function shape: takes 41 Mercury inferior-conjunction longitudes (chronologically
ordered over ~13yr cycle); composes adjacent-conjunction angular separations;
emits cycle-closure state.

Substrate distinction from Venus pentagram:
  - Venus: N=5 (pentagram), 2880t / 8yr, adjacent step ≈ 144°
  - Mercury: N=41 (41-gon), 4680t / 13yr, adjacent step ≈ 114.5° (360 × 13.04/41)
  - Both: 1-planet × N-time-samples (temporal composition)
  - Both: planet's inferior conjunctions over orbital cycle
  - Both: inscribed N-vertex polygon in zodiac (closes after N cycles)
  - Both: substrate-canonically locked in canon §23b

If shape MATCHES at the substrate-position-agnostic compute level (cyclic-N-gon
closure from N planet-longitude-samples), function-class is shell-agnostic +
N-agnostic + planet-agnostic. Cross-N temporal-composition residency.

Candidate function-class name (cross-planet, cross-N):
  `cyclic-conjunction-activate` (names compute: cyclic, conjunction-based, activation)
  OR `temporal-cyclic-activate` (more abstract)
  OR `planet-cycle-activate` (planet-cycle structure)
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


# Substrate constants per canon §23b OQ-RINGS-07
__canonical__ = {
    'function_class':     'cyclic-syzygy-activate',
    'functional_tier':    'first-composition',
    'compositional_axis': 'temporal',
    'residency_id':       'mercury-ring5-cycle',
    'canon_citation':     'canon §23b OQ-RINGS-07 / Mercury Ring 5 / 41 inferior-conjunction syzygies / 4680t / 13yr',
    'status':             'canonical',
}


MERCURY_RING_TITHIS  = 4680           # 13 years per canon
MERCURY_CYCLE_N      = 41             # 41 inferior conjunctions per Mercury Ring cycle
MERCURY_ADJ_STEP_DEG = 360.0 * 13.04 / 41.0  # ≈ 114.5° per adjacent conjunction
# Note: exact value 360 × 13.04/41 = 114.46°; canon doesn't lock to higher precision
MERCURY_CLOSURE_STEP_DEG = 360.0 / 41.0   # 8.78° per inscribed-vertex step (if all 41 fit on closure)


@dataclass
class MercuryCycleState:
    """Substrate-honest snapshot of a Mercury 41-conjunction cycle."""
    # Permanent definition
    cycle_id:            str
    canonical_steps:     int               # 41 per canon
    cycle_tithis:        int               # 4680 per canon
    adjacent_step_deg:   float             # ≈ 114.5° expected zodiac step between consecutive conjunctions
    closure_step_deg:    float             # 360/41 ≈ 8.78° if treating cycle as inscribed 41-gon

    # Live state
    longitudes:          Optional[list]    # 41 Mercury lons at inferior conjunctions, ordered
    pairwise_separations: Optional[list]   # 40 separations between consecutive conjunctions
    mean_adjacent_step:  Optional[float]
    drift_deg:           Optional[float]   # mean_step - expected adjacent step
    closure:             Optional[bool]    # closure achieved within drift tolerance
    drift_tolerance:     float = 6.0       # V2.6 G4 ignition orb

    def to_dict(self) -> dict:
        return asdict(self)


def _angular_step(a: float, b: float) -> float:
    return (b - a) % 360.0


def compute_mercury_cycle_state(
    cycle_id: str,
    longitudes: Optional[list] = None,
) -> MercuryCycleState:
    """Compute Mercury cycle state from 41 chronologically-ordered conjunction longitudes.

    None → frozen state.
    list of 41 → live cycle-state with closure check.
    Other → ValueError (substrate-honest reject — partial cycle is incomplete).
    """
    if longitudes is None:
        return MercuryCycleState(
            cycle_id=cycle_id,
            canonical_steps=MERCURY_CYCLE_N,
            cycle_tithis=MERCURY_RING_TITHIS,
            adjacent_step_deg=MERCURY_ADJ_STEP_DEG,
            closure_step_deg=MERCURY_CLOSURE_STEP_DEG,
            longitudes=None, pairwise_separations=None,
            mean_adjacent_step=None, drift_deg=None, closure=None,
        )

    if len(longitudes) != MERCURY_CYCLE_N:
        raise ValueError(
            f"Mercury cycle {cycle_id} requires exactly {MERCURY_CYCLE_N} "
            f"conjunction longitudes, got {len(longitudes)}. Substrate-incomplete."
        )

    seps = [_angular_step(longitudes[i], longitudes[i + 1]) for i in range(MERCURY_CYCLE_N - 1)]
    mean_step = sum(seps) / len(seps)
    drift = mean_step - MERCURY_ADJ_STEP_DEG
    closure = abs(drift) <= 6.0

    return MercuryCycleState(
        cycle_id=cycle_id,
        canonical_steps=MERCURY_CYCLE_N,
        cycle_tithis=MERCURY_RING_TITHIS,
        adjacent_step_deg=MERCURY_ADJ_STEP_DEG,
        closure_step_deg=MERCURY_CLOSURE_STEP_DEG,
        longitudes=longitudes,
        pairwise_separations=seps,
        mean_adjacent_step=mean_step,
        drift_deg=drift,
        closure=closure,
    )


def describe() -> str:
    return (
        "MERCURY 41-CONJUNCTION CYCLE (temporal-composition probe, peer to Venus pentagram)\n"
        f"Substrate-canonical (canon §23b OQ-RINGS-07): Mercury pt5 / Sol / Ring 5\n"
        f"  - {MERCURY_CYCLE_N} inferior conjunctions per cycle\n"
        f"  - {MERCURY_RING_TITHIS} tithis (~13 years) per cycle\n"
        f"  - ~{MERCURY_ADJ_STEP_DEG:.1f}° apparent zodiac step between consecutive conjunctions\n"
        f"  - {MERCURY_CLOSURE_STEP_DEG:.2f}° per inscribed-vertex step if read as 41-gon\n"
        f"  - 65-octave: 13 (Mercury Ring 5) × 5 (Venus pentagram) = 65 φ-family\n"
        f"\n"
        f"Function-class candidate: `cyclic-conjunction-activate` (cross-planet, cross-N).\n"
        f"  Same shape as Venus pentagram (1-planet × N-time-samples) at different N=41.\n"
        f"  If shape match holds at substrate-position-agnostic compute level →\n"
        f"  2 INDEPENDENT primitive-class residencies (Venus Ring 3 + Mercury Ring 5) →\n"
        f"  Athena lock-by-redundancy MET → canonical temporal-cyclic-family entry.\n"
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('FROZEN STATE:')
    print(json.dumps(compute_mercury_cycle_state('cycle_frozen').to_dict(), indent=2)[:500])
    print('...')
    print()
    # Sample: ideal Mercury cycle — 41 lons at 114.46° steps starting at 0°
    ideal_lons = [(i * MERCURY_ADJ_STEP_DEG) % 360.0 for i in range(MERCURY_CYCLE_N)]
    print(f'SAMPLE: IDEAL CYCLE ({MERCURY_CYCLE_N} conjunctions at exact {MERCURY_ADJ_STEP_DEG:.2f}° steps):')
    state = compute_mercury_cycle_state('ideal_cycle', ideal_lons)
    d = state.to_dict()
    print(f"  canonical_steps: {d['canonical_steps']}")
    print(f"  cycle_tithis: {d['cycle_tithis']}")
    print(f"  mean_adjacent_step: {d['mean_adjacent_step']:.2f}°")
    print(f"  drift_deg: {d['drift_deg']:.4f}°")
    print(f"  closure: {d['closure']}")
    print(f"  separations (first 5): {[round(s,2) for s in d['pairwise_separations'][:5]]}")
