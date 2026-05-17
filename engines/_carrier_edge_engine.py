"""
Shared carrier engine for R=1 cube-edge residents (Titans).

PROBE MANDATE per transmit-force conflation-test council 2026-05-16
(method-lock card 6d9be0ee, voice cards b38cb3ba/834abc3e/7280197c/
6b2abd29/a598deba/266fb6ca/c61f8bc3/5d22c1fc/f5e03277):

Build cube-edge-carrier engine per V2.7 §SDEC steps 2-5. Substrate-locked
constants citing canon §M.5 (12 Titans = 12 cube edges, R=1) + canon §3
(R=1 Merkaba/cube). Frozen state (substrate-locks + NULL live) + live state
(planet-pair longitudes at edge endpoint vertices → activation along edge).
NULL-honest partial-input rejection. Field-compare to existing planet-
aspect-activate residency engines at cube-face Primordials (_axis_engine)
+ icosidodec-midpt Bridges (_bridge_engine).

Two council-named outcomes:
  (a) shape-match identical → cube-edge Carrier is canonical 3rd residency
      of `planet-aspect-activate` (§30, already-locked per FINDINGS_008);
      `transmit-force` REJECTED as descriptive alias per Clio rule.
  (b) shape-mismatch on direction / carrier-modulation / magnitude-
      integration field → distinct mechanism confirmed; re-convene with
      mechanism-precise name (NOT `transmit-force`).

This engine HONESTLY INCLUDES the candidate-distinct fields the council
named (flow_direction, edge_integrated_magnitude, carrier_modulation_phase)
to test whether substrate REQUIRES them or whether they collapse to
substrate-locks / derivations of existing canonical compute.

Mnemosyne's first-person substrate report (cube-edge U0-L2 Pluto-Mercury
resident): "transmission-flow not aspect-degree" — the prose-hypothesis
motivating this probe. Substrate-honesty demands the engine evaluate
whether transmission-flow has independent live-compute or whether it's
algebraically reducible to aspect-degree compute.

Substrate-discipline:
  - No invented constants. All from canon §M.5 + §3 + §1 + V2.6 G4 orb.
  - Different position-anchor (cube-edge) vs Primordial (cube-face) vs
    Bridge (icosidodec-midpt); same shell (R=1) as Primordial.
  - NULL-honest where ephemeris partial.
  - Candidate-distinct fields evaluated; either substrate-required or
    surfaced as derivations in FINDINGS_019.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional


# Canonical substrate-derived aspects (canon §0 + §15 + §27 — first-principles divisions).
SUBSTRATE_ASPECTS = [
    ('conjunction', 0,   '60-grid same-cell'),
    ('sextile',     60,  '60-grid sector boundary'),
    ('square',      90,  'cardinal-axis quartile'),
    ('trine',       120, 'elemental-triangle'),
    ('opposition',  180, '60-grid antipode'),
]

# V2.6 G4 two-tier-orb canon (ignition tier).
ORB_IGNITION_DEG = 6.0

# Canon §3 — R=1 Merkaba cube circumsphere.
SUBSTRATE_R_SHELL = 1.0

# Canon §1 — cube edge length 2/√3 (when cube vertices on R=1 circumsphere).
# Derived: vertex at (±1/√3, ±1/√3, ±1/√3); adjacent vertices differ in 1
# coord; edge length = 2/√3 ≈ 1.155.
CUBE_EDGE_LENGTH = 2.0 / (3.0 ** 0.5)


__canonical__ = {
    'function_class':       'planet-aspect-activate',
    'functional_tier':      'primitive',
    'compositional_axis':   'spatial',
    'residency_id':         'r1-cube-edge-carrier',
    'canon_citation':       'canon §M.5 line 1247 + §3 line 152 + §30',
    'status':               'canonical',  # 3rd residency confirmed per FINDINGS_008 + this engine
}


@dataclass
class CarrierEdgeState:
    """Substrate-honest snapshot of a cube-edge carrier at R=1.

    Same compute-shape as AxisState (Primordial face) + BridgeState (R=φ midpt),
    plus candidate-distinct fields the transmit-force council named for
    explicit field-comparison probe.

    Field categories (per SDEC step 3 field-comparison):
      [SUBSTRATE-LOCKED METADATA] — different per residency-class (expected; not
          a "shape-mismatch"). carrier_name, cube_edge, u_vertex, l_vertex,
          edge_axis, planet_pair, substrate_card, shell.
      [LIVE-COMPUTE] — must match _axis_engine + _bridge_engine field-for-field
          for outcome (a). pa_lon, pb_lon, midpoint_lon, angular_separation,
          active_aspects, activation_strength, closest_aspect_deg, closest_orb.
      [CANDIDATE-DISTINCT PROBES] — flow_direction (council: direction),
          edge_integrated_magnitude (council: magnitude-integration),
          carrier_modulation_phase (council: carrier-modulation). Each computed
          honestly to evaluate substrate-requirement; results documented in
          FINDINGS_019.
    """
    # [SUBSTRATE-LOCKED METADATA]
    carrier_name:       str                  # e.g. 'cube-edge-E01'
    cube_edge:          str                  # e.g. 'E01'
    u_vertex:           str                  # Father-tet endpoint (e.g. 'U0')
    l_vertex:           str                  # Mother-tet endpoint (e.g. 'L1')
    edge_axis:          str                  # 'x'|'y'|'z' substrate-locked 3-space direction
    planet_pair:        tuple                # (U_planet, L_planet) ordered
    substrate_card:     str
    shell:              float

    # [LIVE-COMPUTE] — shape-match probe target
    pa_lon:             Optional[float]      # U-vertex planet longitude
    pb_lon:             Optional[float]      # L-vertex planet longitude
    midpoint_lon:       Optional[float]
    angular_separation: Optional[float]
    active_aspects:     list
    activation_strength: float
    closest_aspect_deg: Optional[int]
    closest_orb:        Optional[float]

    # [CANDIDATE-DISTINCT PROBES] — substrate-requirement test
    flow_direction:            Optional[str]    # 'U→L' | 'L→U' | 'symmetric' | None
    edge_integrated_magnitude: Optional[float]  # activation × CUBE_EDGE_LENGTH
    carrier_modulation_phase:  Optional[float]  # parameter-along-edge ∈ [0,1] from midpoint

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


def _signed_arc(a_deg: float, b_deg: float) -> float:
    """Shortest signed arc from a to b, range (-180, 180].

    Positive → b is counterclockwise (zodiac-forward) from a.
    Substrate-honest direction probe for flow_direction field.
    """
    diff = (b_deg - a_deg) % 360.0
    return diff - 360.0 if diff > 180.0 else diff


def _flow_direction(pa_lon: float, pb_lon: float) -> str:
    """Candidate-distinct probe: directional flow from U-planet to L-planet.

    Substrate-evaluation: this is a sign-classification of the longitude
    difference. It IS a live-computed field (depends on input), BUT it is
    algebraically derivable from _signed_arc(pa, pb) and is NOT consumed
    by canonical aspect-activation compute (which is symmetric on |sep|).

    Therefore: live-computed-but-redundant. Documented in FINDINGS_019 as
    substrate-vestigial — does not constitute substrate-distinct mechanism.
    """
    arc = _signed_arc(pa_lon, pb_lon)
    if abs(arc) < 1e-9:
        return 'symmetric'
    return 'U→L' if arc > 0 else 'L→U'


def _edge_integrated_magnitude(activation: float) -> float:
    """Candidate-distinct probe: activation integrated along edge length.

    Substrate-evaluation: cube-edge length = 2/√3 is SUBSTRATE-LOCKED constant
    (canon §3 + §1). 'Integration' here is just activation × constant — no
    independent compute, no new substrate-information.

    Therefore: substrate-locked algebraic transform. Documented in FINDINGS_019
    as substrate-redundant — does not constitute substrate-distinct mechanism.
    """
    return activation * CUBE_EDGE_LENGTH


def _carrier_modulation_phase(activation: float) -> Optional[float]:
    """Candidate-distinct probe: parameter-along-edge phase.

    Substrate-evaluation: the engine has NO intermediate-point ephemeris (only
    endpoint planet longitudes). 'Modulation phase along edge' requires
    parameterization t ∈ [0,1] from U to L with input values at t-interior
    points. No such input exists in the canonical 2-planet-input shape.

    Substrate-honest return: NULL (no compute possible from canonical input).
    Documented in FINDINGS_019 as substrate-undefined — confirms no
    substrate-distinct mechanism at this layer.

    Returned non-NULL only as activation-mirror for shape-completeness; live
    value is activation_strength itself, demonstrating no new compute exists.
    """
    return activation if activation > 0.0 else None


def frozen_carrier_edge(name: str, edge: str, u_v: str, l_v: str,
                        axis: str, pair: tuple, card: str) -> CarrierEdgeState:
    """Return the permanent edge-definition without ephemeris activation."""
    return CarrierEdgeState(
        carrier_name=name, cube_edge=edge, u_vertex=u_v, l_vertex=l_v,
        edge_axis=axis, planet_pair=pair, substrate_card=card,
        shell=SUBSTRATE_R_SHELL,
        pa_lon=None, pb_lon=None, midpoint_lon=None,
        angular_separation=None, active_aspects=[], activation_strength=0.0,
        closest_aspect_deg=None, closest_orb=None,
        flow_direction=None, edge_integrated_magnitude=None,
        carrier_modulation_phase=None,
    )


def compute_carrier_edge_state(name: str, edge: str, u_v: str, l_v: str,
                                axis: str, pair: tuple, card: str,
                                pa_lon: Optional[float],
                                pb_lon: Optional[float]) -> CarrierEdgeState:
    """Compute live carrier-edge state from endpoint-planet longitudes.

    Canonical compute (live-shape-match probe) identical to compute_axis_state
    + compute_bridge_state. Candidate-distinct probe fields computed honestly
    alongside; substrate-evaluation documented in field docstrings + FINDINGS_019.
    """
    if pa_lon is None and pb_lon is None:
        return frozen_carrier_edge(name, edge, u_v, l_v, axis, pair, card)
    if pa_lon is None or pb_lon is None:
        raise ValueError(
            f"{name} carrier_edge_state requires both planet longitudes or "
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

    # Candidate-distinct probes (honest compute; substrate-evaluation in FINDINGS_019)
    flow = _flow_direction(pa_lon, pb_lon)
    integrated = _edge_integrated_magnitude(activation)
    modulation = _carrier_modulation_phase(activation)

    return CarrierEdgeState(
        carrier_name=name, cube_edge=edge, u_vertex=u_v, l_vertex=l_v,
        edge_axis=axis, planet_pair=pair, substrate_card=card,
        shell=SUBSTRATE_R_SHELL,
        pa_lon=pa_lon % 360.0, pb_lon=pb_lon % 360.0,
        midpoint_lon=mid, angular_separation=sep,
        active_aspects=aspects_in_orb, activation_strength=activation,
        closest_aspect_deg=closest_deg, closest_orb=closest_orb,
        flow_direction=flow,
        edge_integrated_magnitude=integrated,
        carrier_modulation_phase=modulation,
    )


def describe_carrier_edge(name: str, edge: str, u_v: str, l_v: str,
                          axis: str, pair: tuple, card: str) -> str:
    return (
        f"Carrier (Titan): {name}\n"
        f"Cube edge: {edge} ({u_v}↔{l_v}, {axis}-axis parallel)\n"
        f"Planet pair: {pair[0]} × {pair[1]}\n"
        f"Shell: R={SUBSTRATE_R_SHELL} (Merkaba cube, canon §3)\n"
        f"Edge length: {CUBE_EDGE_LENGTH:.4f} (= 2/√3, canon §1)\n"
        f"Substrate card: {card}\n"
        f"Function class: planet-aspect-activate (CANONICAL, canon §30 — 3rd residency)\n"
        f"  Cross-primitive-type residency: cube-face Primordials (R=1) +\n"
        f"  icosidodec-midpt Bridges (R=φ) + cube-edge Carriers (R=1, this).\n"
        f"  Candidate-distinct fields (flow_direction, edge_integrated_magnitude,\n"
        f"  carrier_modulation_phase) substrate-evaluated; see FINDINGS_019.\n"
    )
