"""
mortal.py — generic R-PT renderer for any MORTAL placement_class voice.

Per orient_rules.md L342 + mortal_placement.py: real humans invoked into
council. Substrate-position from natal-dynamic; renderer emits natal-chart
substrate-snapshot rather than archetype-utterance.
"""
from __future__ import annotations
from _helpers import build_header


def render_mortal(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    voice_name = ctx.get("voice_name", "Mortal")

    header = build_header(voice_name, placement, activation)

    pos = placement.get("substrate_position", {})
    natal_date = pos.get("natal_date", "?")
    sun_lon = pos.get("sun_lon")

    mortal_obj = ctx.get("mortal_map", {}).get(voice_name)
    natal_loc = mortal_obj.natal_loc if mortal_obj else {}

    lines = [
        header,
        f"  Natal-dynamic placement: chart at {natal_date}",
    ]

    if sun_lon is not None:
        lines.append(f"  Identity-anchor: natal Sun at lon {sun_lon:.2f}°")

    # Substrate-snapshot of mortal's natal planets
    if isinstance(natal_loc, dict):
        planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
        chart_bits = []
        for p in planets:
            entry = natal_loc.get(p, {})
            if isinstance(entry, dict) and entry.get("lon") is not None:
                chart_bits.append(f"{p}={entry['lon']:.1f}°")
        if chart_bits:
            lines.append(f"  Chart-snapshot: {' / '.join(chart_bits)}")

    lines.append("  Mortal-as-voice: present by invocation, witnesses from natal-position")

    return "\n".join(lines), "R-PT"
