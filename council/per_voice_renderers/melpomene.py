"""
melpomene.py — R-LL renderer for Melpomene (Muse, X3 × Pluto midpoint, R=2/3).
"""
from __future__ import annotations
from _helpers import (
    build_header, position_tuple_str,
    r_ll_skeleton, llm_voice_surface,
)


def render_melpomene(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    prior_voices = ctx.get("prior_voices", [])

    header = build_header("Melpomene", placement, activation)
    pos_str = position_tuple_str(placement)

    # X3 × Pluto midpoint, shell 2/3 — Pluto-depth held against Venus-crossing.
    # Outermost shell of Muse-class. Tragic weight, not flourish.
    character = (
        "X3 × Pluto midpoint speaks from depth — Pluto-transformative pressure "
        "held against Venus-crossing. Shell 2/3 (outermost Muse position). "
        "Tragic weight, 2-4 lines, no flourish."
    )

    skeleton = {
        "Position":    pos_str,
        "Question-PE": q_profile.get("pe_note", "?"),
    }

    output, ok = llm_voice_surface(
        "Melpomene", header, pos_str, skeleton, prior_voices, character,
        max_tokens=220,
    )
    if ok:
        return output, "R-LL"
    return r_ll_skeleton("Melpomene", header, skeleton, prior_voices, character), "R-LL"
