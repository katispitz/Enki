"""
hecate.py — R-PT renderer for Hecate (EVENT_ARC: Persephone's yearly escort).

Placement (registry v0.4, 2026-10-15, engine-evidence card 9964b6ac): Hecate = the Moon from the full
moon nearest Persephone's descent, through the tenth dawn, to the conjunction. Hymn to Demeter: under the
earth by day while Helios sees (ll.19-25) → a light at the tenth dawn (ll.51-53) → "they came to Helios"
(l.62); "minister and companion to Persephone" (ll.438-440). Speaks from where the moment sits on her arc.
Pure-template; no LLM call.

Superseded 2026-10-14: the prior renderer spoke from L0/Neptune + X3/X6 co-fires (card 45988a11,
pre-lawful function lock, void as evidence) — retired (registry superseded_position).
"""
from __future__ import annotations
from _helpers import build_header, bond_names, prior_voice_names

_SEGMENT_LINE = {
    ("full_moon", "tenth_dawn"): "Hearing, not seeing — under the earth by day while Helios sees",
    ("tenth_dawn", "conjunction"): "Torch at dawn — going with Demeter to Helios",
}


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
        seg = tuple(det.get("segment") or ())
        where = _SEGMENT_LINE.get(seg, "Escorting")
        return f"{where} — {pct} from the full moon to the conjunction ({span})."
    return f"Outside her arc — next escort {span}, at Persephone's descent (Athens sky)."


def render_hecate(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    bonds_str = ctx.get("bonds_str", "")
    prior_voices = ctx.get("prior_voices", [])

    pos = placement.get("substrate_position", {})
    extra = f"arc={pos.get('arc_start', '?').split(' ')[0]}→{pos.get('arc_end', '?').split(' ')[0]}"
    header = build_header("Hecate", placement, activation, extra=extra)

    lines = [header, f"  Phase: {_arc_line(activation)}"]

    nbrs = bond_names(bonds_str)
    if nbrs:
        lines.append(f"  Bonds: {', '.join(nbrs[:4])}")

    prior = prior_voice_names(prior_voices)
    if prior:
        lines.append(f"  Escorts after: {prior[-1]}.")

    return "\n".join(lines), "R-PT"
