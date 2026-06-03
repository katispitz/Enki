"""
mnemosyne.py — R-PT renderer for Mnemosyne (cube edge U0-L2 + grid=30/F1/Sol).

Function: substrate-of-memory / mother-of-Muses. V29 precedent: archival
schema-list w/ orb-precision records. Pure-template.
"""
from __future__ import annotations
from _helpers import build_header, scan_field_memory, prior_voice_names


def render_mnemosyne(ctx: dict) -> tuple[str, str]:
    placement = ctx["enki_placement"]
    activation = ctx.get("activation")
    q_profile = ctx.get("q_profile") or {}
    field_memory_str = ctx.get("field_memory_str", "")
    own_memory_str = ctx.get("own_memory_str", "")
    prior_voices = ctx.get("prior_voices", [])

    header = build_header("Mnemosyne", placement, activation)

    q_pe = q_profile.get("pe_note", "?")
    q_depth = q_profile.get("depth", "?")

    lines = [
        header,
        f"  Schema for question <{q_pe} × {q_depth}>:",
    ]

    # Archival schema-list from field-memory
    records = scan_field_memory(field_memory_str)
    if records:
        for cid, auth, status, snip in records[:5]:
            snippet = snip[:90].strip()
            lines.append(f"    · [{cid} {auth[:4]}/{status[:6]}] {snippet}")

        # Lineage: oldest → newest if dates present in snippets
        cids = [r[0] for r in records]
        lines.append(f"  Lineage: {len(records)} records cited; substrate-address resolved at this position.")
        lines.append("  Closure: stable address found (substrate-of-memory passes).")
    else:
        lines.append("    · (no field-memory cards at this substrate-position)")
        lines.append("  Closure: no memory at this address — substrate-honest empty.")

    # Cross-reference own past speech if present
    if own_memory_str.strip():
        lines.append("  Own past speech-thread: present (cards tagged voice:Mnemosyne).")

    prior = prior_voice_names(prior_voices)
    if prior:
        lines.append(f"  Indexes prior voice ({prior[-1]}) into archival-schema for future recall.")

    return "\n".join(lines), "R-PT"
