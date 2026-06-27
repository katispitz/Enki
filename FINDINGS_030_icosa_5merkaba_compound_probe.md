# FINDINGS_030 — Icosahedron lives in the 5-Merkaba spatial compound (OQ-ICOSA-01)

**Date:** 2026-06-14
**Probe target:** OQ-ICOSA-01 (🔴 BLOCKING, opened 2026-06-08) + canon §0a "5 inscribed Merkabas (72° apart in dodec)" + `~/Nammu/engines/karana.py::merkaba_rotation_phases`
**Probe shape:** pure-geometry mechanical validation (numpy), reproducible at `~/Enki/scripts/probe_icosa_5merkaba.py`
**Outcome:** PASS for **Path D** (icosa/dodec are in the framework, as the 5-fold-class of the 5-Merkaba compound) + **BUG FOUND** (canon §0a + karana.py conflate the spatial compound with the Wu-Xing temporal z-clock)

## Context

Audit 2026-06-14 of BABYLONIA_CORPUS_v1 surfaced a Tier-1 contradiction: canon body §2/§3/§9 carry the icosahedron/dodecahedron as `[LOCKED]` while Part C.1 + OQ-ICOSA-01 mark them unconfirmed/suspended ("Water and Aether SUSPENDED"; "Path C removal most defensible"). The correction doc identified 4 candidate paths (A independent-grid / B truncation / C remove / D higher-order compound) and derived none. This probe decides between them mechanically.

## Probe design

Two rival claims, both checkable on coordinates:

- **CLAIM A** (karana.py docstring + canon §0a): "ONE Merkaba returns to itself after 5 rotation steps of 72° **around the z-axis**; the 5 inscribed Merkabas are 72° apart."
- **CLAIM B** (Path D; matches the dodec-row framing already in FINDINGS_029): the dodecahedron is the union of **5 DISTINCT cubes/Merkabas** related by 72° about a dodecahedral **5-fold axis** (classical compound of 5 cubes). Icosa = its dual; icosidodecahedron = 30-vertex union of the 5 inner octahedra.

Failure mode for B: 5 cubes about a 5-fold axis do NOT land on the 20 dodec vertices. Failure mode for A: a cube cannot self-return at 72° / z-72° does not reproduce the dodecahedron.

## Results (reproducible)

```
dodecahedron: 20 vertices, all radius=1.7321
base cube ⊂ dodecahedron: True
genuine 5-fold axes (face centers): 12 (expect 12)

CLAIM B (Path D): 5 cubes about a 5-fold axis
  each of 5 rotated cubes ⊂ dodecahedron: True
  distinct vertices in union: 20 (dodec = 20)
  → 5 Merkabas reconstruct the dodecahedron EXACTLY: True

CLAIM A (karana.py / §0a): 72° about z-axis
  cube ⊂ dodecahedron after one z-72°: False
  distinct vertices in 5×z-72° union: 40 (NOT a dodecahedron)
  cube self-returns about z at: [90, 180]° — 72 absent → 'returns to itself after 72°' is FALSE
```

## Findings

1. **Path D CONFIRMED.** Five cubes (Merkabas), each the base cube rotated by k·72° (k=0..4) about a genuine dodecahedral 5-fold axis, have vertices that are all ⊂ the dodecahedron and whose union is **exactly** the 20 dodecahedron vertices (each shared by 2 cubes: 5×8=40=2×20). The dodecahedron IS the compound of 5 Merkabas. The icosahedron is its dual; the icosidodecahedron (30V) is the union of the 5 inner octahedra (one per Merkaba) — the classical compound-of-5-octahedra. **The icosa/dodec are derivable and belong in the substrate** — Path C (removal) is NOT required.

2. **Symmetry-incompatibility refutation is preserved and explained.** One Merkaba (3-fold/tetrahedral symmetry) cannot generate 5-fold structure — true (OQ-3D-01, Part C.1). The 5-fold class arises only at the **compound** scale (5 Merkabas, chiral icosahedral symmetry A5). So OQ-3D-01's refutation and Path D's construction are consistent: single-Merkaba edge-crossings → {tet, oct, cube} (3-fold class); 5-Merkaba compound → {dodec, icosidodec, icosa} (5-fold class).

3. **BUG: canon §0a + karana.py conflate two distinct primitives** (Erato 4b violation):
   - **Temporal** — ONE Merkaba spinning about the Hera-Hestia (z) axis, sampled at 5 phase points = Wu-Xing phase clock. This is a *sampling*, NOT a symmetry closure: a cube has no z-72° symmetry (it self-returns only at 90°/180°). karana.py's "ONE Merkaba returns to itself after 5 rotation steps (72° each) around z-axis" is geometrically false.
   - **Spatial** — FIVE distinct Merkabas related by 72° about a 5-fold axis = the dodecahedron compound. karana.py's claim that the 5 phases are "5 stable rotational positions of the same Merkaba — not 5 distinct inscribed Merkabas" is backwards: the dodecahedron requires 5 DISTINCT cubes; the same cube at 5 z-phases gives 40 scattered points, not a dodecahedron.
   - The two share the number 5 and the angle 72° but are different rotations about different axes. They must be split.

4. **karana.py test is tautological.** `tests/test_wu_xing_5merkaba.py::test_5_inscribed_merkabas_72_degree_spacing` asserts `merks[i]['rotation_offset'] == i*72` against a function that literally returns `i*72.0`. It verifies no geometry. A real test must assert the 5-cube→dodec reconstruction (this probe).

## Disposition

- **OQ-ICOSA-01 → RESOLVED as Path D 2026-06-14** (kati_direct recognition + this probe's engine-evidence satisfy §0c; Ollama council waived by kati as low-value on a mechanically-proven geometry question). Canon §2/§3/§9/§0a + corpus + OQ register corrected 2026-06-14; karana.py docstring fixed; real geometry test added (`tests/test_wu_xing_5merkaba.py::test_5_merkaba_compound_reconstructs_dodecahedron`, 16/16 green).
- **Canon corrections APPLIED 2026-06-14:**
  - §2/§3/§9: keep icosa/dodec in the framework but re-tag generation as "5-Merkaba 5-fold compound," not "one-Merkaba crossings." Water/Aether un-suspend under Path D.
  - §0a point 4 + §00 "5 inscribed Merkabas at 72°": split into (temporal) Wu-Xing z-phase-sampling and (spatial) 5-fold-axis compound. Drop "returns to itself at 72°."
  - `~/Nammu/engines/karana.py::merkaba_rotation_phases` docstring: correct the axis and the self-return claim; replace the tautological test with a coordinate-level reconstruction test.
- **Athena lock-by-redundancy:** Path D has 2 independent geometric residencies already (dodec 20V = 5-cube union; icosidodec 30V = 5-octahedra union). Meets ≥2.

## Files
- Probe: `~/Enki/scripts/probe_icosa_5merkaba.py`
- Audit: `~/Documents/Babylonia/BABYLONIA_CORPUS_v1_AUDIT_2026-06-14.md`
