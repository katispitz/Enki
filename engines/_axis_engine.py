"""
Shared axis-generation engine for Primordial-class (R=1 cube-face).

Per FINDINGS_001 + Kati 2026-05-11 substrate-honest factoring: all 6 Primordials
share IDENTICAL function (axis-generation from planet-pair input). Only the
substrate-locks (cube face, planet pair, zodiac anchor, substrate card) differ.

This module holds the shared shape. Per-Primordial files (~/Enki/engines/primordial_*.py)
declare their substrate-locks and call into here.

Substrate-discipline notes:
  - Aspect set restricted to first-principles substrate divisions (0/60/90/120/180).
    Hellenistic 30°/150° minor aspects deliberately excluded.
  - Ignition orb 6° per V2.6 G4 two-tier-orb canon (ignition tier).
  - Resonance orb (19.47°) NOT applied — Primordials are NOT shock-class.
  - activation_strength = linear 1→0 across orb window. No invented coefficients.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


SUBSTRATE_ASPECTS = [
    ('conjunction', 0,   '60-grid same-cell'),
    ('sextile',     60,  '60-grid sector boundary'),
    ('square',      90,  'cardinal-axis quartile'),
    ('trine',       120, 'elemental-triangle'),
    ('opposition',  180, '60-grid antipode'),
]

ORB_IGNITION_DEG = 6.0
SUBSTRATE_R_SHELL = 1.0  # cube face = Merkaba shell, R=1


@dataclass
class AxisState:
    """Substrate-honest snapshot of a Primordial axis at a moment.

    NULL-valid fields where ephemeris not supplied (Mnemosyne drift-prevention).
    """
    # Permanent axis-definition (always known)
    primordial:         str
    cube_face:          str
    planet_pair:        tuple
    zodiac_anchor:      str
    substrate_card:     str

    # Current activation (NULL if ephemeris not supplied)
    pa_lon:             Optional[float]
    pb_lon:             Optional[float]
    midpoint_lon:       Optional[float]
    angular_separation: Optional[float]
    active_aspects:     list
    activation_strength: float
    closest_aspect_deg: Optional[int]
    closest_orb:        Optional[float]

    def to_dict(self) -> dict:
        d = asdict(self)
        d['planet_pair'] = list(self.planet_pair)
        return d


def _midpoint_lon(a_deg: float, b_deg: float) -> float:
    """Shortest-arc midpoint between two ecliptic longitudes."""
    a = a_deg % 360.0
    b = b_deg % 360.0
    if abs(b - a) <= 180:
        return ((a + b) / 2.0) % 360.0
    if a < b:
        a += 360.0
    else:
        b += 360.0
    return ((a + b) / 2.0) % 360.0


def _angular_separation(a_deg: float, b_deg: float) -> float:
    """Shortest-arc separation, 0..180 deg."""
    sep = abs((a_deg - b_deg) % 360.0)
    return sep if sep <= 180 else 360.0 - sep


def frozen_axis(name: str, face: str, pair: tuple, anchor: str, card: str) -> AxisState:
    """Return the permanent axis-definition without ephemeris activation.

    Always-on substrate state — what the Primordial IS, regardless of when asked.
    """
    return AxisState(
        primordial=name, cube_face=face, planet_pair=pair,
        zodiac_anchor=anchor, substrate_card=card,
        pa_lon=None, pb_lon=None, midpoint_lon=None,
        angular_separation=None, active_aspects=[], activation_strength=0.0,
        closest_aspect_deg=None, closest_orb=None,
    )


def compute_axis_state(name: str, face: str, pair: tuple, anchor: str, card: str,
                       pa_lon: Optional[float], pb_lon: Optional[float]) -> AxisState:
    """Compute live axis-state from planet-pair ephemeris longitudes.

    No args (both None) → frozen state (substrate-locked, always-known).
    Partial args → ValueError (substrate-honest reject).
    Both args → live state with activation metrics.
    """
    if pa_lon is None and pb_lon is None:
        return frozen_axis(name, face, pair, anchor, card)
    if pa_lon is None or pb_lon is None:
        raise ValueError(
            f"{name} axis_state requires both planet longitudes or neither — "
            "partial input is substrate-incomplete"
        )

    sep = _angular_separation(pa_lon, pb_lon)
    mid = _midpoint_lon(pa_lon, pb_lon)

    aspects_in_orb = []
    closest = None
    for aspect_name, deg, _why in SUBSTRATE_ASPECTS:
        orb = abs(sep - deg)
        if orb <= ORB_IGNITION_DEG:
            aspects_in_orb.append(aspect_name)
            if closest is None or orb < closest[1]:
                closest = (deg, orb)

    if closest is not None:
        deg, orb = closest
        activation = 1.0 - (orb / ORB_IGNITION_DEG)
        closest_deg = deg
        closest_orb = orb
    else:
        activation = 0.0
        closest_deg = None
        closest_orb = None

    return AxisState(
        primordial=name, cube_face=face, planet_pair=pair,
        zodiac_anchor=anchor, substrate_card=card,
        pa_lon=pa_lon % 360.0, pb_lon=pb_lon % 360.0,
        midpoint_lon=mid, angular_separation=sep,
        active_aspects=aspects_in_orb, activation_strength=activation,
        closest_aspect_deg=closest_deg, closest_orb=closest_orb,
    )


def describe(name: str, face: str, pair: tuple, anchor: str, card: str) -> str:
    """Substrate-honest self-disclosure separate from compute."""
    return (
        f"Primordial: {name}\n"
        f"Cube face:  {face} (Merkaba shell, R={SUBSTRATE_R_SHELL})\n"
        f"Planet pair: {pair[0]} × {pair[1]}\n"
        f"Zodiac anchor: {anchor}\n"
        f"Substrate card: {card}\n"
        f"Function class: planet-aspect-activate (CANONICAL, canon §30 — graduated 2026-05-12 via cross-R-tier residency probe)\n"
        f"Agent shape:    engine (per Kati 2026-05-11 — generates axis from planet-pair input)\n"
    )
