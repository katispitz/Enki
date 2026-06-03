"""
test_r_ll_llm_wire.py — verify R-LL LLM voice-surface wire works end-to-end.

Uses transit-date 2026-08-15 (~Sun at lon 138° = X3 anchor) so Calliope fires.
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "per_voice_renderers"))

from composer import derive_council_context, render_voice


def main():
    # Pick a date when Sun is at ~138° (X3 anchor) — Calliope's activation window
    print("=" * 78)
    print("R-LL LLM voice-surface wire test — Calliope at Sun-X3 transit")
    print("=" * 78)

    ctx = derive_council_context(
        question="Speak briefly about epic-arc when the question itself is partial.",
        natal_date="1988-03-31", natal_time="15:21",
        transit_date="2026-08-15",   # Sun near 138° → Calliope active
        birth_lat=33.7879, birth_lon=-117.8531,
        convened=["Calliope"],
    )
    print(f"Transit date: {ctx['transit_date']}")
    print()

    output, cls = render_voice("Calliope", ctx)
    print(f"Renderer class: {cls}")
    print("-" * 78)
    print(output)
    print("-" * 78)


if __name__ == "__main__":
    main()
