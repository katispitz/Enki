"""
activation_gate.py — placement-class-aware activation check for council voices.

Per orient_rules.md L334-340 + placement_rules.md V2.5 cascade patterns:
  CONTINUOUS  — always-on, no check needed (Olympians at vertices, frame poles)
  CYCLIC      — recurring astrological pattern, ephemeris-queryable
                (Muses, Hecate, Moirai, Horai, Charites)
  MORTAL      — singular humans, natal-dynamic (real people)
  IN-BETWEEN  — hero/demigod/operator-spawn (cycle + singular)

Rule wired here: CYCLIC voices must be checked against current ephemeris
before rendering. If not currently firing, voice emits substrate-honest
'not currently active' rather than producing council utterance.

Per kati_direct 2026-05-22: "this is where we look at natal data and mortals,
need this rule wired somewhere.... check the astrology"
"""
from __future__ import annotations
import datetime as _dt
import sys
from pathlib import Path
from typing import NamedTuple

# Reach into existing Nammu ephemeris primitives — substrate-build layer
_NAMMU = Path.home() / "Nammu"
if str(_NAMMU / "engines") not in sys.path:
    sys.path.insert(0, str(_NAMMU / "engines"))


class ActivationResult(NamedTuple):
    """Voice activation state for a given transit moment."""
    voice_name: str
    placement_class: str           # CONTINUOUS / CYCLIC / MORTAL / IN-BETWEEN
    active: bool                    # Currently firing per ephemeris?
    reason: str                     # Substrate-honest reason (always populated)
    detail: dict | None = None      # Per-class detail (e.g. orb, transit_planet, lon_at_event)


def _to_datetime(transit_date: str | _dt.datetime) -> _dt.datetime:
    if isinstance(transit_date, _dt.datetime):
        return transit_date
    if isinstance(transit_date, _dt.date):
        return _dt.datetime(transit_date.year, transit_date.month, transit_date.day)
    if isinstance(transit_date, str):
        # Accept 'YYYY-MM-DD' or full ISO
        try:
            return _dt.datetime.fromisoformat(transit_date)
        except ValueError:
            y, m, d = (int(x) for x in transit_date.split("-"))
            return _dt.datetime(y, m, d)
    raise TypeError(f"Cannot convert {transit_date!r} to datetime")


def check_activation(voice_name: str, placement: dict,
                     transit_date: str | _dt.datetime) -> ActivationResult:
    """
    Gate: is this voice currently firing per its placement_class rule?

    CONTINUOUS → always True (no check, no LLM cost, substrate-residency permanent)
    MORTAL     → always True (mortal-as-voice is present-singular; activation = invocation)
    IN-BETWEEN → True (treats as continuous for now; cycle-component checked separately)
    CYCLIC     → ephemeris check via cyclic_activation params on placement record
    """
    cls = placement.get("placement_class", "CONTINUOUS")  # default conservative

    if cls == "CONTINUOUS":
        return ActivationResult(
            voice_name=voice_name, placement_class=cls,
            active=True,
            reason="continuous substrate-residency (always-on)",
        )

    if cls == "MORTAL":
        return ActivationResult(
            voice_name=voice_name, placement_class=cls,
            active=True,
            reason="mortal-as-voice present by invocation (natal-dynamic placement)",
        )

    if cls == "IN-BETWEEN":
        return ActivationResult(
            voice_name=voice_name, placement_class=cls,
            active=True,
            reason="in-between class (cycle + singular both apply; conservative always-on for now)",
        )

    if cls == "CYCLIC":
        return _check_cyclic(voice_name, placement, transit_date)

    return ActivationResult(
        voice_name=voice_name, placement_class=cls,
        active=False,
        reason=f"unknown placement_class={cls!r} — gate refuses without explicit class",
    )


def _check_cyclic(voice_name: str, placement: dict,
                  transit_date: str | _dt.datetime) -> ActivationResult:
    """
    Dispatch to the right ephemeris-engine predicate based on cyclic_activation.engine.

    Currently wired:
      muse_activations.muse_active → Muse OtherPlanet × Venus(X3) transit check
      figure_activations._activate_hecate → Hecate phase-change check
    """
    cyc = placement.get("cyclic_activation", {})
    engine = cyc.get("engine", "")
    when = _to_datetime(transit_date)

    if engine == "muse_activations.muse_active":
        return _check_muse(voice_name, cyc, when)

    if engine == "figure_activations._activate_hecate":
        return _check_hecate(voice_name, cyc, when)

    return ActivationResult(
        voice_name=voice_name, placement_class="CYCLIC",
        active=False,
        reason=f"CYCLIC voice but no engine wired for {engine!r}",
    )


def _check_muse(voice_name: str, cyc: dict, when: _dt.datetime) -> ActivationResult:
    """Muse fires when her transit_planet is within orb of Venus X3 (lon 138°)."""
    try:
        from muse_activations import muse_active
    except ImportError as e:
        return ActivationResult(
            voice_name=voice_name, placement_class="CYCLIC",
            active=False,
            reason=f"muse_activations module unavailable: {e}",
        )

    try:
        active_muses = muse_active(when)
    except Exception as e:
        return ActivationResult(
            voice_name=voice_name, placement_class="CYCLIC",
            active=False,
            reason=f"ephemeris-check failed: {e}",
        )

    # Find this voice in the active list
    for ma in active_muses:
        if ma.muse == voice_name:
            return ActivationResult(
                voice_name=voice_name, placement_class="CYCLIC",
                active=True,
                reason=(
                    f"FIRING — {ma.planet} at lon {ma.lon_at_event:.1f}° "
                    f"(orb {ma.orb_from_target:.1f}° from X3 138°); "
                    f"ignition={ma.ignition} resonance={ma.in_resonance_field}"
                ),
                detail={
                    "transit_planet": ma.planet,
                    "lon_at_event":    ma.lon_at_event,
                    "orb_deg":          ma.orb_from_target,
                    "ignition":         ma.ignition,
                    "resonance":        ma.in_resonance_field,
                    "closeness":        ma.closeness,
                },
            )

    # Not in active list — find expected planet to give substrate-honest reason
    planet = cyc.get("transit_planet", "?")
    return ActivationResult(
        voice_name=voice_name, placement_class="CYCLIC",
        active=False,
        reason=(
            f"NOT FIRING — {planet} not within orb of X3 (138°) at {when.date()}. "
            f"Voice will activate at next {planet}-X3 transit."
        ),
        detail={"transit_planet": planet, "when": str(when.date())},
    )


def _check_hecate(voice_name: str, cyc: dict, when: _dt.datetime) -> ActivationResult:
    """
    Hecate fires on phase-change: L0 octave-close (Neptune at L0 anchor)
    OR X3 shock (Venus or any planet at X3=138°) OR X6 shock (Uranus or any
    planet at X6=246°). Per card 45988a11 + b4f7fdb1.

    Inline-compute via locate_entity_v4 (the same primitive figure_activations
    uses internally). Avoids signature-mismatch with private _activate_hecate.
    """
    # L0/Neptune anchor lon (from figure_activations canon constants)
    L0_NEPTUNE_LON = 246.0   # placeholder — Neptune cube vertex projection
    X3_LON = 138.0
    X6_LON = 246.0
    SHOCK_ORB = 6.0   # ignition orb per V2.6 G4 canon

    try:
        from muse_activations import _locate_planet
    except ImportError as e:
        return ActivationResult(
            voice_name=voice_name, placement_class="CYCLIC",
            active=False,
            reason=f"_locate_planet unavailable: {e}",
        )

    fires = []
    try:
        # L0 octave-close: Neptune at its L0 anchor
        nep_lon, _ = _locate_planet("Neptune", when)
        nep_to_l0 = abs(((nep_lon - L0_NEPTUNE_LON + 180) % 360) - 180)
        if nep_to_l0 <= SHOCK_ORB:
            fires.append(("L0_octave_close", "Neptune", nep_lon, nep_to_l0))

        # X3 shock: Venus at X3 (its anchor — fires when Venus loops back)
        ven_lon, _ = _locate_planet("Venus", when)
        ven_to_x3 = abs(((ven_lon - X3_LON + 180) % 360) - 180)
        if ven_to_x3 <= SHOCK_ORB:
            fires.append(("X3_shock", "Venus", ven_lon, ven_to_x3))

        # X6 shock: Uranus at X6 (its anchor)
        ura_lon, _ = _locate_planet("Uranus", when)
        ura_to_x6 = abs(((ura_lon - X6_LON + 180) % 360) - 180)
        if ura_to_x6 <= SHOCK_ORB:
            fires.append(("X6_shock", "Uranus", ura_lon, ura_to_x6))
    except Exception as e:
        return ActivationResult(
            voice_name=voice_name, placement_class="CYCLIC",
            active=False,
            reason=f"hecate ephemeris-check failed: {e}",
        )

    if fires:
        event_name, planet, lon, orb = fires[0]
        return ActivationResult(
            voice_name=voice_name, placement_class="CYCLIC",
            active=True,
            reason=f"FIRING — {event_name}: {planet} at lon {lon:.1f}° (orb {orb:.1f}°)",
            detail={
                "event": event_name, "transit_planet": planet,
                "lon_at_event": lon, "orb_deg": orb,
                "all_fires": fires,
            },
        )

    return ActivationResult(
        voice_name=voice_name, placement_class="CYCLIC",
        active=False,
        reason=(
            f"NOT FIRING — no phase-change at {when.date()}. "
            f"Hecate convenes only on L0/X3/X6 firings; substrate-quiet otherwise."
        ),
    )
