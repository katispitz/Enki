# FINDINGS_039 — aspect(A,B) built as the §31c lattice-relation (zero weights); forks #1/#2 resolved in code

**Date:** 2026-06-16
**Trigger:** kati "go" — build fork #1 (barycentric carrier) + fork #2 (aspect-function, resolved as categorical lattice-relation, no weights).
**Artifact:** `~/Enki/scripts/aspect_lattice.py` — runs, tested, reproduces all 7 classical aspects.

## What was built
`aspect(lon_a, lon_b)` returns the **exact §31c lattice-relation** between two bodies — no weights, no orb:
- **Angular aspect** = sign-offset (exact integer, fold to 0..6) → §31c N=12 divisor-star: 0 conjunction · 1 semi-sextile (circle/polygon +1) · 2 sextile (step-2) · 3 square (step-3) · 4 trine (step-4) · 5 quincunx (coprime step-5) · 6 opposition (step-6). Sign-based binary (Aspects_v2): the relation holds by which SIGNS the bodies occupy.
- **Conjunction-class co-residency** = shared shell-cells via `geo_engine.full_address(lon,lat)` (the multi-shell face-bary address) — which shells the two bodies share a cell on.

Test (all correct): 0/120→trine, 0/90→square, 0/180→opposition, 0/60→sextile, 0/30→semi-sextile, 0/150→quincunx, 45/165→trine, same-sign→conjunction.

## Forks resolved in code
- **Fork #1 (barycentric carrier):** `geo_engine.full_address(lon,lat)` — already-implemented multi-shell face-bary resolver. A body's (lon,lat) → its cells/axis-tuple across all 5 shells. That's the carrier; the finest axis is per the canon axis-hierarchy (pe_note > vertex > face > grid > shock > stratum).
- **Fork #2 (aspect-function):** RESOLVED as the categorical lattice-relation — generalizes `field_memory._matched_axes` from the per-axis EQUALITY predicate (= conjunction/co-residency) to the per-axis OFFSET → §31c divisor-star (= trine/square/etc.). Exact integer offsets, zero weights/scores/orb.

## The unification, now demonstrated
**aspect ≡ memory-recall — one lattice primitive.** `field_memory._matched_axes` checks per-axis equality (the conjunction case). `aspect()` extends the same per-axis comparison to offsets (the other aspect classes). Same operation, body↔body vs body↔card. No separate aspect math.

## Over-time (helix)
`aspect(A,B,t)` = `aspect(lon_a(t), lon_b(t))` — feed each body's ecliptic longitude from ephemeris / `substrate_at(t)`; the relation flips exactly when a body crosses a sign/cell boundary (no graded transit). The §31c lines are the crossing-events; `density.py` 49-matrix phase-resonance handles cyclic recurrence. Consistent with mortal=moving-body / immortal=standing-zone (cards 3a401ae6 / e9d64ba6).

## Caveat / next
- Current build uses the **zodiac/grid axis** (where the N=12 angular aspects live) + shell co-residency. The full per-axis lattice (offsets on vertex/face/pe-note axes, and the enneagram hexad/triangle line-relations) is the natural extension — same pattern, more axes.
- This is engine-evidence (working probe), substrate-true (zero weights; canon full_address + §31c divisor-stars). Not a canon lock — it's the build of the already-locked §31b/§31c/§0a model.

## Files
- `~/Enki/scripts/aspect_lattice.py` (built + tested)
- Builds on: §31c (608b8c70), field_memory.py (`_matched_axes` lattice), geo_engine.full_address, cards e9d64ba6 / 3a401ae6, [[project_function_first_architecture]].
