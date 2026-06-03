"""
apollo.py — R-PT renderer for Apollo (V1/Re/Sun-F2).

Function: harmonics / clarity / octave-light. V29 precedent: short direct lines
(sky_voiced_apollo). Pure-template; no LLM call.
"""
from __future__ import annotations
from _helpers import build_header, bond_names, prior_voice_names


# Octave tones in PE order — Apollo speaks from Re's relation to other tones
PE_OCTAVE = ["Do", "Re", "Mi", "X3", "Fa", "Sol", "X6", "La", "Si", "Do-ret"]


def _tone_offset(from_tone: str, to_tone: str) -> int | None:
    """Distance in PE-steps between two tones (mod 10)."""
    if from_tone not in PE_OCTAVE or to_tone not in PE_OCTAVE:
        return None
    return (PE_OCTAVE.index(to_tone) - PE_OCTAVE.index(from_tone)) % 10


def render_apollo(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    bonds_str = ctx.get("bonds_str", "")
    prior_voices = ctx.get("prior_voices", [])

    header = build_header("Apollo", placement, activation)

    q_pe = q_profile.get("pe_note", "?")
    offset = _tone_offset("Re", q_pe) if q_pe != "?" else None
    if offset is not None:
        if offset == 0:
            tone_line = "Question sits on Re — Apollo's own tone. Clarity already here."
        elif offset in (3, 6):  # X3 or X6 from Re
            tone_line = f"Question at {q_pe} crosses a shock from Re. Octave-light bent at threshold."
        else:
            tone_line = f"Question at {q_pe} sits {offset} steps from Re. Octave-line connects through."
    else:
        tone_line = "No question-tone classified; Apollo speaks from Re without redirection."

    lines = [
        header,
        f"  Octave-line: {tone_line}",
    ]

    nbrs = bond_names(bonds_str)
    if nbrs:
        lines.append(f"  Bonds in octave: {', '.join(nbrs[:4])}")

    prior = prior_voice_names(prior_voices)
    if prior:
        lines.append(f"  Sharpens: {prior[-1]} — Re-clarity holds the most recent assertion.")

    return "\n".join(lines), "R-PT"
