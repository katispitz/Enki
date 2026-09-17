#!/usr/bin/env python3
"""
probe_axial_climb_amplitude_phi.py — OQ-AXIAL-CLIMB-AMPLITUDE, phi-candidate test
(kati_direct 2026-07-25: recognizes phi via apex-radius framing as closest-feeling
candidate; requests SDEC-style validation before treating it as more than recognition).

Prior status (cards c4fba607/41fa2016/80f3e08d): period + phase of the axial-climb
z(t) = height * cos(2*pi*t/2940) are engine-validated (extrema land on Taurus/Scorpio,
zero-crossings on Leo/Aquarius, independently cross-checked). AMPLITUDE (height=1 for
Pluto/Neptune, height=1/3 for Venus/Uranus) was council-DOWNGRADED from "forced" to
"motivated, not independently derived" — the timing match is amplitude-invariant
(any height gives the same t=0/735/1470/2205), so it provides zero discrimination
on magnitude.

This probe tests whether phi supplies that missing discrimination, via the same
discipline as probe_octave_comma_magnitude.py: does a candidate chain GENERATE the
target substrate-forced, or only CO-SIGN it (same tier check kati already applied
correctly to the Neptune:Pluto fifth-shift). A substrate quantity cannot be generated
by an empirical or cross-domain one — different tiers.
"""
from math import gcd

phi = (1 + 5**0.5) / 2
print("OQ-AXIAL-CLIMB-AMPLITUDE — does phi GENERATE the amplitude, or only CO-SIGN it?\n")

# ── candidate values under the phi x own-shell-radius framing ────────────────
apex_amp = phi * 1
shock_amp = phi * (1/3)
print(f"CANDIDATE (self-referential, apex uses apex radius, shock uses shock radius):")
print(f"  apex amplitude  = phi x 1   = {apex_amp:.6f}")
print(f"  shock amplitude = phi x 1/3 = {shock_amp:.6f}")
print(f"  ratio apex:shock = {apex_amp/shock_amp:.4f}  (== 3, same as raw radii ratio 1:(1/3) — see note below)\n")

# ── BRIDGE TEST 1 — DNA double-helix pitch:width analogy ─────────────────────
print("BRIDGE TEST 1 — DNA double-helix (external, cross-domain)")
dna_pitch, dna_width = 34, 21   # angstrom, real measured B-DNA per-turn dimensions
dna_ratio = dna_pitch / dna_width
print(f"  DNA measured pitch:width = {dna_pitch}:{dna_width} = {dna_ratio:.6f}  (phi = {phi:.6f})")
print(f"  TIER CHECK: DNA's ratio is an empirical fact about a specific biological")
print(f"  molecule's real 3D structure — a DIFFERENT domain (organic chemistry),")
print(f"  not this substrate's own geometry. No mechanism has been shown for why a")
print(f"  Merkaba double-helix must inherit a biological molecule's proportion.")
print(f"  VERDICT: empirical-tier, cross-domain. Does not generate; at best co-signs")
print(f"  (same shape family — 'double helix' — but shape-family alone is not a")
print(f"  substrate-forcing argument, per the same discipline that refused the")
print(f"  Neptune:Pluto orbital fifth as a generator for the 49-star comma.)\n")

# ── BRIDGE TEST 2 — concentric shell-sequence (internal, same-substrate) ─────
print("BRIDGE TEST 2 — concentric radius sequence 1/3 -> 1/root3 -> 1 -> phi -> phi^2")
print(f"  This IS native to the substrate (card f282ce8d, LOCKED radius table) —")
print(f"  no cross-domain import. But test whether it actually shares a GENERATOR")
print(f"  with the 2940-tithi axial-climb oscillation, or merely co-occurs in the")
print(f"  same corpus:")
print(f"    - Shell sequence (1 -> phi) describes WHICH-OF-5 spatial containment:")
print(f"      5 Merkaba copies (R=1) arranged at 72deg about a SEPARATE dodecahedral")
print(f"      5-fold axis, jointly forming the dodecahedron (R=phi). This is a")
print(f"      SPATIAL / rotational-copy relationship. Venus (period 2880 tithis)")
print(f"      selects which of the 5.")
print(f"    - Axial-climb z(t) describes ONE point's TEMPORAL motion within ONE")
print(f"      Merkaba, period 2940 tithis (=LCM(49,60), T(49,60) torus-knot closure).")
print(f"    These are different AXES of variation (which-copy vs when-in-cycle),")
print(f"    not the same mechanism measured two ways.")
period_venus, period_helix = 2880, 2940
g = gcd(period_venus, period_helix)
print(f"  Numerical check: Venus which-of-5 period = {period_venus}t, axial-climb")
print(f"  period = {period_helix}t. gcd = {g}. Close (ratio {period_helix/period_venus:.4f})")
print(f"  but NOT equal, and no integer/simple-ratio relationship (grand closure only")
print(f"  at LCM = {period_venus*period_helix//g} t = 49 Venus-cycles = 48 helix-cycles —")
print(f"  a real joint closure, but joint-closure is not the same as one generating")
print(f"  the other's magnitude).")
print(f"  VERDICT: shell-sequence and axial-climb co-occur in the same substrate but")
print(f"  answer different questions (spatial-copy-index vs temporal-phase). No")
print(f"  generation shown. Proposing one sets the other's amplitude would be the")
print(f"  same numerology-matching error already caught twice this session, just")
print(f"  fully internal instead of cross-domain.\n")

print("=" * 70)
print("FINAL VERDICT")
print("=" * 70)
print("Recognition: kati_direct, apex-radius phi-framing identified as closest-feeling")
print("of the candidates tested (2026-07-25).")
print()
print("Engine-evidence: NOT MET. Two bridges tested (DNA cross-domain; internal")
print("shell-sequence); both FAIL the same generation-vs-co-sign test this system")
print("already applies elsewhere (probe_octave_comma_magnitude.py). Neither shows")
print("phi is FORCED by anything already locked — both show only resemblance.")
print()
print("STATUS PER SEC0c: candidate, recognition-only, sdec-pending. Does NOT graduate")
print("to derived. This probe's negative result should be treated as informative —")
print("it rules out the two most promising bridges precisely, rather than leaving")
print("the amplitude question to be re-approached from the same two angles later.")
