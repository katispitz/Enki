"""
test_memory_writeback.py — verify substrate-true council write-back closes the
memory loop. Run small council, commit voice-cards, verify they land in cards.json
at correct substrate-positions for future field_memory recall.
"""
from __future__ import annotations
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "per_voice_renderers"))
sys.path.insert(0, str(Path.home() / "Nammu" / "cards"))

from composer import derive_council_context, iterate_voices


CARDS_PATH = Path.home() / "Nammu" / "cards" / "cards.json"


def count_enki_cards():
    cards = json.loads(CARDS_PATH.read_text())
    return sum(1 for c in cards if "substrate-true-council" in (c.get("tags") or []))


def main():
    print("=" * 78)
    print("SUBSTRATE-TRUE COUNCIL WRITE-BACK TEST")
    print("=" * 78)

    before = count_enki_cards()
    print(f"Enki-council cards in cards.json BEFORE: {before}")
    print()

    # Run 3-voice mini-council (all CONTINUOUS, so all render)
    ctx = derive_council_context(
        question="Test substrate-memory write-back closes the loop.",
        natal_date="1988-03-31", natal_time="15:21",
        birth_lat=33.7879, birth_lon=-117.8531,
        convened=["Athena", "Hermes", "Mnemosyne"],
    )

    results = iterate_voices(ctx, ["Athena", "Hermes", "Mnemosyne"],
                             mode="sequential", commit=True)

    print("Results:")
    for r in results:
        cid = r["card_id"][:8] if r["card_id"] else "(not written)"
        print(f"  {r['name']:12s}  class={r['class_']:6s}  card_id={cid}")
    print()

    after = count_enki_cards()
    print(f"Enki-council cards in cards.json AFTER: {after}")
    print(f"Added: {after - before}")

    # Verify cards landed at substrate-positions
    print()
    print("Verifying substrate-positions written:")
    cards = json.loads(CARDS_PATH.read_text())
    for r in results:
        if not r["card_id"]:
            continue
        for c in cards:
            if c["id"] == r["card_id"]:
                pos_fields = {k: c.get(k) for k in
                              ("stratum", "pe_note", "grid", "face",
                               "oct_vertex", "merkaba_vertex", "cube_edge")                              if c.get(k) is not None}
                tags = [t for t in (c.get("tags") or [])
                        if t.startswith("voice:") or t.startswith("session:")
                        or t.startswith("renderer:") or t == "substrate-true-council"]
                print(f"  {r['name']:12s} [{c['id'][:8]}] pos={pos_fields}  tags={tags}")
                break


if __name__ == "__main__":
    main()
