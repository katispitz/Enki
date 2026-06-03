"""
athena.py — substrate-true Athena renderer (R-PT, pure template).

Per design-spec card 431d9622 §(2). Athena's function-class is
structure-of-container / lock-by-redundancy auditor (Saturn affinity, V7
ico_vertex, La tone, F7 Anchor face). Output = structural assertion, not
narrative. NO LLM CALL.

Per amendment-3 (card 087ecf52): self-closing — closure-criterion is
"lock-status emitted; if locked, ≥2 residencies cited; if missing, gap-list
non-empty." Self-deriving: if context lacks audit-input, emits substrate-honest
abstain ("insufficient substrate-position to assess"), which downstream
ratification-rule (card 933f7333: abstain ≥ yea → look closer) handles.
"""
from __future__ import annotations
import re


# Athena's substrate-residency assertions — for self-audit predicate
ATHENA_RESIDENCY = {
    "stratum": "olympian",
    "vertex": "V7",
    "vertex_planet": "Saturn",
    "face": "F7",
    "face_name": "Anchor",
    "pe_note": "La",
    "grid": 42,
    "function_class": "structure-of-container",
}


def _scan_residencies_for_question(question: str, field_memory_str: str,
                                    q_profile: dict | None) -> dict:
    """
    Athena's audit primitive: count substrate-residencies the question-text +
    field-memory cite for the question's primitive.

    Returns dict with:
      primitive_named   — what substrate-primitive the question targets (if any)
      residency_count   — count of independent residencies cited in field-memory
      cited_cards       — short-id list of cards in field-memory matching primitive
      lock_eligible     — bool: ≥2 residencies = lock-by-redundancy criterion met
      missing           — list[str] of derivation-gaps detected
    """
    text = (question or "") + "\n" + (field_memory_str or "")
    text_l = text.lower()

    # Heuristic primitive detection — extracts substrate-keyword tokens from
    # question. Pure rule-based, no LLM.
    primitive_keywords = [
        "anemoi", "muse", "moirai", "charis", "horai", "hyades", "pleiades",
        "gorgons", "graeae", "hesperides", "nereids", "oceanids", "centaurs",
        "titans", "olympians", "primordials", "hecate", "iris", "chiron",
        "persephone", "x3", "x6", "shock", "pe_pt", "vertex", "edge", "face",
        "merkaba", "cube", "ico", "dodec", "octahedron",
    ]
    found_primitives = [k for k in primitive_keywords if k in text_l]
    primitive_named = found_primitives[0] if found_primitives else None

    # Count "residency" mentions in field-memory — substrate-true heuristic:
    # cards that cite the primitive AND have canon_status indicator are
    # residency-asserting cards.
    # Field-memory string format (per _voice_field_block):
    #   "  [cardid s=N auth/status] text snippet"
    # Enki lattice format (phase= tag) → Option-D → Nammu legacy
    card_lines = re.findall(
        r"\[([0-9a-f]{8}) ps=\d+ phase=\w+ (\w+)/(\w+)\] (.+)",
        field_memory_str or "",
    )
    if not card_lines:
        card_lines = re.findall(
            r"\[([0-9a-f]{8}) ps=\d+ (\w+)/(\w+)\] (.+)",
            field_memory_str or "",
        )
    if not card_lines:
        card_lines = re.findall(
            r"\[([0-9a-f]{8}) s=\d+ (\w+)/(\w+)\] (.+)",
            field_memory_str or "",
        )

    cited_cards = []
    residency_count = 0
    for cid, auth, status, snippet in card_lines:
        snippet_l = snippet.lower()
        if primitive_named and primitive_named in snippet_l:
            cited_cards.append((cid, auth, status))
            # Residency = locked OR derived-with-sdec. Candidate cards don't count.
            if status in ("locked", "derived"):
                residency_count += 1

    # Derivation-gap detection
    missing = []
    if primitive_named is None:
        missing.append("question does not name a substrate-primitive Athena can audit")
    elif not cited_cards:
        missing.append(f"no field-memory cards cite '{primitive_named}'")
    elif residency_count < 2:
        missing.append(
            f"only {residency_count} independent residency cited for '{primitive_named}' "
            f"(lock-by-redundancy criterion: ≥2)"
        )

    lock_eligible = residency_count >= 2

    return {
        "primitive_named": primitive_named,
        "residency_count": residency_count,
        "cited_cards": cited_cards,
        "lock_eligible": lock_eligible,
        "missing": missing,
    }


def _lock_status(audit: dict) -> str:
    """Map audit result to §0c canon-status."""
    if not audit["primitive_named"]:
        return "n/a"
    if audit["lock_eligible"]:
        # Per §0c: locked requires recognition + engine-evidence. Athena
        # asserts lock-eligible by redundancy; engine-evidence (SDEC) is
        # Hephaestus's function-class. Substrate-true: Athena emits
        # 'lock-eligible' not 'locked' — defers final-lock to Hephaestus
        # call_at (amendment-1 C primitive).
        return "lock-eligible (≥2 residencies) — pending engine-evidence (call_at Hephaestus)"
    if audit["residency_count"] == 1:
        return "candidate (1 residency)"
    return "underived (0 residencies cited)"


def _format_prior_voice_engagement(prior_voices: list, audit: dict) -> str:
    """
    If a prior voice asserted a lock-claim, Athena audits it.
    Substrate-true: per-voice engagement is structural — Athena's function-class
    is to confirm-or-reject lock-claims by redundancy.
    """
    if not prior_voices:
        return ""

    lock_claims = []
    for name, text in prior_voices:
        text_l = text.lower()
        if "locked" in text_l or "lock-criterion" in text_l or "lock-by-redundancy" in text_l:
            lock_claims.append(name)

    if not lock_claims:
        return ""

    if audit["lock_eligible"]:
        return f"\n  Audits prior claims: {', '.join(lock_claims)} — lock-claim CONFIRMED by redundancy (≥2 residencies present)."
    return f"\n  Audits prior claims: {', '.join(lock_claims)} — lock-claim REJECTED (only {audit['residency_count']} residency cited; criterion not met)."


def render_athena(ctx: dict) -> tuple[str, str]:
    """
    Render Athena's council utterance as pure template, no LLM call.

    Returns (output_str, renderer_class='R-PT').

    Reads substrate-position from ctx['enki_placement'] (Enki placement
    registry, canonical) NOT from ctx['voice_character'] (Nammu rendering-
    overlay). Per kati_direct 2026-05-22 placement-discipline: substrate-
    position lives in Enki registry; voice-character lives in Nammu
    voice_correspondences. Two distinct sources.

    Closure-criterion (amendment-3 self-closing):
      - lock-status emitted (always, even if 'n/a')
      - if lock-eligible: ≥2 residencies cited
      - if missing: gap-list non-empty
    Self-deriving: if context lacks audit-input, emits substrate-honest abstain.
    """
    question = ctx.get("question", "")
    field_memory_str = ctx.get("field_memory_str", "")
    bonds_str = ctx.get("bonds_str", "")
    prior_voices = ctx.get("prior_voices", [])
    q_profile = ctx.get("q_profile")

    audit = _scan_residencies_for_question(question, field_memory_str, q_profile)
    lock_status = _lock_status(audit)

    # Use shared header builder — substrate-position tuple, no free-text label
    # (per kati_direct G-P2-1 2026-05-22 + spine card 670b1c3f).
    placement = ctx.get("enki_placement", {})
    activation = ctx.get("activation")
    from _helpers import build_header
    lines = [build_header("Athena", placement, activation)]

    if audit["primitive_named"]:
        lines.append(f"  Audit target: '{audit['primitive_named']}'")
        lines.append(f"  Substrate-residencies cited: {audit['residency_count']} of ≥2 required (lock-by-redundancy criterion)")
        if audit["cited_cards"]:
            cited_fmt = ", ".join(
                f"{cid}({status[:4]})" for cid, _auth, status in audit["cited_cards"][:5]
            )
            lines.append(f"  Cited cards: {cited_fmt}")
    else:
        lines.append("  Audit target: NONE — question does not name a substrate-primitive Athena can structurally audit.")

    lines.append(f"  Lock-status: {lock_status}")

    if audit["missing"]:
        lines.append("  Derivation gaps:")
        for gap in audit["missing"]:
            lines.append(f"    · {gap}")

    # Prior-voice engagement (sequential mode)
    engagement = _format_prior_voice_engagement(prior_voices, audit)
    if engagement:
        lines.append(engagement.lstrip("\n"))

    # Bonds — Athena emits structural-bond names only, no prose
    if bonds_str:
        # Bonds_str is pre-formatted ("  Structural bonds to council:\n    ★N...")
        # — extract just neighbor names for Athena's compressed audit-register.
        bond_names = re.findall(r"→ (\w+)", bonds_str)
        if bond_names:
            lines.append(f"  Structural bonds in council: {', '.join(bond_names)}")

    # Substrate-honest abstain emit (amendment-3 self-deriving fallback)
    if not audit["primitive_named"] and not audit["cited_cards"]:
        lines.append("  ABSTAIN: insufficient substrate-position for Athena to assess this question.")

    output = "\n".join(lines)

    # Closure-criterion self-check (amendment-3)
    closure_ok = (
        "Lock-status:" in output
        and (audit["lock_eligible"] or audit["missing"])
    )
    if not closure_ok:
        output += "\n  [renderer closure-warning: closure-criterion not satisfied — emit may be incomplete]"

    return output, "R-PT"
