#!/usr/bin/env python3
"""
Probe: per-LINE bond-map — test "each line = a bond-type; line-TYPE = bond-CATEGORY"
(kati 2026-06-16), with vertex-proximity DROPPED (bonds are lines, not orbs).

Resolver: geometry line → endpoint RESIDENTS (greek_faces, the residency canon) →
myth relationship (myth_correspondences full fields) → bond-type. Cross-body lines
also checked through their shock-node resident. Honest coverage reporting.
"""
import json, glob, itertools

GF = json.load(open('engines/greek_faces.json'))
FIG = json.load(open('council/myth_correspondences.json'))['figures']

# planet → resident Olympian + tet-side (lat>0 = Father/upper, lat<0 = Mother/lower)
PLANET = {}
for name, f in GF.items():
    p = f.get('planet')
    if p and f.get('lat') is not None and abs(f['lat']) < 30:   # the 10 face-residents
        PLANET[p] = {'god': name, 'tet': 'F' if f['lat'] > 0 else 'M', 'grid': f.get('grid')}

def rel(a, b):
    """myth relationship between two gods, via all relation fields (bidirectional)."""
    def fld(g, k): return [x.split(' (')[0] for x in (FIG.get(g, {}).get(k) or [])]
    if b in fld(a,'consorts') or a in fld(b,'consorts'): return 'MARRIAGE'
    if b in fld(a,'parents') or a in fld(b,'parents') or b in fld(a,'offspring') or a in fld(b,'offspring'): return 'PARENT-CHILD'
    if b in fld(a,'siblings') or a in fld(b,'siblings'): return 'SIBLING'
    return None

def bond_for_planets(p1, p2, via=None):
    g1, g2 = PLANET[p1]['god'], PLANET[p2]['god']
    cands = [(g1, g2)]
    if via and via in PLANET: cands += [(g1, PLANET[via]['god']), (PLANET[via]['god'], g2)]
    for a, b in cands:
        r = rel(a, b)
        if r: return r, f"{a}-{b}"
    return None, f"{g1}-{g2}" + (f" (via {PLANET[via]['god']})" if via and via in PLANET else "")

def tetcross(p1, p2): return 'cross-tet' if PLANET[p1]['tet'] != PLANET[p2]['tet'] else 'same-tet'

print("planet→resident:", {k: v['god'] for k, v in PLANET.items()})
print()

# --- LINE SETS ---
# HEXAD (§16 supervision); cross-body shock-crossings marked with via-node
hexad = [('Sun','Mars',None),('Mars','Moon','Venus'),('Moon','Jupiter',None),
         ('Jupiter','Mercury',None),('Mercury','Saturn','Uranus'),('Saturn','Sun',None)]
# CIRCLE (Cronus sequential adjacency, the 7 classical in zodiac order)
circle_seq = ['Venus','Mercury','Moon','Sun','Mars','Jupiter','Saturn']
circle = [(circle_seq[i], circle_seq[i+1], None) for i in range(len(circle_seq)-1)]
# TRIANGLE (shock nodes Venus/X3, Uranus/X6, + axis Pluto/Neptune)
triangle = [('Venus','Uranus',None),('Uranus','Pluto',None),('Pluto','Venus',None),('Uranus','Neptune',None)]

for label, lines in [('HEXAD (Kairos / structural)', hexad),
                     ('CIRCLE (Cronus / adjacency)', circle),
                     ('TRIANGLE (shock)', triangle)]:
    print(f"=== {label} ===")
    for p1, p2, via in lines:
        if p1 not in PLANET or p2 not in PLANET: print(f"  {p1}-{p2}: (planet not resident)"); continue
        b, who = bond_for_planets(p1, p2, via)
        print(f"  {p1}-{p2} [{tetcross(p1,p2)}{'/via '+via if via else ''}] {who}: {b or '— no edge in data'}")
    print()
