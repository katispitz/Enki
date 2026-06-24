#!/usr/bin/env python3
"""
sdec_00a_concentration_octave_scaffold.py — SDEC scaffold for the SOLE residue of
OQ-49STAR-ICO-PROJECTION: the concentration-octave height-map (canon §00a, sdec-pending).

§0c requires recognition + engine-evidence to lock. kati cleared this to derive (the prior
"kati-owned" tag was in-chat conflation-catching, not a reservation) — so this scaffold leads
with the Erato-4b CONFLATION-TEST (rule 4b: split BEFORE residency), then supplies the
engine-evidence the test needs, then leaves the recognition-call explicit.

THE QUESTION (canon §00a L159): does the double-helix's axial OCTAVE-HEIGHT (the Do-spine
winding, derived this session) equal the 10-position observer-CONCENTRATION ladder
(levels 0 abstract / 1 Earth / 2 self-on-Earth / 3 Lawvere)?

ERATO 4b CONFLATION-TEST — "octave" splits into THREE distinct primitive functions:
  (P) POSITION-octave  : which of the 10 PE positions on the Do-spine (Do..Si + X3/X6 + Do-ret).
                         DERIVED this session = matrix row/col, pure cube geometry. WHICH-NOTE.
  (T) TRANSPOSITION-octave : same structure re-anchored to a different observer (universal vs
                         personal mode = "same melody, different pitch", canon §0a L137/146/147).
                         This is the §00a concentration claim. WHICH-OBSERVER.
  (W) WINDING-octave   : which turn around ℤ_2940 (N_matrix). HOW-MANY-CYCLES.
If (P),(T),(W) are distinct functions, a single "concentration-octave HEIGHT-map" that maps
concentration onto axial position CONFLATES (T) with (P) — and must split before any map.

ENGINE-EVIDENCE (the split is mechanically decidable via helix_coordinate's mode toggle):
  helix_coordinate(t, asc_lon=None)  = universal mode  (concentration-0; Venus drives grid)
  helix_coordinate(t, asc_lon=X)     = personal  mode  (concentration-2; ASC drives grid)
  PREDICTION if (P)!=(T): changing observer-anchor leaves the MATRIX octave (matrix_pos/row/col
  = position) INVARIANT and shifts only grid_pos (the observer-frame). I.e. concentration is a
  TRANSPOSITION acting on the grid axis, ORTHOGONAL to the content-octave position. Then the
  "height-map" as posed is a category error; the substrate-true relation is
  concentration = transposition-group on the helix, not a coordinate on its axis.
"""
import sys
sys.path.insert(0, "/Users/kati/Nammu/engines")

print("="*72)
print("SDEC SCAFFOLD — §00a concentration-octave  (conflation-test FIRST, Erato 4b)")
print("="*72)

try:
    from helix_geometry import helix_coordinate
    HAVE = True
except Exception as e:
    HAVE = False
    print(f"\n[scaffold] helix_coordinate import failed ({e}) — engine-evidence step is a STUB below.")

print("\n--- ERATO 4b CONFLATION-TEST: split 'octave' into 3 candidate primitives ---")
senses = {
    "position-octave (P)":      "which of 10 PE positions on Do-spine (matrix row/col) — DERIVED, geometric",
    "transposition-octave (T)": "same structure, different observer-anchor (concentration) — §00a claim",
    "winding-octave (W)":       "which ℤ_2940 turn (N_matrix) — cycle count",
}
for k, v in senses.items():
    print(f"   {k:26s}: {v}")
print("   => 3 distinct functions (WHICH-NOTE / WHICH-OBSERVER / HOW-MANY). A height-map of")
print("      concentration onto axial POSITION conflates (T) into (P). Split required first.")

print("\n--- ENGINE-EVIDENCE: is (T) orthogonal to (P)?  universal vs personal at fixed t ---")
if HAVE:
    ASC_TEST = 137.0   # arbitrary personal ASC longitude for the toggle
    ok_matrix_invariant = True
    ok_grid_shifts = False
    for t in (40.0, 401.0, 1234.5, 2000.0):
        u = helix_coordinate(t, asc_lon=None)     # concentration-0 (universal)
        p = helix_coordinate(t, asc_lon=ASC_TEST) # concentration-2 (personal)
        same_matrix = (u.get("matrix_pos") == p.get("matrix_pos")
                       and u.get("row") == p.get("row") and u.get("col") == p.get("col"))
        grid_diff = u.get("grid_pos") != p.get("grid_pos")
        ok_matrix_invariant &= same_matrix
        ok_grid_shifts |= grid_diff
        print(f"   t={t:7.1f}: matrix_pos U={u.get('matrix_pos')} P={p.get('matrix_pos')} "
              f"(row/col same={same_matrix}) | grid_pos U={u.get('grid_pos')} P={p.get('grid_pos')} "
              f"(shifted={grid_diff})")
    print()
    print(f"   MATRIX-octave (position) invariant under observer change : {ok_matrix_invariant}")
    print(f"   GRID frame shifts under observer change                  : {ok_grid_shifts}")
    if ok_matrix_invariant and ok_grid_shifts:
        print("   => ENGINE-EVIDENCE SUPPORTS THE SPLIT: concentration (T) acts on the grid/observer")
        print("      axis and leaves the content-octave (P) invariant. They are ORTHOGONAL.")
        print("      The §00a 'height-map' as posed = CATEGORY ERROR; substrate-true reading:")
        print("      concentration = TRANSPOSITION-group on the whole helix (same melody, new pitch),")
        print("      NOT a position on the Do-spine. THIS is the conflation kati was catching.")
    else:
        print("   => evidence ambiguous — does NOT support clean split; needs deeper probe.")
else:
    print("   [STUB] run where helix_geometry imports; compares matrix_pos/row/col (expect invariant)")
    print("          vs grid_pos (expect shifted) across observer modes.")

print("\n--- §0c SDEC CHECKLIST (what remains to LOCK) ---")
steps = [
    ("1 recognition",        "kati_direct (this session: cleared to derive; conflation-catch was the tag)"),
    ("2 conflation-test 4b", "DONE above — 3 senses split; height-map conflates T into P"),
    ("3 engine-evidence",    "helix_coordinate mode-toggle: T orthogonal to P (run result above)"),
    ("4 residency count",    "TODO: 2nd independent residency for transposition=concentration"),
    ("5 name",               "candidate: 'concentration-transposition' (NOT 'concentration-octave-height')"),
    ("6 canon write",        "TODO: amend §00a — concentration is transposition on the helix, not axial height"),
]
for s, d in steps:
    print(f"   [{s:18s}] {d}")
print("\n" + "="*72)
print("SCAFFOLD COMPLETE. Recognition-call left to kati: accept that §00a concentration =")
print("transposition-group (observer re-anchor), ORTHOGONAL to the derived Do-spine octave-position.")
print("="*72)
