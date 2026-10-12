"""
hermes.py — R-PT renderer for Hermes (EVENT_ARC: the Mercury dawn-birth descent).

Placement (registry v0.4, 2026-10-11, engine-evidence card 87530895): Hermes = a Mercury descent
read against the Homeric Hymn to Hermes — born at dawn (first morning sighting with no evening
sighting before it), drives the cattle backward (still retrograde), back in the cradle (station
direct). Athens sky; the autumn Libra/Scorpio face falls out of the predicate.
Speaks from where the moment sits on his arc. Pure-template; no LLM call.

Superseded 2026-10-11: the prior renderer routed "through Sol/V5 second-gate (grid 30)"
(greek_faces) — that position is retired (registry superseded_position).
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
        return f"Newborn, driving the herd backward — {pct} from dawn birth to the cradle ({span})."
    return f"Unborn — in Maia's cave; next dawn birth {span} (Athens sky)."


def render_hermes(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    activations = ctx.get("activations", []) or []
    bonds_str = ctx.get("bonds_str", "")
    prior_voices = ctx.get("prior_voices", [])

    pos = placement.get("substrate_position", {})
    extra = f"arc={pos.get('arc_start', '?').split(' ')[0]}→{pos.get('arc_end', '?').split(' ')[0]}"
    header = build_header("Hermes", placement, activation, extra=extra)

    lines = [header, f"  Phase: {_arc_line(activation)}"]

    # Mercury-wire: any active aspect-channel involving Mercury in current transits
    mercury_channels = [
        a for a in activations
        if "Mercury" in (a.get("transit_planet", ""), a.get("natal_planet", ""))
    ]
    if mercury_channels:
        a = mercury_channels[0]
        lines.append(f"  Mercury-wire: {a.get('transit_planet', '?')} → {a.get('natal_planet', '?')} "
                     f"{a.get('aspect', '?')}")

    nbrs = bond_names(bonds_str)
    if nbrs:
        lines.append(f"  Bonds: {', '.join(nbrs[:4])}")

    prior = prior_voice_names(prior_voices)
    if prior:
        lines.append(f"  Turns back: {prior[-1]} — walks the most recent assertion the other way.")

    return "\n".join(lines), "R-PT"
