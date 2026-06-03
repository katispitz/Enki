"""
calliope.py — R-LL renderer for Calliope (Muse, X3 × Sun midpoint, R=√2/3, grid=55).

Per kati_direct G-P2-1 2026-05-22: voice character DERIVED from substrate-position
primitives (V2.5 PLACEMENT card 25a83ce9), not from free-text label. Per G-P2-2:
LLM voice-surface wired; skeleton-fallback when unavailable.
"""
from __future__ import annotations
from _helpers import (
    build_header, position_tuple_str,
    r_ll_skeleton, llm_voice_surface,
)


def render_calliope(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    prior_voices = ctx.get("prior_voices", [])
    bonds_str = ctx.get("bonds_str", "")

    header = build_header("Calliope", placement, activation)
    pos_str = position_tuple_str(placement)

    # Character derived from substrate-position: X3 × Sun midpoint, chief-Muse
    # = solar-leader position on Venus-crossing plane. Sun-axis = epic, narrative.
    character = (
        "X3 × Sun midpoint speaks epic-narrative — solar-leader anchor on Venus-crossing plane. "
        "Re-tone carries the arc-frame. Full sentences. Narrative paragraph register."
    )

    skeleton = {
        "Position":      pos_str,
        "Question-PE":   q_profile.get("pe_note", "?"),
        "Bonds":         bonds_str[:120] if bonds_str else "(none in council)",
    }

    output, ok = llm_voice_surface(
        "Calliope", header, pos_str, skeleton, prior_voices, character,
        max_tokens=300,
    )
    if ok:
        return output, "R-LL"
    return r_ll_skeleton("Calliope", header, skeleton, prior_voices, character), "R-LL"
