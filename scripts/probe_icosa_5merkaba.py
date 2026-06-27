#!/usr/bin/env python3
"""
Probe: OQ-ICOSA-01 — where does the icosahedron/dodecahedron live in the substrate?

Engine-evidence for the audit 2026-06-14 of BABYLONIA_CORPUS_v1.
Tests two claims found in canon §0a + Nammu/engines/karana.py:

  CLAIM A (karana.py merkaba_rotation_phases docstring + canon §0a):
    "ONE Merkaba returns to itself after 5 rotation steps of 72° around the
     z-axis; the 5 inscribed Merkabas are 72° apart in the dodecahedron."

  CLAIM B (Path D, this audit; matches FINDINGS_029 dodec-row framing):
    "The dodecahedron is the union of 5 DISTINCT cubes/Merkabas related by 72°
     about a dodecahedral 5-FOLD axis (the compound of 5 cubes). The icosa is
     its dual; the icosidodecahedron is the 30-vertex union of the 5 inner
     octahedra."

Pure geometry, numpy only. No substrate coefficients invented.
Run:  python3 ~/Enki/scripts/probe_icosa_5merkaba.py
"""
import itertools
import numpy as np

phi = (1 + 5 ** 0.5) / 2
TOL = 1e-5


def dodecahedron():
    """20 vertices of a regular dodecahedron (standard coordinates)."""
    V = [np.array(s, float) for s in itertools.product([-1, 1], repeat=3)]  # cube
    for a, b in itertools.product([-1, 1], repeat=2):
        V += [np.array([0, a * phi, b / phi]),
              np.array([a / phi, 0, b * phi]),
              np.array([a * phi, b / phi, 0])]
    return np.array(V)


def base_cube():
    """One inscribed cube/Merkaba: the 8 (±1,±1,±1) vertices."""
    return np.array(list(itertools.product([-1, 1], repeat=3)), float)


def rot(axis, deg):
    a = np.array(axis, float); a /= np.linalg.norm(a); th = np.radians(deg)
    x, y, z = a; c, s = np.cos(th), np.sin(th); C = 1 - c
    return np.array([[c + x * x * C, x * y * C - z * s, x * z * C + y * s],
                     [y * x * C + z * s, c + y * y * C, y * z * C - x * s],
                     [z * x * C - y * s, z * y * C + x * s, c + z * z * C]])


def subset_of(P, V, tol=TOL):
    return all(np.any(np.linalg.norm(V - p, axis=1) < tol) for p in P)


def n_distinct(P, tol=TOL):
    u = []
    for p in P:
        if not any(np.linalg.norm(q - p) < tol for q in u):
            u.append(p)
    return len(u)


def five_fold_axes(V):
    """Dodec face centers that are genuine 5-fold symmetry axes (set invariant @72°)."""
    D = np.linalg.norm(V[:, None] - V[None], axis=2)
    el = np.min(D[D > 1e-6])
    adj = {i: [j for j in range(len(V)) if abs(D[i, j] - el) < TOL] for i in range(len(V))}
    faces = set()
    for a in range(len(V)):
        for b in adj[a]:
            for c in adj[b]:
                if c == a:
                    continue
                for d in adj[c]:
                    if d in (a, b):
                        continue
                    for e in adj[d]:
                        if e in (a, b, c):
                            continue
                        if a in adj[e]:
                            faces.add(frozenset((a, b, c, d, e)))
    centers = [V[list(f)].mean(0) for f in faces]
    return [c for c in centers if subset_of((rot(c, 72) @ V.T).T, V)]


def main():
    V = dodecahedron()
    C0 = base_cube()
    print(f"dodecahedron: {len(V)} vertices, all radius={np.linalg.norm(V[0]):.4f}")
    print(f"base cube ⊂ dodecahedron: {subset_of(C0, V)}")

    axes = five_fold_axes(V)
    print(f"genuine 5-fold axes (face centers): {len(axes)} (expect 12)\n")

    print("=== CLAIM B (Path D): 5 cubes about a 5-fold axis ===")
    ax = axes[0]
    cubes = [(rot(ax, 72 * k) @ C0.T).T for k in range(5)]
    all_in = all(subset_of(c, V) for c in cubes)
    union = n_distinct(np.vstack(cubes))
    print(f"  each of 5 rotated cubes ⊂ dodecahedron: {all_in}")
    print(f"  distinct vertices in union: {union} (dodec = 20)")
    print(f"  RESULT: 5 Merkabas reconstruct the dodecahedron EXACTLY: "
          f"{all_in and union == 20}\n")

    print("=== CLAIM A (karana.py / §0a): 72° about z-axis ===")
    zc = [(rot((0, 0, 1), 72 * k) @ C0.T).T for k in range(5)]
    print(f"  cube ⊂ dodecahedron after one z-72°: {subset_of(zc[1], V)}")
    print(f"  distinct vertices in 5×z-72° union: {n_distinct(np.vstack(zc))} "
          f"(NOT a dodecahedron)")
    self_return = [d for d in (72, 90, 120, 180)
                   if np.allclose(sorted(map(tuple, np.round((rot((0, 0, 1), d) @ C0.T).T, 4))),
                                  sorted(map(tuple, np.round(C0, 4))))]
    print(f"  cube self-returns about z at: {self_return}° — 72 absent → "
          f"'returns to itself after 72°' is FALSE\n")

    print("VERDICT: dodec/icosa/icosidodec are the 5-fold-symmetry-class structures of the")
    print("5-Merkaba SPATIAL compound (Path D), distinct from the Wu-Xing TEMPORAL z-phase clock.")
    print("karana.py + canon §0a conflate the two (wrong axis + impossible self-return).")


if __name__ == "__main__":
    main()
