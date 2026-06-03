"""
polyhymnia.py — R-LL renderer for Polyhymnia (Muse, X3 × Jupiter midpoint, R=1/√3).
"""
from __future__ import annotations
from _helpers import (
    build_header, position_tuple_str,
    r_ll_skeleton, llm_voice_surface,
)


def render_polyhymnia(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    prior_voices = ctx.get("prior_voices", [])

    header = build_header("Polyhymnia", placement, activation)
    pos_str = position_tuple_str(placement)

    # X3 × Jupiter midpoint — Jupiter-sovereignty held against Venus-crossing.
    # Hymnal register: reverent, formal, sovereign-acknowledging.
    character = (
        "X3 × Jupiter midpoint speaks hymnal — Jupiter-sovereignty addressed at "
        "Venus-crossing. Reverent register, 2-3 lines, formal cadence."
    )

    skeleton = {
        "Position":    pos_str,
        "Question-PE": q_profile.get("pe_note", "?"),
    }

    output, ok = llm_voice_surface(
        "Polyhymnia", header, pos_str, skeleton, prior_voices, character,
        max_tokens=180,
    )
    if ok:
        return output, "R-LL"
    return r_ll_skeleton("Polyhymnia", header, skeleton, prior_voices, character), "R-LL"
