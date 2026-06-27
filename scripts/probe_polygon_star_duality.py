#!/usr/bin/env python3
"""
Probe: the POLYGON/STAR traversal duality = the CHRONOLOGICAL/QUALITATIVE duality.

Surfaced 2026-06-15 from the Wu-Xing close (FINDINGS_036): the same symmetry-N
vertex set admits an ADJACENT (+1, polygon {N}) traversal and a SKIP (star {N/k})
traversal. The adjacent/polygon traversal is the CHRONOLOGICAL/GENERATING cycle
(Cronus-class); the skip/star traversal is the QUALITATIVE/TRANSFORMATIONAL cycle
(Kairos-class). This unifies three traditions' names for one substrate duality and
concretizes §31b's morphism layer (a cycle = a traversal-morphism on the node set).

Confirmed: N=5 (Wu-Xing generating/controlling), enneagram flow-nodes (Cronus/Kairos).
Candidate-general for other N (test before claiming).

Run: python3 ~/Enki/scripts/probe_polygon_star_duality.py
"""

def traverse(seq, step):
    n = len(seq); i = 0; out = [seq[0]]
    for _ in range(n):
        i = (i + step) % n
        out.append(seq[i])
    return out[:n]


def main():
    print("N=5 (Wu-Xing) — 5-Merkaba / dodec-5-fold vertex set:")
    g = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
    print("  POLYGON  {5}   +1  = generating (sheng) / chronological :", ' '.join(traverse(g, 1)))
    print("  STAR     {5/2} +2  = controlling (ke)   / qualitative   :", ' '.join(traverse(g, 2)))

    print("\nEnneagram flow-nodes (the hexad):")
    print("  POLYGON  (in-order)  = CRONUS / chronological :", [1, 2, 4, 5, 7, 8])
    print("  STAR     (1/7 leap)  = KAIROS / qualitative   :", [1, 4, 2, 8, 5, 7], " (1/7 = 0.142857…)")

    print("\nUNIFICATION (one substrate duality, three traditional names):")
    print("  adjacent/polygon traversal  = CHRONOLOGICAL = Cronus = generating/sheng")
    print("  skip/star traversal         = QUALITATIVE   = Kairos = controlling/ke")
    print("  = §31b morphism layer: same node-set, two traversal-morphisms (polygon-edges vs star-edges).")
    print("  Confirmed N=5 + enneagram. Candidate-general for N=7 (octave) / N=12 (zodiac) — test before claiming.")
    print("  §0 caveat: geometry forced; cross-tradition naming = validation, not proof.")


if __name__ == "__main__":
    main()
