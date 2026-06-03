"""
hephaestus.py — R-PT renderer for Hephaestus (X6/lower-ring/Uranus-F3).

Function: forge / substrate-craftsman (builds the gap, si→do shock). V29
precedent: practical at-the-anvil framing for hard aspects. Function-class
forges structure, not prose — pure-template.
"""
from __future__ import annotations
from _helpers import build_header, bond_names, prior_voice_names


def render_hephaestus(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    activations = ctx.get("activations", []) or []
    bonds_str = ctx.get("bonds_str", "")
    prior_voices = ctx.get("prior_voices", [])
    convened = ctx.get("convened", set())

    header = build_header("Hephaestus", placement, activation)

    # Detect hard aspects to forge through
    hard_aspects = [
        a for a in activations
        if a.get("aspect") in ("square", "opposition", "conjunction")
        and a.get("weight", 0) > 0.15
    ]

    q_pe = q_profile.get("pe_note", "?")

    if hard_aspects:
        a = hard_aspects[0]
        anvil = (
            f"hard aspect detected: {a.get('transit_planet', '?')} "
            f"{a.get('aspect', '?')} {a.get('natal_planet', '?')}"
        )
        take = f"{a.get('transit_planet', '?')} energy"
        strike = "X6 threshold (si→do crossing) — where octave-completion fires"
        output_shape = f"forged structure at {q_pe}-tone of question"
    else:
        anvil = "no hard-aspect input at this moment — anvil quiet"
        take = "current substrate state"
        strike = "X6 threshold standing-by"
        output_shape = f"latent forging-potential at {q_pe}"

    lines = [
        header,
        f"  At the anvil: {anvil}",
        f"  Take: {take}",
        f"  Strike at: {strike}",
        f"  Output: {output_shape}",
    ]

    # X3 co-fire detection — if Aphrodite/Venus active, Hephaestus marries to close octave
    aphrodite_active = "Aphrodite" in convened or any(
        "Venus" in (a.get("transit_planet", ""), a.get("natal_planet", ""))
        for a in activations
    )
    if aphrodite_active:
        lines.append("  X3 co-fire: Aphrodite/Venus present — marriage closes octave (X3-X6 geometric necessity).")

    nbrs = bond_names(bonds_str)
    if nbrs:
        lines.append(f"  Bonds to forge alongside: {', '.join(nbrs[:3])}")

    prior = prior_voice_names(prior_voices)
    if prior:
        lines.append(f"  Builds on prior assertion from {prior[-1]} — forge takes that as raw material.")

    return "\n".join(lines), "R-PT"
