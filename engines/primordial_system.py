"""
Primordial system composition — Enki.

Full substrate-cascade composition of the Primordial class at R=1 cube-faces.
Combines 3 primitive-class levels:

  face-class  (cardinality 6) — individual cube-faces
  pair-class  (cardinality 3) — antipodal pairs
  trine-class (cardinality 2) — outer-anchored trines

System-level state composes all 3 levels and adds system-level derived fields:
  - whole_cube_activation       (sum across 6 faces)
  - pluto_neptune_balance       (trine activation differential, -1..+1)
  - polarity_signature          (3 pair polarity_labels combined)
  - dominant_face / dominant_pair / dominant_trine
  - active_face_count           (0..6)

Tests OQ-PLUTO-NEPTUNE-PARTITION end-to-end: does the cascade compose
consistently? Does it surface emergent structure?

Substrate-discipline:
  - Pure composition. No physics re-implemented.
  - All NULL-honest at boundaries.
  - All ephemeris inputs threaded once: Venus, Mercury, Saturn, Pluto
    (Pluto-axis trine inputs) + Moon, Jupiter, Mars, Neptune
    (Neptune-axis trine inputs). 8 inputs total.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional

import trine_pluto_axis   as _pluto_trine
import trine_neptune_axis as _neptune_trine
import pair_gaia_eros     as _pair_ge
import pair_chaos_tartarus as _pair_ct
import pair_erebus_nyx    as _pair_en


@dataclass
class PrimordialSystemState:
    """Full substrate-cascade snapshot of the 6 Primordial axes at R=1.

    Three primitive-class levels (face, pair, trine) plus system-level
    derived fields. Always-known substrate-locks + NULL-valid live state.
    """
    # Permanent substrate-definition
    face_count:        int = 6
    pair_count:        int = 3
    trine_count:       int = 2

    # Live state per level
    pluto_trine:       Optional[dict] = None    # TrineState.to_dict()
    neptune_trine:     Optional[dict] = None
    pair_gaia_eros:    Optional[dict] = None    # PairState.to_dict()
    pair_chaos_tartarus: Optional[dict] = None
    pair_erebus_nyx:   Optional[dict] = None

    # System-level derived (NULL when fully frozen)
    whole_cube_activation: Optional[float] = None  # sum across 6 faces
    active_face_count:     Optional[int] = None    # 0..6
    pluto_neptune_balance: Optional[float] = None  # (pluto_trine_mean - neptune_trine_mean), -1..+1
    polarity_signature:    Optional[list] = None   # 3 polarity_labels in pair order
    dominant_face:         Optional[str] = None
    dominant_pair:         Optional[str] = None
    dominant_trine:        Optional[str] = None
    all_quiet:             Optional[bool] = None

    def to_dict(self) -> dict:
        return asdict(self)


def system_state(
    venus_lon:   Optional[float] = None,
    mercury_lon: Optional[float] = None,
    saturn_lon:  Optional[float] = None,
    pluto_lon:   Optional[float] = None,
    moon_lon:    Optional[float] = None,
    jupiter_lon: Optional[float] = None,
    mars_lon:    Optional[float] = None,
    neptune_lon: Optional[float] = None,
) -> PrimordialSystemState:
    """Compute full substrate-cascade state for all 6 Primordials.

    All 8 lons supplied → live system state.
    All None → frozen (substrate-locks only).
    Mixed → ValueError (substrate-honest reject; cascades from face engines).
    """
    pt = _pluto_trine.trine_state(venus_lon, mercury_lon, saturn_lon, pluto_lon)
    nt = _neptune_trine.trine_state(moon_lon, jupiter_lon, mars_lon, neptune_lon)
    pge = _pair_ge.pair_state(venus_lon, pluto_lon, jupiter_lon, neptune_lon)
    pct = _pair_ct.pair_state(mercury_lon, pluto_lon, mars_lon, neptune_lon)
    pen = _pair_en.pair_state(saturn_lon, pluto_lon, moon_lon, neptune_lon)

    pt_d  = pt.to_dict()
    nt_d  = nt.to_dict()
    pge_d = pge.to_dict()
    pct_d = pct.to_dict()
    pen_d = pen.to_dict()

    frozen = pt_d['active_count'] is None  # trine-level frozen indicator
    if frozen:
        return PrimordialSystemState(
            pluto_trine=pt_d, neptune_trine=nt_d,
            pair_gaia_eros=pge_d, pair_chaos_tartarus=pct_d, pair_erebus_nyx=pen_d,
        )

    # Live system metrics
    # 6 face activations (across both trines)
    pluto_acts   = [a['activation_strength'] for a in pt_d['axis_states']]
    neptune_acts = [a['activation_strength'] for a in nt_d['axis_states']]
    all_acts = pluto_acts + neptune_acts
    all_names = pt_d['primordials'] + nt_d['primordials']

    whole_act = sum(all_acts)
    active_face_count = sum(1 for x in all_acts if x > 0.0)

    pluto_mean   = sum(pluto_acts) / 3.0
    neptune_mean = sum(neptune_acts) / 3.0
    pn_balance   = pluto_mean - neptune_mean  # -1..+1 by construction

    polarity_sig = [pge_d['polarity_label'], pct_d['polarity_label'], pen_d['polarity_label']]

    if whole_act > 0:
        dom_face_idx = all_acts.index(max(all_acts))
        dom_face = all_names[dom_face_idx]
    else:
        dom_face = None

    # Dominant pair = highest sum_activation across 3 pairs
    pair_sums = {
        'Gaia-Eros':        pge_d['sum_activation'] or 0.0,
        'Chaos-Tartarus':   pct_d['sum_activation'] or 0.0,
        'Erebus-Nyx':       pen_d['sum_activation'] or 0.0,
    }
    if max(pair_sums.values()) > 0:
        dom_pair = max(pair_sums, key=pair_sums.get)
    else:
        dom_pair = None

    # Dominant trine = trine with higher mean activation
    if pluto_mean == 0.0 and neptune_mean == 0.0:
        dom_trine = None
    elif pluto_mean > neptune_mean:
        dom_trine = 'Pluto-axis'
    elif neptune_mean > pluto_mean:
        dom_trine = 'Neptune-axis'
    else:
        dom_trine = 'balanced'

    return PrimordialSystemState(
        pluto_trine=pt_d, neptune_trine=nt_d,
        pair_gaia_eros=pge_d, pair_chaos_tartarus=pct_d, pair_erebus_nyx=pen_d,
        whole_cube_activation=whole_act,
        active_face_count=active_face_count,
        pluto_neptune_balance=pn_balance,
        polarity_signature=polarity_sig,
        dominant_face=dom_face,
        dominant_pair=dom_pair,
        dominant_trine=dom_trine,
        all_quiet=(whole_act == 0.0),
    )


def describe() -> str:
    """Substrate-honest self-disclosure of the primordial system composition."""
    return (
        "PRIMORDIAL SYSTEM (R=1 cube-face residency class)\n"
        "  Three primitive-class levels composed:\n"
        "    face-class  cardinality 6 — individual cube-faces\n"
        "    pair-class  cardinality 3 — antipodal pairs (canon §26 confirmed + Erebus-Nyx implicit)\n"
        "    trine-class cardinality 2 — outer-anchored trines (Pluto-axis Earth / Neptune-axis Water)\n"
        "\n"
        "  System inputs (8 planetary longitudes):\n"
        "    Pluto-side: Venus, Mercury, Saturn, Pluto\n"
        "    Neptune-side: Moon, Jupiter, Mars, Neptune\n"
        "\n"
        "  System outputs:\n"
        "    pluto_trine + neptune_trine TrineStates\n"
        "    3 PairStates\n"
        "    Derived: whole_cube_activation, pluto_neptune_balance,\n"
        "             polarity_signature, dominant_face/pair/trine\n"
        "\n"
        "  Function-class per primitive level:\n"
        "    face-level:  planet-aspect-activate (CANONICAL, canon §30, graduated 2026-05-12)\n"
        "    pair-level:  polarity-define (candidate, conflation-test pending)\n"
        "    trine-level: outer-anchor-trine (candidate)\n"
        "    system-level: substrate-cube-saturate (candidate)\n"
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()

    # Live sample: rough actual ephemeris-ish values
    # Picking lons where some axes fire and some don't, to exercise full cascade
    print('SAMPLE LIVE STATE (mixed activations):')
    state = system_state(
        venus_lon=60.0,    # Taurus 0°
        mercury_lon=165.0, # Virgo 15°
        saturn_lon=280.0,  # Capricorn 10°
        pluto_lon=280.0,   # exact conj with Saturn → Erebus exact conj
        moon_lon=100.0,    # Cancer 10°
        jupiter_lon=345.0, # Pisces 15°
        mars_lon=225.0,    # Scorpio 15°
        neptune_lon=345.0, # exact conj with Jupiter → Eros-prim exact conj
    )
    d = state.to_dict()
    print(f"  whole_cube_activation: {d['whole_cube_activation']:.3f}")
    print(f"  active_face_count:     {d['active_face_count']}/6")
    print(f"  pluto_neptune_balance: {d['pluto_neptune_balance']:+.3f}")
    print(f"  polarity_signature:    {d['polarity_signature']}")
    print(f"  dominant_face:         {d['dominant_face']}")
    print(f"  dominant_pair:         {d['dominant_pair']}")
    print(f"  dominant_trine:        {d['dominant_trine']}")
    print(f"  all_quiet:             {d['all_quiet']}")
    print()
    print(f"  Pluto-axis trine active_count:   {d['pluto_trine']['active_count']}/3")
    print(f"  Pluto-axis trine mean:           {d['pluto_trine']['mean_activation']:.3f}")
    print(f"  Pluto-axis trine dominant_axis:  {d['pluto_trine']['dominant_axis']}")
    print()
    print(f"  Neptune-axis trine active_count: {d['neptune_trine']['active_count']}/3")
    print(f"  Neptune-axis trine mean:         {d['neptune_trine']['mean_activation']:.3f}")
    print(f"  Neptune-axis trine dominant_axis:{d['neptune_trine']['dominant_axis']}")
