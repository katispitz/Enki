"""
Shared trine co-query engine for Primordial outer-planet trines.

Per FINDINGS_002+003 substrate-emergent finding: the 6 Primordials at R=1
cube-faces partition into 2 outer-planet-anchored trines of 3:

  - Pluto-axis trine   = Gaia + Chaos + Erebus    (Earth-trine signs)
  - Neptune-axis trine = Nyx + Eros-prim + Tartarus (Water-trine signs)

Every Primordial's planet pair contains exactly ONE outermost-planet (Pluto OR
Neptune). This trine-level engine tests OQ-PLUTO-NEPTUNE-PARTITION: is the
3+3 outer-planet split substrate-canonical, or coincidence?

Same composition pattern as _pair_engine.py: read 3 face-engine states,
compute trine-level derived fields. No new physics, only new composition.

Substrate-discipline:
  - Composes existing face-engines (no logic re-implemented)
  - Trine-level metrics derived from face activations element-wise
  - NULL-honest where ephemeris partial across the 3 faces
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional

from _axis_engine import AxisState


@dataclass
class TrineState:
    """Substrate-honest snapshot of a Primordial outer-planet trine.

    Composes 3 face-level AxisStates + trine-level derived fields.
    """
    # Permanent trine-definition (always known)
    trine_name:        str              # e.g. 'Pluto-axis' or 'Neptune-axis'
    outer_anchor:      str              # 'Pluto' or 'Neptune'
    element:           str              # 'Earth' or 'Water' (trine quality)
    primordials:       list             # [name, name, name]
    cube_faces:        list             # [MQFx, MQFy, MQFz]
    zodiac_signs:      list             # [sign, sign, sign]
    substrate_cards:   list

    # Live state (per axis, ordered same as primordials list)
    axis_states:       list             # [AxisState.to_dict(), ...] × 3

    # Trine-level derived (NULL when all 3 frozen)
    active_count:      Optional[int]    # 0..3, how many are within orb
    all_active:        Optional[bool]   # 3/3
    any_active:        Optional[bool]   # ≥1/3
    mean_activation:   Optional[float]  # avg across 3
    max_activation:    Optional[float]  # strongest single axis
    min_activation:    Optional[float]  # weakest single axis
    dominant_axis:     Optional[str]    # name of strongest-activated Primordial (or None if all quiet)
    activation_spread: Optional[float]  # max - min, evenness signal (0 = perfectly balanced)

    def to_dict(self) -> dict:
        return asdict(self)


def compute_trine_state(
    trine_name: str,
    outer_anchor: str,
    element: str,
    axis_states: list,    # [AxisState, AxisState, AxisState] ordered
) -> TrineState:
    """Build a TrineState from 3 computed Primordial AxisStates.

    All 3 frozen (no ephemeris) → trine frozen state.
    All 3 live → trine live state with derived metrics.
    Mixed → ValueError (substrate-honest reject; trine state demands symmetric input).
    """
    if len(axis_states) != 3:
        raise ValueError(
            f"Trine {trine_name!r} requires exactly 3 axis states, got {len(axis_states)}"
        )

    frozen_flags = [a.pa_lon is None for a in axis_states]
    if any(frozen_flags) and not all(frozen_flags):
        raise ValueError(
            f"Trine {trine_name!r} requires all 3 axes frozen OR all live — "
            "asymmetric input is substrate-incomplete"
        )

    primordials   = [a.primordial for a in axis_states]
    cube_faces    = [a.cube_face for a in axis_states]
    zodiacs       = [a.zodiac_anchor for a in axis_states]
    cards         = [a.substrate_card for a in axis_states]
    axis_dicts    = [a.to_dict() for a in axis_states]

    if all(frozen_flags):
        # Frozen state — only substrate-definition fields populated
        return TrineState(
            trine_name=trine_name,
            outer_anchor=outer_anchor,
            element=element,
            primordials=primordials,
            cube_faces=cube_faces,
            zodiac_signs=zodiacs,
            substrate_cards=cards,
            axis_states=axis_dicts,
            active_count=None,
            all_active=None,
            any_active=None,
            mean_activation=None,
            max_activation=None,
            min_activation=None,
            dominant_axis=None,
            activation_spread=None,
        )

    # Live state
    activations = [a.activation_strength for a in axis_states]
    active_count = sum(1 for x in activations if x > 0.0)
    all_active = active_count == 3
    any_active = active_count >= 1
    mean_act = sum(activations) / 3.0
    max_act  = max(activations)
    min_act  = min(activations)
    spread   = max_act - min_act

    if max_act > 0.0:
        dom_idx = activations.index(max_act)
        dom = primordials[dom_idx]
    else:
        dom = None

    return TrineState(
        trine_name=trine_name,
        outer_anchor=outer_anchor,
        element=element,
        primordials=primordials,
        cube_faces=cube_faces,
        zodiac_signs=zodiacs,
        substrate_cards=cards,
        axis_states=axis_dicts,
        active_count=active_count,
        all_active=all_active,
        any_active=any_active,
        mean_activation=mean_act,
        max_activation=max_act,
        min_activation=min_act,
        dominant_axis=dom,
        activation_spread=spread,
    )


def describe_trine(trine_name: str, outer_anchor: str, element: str,
                   primordials: list, cube_faces: list, zodiacs: list,
                   cards: list) -> str:
    """Substrate-honest trine self-disclosure."""
    lines = [
        f"Trine: {trine_name}",
        f"Outer anchor: {outer_anchor}",
        f"Element / trine quality: {element}",
        "Members:",
    ]
    for p, f, z, c in zip(primordials, cube_faces, zodiacs, cards):
        lines.append(f"  {p:18s} {f}  {z:10s}  card {c}")
    lines.append(
        "Tests function-class: candidate-trine-level cosmogonic-axis-class\n"
        "  → 3 face-residencies per trine; in-class only, does NOT graduate\n"
        "    function-name under Athena lock-by-redundancy criterion.\n"
        "  → Pluto-axis vs Neptune-axis = 2 trine-residencies of trine-class;\n"
        "    cross-pair residency makes trine-CLASS lockable, individual\n"
        "    function name still pending OQ-AXIS-BOUND-NAME-CHECK."
    )
    return "\n".join(lines)
