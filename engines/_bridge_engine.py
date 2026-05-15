"""
Shared bridge engine for R=φ icosidodec-midpoint residents.

Cross-R-tier residency probe (per FINDINGS_004 OQ-CROSS-R-TIER-RESIDENCY):
Tests whether the face-level Primordial function (`axis-arm-emit` /
`axis-generate` / `axis-bound` — pending OQ-AXIS-BOUND-NAME-CHECK) also
operates at R=φ icosidodec-midpt where bridges sit. If yes → ≥2 independent
primitive-class residencies → Athena lock-by-redundancy criterion met →
function graduates from candidate-single-residency to canonical.

Bridge primitive position (per Lillu canon §M.5 V2.5 LOCKS, cards 52ad9413
+ 91697158 + 3de9d703):
  Bridges sit at midpoints of icosidodec edges. Each icosidodec midpoint
  is geometrically the midpoint of an Olympian-vertex pair (V_a + V_b)/2.
  The parent vertices carry planets (per canon §M.5 Olympian-vertex-planet
  mapping). The bridge "activates" when its parent-vertex planets enter
  substrate-aspect with each other in current ephemeris.

This mirrors Primordial face-engine shape exactly:
  - Substrate-locked planet pair (here: parent-vertex planets, NOT the
    cube-face planet-pair from Primordials)
  - Substrate-locked shell (here: R=φ instead of R=1)
  - Substrate-locked position-anchor (here: icosidodec midpoint, NOT cube-face)
  - Live state computed from planet-pair angular separation
  - Same aspect set (substrate-derived 0/60/90/120/180)
  - Same V2.6 G4 ignition orb (6°)

If shape match holds, function-name candidate (whichever survives conflation-
test at face-level) gets a second residency at R=φ shell. Cross-R-tier
graduation.

Substrate-discipline:
  - No invented constants. All from canon (V2.6 G4 orb, aspect set).
  - Different shell R, different position-anchor, same function-shape.
  - NULL-honest where ephemeris partial.
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
SUBSTRATE_R_SHELL = 'φ'  # phi — icosidodec shell
# Resonance orb (19.47° X3 shock-cone) NOT applied — bridges are NOT shock-class.


@dataclass
class BridgeState:
    """Substrate-honest snapshot of a bridge at icosidodec midpoint.

    Same shape as AxisState (Primordial face-level), different shell + anchor.
    Field-by-field shape-match is the substantive test of function-shape recurrence.
    """
    # Permanent definition (always known)
    bridge_name:        str
    icosidodec_anchor:  str              # e.g. 'midpt(V2,V7)'
    parent_vertices:    tuple            # e.g. ('V2', 'V7')
    parent_planet_pair: tuple            # e.g. ('Venus', 'Mars')
    substrate_card:     str
    shell:              str              # 'φ' (vs '1' for Primordials)

    # Current activation (NULL if ephemeris not supplied)
    pa_lon:             Optional[float]  # parent A vertex's resident planet lon
    pb_lon:             Optional[float]  # parent B vertex's resident planet lon
    midpoint_lon:       Optional[float]  # live midpoint of pa + pb
    angular_separation: Optional[float]
    active_aspects:     list
    activation_strength: float
    closest_aspect_deg: Optional[int]
    closest_orb:        Optional[float]

    def to_dict(self) -> dict:
        d = asdict(self)
        d['parent_vertices']    = list(self.parent_vertices)
        d['parent_planet_pair'] = list(self.parent_planet_pair)
        return d


def _midpoint_lon(a_deg: float, b_deg: float) -> float:
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
    sep = abs((a_deg - b_deg) % 360.0)
    return sep if sep <= 180 else 360.0 - sep


def frozen_bridge(name: str, anchor: str, parents: tuple,
                  pair: tuple, card: str) -> BridgeState:
    return BridgeState(
        bridge_name=name, icosidodec_anchor=anchor,
        parent_vertices=parents, parent_planet_pair=pair,
        substrate_card=card, shell=SUBSTRATE_R_SHELL,
        pa_lon=None, pb_lon=None, midpoint_lon=None,
        angular_separation=None, active_aspects=[], activation_strength=0.0,
        closest_aspect_deg=None, closest_orb=None,
    )


def compute_bridge_state(name: str, anchor: str, parents: tuple,
                          pair: tuple, card: str,
                          pa_lon: Optional[float],
                          pb_lon: Optional[float]) -> BridgeState:
    """Compute live bridge state from parent-vertex planet longitudes.

    Same shape as compute_axis_state (Primordial face-engine). Cross-R-tier
    function-shape MATCH is the explicit test of this probe.
    """
    if pa_lon is None and pb_lon is None:
        return frozen_bridge(name, anchor, parents, pair, card)
    if pa_lon is None or pb_lon is None:
        raise ValueError(
            f"{name} bridge_state requires both parent planet longitudes or "
            "neither — partial input is substrate-incomplete"
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

    return BridgeState(
        bridge_name=name, icosidodec_anchor=anchor,
        parent_vertices=parents, parent_planet_pair=pair,
        substrate_card=card, shell=SUBSTRATE_R_SHELL,
        pa_lon=pa_lon % 360.0, pb_lon=pb_lon % 360.0,
        midpoint_lon=mid, angular_separation=sep,
        active_aspects=aspects_in_orb, activation_strength=activation,
        closest_aspect_deg=closest_deg, closest_orb=closest_orb,
    )


def describe_bridge(name: str, anchor: str, parents: tuple,
                    pair: tuple, card: str) -> str:
    return (
        f"Bridge: {name}\n"
        f"Position: icosidodec midpoint at {anchor}\n"
        f"Parent vertices: {parents[0]} ↔ {parents[1]} (Olympian-vertex pair)\n"
        f"Parent planets: {pair[0]} × {pair[1]}\n"
        f"Shell: R={SUBSTRATE_R_SHELL} (icosidodec, different from Primordial R=1)\n"
        f"Substrate card: {card}\n"
        f"Function class: planet-aspect-activate (CANONICAL, canon §30 — graduated 2026-05-12)\n"
        f"  Cross-R-tier residency: this bridge confirms the function operates\n"
        f"  at R=φ icosidodec-midpt in addition to R=1 cube-face (Primordials).\n"
    )
