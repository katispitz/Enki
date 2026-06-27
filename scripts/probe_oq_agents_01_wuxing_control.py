#!/usr/bin/env python3
"""
Probe: OQ-AGENTS-01 — geometric basis of the Wu-Xing CONTROLLING cycle.

Generating cycle is LOCKED = the 5 Merkaba rotation phases (Wood→Fire→Earth→
Metal→Water), adjacent +1 steps (72°) — the PENTAGON {5} on the dodec 5-fold
axis vertex set (Path D / §2 / FINDINGS_030).

Finding: the CONTROLLING cycle (ke / overcoming) = the PENTAGRAM {5/2} = +2 steps
(144°) on the SAME 5 vertices. Mechanically reproduces classic ke exactly. The
five-fold star's 4 non-trivial step-sizes {1,2,3,4} = the 4 traditional Wu-Xing
inter-element relations. The +2 (pentagram) traversal = Venus synodic order
(the 8-yr Venus pentagram; canon venus_pentagram + Path D Venus=Merkaba-rotation).

Run: python3 ~/Enki/scripts/probe_oq_agents_01_wuxing_control.py
"""
GEN = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']   # 5 Merkaba phases, generating order (LOCKED)
CLASSIC_KE = {'Wood': 'Earth', 'Earth': 'Water', 'Water': 'Fire',
              'Fire': 'Metal', 'Metal': 'Wood'}       # traditional overcoming cycle


def traverse(step):
    seq, i = [0], 0
    for _ in range(5):
        i = (i + step) % 5
        seq.append(i)
    return [GEN[k] for k in seq]


def main():
    print("5-fold vertex set = dodec 5-fold axis / 5-Merkaba rotation phases (72° apart):", GEN)
    print(f"  +1  PENTAGON  {{5}}    generating (sheng): {' → '.join(traverse(1))}")
    print(f"  +2  PENTAGRAM {{5/2}}  controlling (ke):   {' → '.join(traverse(2))}")
    ke = traverse(2)[:5]
    ok = all(CLASSIC_KE[ke[i]] == ke[(i + 1) % 5] for i in range(5))
    print(f"  controlling (+2) reproduces classic ke exactly?  {ok}")
    print(f"  +3  reverse-pentagram  insulting (wu):     {' → '.join(traverse(3))}")
    print(f"  +4  reverse-pentagon   reverse-generating:  {' → '.join(traverse(4))}")
    print()
    print("VERDICT: controlling cycle = pentagram (+2) on the 5-Merkaba/dodec-5-fold vertex set;")
    print("generating = pentagon (+1). The {5} and {5/2} polygons on the same 5 vertices. The four")
    print("inter-element relations = the four step-sizes {1,2,3,4}. The +2 pentagram = Venus synodic")
    print("order (8-yr Venus pentagram). Engine-evidence; canon lock pends kati_direct.")


if __name__ == "__main__":
    main()
