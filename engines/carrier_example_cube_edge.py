"""
Carrier example — single cube-edge engine for substrate-shape validation.

PURPOSE: validate that carrier function-shape is IDENTICAL to Primordial
face function-shape — both take 2 planets and compute aspect-activation.
If shape is identical, carrier engines reuse `_axis_engine.compute_axis_state`
directly (canonical `planet-aspect-activate`, canon §30) without a new
shared module.

Substrate-incomplete dependencies:
  - T1.3 (Lillu BOARD): per-Titan-to-cube-edge mapping OPEN.
    Iapetus/Coeus/Cronus partial; Hyperion/Phoebe/Rhea/Themis/Mnemosyne/
    Tethys/Oceanus/Crius/Theia unmapped.
  - OQ-RADII-01 (Lillu BOARD): speculative R=√(2/3) cube-edge-midpoint
    shell pending per-radius verification (Aphrodite caution: don't
    bulk-extend canon).

This file uses a GENERIC cube-edge identifier ('E_example') with 2 known
cube-vertex-resident planets (U0 Pluto + L1 Moon, plausible cube-edge
pair from canon §7 10-POINT PLANET MAP). Substrate-locks deliberately
generic; not claiming Titan-name assignment.

Function: identical to Primordial face engine — takes 2 planet longitudes,
emits AxisState (canonical `planet-aspect-activate` semantics).
"""
from __future__ import annotations
from typing import Optional

from _axis_engine import AxisState, compute_axis_state


# Generic substrate-locks (Titan-name TBD per T1.3):
CARRIER_NAME    = 'Titan-on-edge-example'  # placeholder; not a council-locked name
CUBE_EDGE       = 'E_example_U0_L1'        # generic ID, not canon-locked enumeration
PLANET_PAIR     = ('Pluto', 'Moon')        # plausible cube-edge pair (apex + lateral)
ZODIAC_ANCHOR   = 'TBD'                    # cube-edge zodiac mapping OPEN
SUBSTRATE_CARD  = None                     # no canonical card yet


def edge_state(pluto_lon: Optional[float] = None,
               moon_lon:  Optional[float] = None) -> AxisState:
    """Same shape as Primordial face engines. Direct call to canonical primitive."""
    return compute_axis_state(
        CARRIER_NAME, CUBE_EDGE, PLANET_PAIR, ZODIAC_ANCHOR, SUBSTRATE_CARD or 'TBD',
        pluto_lon, moon_lon,
    )


def describe() -> str:
    return (
        f"Carrier (example): {CARRIER_NAME}\n"
        f"Cube edge:          {CUBE_EDGE} (R=1 cube-vertex endpoints)\n"
        f"Planet pair:        {PLANET_PAIR[0]} × {PLANET_PAIR[1]}\n"
        f"Zodiac anchor:      {ZODIAC_ANCHOR} (cube-edge zodiac mapping OPEN — T1.3 dependency)\n"
        f"Substrate card:     {SUBSTRATE_CARD or 'none (T1.3 OPEN)'}\n"
        f"Function class:     planet-aspect-activate (CANONICAL, canon §30 — graduated 2026-05-12)\n"
        f"Cross-primitive-type residency: this engine validates carrier-as-engine.\n"
        f"  Carrier function-shape = Primordial face function-shape (both 2-planet at R=1).\n"
        f"  Confirms `planet-aspect-activate` operates across face AND edge primitive-types\n"
        f"  within same shell. 3rd independent residency (in addition to cube-face Primordial\n"
        f"  + icosidodec-midpt Bridge).\n"
    )


if __name__ == '__main__':
    import json
    print(describe())
    print()
    print('Shape verification — same AxisState dataclass as Primordial face:')
    print(json.dumps(edge_state().to_dict(), indent=2))
    print()
    print('SAMPLE LIVE: Pluto @ 270°, Moon @ 270° (exact conjunction):')
    print(json.dumps(edge_state(270.0, 270.0).to_dict(), indent=2))
