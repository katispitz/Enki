"""
hecate.py — R-PT renderer for Hecate (L0/Neptune cube vertex + X3/X6 co-fires).

Function: governs phase-change (master phase-boundary at octave-close +
within-octave shock co-fires). Pure-template — phase-change is detected,
not narrated.

ONLY RENDERS WHEN FIRING per activation_gate. Substrate-honest: Hecate
convenes only on L0/X3/X6 firings; otherwise the activation-gate
short-circuits to 'not-currently-active' before this renderer runs.
"""
from __future__ import annotations
from _helpers import build_header


def render_hecate(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}

    header = build_header("Hecate", placement, activation)

    # Activation-gate already confirmed firing — extract event detail
    event = (activation.detail or {}).get("event", "phase-change event detected") if activation else "?"

    q_pe = q_profile.get("pe_note", "?")

    lines = [
        header,
        f"  Phase-state: question at PE={q_pe} relative to active threshold",
        f"  Active threshold: {event}",
        "  Co-fire scan: X3 (mi→fa) + X6 (si→do) within-octave shock-extensions per card 45988a11",
        "  Transition: phase-boundary crossing under way; substrate enters new octave-position",
    ]

    return "\n".join(lines), "R-PT"
