#!/usr/bin/env python3
"""
probe_octave_comma_magnitude.py — OQ-OCTAVE-COMMA-MAGNITUDE (Thalia sub-question,
inline council OQ-OCTAVE-NONCLOSURE-UNIFICATION 2026-06-20).

Tests whether the three non-closure instances share ONE generator (49-star gap →
fifth-shift → drift), or only co-sign the same qualitative class. Discipline:
OQ-RINGS-06-PRECISION — a numerical lock needs ONE rigorous chain; substrate-forced
counts ≠ observation-calibrated (orbital) counts.
"""
from fractions import Fraction
from math import log2, gcd

CENTS = lambda ratio: 1200.0 * log2(ratio)
print("OQ-OCTAVE-COMMA-MAGNITUDE — does the 49-star gap GENERATE the other two?\n")

# ── (1) 49-star one-ray gap — SUBSTRATE-FORCED (pure 49-geometry) ────────────
# 7 self-resonance diagonals at matrix_pos = row×8 (0,8,16,24,32,40,48) span 0..48
# of 49 positions. Loop closes one ray short. Gap = 1/49 of the cycle.
diag = [r*8 for r in range(7)]
span = diag[-1] - diag[0]                 # 48
gap_rays = 49 - span                      # 1
gap_frac = Fraction(gap_rays, 49)
gap_deg = 360.0 * gap_rays / 49
gap_cents = 1200.0 * gap_rays / 49        # if one 49-cycle = one octave
print(f"(1) 49-STAR GAP   [substrate-forced]")
print(f"    diagonals {diag}  span {span}/49  gap = {gap_frac} = {gap_deg:.3f}° = {gap_cents:.2f} cents")
print(f"    Pythagorean comma (ref) = {CENTS((3/2)**12 / 2**7):.2f} cents  →  gap is {gap_cents/23.46:.3f}× the comma\n")

# ── (2) Cronus drift — SUBSTRATE-FORCED (gcd(5,6)=1 beat, §27i LOCKED) ───────
drift = [0,-1,-2,3,2,1]
half = sum(drift)                         # +3 per half (30 grids)
full = 2*half                             # +6 per full (60 grids) — §27h LOCKED non-conservative
drift_frac = Fraction(full, 60)
print(f"(2) CRONUS DRIFT  [substrate-forced, §27h LOCKED]")
print(f"    {drift}  sum/half = +{half}  sum/full = +{full}  net-forward frac = {drift_frac} of 60-grid")
print(f"    origin: gcd(5,6)=1, LCM=30  (zodiac 5-step vs PE 6-step beat)\n")

# ── (3) Neptune:Pluto fifth-shift — EMPIRICAL (orbital, §28c correspondence) ─
nep, plu = 59400, 89280                   # canon §23b ring periods (tithis)
ratio = plu / nep
print(f"(3) NEP:PLU FIFTH [EMPIRICAL — orbital, §28c, NOT substrate-forced]")
print(f"    Pluto/Neptune = {plu}/{nep} = {ratio:.4f}  vs 3:2 = 1.5000  (gap {abs(ratio-1.5)/1.5*100:.2f}%)")
print(f"    fifth = {CENTS(3/2):.1f} cents; octave-shortfall (4:3) = {CENTS(4/3):.1f} cents\n")

# ── GENERATION TESTS ─────────────────────────────────────────────────────────
print("GENERATION TESTS (does one chain force the others?):")
# (a) 49-gap vs drift: both are coprime-incommensurability. Common generator?
print(f"  a) 49-gap (1/49) vs drift (6/60=1/10): 49 & 60 coprime; 1/49 ≠ 1/10 ·k for integer k.")
print(f"     49-gap cents {gap_cents:.2f} / drift-as-cents (6/60·1200={6/60*1200:.0f}) = {gap_cents/(6/60*1200):.4f}  → no integer/simple ratio")
# (b) 49-gap → fifth?
print(f"  b) 49-gap {gap_cents:.2f}c vs fifth {CENTS(3/2):.1f}c: ratio {CENTS(3/2)/gap_cents:.2f} → not an integer; fifth is ORBITAL/empirical tier")
# (c) tier check — the decisive one
print(f"  c) TIER: (1) & (2) substrate-FORCED (49=7² geometry; 5/6 coprime beat).")
print(f"           (3) observation-CALIBRATED (orbital period). Per OQ-RINGS-06-PRECISION,")
print(f"           a substrate count cannot GENERATE an empirical one — different tiers.")
print()
print("VERDICT: single-generator across all three = REFUTED (the fifth is empirical-tier).")
print("         (1) 49-star gap and (2) Cronus drift share a QUALITATIVE generator —")
print("         coprime-incommensurability (a cycle whose sub-periods don't divide evenly) —")
print("         but NOT a numerical one (1/49 vs 1/10, different coprime pairs 49|60 vs 5|6).")
print("         (3) fifth-shift = §0 astrology-validator correspondence (§28c), not generated.")
print()
print("So: CLASS holds (council's finding) at 2 substrate residencies + 1 empirical co-sign;")
print("    numerical comma-IDENTITY stays REFUTED. Thalia sub-question answered: co-sign, not generate.")
