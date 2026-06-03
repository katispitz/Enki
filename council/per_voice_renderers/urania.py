"""
urania.py — R-PT renderer for Urania (Muse, X3 × Uranus / origin / R=0).

Function: astronomy / origin-observer / center-frame-anchor. V29 precedent:
precise ecliptic-longitude data table w/ aspect angles. Pure-template.
"""
from __future__ import annotations
from _helpers import build_header, prior_voice_names


def render_urania(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    transit_loc = ctx.get("transit_loc", {}) or {}
    natal_loc = ctx.get("natal_loc", {}) or {}
    q_points = ctx.get("q_points") or []
    activations = ctx.get("activations", []) or []
    prior_voices = ctx.get("prior_voices", [])

    header = build_header("Urania", placement, activation)

    lines = [
        header,
        "  Ecliptic data (council moment):",
        "    | Planet  | Transit lon | Natal lon |",
        "    |---------|-------------|-----------|",
    ]

    planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
    for p in planets:
        t = transit_loc.get(p, {}) or {}
        n = natal_loc.get(p, {}) or {}
        t_lon = t.get("lon")
        n_lon = n.get("lon")
        if t_lon is not None or n_lon is not None:
            lines.append(
                f"    | {p:7s} | {(t_lon or 0):11.2f} | {(n_lon or 0):9.2f} |"
            )

    # Question-relevant aspects
    if activations:
        lines.append("  Aspects (orb-tight):")
        for a in activations[:5]:
            if a.get("weight", 0) >= 0.2:
                lines.append(
                    f"    · {a.get('transit_planet', '?')} {a.get('aspect', '?')} "
                    f"{a.get('natal_planet', '?')} (orb~{(1 - a.get('weight', 0)) * 10:.1f}°)"
                )

    lines.append("  Origin-frame: observer at (0,0,0); X3+X6 cancel at center; sees-all")

    prior = prior_voice_names(prior_voices)
    if prior:
        lines.append(f"  Astronomical placement of {prior[-1]}'s claim: data above stands as verification-frame.")

    return "\n".join(lines), "R-PT"
