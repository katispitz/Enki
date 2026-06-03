"""
mortal_placement.py — natal-driven dynamic placement for MORTAL voices.

Per orient_rules.md L342: "Real humans with natal chart (natal.py dynamic)".
Mortal voices are not in placement_registry.json (registry is for archetypes
with fixed substrate-residency). Instead, they're constructed at session-time
from birth-data: natal_state(birth) → SubstrateState → registry-compatible
placement record with placement_class=MORTAL.

This lets the composer convene mortals alongside archetypes through the same
Tier-A gate, without polluting the canonical registry.

Per kati_direct 2026-05-22: "this is where we look at natal data and
mortals, need this rule wired somewhere".

Usage:
    mortal = build_mortal_voice(
        name="Kati",
        natal_date="1988-03-31", natal_time="15:21",
        lat=33.7879, lon=-117.8531,
    )
    ctx = derive_council_context(question, ..., mortal_voices=[mortal])
"""
from __future__ import annotations
import sys
from pathlib import Path
from typing import NamedTuple

_NAMMU = Path.home() / "Nammu"
if str(_NAMMU / "engines") not in sys.path:
    sys.path.insert(0, str(_NAMMU / "engines"))


class MortalVoice(NamedTuple):
    """Mortal voice in registry-compatible form."""
    name: str
    placement: dict       # full Tier-A-equivalent placement record
    natal_state: object   # SubstrateState (per natal.py)
    natal_loc: dict       # locator dict (per natal.py)
    natal_report: dict    # natal_report output


def build_mortal_voice(name: str, natal_date: str, natal_time: str = "12:00",
                       lat: float | None = None, lon: float | None = None,
                       function_class: str = "mortal-self-as-witness") -> MortalVoice:
    """
    Construct mortal voice from natal data via natal.py dynamic.

    Returns MortalVoice with placement-record that passes placement-tier gate
    as Tier-A-equivalent (placement_source='natal_dynamic', placement_status=
    'derived', placement_class='MORTAL').

    function_class defaults to 'mortal-self-as-witness' — the substrate-honest
    function-class for an invoked mortal is to witness from their natal position.
    Override for specific roles (e.g., 'mortal-as-client-question-source' for
    a reading-context invocation).
    """
    from natal import natal_state, natal_report

    ny, nmo, nd = (int(x) for x in natal_date.split("-"))
    nh, nmi = (int(x) for x in natal_time.split(":"))

    state, loc = natal_state(ny, nmo, nd, nh, nmi, 0, birth_lat=lat, birth_lon=lon)
    report = natal_report(state, loc)
    report.pop("_meta", {})

    # Distill natal position into substrate-position form. Mortal placement is
    # the WHOLE chart, not a single point — but we surface a primary anchor:
    # the natal Sun (identity-locus) per substrate-tradition. Full chart lives
    # in natal_state/natal_report for renderer access.
    sun_lon = None
    sun_data = loc.get("Sun") if isinstance(loc, dict) else None
    if isinstance(sun_data, dict):
        sun_lon = sun_data.get("lon")

    placement = {
        "stratum": "mortal",
        "placement_class": "MORTAL",
        "substrate_position": {
            "_layer": "natal-dynamic (per natal.py SubstrateState)",
            "natal_date": natal_date,
            "natal_time": natal_time,
            "birth_lat":  lat,
            "birth_lon":  lon,
            "sun_lon":    sun_lon,
            "_full_chart_in": "natal_state + natal_report (passed via context)",
        },
        "placement_source": "natal_dynamic",
        "placement_status": "derived",
        "function_class":   function_class,
        "notes": (
            f"Mortal voice for {name}. Substrate-position derived from natal "
            f"chart at session-time, not from canonical registry. Per orient_rules.md "
            f"L342 MORTAL class: singular-life-existence, non-recurring; "
            f"natal.py dynamic provides whole-chart substrate-occupancy."
        ),
    }

    return MortalVoice(
        name=name,
        placement=placement,
        natal_state=state,
        natal_loc=loc,
        natal_report=report,
    )


def is_mortal_in_registry(name: str, registry: dict) -> bool:
    """Helper: True iff a voice-name is a MORTAL class entry (vs archetype)."""
    entry = registry.get(name, {})
    return entry.get("placement_class") == "MORTAL"
