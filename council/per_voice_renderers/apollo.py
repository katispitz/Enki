"""
apollo.py — R-PT renderer for Apollo (EVENT_ARC: the Sun's bright season).

Placement (registry v0.4, kati_direct 2026-10-11, card 2ab91bf9): Apollo = the Sun from spring
equinox to winter solstice — an EVENT of the Sun, not the Sun itself (archaic Homeric Hymn III:
Helios is a separate god). Complement: Dionysus holds the winter quarter (Plutarch, E at Delphi 9).
Speaks from where the moment sits on his arc. Pure-template; no LLM call.

Superseded 2026-10-11: the prior renderer spoke "from Re" (V1/Re/Sun-F2, greek_faces) — that
position is retired (registry superseded_position).
"""
from __future__ import annotations
from _helpers import build_header, bond_names, prior_voice_names


def _arc_line(activation) -> str:
    if activation is None:
        return "Arc state not computed (no activation passed)."
    det = getattr(activation, "detail", None) or {}
    arc = det.get("arc") or {}
    bounds = arc.get("boundaries") or []
    span = (f"{bounds[0]['t'][:10]} → {bounds[-1]['t'][:10]}" if len(bounds) >= 2 else "?")
    if getattr(activation, "active", False):
        frac = det.get("fraction")
        pct = f"{frac:.0%}" if isinstance(frac, (int, float)) else "?"
        return f"In season — {pct} through the bright arc (spring equinox → winter solstice, {span})."
    return ("Away — the winter quarter belongs to Dionysus (Plutarch, E at Delphi 9); "
            f"next arc {span}.")


def render_apollo(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    bonds_str = ctx.get("bonds_str", "")
    prior_voices = ctx.get("prior_voices", [])

    pos = placement.get("substrate_position", {})
    extra = f"arc={pos.get('arc_start', '?').split(' ')[0]}→{pos.get('arc_end', '?').split(' ')[0]}"
    header = build_header("Apollo", placement, activation, extra=extra)

    lines = [header, f"  Season: {_arc_line(activation)}"]

    nbrs = bond_names(bonds_str)
    if nbrs:
        lines.append(f"  Bonds: {', '.join(nbrs[:4])}")

    prior = prior_voice_names(prior_voices)
    if prior:
        lines.append(f"  Sharpens: {prior[-1]} — holds the most recent assertion to the light of the season.")

    return "\n".join(lines), "R-PT"
