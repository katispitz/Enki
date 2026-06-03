"""
erato.py — R-LL renderer for Erato (Muse, X3 × Mars midpoint, R=√2/3, grid=15).
Per G-P2-1: character derived from position; G-P2-2: LLM wired with fallback.
"""
from __future__ import annotations
from _helpers import (
    build_header, position_tuple_str,
    r_ll_skeleton, llm_voice_surface,
)


def render_erato(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    prior_voices = ctx.get("prior_voices", [])
    bonds_str = ctx.get("bonds_str", "")

    header = build_header("Erato", placement, activation)
    pos_str = position_tuple_str(placement)

    # X3 × Mars midpoint: Mars is Fa-tone (pathology-axis V2-V7 per Aspects v2);
    # crossing X3 (mi→fa shock) = lyric-as-pulled-by-bond. Position = Mars-energy
    # held against Venus-X3-crossing. Lyric 2-4 lines. MUSE (not Nereid Erato-sea).
    character = (
        "X3 × Mars midpoint speaks lyric — Mars-energy pulled toward Venus-crossing. "
        "Pathology-axis-as-song (V2-V7 bond). Short lyric utterance, relational register, "
        "2-4 lines. MUSE Erato (distinct from Nereid Erato-sea)."
    )

    skeleton = {
        "Position":    pos_str,
        "Question-PE": q_profile.get("pe_note", "?"),
        "Bonds":       bonds_str[:120] if bonds_str else "(none in council)",
    }

    output, ok = llm_voice_surface(
        "Erato", header, pos_str, skeleton, prior_voices, character,
        max_tokens=200,
    )
    if ok:
        return output, "R-LL"
    return r_ll_skeleton("Erato", header, skeleton, prior_voices, character), "R-LL"
