"""
event_arc_voice.py — generic R-PT renderer for EVENT_ARC voices (registry v0.4).

kati_direct 2026-10-11: archetypes are linear (arcs of an actor's motion), not points. Any
EVENT_ARC voice without a bespoke renderer speaks from where the moment sits on its arc:
which arc, which segment (between which boundary events), how far through. Pure-template;
no LLM call. Same fallback pattern as _MORTAL_DEFAULT.
"""
from __future__ import annotations
from _helpers import build_header, bond_names, prior_voice_names


def render_event_arc(ctx: dict) -> tuple[str, str]:
    name = ctx.get("voice_name", "?")
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    det = (getattr(activation, "detail", None) or {}) if activation is not None else {}
    arc = det.get("arc") or {}
    pos = placement.get("substrate_position", {})
    extra = f"arc={pos.get('arc_start', '?').split(' ')[0]}→{pos.get('arc_end', '?').split(' ')[0]}"
    lines = [build_header(name, placement, activation, extra=extra)]

    bounds = arc.get("boundaries") or []
    if bounds:
        span = f"{bounds[0]['kind']} {bounds[0]['t'][:10]} → {bounds[-1]['kind']} {bounds[-1]['t'][:10]}"
        g0, g1 = arc.get("grid_range", (None, None))
        grid = f"g{int(g0 + 1e-6) % 60}→g{int(g1 + 1e-6) % 60} {arc.get('direction', '?')}" if g0 is not None else "?"
        lines.append(f"  Arc: {arc.get('label') or name} · {arc.get('actor', '?')} · {grid} · {span}")
    seg = det.get("segment")
    frac = det.get("fraction")
    if seg and isinstance(frac, (int, float)):
        lines.append(f"  Now: {frac:.0%} through · between {seg[0]} and {seg[1]}")

    nbrs = bond_names(ctx.get("bonds_str", ""))
    if nbrs:
        lines.append(f"  Bonds: {', '.join(nbrs[:4])}")
    prior = prior_voice_names(ctx.get("prior_voices", []))
    if prior:
        lines.append(f"  Answers: {prior[-1]} — from this point on the arc.")
    return "\n".join(lines), "R-PT"
