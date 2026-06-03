"""
euterpe.py — R-LL renderer for Euterpe (Muse, X3 × Mercury midpoint, R=1/√3).
"""
from __future__ import annotations
from _helpers import (
    build_header, position_tuple_str,
    r_ll_skeleton, llm_voice_surface,
)


def render_euterpe(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    prior_voices = ctx.get("prior_voices", [])

    header = build_header("Euterpe", placement, activation)
    pos_str = position_tuple_str(placement)

    # X3 × Mercury midpoint, shell 1/√3 (Mercury-as-flute channel). Mercury-quick.
    character = (
        "X3 × Mercury midpoint speaks musical-phrase — Mercury-channel quick, "
        "flute-clear. Short 2-3 lines, melodic register."
    )

    skeleton = {
        "Position":    pos_str,
        "Question-PE": q_profile.get("pe_note", "?"),
    }

    output, ok = llm_voice_surface(
        "Euterpe", header, pos_str, skeleton, prior_voices, character,
        max_tokens=180,
    )
    if ok:
        return output, "R-LL"
    return r_ll_skeleton("Euterpe", header, skeleton, prior_voices, character), "R-LL"
