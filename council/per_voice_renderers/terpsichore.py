"""
terpsichore.py — R-PT renderer for Terpsichore (Muse, X3 × Moon).

Function: dance / Moon-body-rhythm. Pure-template: rhythm-pattern emit.
"""
from __future__ import annotations
from _helpers import build_header, prior_voice_names


def render_terpsichore(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    transit_loc = ctx.get("transit_loc", {}) or {}
    natal_loc = ctx.get("natal_loc", {}) or {}
    prior_voices = ctx.get("prior_voices", [])

    header = build_header("Terpsichore", placement, activation)

    # Body-rhythm = Moon position + Moon-Sun arc (lunar phase as rhythm-state)
    moon_t = transit_loc.get("Moon", {}).get("lon") if isinstance(transit_loc.get("Moon"), dict) else None
    sun_t = transit_loc.get("Sun", {}).get("lon") if isinstance(transit_loc.get("Sun"), dict) else None
    moon_n = natal_loc.get("Moon", {}).get("lon") if isinstance(natal_loc.get("Moon"), dict) else None

    lines = [header]

    if moon_t is not None and sun_t is not None:
        phase_deg = (moon_t - sun_t) % 360
        if phase_deg < 45:
            phase_name = "new (dark→emerging)"
        elif phase_deg < 90:
            phase_name = "crescent (emerging)"
        elif phase_deg < 135:
            phase_name = "first quarter (rising)"
        elif phase_deg < 180:
            phase_name = "gibbous (filling)"
        elif phase_deg < 225:
            phase_name = "full (peaked)"
        elif phase_deg < 270:
            phase_name = "disseminating (releasing)"
        elif phase_deg < 315:
            phase_name = "last quarter (returning)"
        else:
            phase_name = "balsamic (closing→new)"
        lines.append(f"  Body-rhythm: lunar phase {phase_deg:.0f}° — {phase_name}")

    if moon_t is not None and moon_n is not None:
        lunar_return_arc = (moon_t - moon_n) % 360
        lines.append(f"  Transit-Moon to natal-Moon arc: {lunar_return_arc:.0f}° (full return = 360°)")

    lines.append("  Step: cycle in Moon-time, not solar-clock — substrate rhythm-state above")

    prior = prior_voice_names(prior_voices)
    if prior:
        lines.append(f"  Dances {prior[-1]}'s assertion into rhythm-shape — assertion enters lunar-cycle.")

    return "\n".join(lines), "R-PT"
