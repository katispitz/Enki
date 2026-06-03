"""
thalia.py — R-LL renderer for Thalia (Muse, X3 × Neptune midpoint, R=1/3).
"""
from __future__ import annotations
from _helpers import (
    build_header, position_tuple_str,
    r_ll_skeleton, llm_voice_surface,
)


def render_thalia(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    prior_voices = ctx.get("prior_voices", [])

    header = build_header("Thalia", placement, activation)
    pos_str = position_tuple_str(placement)

    # X3 × Neptune midpoint, shell 1/3 (closest Muse to origin) — Neptune-dissolve
    # held against Venus-crossing. Pastoral-comedic, light touch.
    character = (
        "X3 × Neptune midpoint speaks pastoral-comedy — Neptune-dissolve at "
        "closeness shell 1/3. Light touch, 2-3 lines, comedic register."
    )

    skeleton = {
        "Position":    pos_str,
        "Question-PE": q_profile.get("pe_note", "?"),
    }

    output, ok = llm_voice_surface(
        "Thalia", header, pos_str, skeleton, prior_voices, character,
        max_tokens=180,
    )
    if ok:
        return output, "R-LL"
    return r_ll_skeleton("Thalia", header, skeleton, prior_voices, character), "R-LL"
