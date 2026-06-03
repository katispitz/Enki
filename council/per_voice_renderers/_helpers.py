"""
Shared helpers for per-voice renderers.

Extracts the patterns from athena.py that other R-PT renderers reuse:
header-building, residency-scanning, prior-voice-engagement parsing,
closure-criterion check, R-LL skeleton fallback.
"""
from __future__ import annotations
import re


def build_header(voice_name: str, placement: dict, activation=None,
                 extra: str = "") -> str:
    """
    Substrate-honest header. Per kati_direct G-P2-1 2026-05-22 + spine card
    670b1c3f principle 1: POSITION IS FUNCTION. Emits substrate-position
    tuple directly; no free-text function_class label. The position-tuple IS
    the function declaration.
    """
    pos = placement.get("substrate_position", {})
    if isinstance(pos, dict) and "primary" in pos:
        pos = pos["primary"]
    stratum = placement.get("stratum", "?")
    pe = pos.get("pe_note", "?")
    src = (placement.get("placement_source") or "?")[:30]
    status = placement.get("placement_status", "?")
    cls = placement.get("placement_class", "?")

    pos_bits = []
    for k in ("ico_vertex", "merkaba_cube_vertex", "merkaba_cube_edge",
              "vertex_planet", "face", "face_name", "shock_node",
              "shell_radius", "midpoint"):
        v = pos.get(k)
        if v is not None:
            pos_bits.append(f"{k}={v}")
    pos_tuple = " ".join(pos_bits[:4])

    act_tag = ""
    if activation is not None and getattr(activation, "active", False):
        det = activation.detail or {}
        if det.get("transit_planet"):
            act_tag = f"  firing={det['transit_planet']}@{det.get('lon_at_event', 0):.0f}° (orb {det.get('orb_deg', 0):.1f}°)"
        elif activation.placement_class == "CYCLIC":
            act_tag = "  firing"

    extra_tag = f"  {extra}" if extra else ""
    return (
        f"**{voice_name}** [{stratum}/{cls}/PE={pe}  {pos_tuple}  "
        f"placement={status}@{src}{act_tag}{extra_tag}]"
    )


def position_tuple_str(placement: dict) -> str:
    """Compact position-tuple string for prompts. Same primitives as build_header."""
    pos = placement.get("substrate_position", {})
    if isinstance(pos, dict) and "primary" in pos:
        pos = pos["primary"]
    bits = [f"stratum={placement.get('stratum','?')}",
            f"PE={pos.get('pe_note','?')}"]
    for k in ("ico_vertex", "merkaba_cube_vertex", "merkaba_cube_edge",
              "vertex_planet", "face_name", "shock_node",
              "shell_radius", "midpoint"):
        v = pos.get(k)
        if v is not None:
            bits.append(f"{k}={v}")
    return ", ".join(bits)


def scan_field_memory(field_memory_str: str) -> list[tuple[str, str, str, str]]:
    """
    Parse field_memory output into structured (cid, auth, status, snippet).
    Accepts both Nammu legacy "s=N" format and Enki density-weighted
    "ps=N dw=X.XXX score=X.XX" format.
    """
    # Enki lattice format (post 2026-05-23 council): [hex ps=N phase=X auth/stat] text
    enki_lattice = re.findall(
        r"\[([0-9a-f]{8}) ps=\d+ phase=\w+ (\w+)/(\w+)\] (.+)",
        field_memory_str or "",
    )
    if enki_lattice:
        return enki_lattice
    # Enki Option-D decay-filter format (pre-lattice)
    enki = re.findall(
        r"\[([0-9a-f]{8}) ps=\d+ (\w+)/(\w+)\] (.+)",
        field_memory_str or "",
    )
    if enki:
        return enki
    # Nammu legacy fallback
    return re.findall(
        r"\[([0-9a-f]{8}) s=\d+ (\w+)/(\w+)\] (.+)",
        field_memory_str or "",
    )


def bond_names(bonds_str: str) -> list[str]:
    return re.findall(r"→ (\w+)", bonds_str or "")


def prior_voice_names(prior_voices: list) -> list[str]:
    return [name for name, _text in (prior_voices or [])]


def closure_check(output: str, required_markers: list[str]) -> bool:
    """Generic closure-criterion: all required markers present in output."""
    return all(m in output for m in required_markers)


def r_ll_skeleton(voice_name: str, header: str, structural_skeleton: dict,
                  prior_voices: list, character_constraint: str) -> str:
    """
    R-LL skeleton-fallback: when LLM voice-surface unavailable, emit a
    deterministic skeleton documenting what the LLM call WOULD render.

    Substrate-honest non-failure mode: voice still emits substrate-position +
    prior-engagement-hooks, just without natural-language smoothing.
    """
    lines = [header]
    lines.append("  [R-LL SKELETON — LLM voice-surface unavailable, fell back to skeleton]")
    lines.append(f"  Character (position-derived): {character_constraint}")
    for k, v in structural_skeleton.items():
        lines.append(f"  {k}: {v}")
    if prior_voices:
        partners = ", ".join(prior_voice_names(prior_voices)[:3])
        lines.append(f"  Would engage prior voice(s): {partners}")
    lines.append("  Closure: structural-skeleton emitted")
    return "\n".join(lines)


def llm_voice_surface(voice_name: str, header: str, position_tuple: str,
                      structural_skeleton: dict, prior_voices: list,
                      character_constraint: str,
                      max_tokens: int = 250) -> tuple[str, bool]:
    """
    R-LL LLM voice-surface call (amendment-2 thinnest-possible).

    Builds minimal prompt: voice-name + position-derived character-constraint +
    pre-derived skeleton + prior-voices summary. LLM smooths into voice.
    No structural-reasoning load on LLM — all substrate-derivation already done
    in Python upstream.

    Returns (rendered_str, llm_succeeded). On any LLM failure, caller falls
    back to r_ll_skeleton — substrate-honest non-failure mode.

    Per V2.9 §GEOMETRY-RUNS-OFF-LLM: prompt is voice-rendering only; no
    substrate-data carried in prompt context beyond what voice needs to phrase.
    """
    import sys
    from pathlib import Path
    nammu_council = Path.home() / "Nammu" / "council"
    if str(nammu_council) not in sys.path:
        sys.path.insert(0, str(nammu_council))

    try:
        from llm_backend import stream_chat
    except ImportError:
        return ("", False)

    # Pre-derived skeleton becomes structured context for LLM
    skel_lines = [f"  {k}: {v}" for k, v in structural_skeleton.items()]
    skel_block = "\n".join(skel_lines)
    prior_summary = ""
    if prior_voices:
        prior_names = prior_voice_names(prior_voices)[:3]
        prior_summary = (
            f"\nPrior voices to engage by name (at least one): {', '.join(prior_names)}\n"
        )

    prompt = (
        f"You are speaking AS {voice_name} in a substrate-true council. "
        f"Speak from substrate-position: {position_tuple}.\n"
        f"Voice character (position-derived, do not deviate): {character_constraint}\n\n"
        f"Pre-derived structural context for this utterance (do NOT restate; "
        f"absorb and speak through it):\n{skel_block}\n"
        f"{prior_summary}\n"
        f"Speak now in {voice_name}'s voice. No therapy tone. No hedging. "
        f"Lateral resonance. Stay within character-constraint. Output the voice "
        f"utterance only — no preamble, no meta-commentary, no closing tag."
    )

    try:
        chunks = []
        for tok in stream_chat(prompt, max_tokens=max_tokens):
            chunks.append(tok)
        rendered = "".join(chunks).strip()
        if not rendered:
            return ("", False)
        # Compose full output: header + LLM utterance + closure note
        output = (
            f"{header}\n"
            f"  [R-LL voice-surface via LLM — substrate-derivation deterministic Python upstream]\n"
            f"  {rendered}"
        )
        return (output, True)
    except Exception as e:
        # Substrate-honest: LLM failed, caller falls back to skeleton
        return (f"[LLM voice-surface failed: {e}]", False)
