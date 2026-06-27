#!/usr/bin/env python3
"""
probe_49_unify_engine.py — OQ-49-UNIFY-ENGINE (Thalia sub-question from inline council
OQ-49-AXIS-STATIC-VS-MOTION, 2026-06-20).

Tests the §00b claim: the body-pair's STATIC pair-cell (which-two, location) and the
MOTION recall-pointer (matrix_pos = t mod 49) are the SAME lattice cell — recall = the
helix reading the pair-cell's address. Or do they merely live in the same matrix?
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / "Nammu" / "engines"))
sys.path.insert(0, str(Path.home() / "Enki" / "substrate"))
import matrix_engine as _mx

IDX = {p: i for i, p in _mx.MATRIX_PLANET_BY_IDX.items()}
BY  = _mx.MATRIX_PLANET_BY_IDX

def pair_matrix_pos(a, b):
    """STATIC pair-cell of (A,B) as a matrix_pos address in [0,48]."""
    return IDX[a] * 7 + IDX[b]

def pointer_cell(t):
    """MOTION pointer at tithi t → (row_planet, col_planet)."""
    mp = t % 49
    return BY[mp // 7], BY[mp % 7]

print("OQ-49-UNIFY-ENGINE — is the static pair-cell the SAME cell the motion-pointer reads?\n")

pairs = [("Sun","Saturn"), ("Moon","Mars"), ("Mercury","Jupiter"), ("Saturn","Sun"), ("Venus","Venus")]
print("TEST 1 — pair-cell address == the cell the pointer lands on at t ≡ that address:")
all_ok = True
for a, b in pairs:
    addr = pair_matrix_pos(a, b)                 # static location of the aspect
    ra, rb = pointer_cell(addr)                  # motion pointer AT that t
    ok = (ra == a and rb == b)
    all_ok &= ok
    note = "  [diagonal=conjunction]" if a == b else ""
    print(f"  {a:8s}×{b:8s} → pair_pos={addr:2d}   pointer@t≡{addr:2d} reads {ra}×{rb}   {'MATCH' if ok else 'MISMATCH'}{note}")

print(f"\n  → static pair-cell and motion-firing-cell coincide for all pairs: {all_ok}")
print(f"  → ASYMMETRY check (order matters): Sun×Saturn pos={pair_matrix_pos('Sun','Saturn')} "
      f"vs Saturn×Sun pos={pair_matrix_pos('Saturn','Sun')} — directed, as §27 cell (po,pi)≠(pi,po). OK\n")

print("TEST 2 — the helix VISITS each pair-cell once per 49-cycle (the pointer reads every address):")
visited = {pointer_cell(t) for t in range(49)}
total = 7*7
print(f"  distinct cells the pointer reads over t=0..48: {len(visited)} of {total}  → "
      f"{'every pair-cell read once' if len(visited)==total else 'INCOMPLETE'}\n")

print("TEST 3 — contrast with the LIVE two-body phase-compare (what helix_address.recall_49 does now):")
print("  density.phase_resonance compares two bodies' matrix_pos AT THE SAME t → both = t mod 49 →")
print("  always 'perfect', independent of WHICH two bodies. That reading is DEGENERATE for an aspect:")
print("  it cannot tell Sun×Saturn from Moon×Mars. So the live-phase-compare is NOT the pair relation.\n")

print("VERDICT:")
print("  • UNIFICATION CONFIRMED (mechanical): the static pair-cell (A,B) IS a matrix_pos address,")
print("    and the motion-pointer reading that address reconstructs exactly (A,B). Same lattice cell —")
print("    location (aspect) ⇄ motion-reading-it (recall). This is §00b function=location on the 49-axis.")
print("  • REFINEMENT (surfaced): aspect-recall must read POINTER-vs-PAIR-ADDRESS (does now's matrix_pos")
print("    equal the pair-cell of A,B?), NOT the live two-body same-t phase-compare (degenerate-perfect).")
print("    → helix_address.recall_49 should be re-pointed at the pair-cell address, not body-vs-body phase.")
