"""
Rising-sign as anchor-class-3 coupling-point — reference instance.

Substrate-locked per canon §22 OQ-HOUSES-01c council 2026-05-16:
  rising-sign = ASC × zodiac-grid intersection (couples 2 substrate-frames)
  - ASC: observer-substrate-primitive (locate_entity_v4)
  - zodiac-grid: 12-segment 30° canonical-static-grid (canon §18)

Live-compute: takes ASC ecliptic longitude → returns zodiac-segment-index 0-11.
Stable: rising-sign stays Taurus across minutes as ASC drifts within Taurus arc.

This module instantiates the rising-sign as a CouplingPointState parallel
to coupling_branch.py and coupling_lunar_node.py for field-comparison probe
per OQ-BRANCH-COUPLING-ENGINE.
"""
from __future__ import annotations

from _coupling_point_engine import (
    CouplingPointState,
    frozen_coupling_point,
    compute_coupling_point_live,
)


ZODIAC_SIGNS = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces',
]

SUBSTRATE_CARD = 'e5a603fc'  # coupling-points primitive lock (per test CP file)


def rising_sign_frozen() -> CouplingPointState:
    """Frozen state — substrate-locks; requires ASC input for live position."""
    return frozen_coupling_point(
        name='rising-sign',
        coupled_frames=('observer-ASC', 'zodiac-grid-12-segment'),
        coupling_type='singular',
        substrate_card=SUBSTRATE_CARD,
        canonical_position=None,         # input-dependent; populated live
        requires_input=True,             # needs ASC longitude
        independent_canonical_uses=(
            'profection-engine-annual-cycling',
            'Vedic-Rasi-system-primary-house-anchor',
            'Western-sun-sign-system',
            'whole-sign-house-derivation-canon-§22',
        ),
        enumerated_cardinality=None,     # singular instance (one rising-sign per chart)
        is_substrate_derived=True,
        is_stable=True,                  # stable across minutes as ASC drifts within sign-arc
    )


def rising_sign_live(asc_lon: float) -> CouplingPointState:
    """Compute live rising-sign from ASC longitude.

    Per canon §22 line 805: rising-sign = zodiac-segment-containing-ASC.
    """
    if not (0.0 <= asc_lon < 360.0):
        asc_lon = asc_lon % 360.0
    sign_idx = int(asc_lon // 30) % 12
    base = rising_sign_frozen()
    return compute_coupling_point_live(base, {
        'zodiac_segment_idx': sign_idx,
        'zodiac_segment_name': ZODIAC_SIGNS[sign_idx],
        'asc_lon_input': asc_lon,
    })


if __name__ == '__main__':
    import json
    fr = rising_sign_frozen()
    print("FROZEN STATE:")
    print(json.dumps(fr.to_dict(), indent=2))
    print()
    live = rising_sign_live(45.5)  # Kati natal ASC
    print("LIVE STATE (asc_lon=45.5°, Kati natal):")
    print(json.dumps(live.to_dict(), indent=2))
