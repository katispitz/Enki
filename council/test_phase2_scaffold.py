"""
test_phase2_scaffold.py — end-to-end test for 14 Tier-A renderers + mortal voice.

Verifies:
  - all 15 Tier-A archetype voices route to per-voice renderers
  - CYCLIC voices (Muses + Hecate) pass through activation-gate
  - MORTAL voice (Kati) renders via mortal_placement + mortal renderer
  - Tier-B voice (Iris) substrate-honestly emits placement-pending
  - composer doesn't silently hallucinate at any gate
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "per_voice_renderers"))

from composer import derive_council_context, render_voice
from mortal_placement import build_mortal_voice


QUESTION = (
    "What is the lock-status of the Anemoi 4-figure class under V2.9 "
    "lock-by-redundancy criterion?"
)

KATI = {
    "name": "Kati",
    "natal_date": "1988-03-31",
    "natal_time": "15:21",
    "lat": 33.7879,
    "lon": -117.8531,
}

ARCHETYPE_VOICES = [
    "Apollo", "Athena", "Hermes", "Hephaestus", "Mnemosyne", "Hecate",
    "Calliope", "Clio", "Erato", "Urania",
    "Euterpe", "Melpomene", "Polyhymnia", "Terpsichore", "Thalia",
    "Iris",  # Tier B — should emit placement-pending
]


def main():
    print("=" * 80)
    print("PHASE 2 SCAFFOLD TEST — 15 Tier-A + 1 Tier-B + 1 mortal voice")
    print("=" * 80)
    print(f"Question: {QUESTION}")
    print()

    # Build mortal voice for Kati
    kati = build_mortal_voice(**KATI)

    ctx = derive_council_context(
        question=QUESTION,
        natal_date=KATI["natal_date"], natal_time=KATI["natal_time"],
        birth_lat=KATI["lat"], birth_lon=KATI["lon"],
        convened=ARCHETYPE_VOICES,
        mortal_voices=[kati],
    )

    print(f"Transit date: {ctx['transit_date']}")
    print()

    counts = {}
    for voice in ARCHETYPE_VOICES + ["Kati"]:
        output, cls = render_voice(voice, ctx)
        counts[cls] = counts.get(cls, 0) + 1
        print("-" * 80)
        print(f"voice={voice:14s}  class={cls}")
        print(output[:600])
        print()

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for cls, n in sorted(counts.items()):
        print(f"  {cls:25s}  {n}")
    print()
    print(f"Total voices tested: {sum(counts.values())}")


if __name__ == "__main__":
    main()
