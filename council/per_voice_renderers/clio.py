"""
clio.py — R-PT renderer for Clio (Muse, X3 × Saturn midpoint).

Function: history / Cronus-time-keeping. V29 precedent: long-period markers +
outer-planet generational aspects. Pure-template.
"""
from __future__ import annotations
from _helpers import build_header, prior_voice_names


OUTER_PLANETS = ("Saturn", "Uranus", "Neptune", "Pluto")


def render_clio(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    activations = ctx.get("activations", []) or []
    prior_voices = ctx.get("prior_voices", [])

    header = build_header("Clio", placement, activation)

    # Long-period markers — outer-planet aspects active
    outer_aspects = [
        a for a in activations
        if any(p in (a.get("transit_planet"), a.get("natal_planet")) for p in OUTER_PLANETS)
    ]

    lines = [
        header,
        "  Long-period markers:",
    ]

    if outer_aspects:
        for a in outer_aspects[:4]:
            tp = a.get("transit_planet", "?")
            np = a.get("natal_planet", "?")
            asp = a.get("aspect", "?")
            lines.append(f"    · {tp} {asp} {np}")
    else:
        lines.append("    · (no outer-planet aspects currently active)")

    q_pe = q_profile.get("pe_note", "?")
    lines.append(f"  Generational context: question at PE={q_pe} placed against Saturn-axis time-keeping")

    prior = prior_voice_names(prior_voices)
    if prior:
        lines.append(f"  Marks {prior[-1]}'s assertion against historical-lineage at this position.")

    return "\n".join(lines), "R-PT"
