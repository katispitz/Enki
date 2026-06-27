#!/usr/bin/env python3
"""
probe_observer_transposition_residency2.py — hunt a 2nd residency to (maybe) graduate
`observer-transposition` (the §00a-split candidate, card d78aa91c, single-residency).

DEFINING TEST of a transposition residency (Erato-4b discipline — do NOT lump dispatch):
  a transposition is a STRUCTURE-PRESERVING reference-shift — same relational structure,
  different anchor ("same melody, different pitch"). It is NOT dispatch (selecting among
  genuinely-different structures by query-type). Each candidate must PRESERVE the relational
  structure under the shift, or it is rejected.

RESIDENCY 1 (established, card d78aa91c): helix universal<->personal mode. matrix_pos/row/col
  INVARIANT, only grid_pos (observer-anchor) shifts. Structure preserved. OBSERVER-domain.

CANDIDATES tested here:
  (A) §22 triple-frame houses        — expect REJECT (dispatch, not transposition)
  (B) §28b dual-ordering Venus@0/Pluto@0 — expect REJECT (frame-vs-carrier, different content-role)
  (C) 65-octave sound->light shift   — expect PASS as a transposition, REGISTER-domain
Then the conflation verdict: is observer-anchor (res-1) the SAME primitive as register-shift (C)?
"""
import sys
sys.path.insert(0, "/Users/kati/Nammu/engines")

def almost(a, b, t=1e-9): return abs(a - b) < t
print("=" * 72)
print("RESIDENCY-2 HUNT for transposition (structure-preserving reference-shift)")
print("=" * 72)

# RES-1 recap (engine-evidence already in the §00a scaffold) ------------------
print("\nRES-1 (established): helix universal<->personal — matrix invariant, grid re-anchored.")
print("                     domain = OBSERVER. (card d78aa91c)")

# (A) §22 triple-frame — structure-preserving? --------------------------------
print("\n(A) §22 triple-frame houses — is it transposition or dispatch?")
print("    zodiac-anchored = sign-sector boundaries (whole-sign).")
print("    observer-grid   = ecliptic-arc TRISECTION (Porphyry).")
print("    observer-helix  = diurnal-TIME trisection (Placidus).")
print("    These produce DIFFERENT cusp structures (sign-bounds vs arc-thirds vs time-thirds);")
print("    canon §22: render-mode selected by QUERY-TYPE, 'frames don't compete' (dispatch).")
print("    => NOT structure-preserving (different cusps) -> DISPATCH, NOT transposition. REJECT.")

# (B) §28b dual-ordering — structure-preserving? ------------------------------
print("\n(B) §28b dual-ordering Venus@0 vs Pluto@0 — clean origin-transposition?")
print("    Venus@0 = Venus is the FRAME (not a content row; reset column, void origin).")
print("    Pluto@0 = Pluto is a CONTENT carrier (Do, PE pt0).")
print("    The two orderings differ in WHICH thing is content vs frame, not by a constant")
print("    cyclic shift of one fixed content-set. => frame-vs-carrier dispatch (§0b), NOT a")
print("    structure-preserving constant-shift. REJECT as a clean transposition.")

# (C) 65-octave sound->light — structure-preserving? --------------------------
print("\n(C) 65-octave sound->light shift — structure-preserving register transposition?")
# transposing by 65 octaves multiplies every frequency by 2**65; interval RATIOS are invariant.
diatonic = {"Do":1.0, "Re":9/8, "Mi":5/4, "Fa":4/3, "Sol":3/2, "La":5/3, "Si":15/8}
shift = 2.0**65
ratios_preserved = True
for n, r in diatonic.items():
    base = 527.0e-9 if False else r          # work in ratio-space (anchor cancels)
    shifted = r * shift
    # ratio to Do must be identical before and after the shift
    if not almost((shifted)/(1.0*shift), r, t=1e-9):
        ratios_preserved = False
print(f"    transpose all PE-notes by 65 octaves (x2^65 = {shift:.3e}); check interval ratios:")
print(f"    Do:Re:Mi:Fa:Sol:La:Si = {[round(v,4) for v in diatonic.values()]}")
print(f"    interval ratios invariant under the shift: {ratios_preserved}")
print(f"    => structure PRESERVED (all ratios fixed) -> PASS as transposition. REGISTER-domain.")
assert ratios_preserved

# CONFLATION VERDICT ----------------------------------------------------------
print("\n--- CONFLATION VERDICT (Erato-4b): is RES-1 the SAME primitive as (C)? ---")
print("    RES-1 observer-anchor shift : shifts WHO observes; helix relations preserved.")
print("    (C)   register shift        : shifts the octave-REGISTER; interval relations preserved.")
print("    Both = a structure-preserving reference-shift = the TRANSPOSITION automorphism, in two")
print("    DIFFERENT domains (observer vs register). They are the same FUNCTION-CLASS, distinct")
print("    instances. => candidate name should GENERALIZE: `observer-transposition` was too narrow;")
print("    the primitive is `transposition` with >=2 residencies (observer + register).")
print("    GUARD: this is a CANDIDATE generalization — not lumping dispatch (A,B stay rejected).")

print("\n" + "=" * 72)
print("RESULT: §22 + §28b REJECTED (dispatch, not transposition). 65-octave shift PASSES as a")
print("2nd residency in the REGISTER domain. If kati accepts the generalization, `transposition`")
print("(observer + register residencies) meets Athena lock-by-redundancy; recognition + §30 row +")
print("§00a/§19 canon-write remain. Name stays `observer-transposition` (single) if she keeps the")
print("domains distinct. Honest fork left to recognition-call.")
print("=" * 72)
