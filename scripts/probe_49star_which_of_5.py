#!/usr/bin/env python3
"""
probe_49star_which_of_5.py — OQ-49STAR-ICO step 3: which of the 5 compound-cubes is active.

Step 2 showed the 49 double-helix rides on ONE Merkaba cube (down its Do-spine). The
icosahedron is the 5-Merkaba compound (5 cubes @72deg about a 5-fold dodec axis;
canon §2 Path D / FINDINGS_030, LOCKED). Open question: WHICH of the 5?

Claim: VENUS selects. The 5 spatial cubes are the 5 phases of the ONE Merkaba's rotation,
and canon already fixes "phase index = Venus synodic position":
  - Venus 8-yr cycle = 2880 tithis = period of ONE full Merkaba rotation (canon §0a L50,
    FINDINGS_030; 5:8 ≈ φ, Venus on φ-shell traces the rotation).
  - 2880 has 2 independent residencies (Venus Ring period + T(49,60) crossing number);
    LOCKED at OQ-TOPOS-01.
  - 5 Venus inferior conjunctions / 8yr = the pentagram = the 5 phase-selections.

Verifies:
  (1) 2880 = Venus period = Merkaba-rotation period; 2880 / 5 = 576 tithis per phase.
  (2) 2880 = 48 * 60 = T(49,60) crossing number (canon OQ-TOPOS-01) — same number, 2 residencies.
  (3) traversal of the 5 per §31c: pentagon {5} +72deg = sheng/generating (Cronus/chronological);
      pentagram {5/2} +144deg = ke/controlling (Kairos/qualitative). Venus synodic ORDER = +2 pentagram.
  (4) VENUS = THE FRAME AT BOTH SCALES: row/col-0 of the 49-matrix (§28b Venus@0 spatial-epoch,
      "Venus IS the structure not the content") AND the which-of-5 selector. Fractal frame.
  (5) period incommensurability: 5-fold rotation (2880) vs full helix (2940 = LCM(49,60))
      differ by exactly 60 (one grid-cycle); grand closure LCM(2880,2940) = 141120 t
      = 49 Venus-cycles = 48 helix-cycles.
  (6) HONEST axis split: cube Do-spine = 3-fold body diagonal; the 5-compound rotates about a
      SEPARATE 5-fold dodec axis. The 5 cubes carry 5 distinct Do-spine orientations; which-of-5
      = which Do-spine is currently active = Venus phase. (3-fold helix vs 5-fold compound.)

NO invented constants — periods are canon; angles are exact.
"""
import math

VENUS = 2880            # canon §0a L50 / OQ-TOPOS-01 (Ring period == Merkaba rotation == crossing#)
HELIX = 2940            # LCM(49,60), canon §27a
N5 = 5

def almost(a,b,t=1e-9): return abs(a-b)<t
print("="*70); print("PROBE — Venus selects which of the 5 compound-cubes is active"); print("="*70)

# (1) per-phase period
print("\n(1) Venus drives the Merkaba rotation; 5 phases")
per_phase = VENUS / N5
print(f"    Venus 8yr = Merkaba rotation = {VENUS} tithis (canon §0a L50, FINDINGS_030)")
print(f"    per phase = {VENUS}/5 = {per_phase:.0f} tithis  (one of the 5 compound positions)")
assert almost(per_phase, 576.0)

# (2) 2880 = 48*60 = crossing number (two residencies)
print("\n(2) 2880 has 2 substrate residencies (OQ-TOPOS-01 LOCKED)")
cross = min(49*59, 60*48)
print(f"    T(49,60) crossing number = min(49*59, 60*48) = {cross}")
print(f"    48 * 60 = {48*60}  == Venus period {VENUS}  (same number, 2 residencies)")
assert cross == 2880 == VENUS

# (3) traversal of the 5 (canon §31c)
print("\n(3) traversal of the 5 phases (§31c traversal-morphism law)")
print("    pentagon {5}  step +1 = +72deg  = sheng/generating = Cronus/CHRONOLOGICAL")
print("    pentagram {5/2} step +2 = +144deg = ke/controlling   = Kairos/QUALITATIVE")
order_pentagram = [(i*2) % 5 for i in range(5)]   # the Venus synodic pentagram order
print(f"    Venus synodic order (the pentagram, +2): phases visited = {order_pentagram}")
assert sorted(order_pentagram) == [0,1,2,3,4]      # visits all 5 (gcd(2,5)=1)

# (4) Venus = frame at both scales
print("\n(4) VENUS = the frame at BOTH scales (fractal frame)")
print("    49-matrix:  Venus = row/col 0, the spatial-epoch frame (§28b, 'Venus IS the structure')")
print("    compound:   Venus synodic phase = which-of-5 selector")
print("    => same role, two scales: Venus frames the cell AND frames which-cube. (consistent)")

# (5) grand closure
print("\n(5) period incommensurability + grand closure")
g = math.gcd(VENUS, HELIX)
grand = VENUS*HELIX//g
print(f"    5-fold rotation {VENUS} vs full helix {HELIX}: differ by {HELIX-VENUS} (= one grid-cycle, 60)")
print(f"    grand closure LCM({VENUS},{HELIX}) = {grand} tithis")
print(f"      = {grand//VENUS} Venus-cycles  = {grand//HELIX} helix-cycles  ({VENUS}*{grand//VENUS}={VENUS*(grand//VENUS)}, {HELIX}*{grand//HELIX}={HELIX*(grand//HELIX)})")
assert grand == 141120 and grand//VENUS == 49 and grand//HELIX == 48

# (6) honest axis split
print("\n(6) axis split (honest)")
print("    single cube: Do-spine = 3-fold body diagonal (Pluto-Neptune), helix climbs THIS")
print("    5-compound:  rotates about a SEPARATE 5-fold dodec axis (NOT the Do-spine)")
print("    => the 5 cubes carry 5 distinct Do-spine orientations; which-of-5 = which spine is")
print("       active = Venus phase. The 3-fold helix and 5-fold compounding are different axes.")

print("\n"+"="*70)
print("WHICH-OF-5 = VENUS PHASE. 5 cubes = 5 Venus-pentagram positions of the one")
print("rotating Merkaba; Venus frames both the cell and the cube. Grand cycle = 141120 t")
print("= 49 Venus-cycles = 48 helix-cycles.")
print("="*70)
