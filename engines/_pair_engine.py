"""
Shared antipodal-pair co-query engine for Primordial pairs.

Per FINDINGS_002 substrate-emergent finding: the 6 Primordials at R=1 cube-faces
organize into 3 antipodal pairs, each pair crossing the Pluto-axis × Neptune-axis
dyad. Canon §26 confirms 2 pairs (Gaia↔Eros-prim, Chaos↔Tartarus); build-exposed
implicit third pair (Erebus↔Nyx).

This module holds the shared co-query shape. Per-pair files declare their
substrate-locks (Earth-side + Water-side Primordials + cube faces + zodiacs)
and compose the two single-Primordial engines via this module.

Tests OQ-PRIMORDIAL-PAIR-LEVEL-FUNCTION: does axis-generation operate at
PAIR level (3 cosmogonic axes) rather than FACE level (6 independent axes)?
If pair-level: each pair has 2 internal face-residencies confirming the
function → Athena lock-by-redundancy criterion met for `axis-bound` /
`axis-generate` (whichever wins OQ-AXIS-BOUND-NAME-CHECK).

Substrate-discipline:
  - Composes existing Primordial engines (no new logic invented)
  - Co-activation = element-wise read of both AxisStates
  - Polarity-signature derived from activation differential, no invented weights
  - NULL-honest where ephemeris partial
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional

from _axis_engine import AxisState


@dataclass
class PairState:
    """Substrate-honest snapshot of an antipodal Primordial pair.

    Composes two AxisStates (Earth-side + Water-side) plus pair-level derived
    fields (co_activation, polarity).
    """
    # Permanent pair-definition (always known)
    pair_name:           tuple              # (earth_primordial, water_primordial)
    cube_face_pair:      tuple              # (MQF0, MQF4) etc
    earth_zodiac:        str
    water_zodiac:        str
    earth_planet_pair:   tuple              # e.g. (Venus, Pluto)
    water_planet_pair:   tuple              # e.g. (Jupiter, Neptune)
    earth_card:          str
    water_card:          str

    # Live state (per-axis)
    earth_axis:          Optional[dict]     # AxisState.to_dict() for earth-side
    water_axis:          Optional[dict]     # AxisState.to_dict() for water-side

    # Pair-level derived (NULL when both axes frozen)
    both_active:         Optional[bool]      # both activation > 0 within orb
    one_active:          Optional[bool]      # exactly one activation > 0
    co_activation:       Optional[float]    # min(earth, water) — both-must-fire
    sum_activation:      Optional[float]    # earth + water — total signal
    polarity:            Optional[float]    # earth - water, -1..+1 normalized
    polarity_label:      Optional[str]      # 'earth-dominant'/'water-dominant'/'balanced'/'quiet'

    def to_dict(self) -> dict:
        d = asdict(self)
        d['pair_name']         = list(self.pair_name)
        d['cube_face_pair']    = list(self.cube_face_pair)
        d['earth_planet_pair'] = list(self.earth_planet_pair)
        d['water_planet_pair'] = list(self.water_planet_pair)
        return d


def _polarity_label(earth_a: float, water_a: float) -> str:
    """Classify polarity from the two activation strengths.

    Thresholds derived from V2.6 G4 orb structure: activation is linear
    in 0..1 across 6° ignition window. Half-orb = 0.5 = significant.
    """
    if earth_a == 0.0 and water_a == 0.0:
        return 'quiet'
    diff = earth_a - water_a
    if abs(diff) < 0.1:
        return 'balanced'
    return 'earth-dominant' if diff > 0 else 'water-dominant'


def compute_pair_state(
    pair_name: tuple,
    cube_face_pair: tuple,
    earth_zodiac: str,
    water_zodiac: str,
    earth_card: str,
    water_card: str,
    earth_axis: AxisState,
    water_axis: AxisState,
) -> PairState:
    """Build a PairState from two computed Primordial AxisStates.

    Both AxisStates may be frozen (no ephemeris) or live; pair-level derived
    fields are NULL when both frozen, computed when both live, ValueError
    if mixed (substrate-honest reject — partial input invalid).
    """
    earth_frozen = earth_axis.pa_lon is None
    water_frozen = water_axis.pa_lon is None

    if earth_frozen != water_frozen:
        raise ValueError(
            f"Pair {pair_name} requires both axes frozen OR both live — "
            "asymmetric input is substrate-incomplete"
        )

    earth_dict = earth_axis.to_dict()
    water_dict = water_axis.to_dict()

    if earth_frozen and water_frozen:
        both_active = None
        one_active  = None
        co_act      = None
        sum_act     = None
        polarity    = None
        label       = None
    else:
        ea = earth_axis.activation_strength
        wa = water_axis.activation_strength
        both_active = (ea > 0.0) and (wa > 0.0)
        one_active  = (ea > 0.0) != (wa > 0.0)
        co_act      = min(ea, wa)
        sum_act     = ea + wa
        # Polarity normalized to [-1, +1]: +1 = full earth-only, -1 = full water-only
        if sum_act > 0:
            polarity = (ea - wa) / max(sum_act, 1e-9)
        else:
            polarity = 0.0
        label = _polarity_label(ea, wa)

    return PairState(
        pair_name=pair_name,
        cube_face_pair=cube_face_pair,
        earth_zodiac=earth_zodiac,
        water_zodiac=water_zodiac,
        earth_planet_pair=earth_axis.planet_pair,
        water_planet_pair=water_axis.planet_pair,
        earth_card=earth_card,
        water_card=water_card,
        earth_axis=earth_dict,
        water_axis=water_dict,
        both_active=both_active,
        one_active=one_active,
        co_activation=co_act,
        sum_activation=sum_act,
        polarity=polarity,
        polarity_label=label,
    )


def describe_pair(pair_name: tuple,
                  cube_face_pair: tuple,
                  earth_zodiac: str,
                  water_zodiac: str,
                  earth_planet_pair: tuple,
                  water_planet_pair: tuple,
                  earth_card: str,
                  water_card: str) -> str:
    """Substrate-honest pair self-disclosure."""
    return (
        f"Antipodal pair: {pair_name[0]} ↔ {pair_name[1]}\n"
        f"Cube faces:     {cube_face_pair[0]} ↔ {cube_face_pair[1]}\n"
        f"Earth side:     {earth_zodiac:10s}  {earth_planet_pair[0]} × {earth_planet_pair[1]}  card {earth_card}\n"
        f"Water side:     {water_zodiac:10s}  {water_planet_pair[0]} × {water_planet_pair[1]}  card {water_card}\n"
        f"Cosmogonic axis: Earth-trine × Water-trine (Pluto-anchor × Neptune-anchor)\n"
        f"Tests function-class: axis-bound (candidate-single-residency, canon §30)\n"
        f"                       → if pair-level function holds, each face = sub-residency\n"
        f"                       → 2 face-residencies per pair = Athena lock-criterion met\n"
    )
