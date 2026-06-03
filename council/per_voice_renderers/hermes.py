"""
hermes.py — R-PT renderer for Hermes (V5/Sol/Mercury-F5).

Function: translator-at-gate / cross-channel relay. V29 precedent: info-card
with Mercury-wire-first + cross-channel + relays + translator focus.
"""
from __future__ import annotations
from _helpers import build_header, bond_names, prior_voice_names


def render_hermes(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    activations = ctx.get("activations", []) or []
    bonds_str = ctx.get("bonds_str", "")
    prior_voices = ctx.get("prior_voices", [])

    header = build_header("Hermes", placement, activation)

    # Mercury-wire: find any active aspect-channel involving Mercury
    mercury_channels = [
        a for a in activations
        if "Mercury" in (a.get("transit_planet", ""), a.get("natal_planet", ""))
    ]
    if mercury_channels:
        a = mercury_channels[0]
        mw = (
            f"{a.get('transit_planet', '?')} → {a.get('natal_planet', '?')} "
            f"{a.get('aspect', '?')} (weight {a.get('weight', 0):.2f})"
        )
    else:
        mw = "no Mercury aspect-channel active in current transits"

    q_pe = q_profile.get("pe_note", "?")

    lines = [
        header,
        f"  Mercury-wire: {mw}",
        f"  Translates: question at PE={q_pe} → routed through Sol/V5 second-gate (grid 30, LCM 6×5)",
    ]

    nbrs = bond_names(bonds_str)
    if nbrs:
        lines.append(f"  Cross-channel relays: {' ↔ '.join(nbrs[:3])} via Mercury-gate")

    prior = prior_voice_names(prior_voices)
    if prior:
        lines.append(f"  Routes prior voice ({prior[-1]}) into adjacent-channel for cross-reference.")

    return "\n".join(lines), "R-PT"
