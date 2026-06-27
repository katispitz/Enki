#!/usr/bin/env python3
"""
enumerate_frame_12.py — the 12 FRAME cells of the 49-matrix (Venus × planet), derived.

Council OQ-VENUS-FRAME-PLACEMENT (card 891b4ee2) cleared this with two binding conditions:
  C1: Venus = the EMERGENT frame holding BOTH distinct positions — engine X3/grid-18 (mi->fa
      shock, shock-SILENT) + Taurus-Do/grid-0 (rulership angle, the Do-onset). Two angles of one
      helix (§752); NEVER "Venus is at grid 0" unqualified.
  C2: matrix-frame = Taurus/Do/grid-0 ONLY. Venus's 2nd domicile Libra (g25) EXCLUDED.
Council OQ-OCTAVE-STACKING-INDEX (9a86d373): frame cells live WITHIN one page -> octave-stacking
is orthogonal; derive them on content alone.

The 4-coord CONTENT framework does NOT transfer (council). Frame cells get their OWN coords from
Venus's unique DOUBLE-THRESHOLD role:
  (1) scale-degree-from-Do-onset : Venus-Taurus-Do (grid 0) originates the planet as the Nth degree
      (Re=2nd ... Si=7th). Frame-specific: Venus as ORIGIN-GATE, not a content interval.
  (2) shock-relation-to-X3       : Venus-engine = X3 at grid 18 (mi->fa). Each planet is PRE-shock
      (grid<18: rising toward the fault) or POST-shock (grid>18: past it). Venus IS the fault, so
      every frame cell relates to it. Shock is SILENT (mono-Fa, §L972).
  (3) gate-direction             : Venus-outer (Venus×planet) = origination/IN (Do-onset gates the
      planet up from silence, ASCENDING/generative). planet-outer (planet×Venus) = dissolution/
      RETURN to the gate (DESCENDING/dissolutive, toward the shock-silence).
  (4) doubleness (C1)            : both readings coexist — Do-onset (origination) AND X3-shock-silence.

GEOMETRY derived (locked grid positions). MYTH-skin = CANDIDATE (Aphrodite at the threshold), kati
validates. NO invented constants.
"""
# Authoritative note->grid (canon, ae5014f0): Do@0 Re@6 Mi@12 X3@18 Fa@24 Sol@30 X6@36 La@42 Si@48 Do-ret@54
GRID = {"Sun":6, "Moon":12, "Mars":24, "Mercury":30, "Saturn":42, "Jupiter":48}
NOTE = {"Sun":"Re", "Moon":"Mi", "Mars":"Fa", "Mercury":"Sol", "Saturn":"La", "Jupiter":"Si"}
DEGREE = {"Re":"2nd", "Mi":"3rd", "Fa":"4th", "Sol":"5th", "La":"6th", "Si":"7th"}
VENUS_DO_GRID = 0      # Taurus-Do rulership angle (C1: the rulership angle, NOT Venus's engine position)
VENUS_X3_GRID = 18     # Venus engine position = X3 mi->fa shock (C1: the engine angle)
GOD = {"Sun":"Apollo","Moon":"Artemis","Mars":"Ares","Mercury":"Hermes","Saturn":"Athena","Jupiter":"Zeus"}
PLANETS = ["Sun","Moon","Mars","Mercury","Saturn","Jupiter"]

# CANDIDATE myth-skin: Aphrodite (Venus) meeting each god AT THE THRESHOLD she holds. kati validates.
# Two readings per god (origination at Do-gate / dissolution at X3-shock-silence).
THRESHOLD_READ = {
 "Sun":     "the favored radiance brought to first-sounding / returned to the silent gate",
 "Moon":    "instinct originated at the gate, still rising toward the fault (pre-shock)",
 "Mars":    "force met at the fault itself — the mi->fa crisis Venus holds (Fa = first post-shock note)",
 "Mercury": "the messenger carried just past the fault — speech released downstream of the shock",
 "Saturn":  "structure far past the fault — order originated late, dissolving toward the gate",
 "Jupiter": "sovereignty at the octave's edge (Si) — last degree before Do-return; gate as horizon",
}

def shock_rel(planet):
    g = GRID[planet]
    if g < VENUS_X3_GRID: return f"PRE-shock (g{g} rising toward X3@18)"
    if g > VENUS_X3_GRID: return f"POST-shock (g{g} past X3@18)"
    return "AT-shock"

print("="*78)
print("THE 12 FRAME CELLS — Venus × planet (Venus = double threshold: Do-onset g0 + X3-shock g18)")
print("="*78)
print("C1: Venus engine = X3/g18; grid-0 = Taurus-Do RULERSHIP angle (two angles, one body).")
print("C2: Taurus/Do/g0 only — Libra (g25) EXCLUDED.\n")

rows = []
for p in PLANETS:
    deg = DEGREE[NOTE[p]]
    sr = shock_rel(p)
    # direction A: Venus×planet (Venus-frame outer) = origination IN (ascending/generative)
    rows.append(("Venus", p, "ASC/generative (origination — Do-onset gates "+p+" up from silence)", deg, sr))
    # direction B: planet×Venus (planet outer) = dissolution to gate (descending/dissolutive)
    rows.append((p, "Venus", "DESC/dissolutive ("+p+" returns/dissolves toward the gate & shock-silence)", deg, sr))

print(f"{'cell':18s} | {'gods':16s} | scale-deg | shock-rel | direction")
print("-"*110)
for outer, inner, direction, deg, sr in rows:
    god_o = "Aphrodite" if outer=="Venus" else GOD[outer]
    god_i = "Aphrodite" if inner=="Venus" else GOD[inner]
    planet = outer if outer!="Venus" else inner
    cell = f"{outer}×{inner}"
    print(f"{cell:18s} | {god_o[:7]}×{god_i[:7]:8s} | Do->{deg:4s}({NOTE[planet]}) | {sr:28s} | {direction}")

print("\n" + "="*78)
print("STRUCTURE (derived): Venus-X3 fault (g18) splits the 6 frame-partners —")
pre = [p for p in PLANETS if GRID[p] < VENUS_X3_GRID]
post = [p for p in PLANETS if GRID[p] > VENUS_X3_GRID]
print(f"  PRE-shock (rising to the fault): {pre}")
print(f"  POST-shock (past the fault):     {post}")
print(f"  Mars (Fa, g24) = FIRST note after the X3 fault — the fault Venus holds opens onto Mars.")
print(f"  Jupiter (Si, g48) = LAST degree before Do-return — gate as far horizon.")
print("MYTH-SKIN = CANDIDATE (Aphrodite-at-threshold per god). Geometry derived; kati validates myth.")
print("="*78)

# candidate threshold readings (for the draft / kati)
print("\nCANDIDATE threshold-readings (validator-skin, NOT geometry):")
for p in PLANETS:
    print(f"  Venus×{p:8s} ({GOD[p]}): {THRESHOLD_READ[p]}")
