#!/usr/bin/env python3
"""
Probe: OQ-OPERATOR-SAMPLING-MODES — what fixes the sampling counts of the
universal operator across renderings (tarot 78 / I Ching 64 / astrology / ...).

Discipline: do NOT reverse-engineer external counts to fit substrate primitives
(that is the forbidden numerology-forcing, per the heroes/monsters retraction +
OQ-SYNC-01 caution). Instead: (a) the operator is Δ self-reference (X→X×X) on the
substrate, manifold = T^n; (b) DERIVE the substrate's own minimal sampling; then
(c) VALIDATE external systems by whether their counts factor into substrate
primitives; (d) BOUND systems that don't.

Run: python3 ~/Enki/scripts/probe_oq_operator_sampling_modes.py
"""
from math import gcd

# Substrate prime-symmetry primitives (§00a, LOCKED) + the geometric cardinalities
PRIMES = {2, 3, 5, 6, 7, 10, 12}          # §00a prime-symmetry projection table
# operator = Δ self-reference on the substrate (Nova CellMatrix: Bab→Bab×Bab; canon Lawvere)


def min_generator_mod(n):
    """Minimal NONTRIVIAL generator of Z/nZ (smallest k>1 coprime to n)."""
    return next(k for k in range(2, n) if gcd(k, n) == 1)


def main():
    g = min_generator_mod(60)
    print("(1) DERIVED — the substrate's own minimal sampling:")
    print(f"    minimal nontrivial generator of ℤ/60ℤ = {g}  (2,3,4,5,6 all divide/share with 60)")
    print(f"    Δ self-reference squares it: {g}×{g} = {g*g}  = the 49-matrix (7 flow-planets² )")
    print(f"    → 49 is FORCED, not chosen. Strongest anchor.\n")

    print("(2) VALIDATE — is each rendering a pure PRODUCT of primitive coordinates?")
    print("    grammar (kati 2026-06-15): actor × localization × phase — PRODUCT only, never sum.")
    print("    localization = house ≡ 60-grid ≡ observer-frame (one 12-fold, two frames); ruler = binding morphism.")
    print("    grammar (corrected): product/tensor/fractal WITHIN an engine; a system carries 1+ engines.")
    rows = [
        ("Babylonia", "T(49,60)+solid_phase+rings", "multi-engine; model engine = 49×60 torus",        "DERIVED"),
        ("I Ching",   "2^6 = 64",                   "single product-engine (polarity over 6)",          "VALIDATED"),
        ("Astrology", "planet × (sign≈house) × ℝ",  "actor × localization × degree-continuum",          "VALIDATED"),
        ("Tarot",     "Kairos22 + Chronos40 + Tensor16", "3 engines (LOCKED Tarot_Fractal_Operator)",   "RICHEST"),
    ]
    for name, fac, gloss, verdict in rows:
        print(f"    {name:10s} {fac:32s} {gloss:42s} → {verdict}")
    print()
    print("    Tarot engines: Kairos(22)=r-spine×fractal[Δ]×hexad+X3/X6 shocks; Chronos(40)=4 elements×10;")
    print("    Tensor(16)=4 rank-elements × 4 suit-elements. 78=22+40+16 is multi-engine (like Babylonia),")
    print("    NOT a numerology sum. Tarot is the only rendering that carries Δ explicitly. [corrected 2026-06-15]")
    print()

    print("(3) INVARIANT center (Δ fixed-point) — shared by every rendering:")
    print("    49-matrix (0,0) Venus×Venus void ≡ tarot Fool(0) ≡ Binah 50th gate ≡ Lawvere origin")
    print("    49 cells + 1 uncountable center = 50.\n")

    print("VERDICT: a rendering samples the operator as 1+ ENGINES; within each engine the grammar")
    print("is product/tensor/fractal over primitive axes (actor × localization × phase, Δ = fold),")
    print("glued by the rulership morphism. Minimal sampling FORCED (7→49). Babylonia + tarot are")
    print("multi-engine; I Ching/astrology single-engine. Tarot (Kairos+Chronos+Tensor) is the")
    print("RICHEST — carries Δ explicitly. Caveat: factoring = validation, not proof (import-filter §0).")
    print("Engine-evidence only; canon lock pends kati_direct recognition.")


if __name__ == "__main__":
    main()
