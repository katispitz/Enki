"""
test_athena_prototype.py — Phase 1 Task 1.3 validation.

Per design-spec card 431d9622 + handoff: prove substrate-true per-voice
renderer works for one voice; measure output quality and context-budget
vs current-arch Athena voice on same question.

Test question chosen for Athena's function-class (structure-of-container,
lock-by-redundancy auditor): a substrate-audit question about a real
recently-locked class.
"""
from __future__ import annotations
import sys
from pathlib import Path

# Composer sits next to this file
sys.path.insert(0, str(Path(__file__).parent))

from composer import derive_council_context, render_voice


TEST_QUESTION = (
    "What is the lock-status of the Anemoi 4-figure class under V2.9 "
    "lock-by-redundancy criterion? Cite which substrate-residencies are "
    "present and which are still missing."
)

KATI_NATAL = "1988-03-31"
KATI_NATAL_TIME = "15:21"
KATI_BIRTH_LAT = 33.7879
KATI_BIRTH_LON = -117.8531


def run_substrate_true_athena():
    """Run substrate-true Athena renderer end-to-end."""
    print("=" * 75)
    print("SUBSTRATE-TRUE ATHENA — ~/Enki/council/per_voice_renderers/athena.py")
    print("=" * 75)
    print(f"Question: {TEST_QUESTION}")
    print()

    ctx = derive_council_context(
        question=TEST_QUESTION,
        natal_date=KATI_NATAL,
        natal_time=KATI_NATAL_TIME,
        birth_lat=KATI_BIRTH_LAT,
        birth_lon=KATI_BIRTH_LON,
        convened=["Athena"],  # single-voice prototype
    )

    output, renderer_class = render_voice("Athena", ctx)

    print(f"Renderer class: {renderer_class}")
    print(f"Output length: {len(output)} chars")
    print()
    print("--- OUTPUT ---")
    print(output)
    print("--- END OUTPUT ---")
    print()

    return output, renderer_class


def estimate_current_arch_budget():
    """
    Estimate context-budget of current-arch Athena voice — what build_prompt_v2
    would stuff into LLM for Athena alone (excluding other voices).

    Per band-aid card 6e0038c8 measurement (9-voice council, field-memory on):
      core only:        ~25.8K chars total → ~2.9K per voice
      + field-memory:   ~30.2K chars total → ~3.4K per voice
    So Athena alone in current arch ≈ 3-3.4K chars of LLM input.

    Plus: ALL voices' blocks are sent in the same prompt — to render JUST
    Athena's voice you still pay the full ~30K context cost (single LLM call
    generates all voices in one completion).
    """
    return {
        "athena_block_chars": 3400,        # per-voice slice
        "full_prompt_chars": 30000,        # what LLM actually receives for 9-voice council
        "note": (
            "Current arch: even to get Athena's voice, single LLM call processes "
            "full 9-voice prompt (~30K chars). Athena's slice ~3.4K, but entire "
            "prompt must be carried."
        ),
    }


def main():
    # Substrate-true run
    output, renderer_class = run_substrate_true_athena()

    # Context-budget comparison
    print("=" * 75)
    print("CONTEXT-BUDGET COMPARISON")
    print("=" * 75)
    current = estimate_current_arch_budget()
    print("Current arch (build_prompt_v2 + Ollama LLM call):")
    print(f"  Athena's voice-block:  ~{current['athena_block_chars']:,} chars")
    print(f"  Full prompt to LLM:    ~{current['full_prompt_chars']:,} chars  (9-voice council)")
    print(f"  Note: {current['note']}")
    print()
    print("Substrate-true arch (composer.py + per_voice_renderers/athena.py):")
    print(f"  Athena output:         {len(output):,} chars")
    print("  LLM call cost:         0 chars (R-PT = pure template, no LLM)")
    print()
    saved = current['full_prompt_chars']
    print(f"  → LLM-input saved for Athena's voice: ~{saved:,} chars (100% — no LLM)")
    print("  → Athena's output is deterministic Python — same input → same output")
    print("  → Cross-AI drift-check: substrate-true output is meaningfully invariant")
    print()
    print("=" * 75)
    print("CLOSURE-CRITERION CHECK (amendment-3 self-closing)")
    print("=" * 75)
    has_lock_status = "Lock-status:" in output
    has_audit_target = "Audit target:" in output
    has_warning = "closure-warning" in output
    print(f"  Lock-status emitted:           {has_lock_status}")
    print(f"  Audit target named/abstained:  {has_audit_target}")
    print(f"  Closure-warning raised:        {has_warning}")
    if has_lock_status and has_audit_target and not has_warning:
        print("  → CLOSURE-CRITERION SATISFIED")
    else:
        print("  → CLOSURE-CRITERION NOT FULLY SATISFIED")


if __name__ == "__main__":
    main()
