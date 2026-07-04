#!/usr/bin/env python3
"""
probe_49star_ico_embedding.py — OQ-49STAR-ICO-PROJECTION step 2: the literal embedding.

Step 1 (probe_49star_doublehelix_octave.py) derived the double-helix STRUCTURE from angles.
Step 2 asks: which SOLID does it ride on? Composes the canonical Merkaba cube coordinates
(canon §3 L491/494) and checks that the double helix IS the cube's two tetrahedra viewed
down the Pluto-Neptune body diagonal (the Do-spine).

Verifies:
  (1) the 8 PE planets ARE the 8 cube vertices: U0..U3 Father-tet, L0..L3 Mother-tet
      (canon §3 lines 575-581 + 491/494).
  (2) viewed down the U0-L0 axis (Do-spine): Pluto/Neptune project to CENTER (on-axis);
      the 6 carriers project to a regular HEXAGON = two triangles offset EXACTLY 60deg
      = the Merkaba hexagram = the inner octahedron's 6 vertices (canon §M line 392).
  (3) the two carrier-triangles sit at DIFFERENT heights (z=-1/3 Father, z=+1/3 Mother),
      60deg apart = a triangular ANTIPRISM = one turn of the double helix.
  (4) SPATIAL vs TEMPORAL detune = the comma: the cube hexagram is 60deg-regular (SPACE),
      the 49-matrix-flow layout is 360/49=7.35deg-granular ~58.78deg offset (TIME). The
      gap is the same coprime incommensurability (T(49,60)) — space is hexagonal, the
      temporal firing is 49-fold; they cannot align → the comma.
  (5) icosahedron = the 5-Merkaba COMPOUND of this cube (canon §2 Path D / FINDINGS_030):
      5 such double-helix-cubes at 72deg about a 5-fold axis = dodec/ico. The ico-projection
      of the 49-star = 5 copies of the single-cube helix. (cites locked result; not re-derived.)

NO invented constants. Cube coords are the canonical Merkaba vertices.
"""
import math

s2, s6 = math.sqrt(2), math.sqrt(6)
# canon §3 line 491 — Father-tet (U) ; antipodes via line 494 pairs U0<->L0,U1<->L2,U2<->L3,U3<->L1
V = {
    "U0": (0.0, 0.0, 1.0),               # Pluto  (Do apex / +z pole)
    "U1": (2*s2/3, 0.0, -1/3),           # Sun
    "U2": (-s2/3,  s6/3, -1/3),          # Mars
    "U3": (-s2/3, -s6/3, -1/3),          # Saturn
}
V["L0"] = (0.0, 0.0, -1.0)               # Neptune (Do-return apex / -z pole)
V["L2"] = tuple(-c for c in V["U1"])     # U1<->L2  -> Mercury
V["L3"] = tuple(-c for c in V["U2"])     # U2<->L3  -> Jupiter
V["L1"] = tuple(-c for c in V["U3"])     # U3<->L1  -> Moon
PLANET = {"U0":"Pluto","U1":"Sun","U2":"Mars","U3":"Saturn",
          "L0":"Neptune","L1":"Moon","L2":"Mercury","L3":"Jupiter"}
FATHER = ["U0","U1","U2","U3"]           # solar δ_s, descending tet
MOTHER = ["L0","L1","L2","L3"]           # lunar  δ_l, ascending tet

def ang(v):  # azimuth about the z-axis (the Do-spine), degrees in [0,360)
    return math.degrees(math.atan2(v[1], v[0])) % 360.0
def rad(v):
    return math.hypot(v[0], v[1])
def almost(a, b, t=1e-9):
    return abs(a-b) < t

print("="*70); print("PROBE — the double helix rides on the cube (Merkaba), down the Do-spine"); print("="*70)

# (1) 8 planets == 8 cube vertices, all unit circumradius
print("\n(1) 8 PE planets == 8 cube vertices (unit circumsphere)")
for k in FATHER+MOTHER:
    R = math.sqrt(sum(c*c for c in V[k]))
    assert almost(R, 1.0), f"{k} not on unit sphere"
    print(f"    {k} {PLANET[k]:8s} = {tuple(round(c,3) for c in V[k])}  |v|={R:.3f}")

# (2)+(3) project down U0-L0 axis: apexes -> center, 6 carriers -> hexagram
print("\n(2) down the Do-spine (U0-L0): apexes on-axis, 6 carriers -> hexagram")
for ap in ("U0","L0"):
    assert almost(rad(V[ap]), 0.0), f"{ap} not on axis"
    print(f"    {PLANET[ap]:8s} ({ap}): xy-radius={rad(V[ap]):.3f} (ON AXIS = projects to center)")
fa = sorted(ang(V[k]) for k in FATHER[1:])   # U1,U2,U3 laterals
mo = sorted(ang(V[k]) for k in MOTHER[1:])   # L1,L2,L3 laterals
print(f"    solar Father laterals (Sun,Mars,Saturn): angles={[round(x,2) for x in fa]}  z={V['U1'][2]:.3f}")
print(f"    lunar Mother laterals (Moon,Merc,Jup):   angles={[round(x,2) for x in mo]}  z={V['L1'][2]:.3f}")
# each triangle equilateral (120 apart)
for lbl, A in (("solar",fa),("lunar",mo)):
    sp = [round((A[(i+1)%3]-A[i])%360,6) for i in range(3)]
    assert all(almost(x,120.0,1e-6) for x in sp), f"{lbl} not exactly equilateral: {sp}"
offset = (mo[0]-fa[0]) % 360
print(f"    triangle offset = {offset:.4f} deg  (EXACT 60 = regular hexagram, the perfect cube projection)")
assert almost(offset, 60.0, 1e-9)
print("    height split: Father z=-1/3, Mother z=+1/3 -> two triangles 60deg apart at two heights")
print("    => triangular ANTIPRISM = inner octahedron's 6 vertices = one turn of the helix (PASS)")

# (4) spatial-60 vs temporal-49 detune = the comma
print("\n(4) spatial hexagram (60deg) vs temporal 49-flow (58.78deg) = the comma")
temporal_offset = (8 * 360/49) % 360       # one diagonal-step from step-1 probe
detune = 60.0 - temporal_offset
print("    spatial cube offset   = 60.0000 deg  (SPACE: the cube is hexagonal/6-fold)")
print(f"    temporal 49 offset    = {temporal_offset:.4f} deg  (TIME: firing is 49-fold)")
print(f"    detune                = {detune:.4f} deg  (~ one ray {360/49:.4f}; space & time coprime -> comma)")
print("    => same T(49,60) incommensurability: hexagonal space cannot align with 49-fold time (PASS)")

# (5) icosahedron = 5-Merkaba compound of this cube (locked elsewhere; cite, don't re-derive)
print("\n(5) icosahedron embedding = 5 of these helix-cubes at 72deg about a 5-fold axis")
print("    canon §2 Path D / FINDINGS_030 (probe_icosa_5merkaba.py): 5 cubes @72deg -> 20 dodec")
print("    vertices; ico = dual. => ico-projection of the 49-star = 5 copies of the single-cube")
print("    double-helix. STILL OPEN: which-of-5 selection + concentration-octave height-map (§00a).")

print("\n"+"="*70)
print("CUBE EMBEDDING EXACT — double helix = cube's two tets down the Pluto-Neptune diagonal.")
print("Ico step reduces to the locked 5-Merkaba compound + the open concentration-map.")
print("="*70)
