"""
Lunar nodes (Rahu/Ketu) as anchor-class-3 coupling-points — reference instance.

Substrate-locked per canon §22 OQ-HOUSES-01c council 2026-05-16 +
test_coupling_points_20260516.py CP3/CP4/CP5:
  Rahu/Ketu = Moon-orbital-plane × ecliptic intersections
  - Moon orbit plane: Ring 2 substrate (canon §23b pt2 / Mi / 30 tithis)
  - ecliptic: canon §18
  Two intersections always 180° apart by orbital-plane geometry.

Live-compute: takes (or assumes ephemeris of) date → returns Rahu lon + Ketu lon.
Stable: nodes drift slowly (~18.61yr precession, substrate-EXTERNAL per
OQ-NODES-PRECESSION negative-resolution); within hours they're stable.

Note on this engine: we don't import Skyfield here — that's a Lillu engine
concern. Substrate-shape probe accepts pre-computed rahu_lon as input.
"""
from __future__ import annotations

from _coupling_point_engine import (
    CouplingPointState,
    frozen_coupling_point,
    compute_coupling_point_live,
)


SUBSTRATE_CARD = '072de238'  # lunar nodes anchor-class-3 lock card


def lunar_nodes_frozen() -> CouplingPointState:
    """Frozen state — substrate-locks; requires Rahu longitude input for live."""
    return frozen_coupling_point(
        name='lunar-nodes',
        coupled_frames=('Moon-orbital-plane', 'ecliptic-plane'),
        coupling_type='pair-180',  # two intersections always 180° opposite
        substrate_card=SUBSTRATE_CARD,
        canonical_position=None,         # input-dependent
        requires_input=True,             # needs Rahu lon (Ketu derived)
        independent_canonical_uses=(
            'Vimshottari-dasha-Rahu-18yr-period',
            'Vimshottari-dasha-Ketu-7yr-period',
            'Vedic-sidereal-eclipse-prediction',
            'Western-karmic-axis-interpretation',
        ),
        enumerated_cardinality=2,        # Rahu + Ketu (the pair)
        is_substrate_derived=True,
        is_stable=True,                  # stable across hours (~18.61yr precession is slow)
    )


def lunar_nodes_live(rahu_lon: float) -> CouplingPointState:
    """Compute live Rahu + Ketu longitudes from Rahu input.

    Per CP4 invariant (test_coupling_points_20260516.py line 100-108): nodes
    always 180° apart by orbital-plane × ecliptic-plane geometry.
    """
    rahu = rahu_lon % 360.0
    ketu = (rahu + 180.0) % 360.0
    base = lunar_nodes_frozen()
    return compute_coupling_point_live(base, {
        'rahu_lon': rahu,
        'ketu_lon': ketu,
        'pair_separation_deg': 180.0,
    })


if __name__ == '__main__':
    import json
    fr = lunar_nodes_frozen()
    print("FROZEN STATE:")
    print(json.dumps(fr.to_dict(), indent=2))
    print()
    live = lunar_nodes_live(90.0)
    print("LIVE STATE (rahu_lon=90°):")
    print(json.dumps(live.to_dict(), indent=2))
