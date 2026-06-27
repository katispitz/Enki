#!/usr/bin/env python3
"""
probe_offdiag_interval_metric.py — OQ-49-OFFDIAG-ENGINE, interval-metric fork.
Runs BOTH candidate metrics over the 30 content cells and lets the shock-structure decide.
  A = scale-degree (consecutive Do..Si = 1..7) — musical interval, ignores shock-gaps
  B = diatonic label {Re1,Mi2,Fa4,Sol5,La7,Si8} — skips shock labels 3,6 (encodes shocks)
Shocks (canon §7/§19): X3 mi→fa between Mi|Fa (deg 3|4); X6 si→do between Sol|La (deg 5|6).
"""
# 6 content planets (Venus=frame, excluded): (name, note, scale_degree, diatonic_label, home_grid)
P = [("Sun","Re",2,1,6), ("Moon","Mi",3,2,12), ("Mars","Fa",4,4,24),
     ("Mercury","Sol",5,5,30), ("Saturn","La",6,7,42), ("Jupiter","Si",7,8,48)]
IVL = {1:"unison",2:"2nd",3:"3rd",4:"4th",5:"5th",6:"6th",7:"7th"}
# shock boundaries in scale-degree space: X3 between deg3&4, X6 between deg5&6
SHOCKS = {3.5:"X3 mi→fa", 5.5:"X6 si→do"}

def shocks_between(da, db):
    lo, hi = sorted((da, db))
    return [name for pos,name in SHOCKS.items() if lo < pos < hi]

print("OQ-49-OFFDIAG-ENGINE — interval-metric fork, both ways over the 30 content cells\n")
print(f"{'pair (po×pi)':16} {'A:scale':9} {'B:label':8} {'B−A':4} {'shocks crossed':16}")
print("-"*60)
ok = True
rows=[]
for po in P:
    for pi in P:
        if po is pi: continue
        na,_,da,la,_ = po; nb,_,db,lb,_ = pi
        Astep = abs(db-da); Bstep = abs(lb-la)
        sh = shocks_between(da,db)
        rows.append((na,nb,Astep,Bstep,Bstep-Astep,len(sh),sh))
# verify the structural identity B−A == #shocks-crossed across all 30
violations = [(na,nb) for na,nb,A,B,d,n,sh in rows if d != n]
for na,nb,A,B,d,n,sh in rows[:12]:
    print(f"{na+'×'+nb:16} {IVL[A+1]+'('+str(A)+')':9} {str(B):8} {d:<4} {','.join(sh) or '—':16}")
print("  ... (30 total)\n")
print(f"STRUCTURAL IDENTITY  B−A == number of shocks crossed:  "
      f"{'HOLDS for all 30' if not violations else 'VIOLATED: '+str(violations)}")
print()
print("→ WHAT FALLS OUT: the two metrics are NOT a fork — they're two COORDINATES.")
print("   A (scale-degree) = the INTERVAL-QUALITY (what kind of relationship).")
print("   B−A             = the SHOCK-LOAD (how many octave-crises the pair must cross).")
print("   B (label) = A + shock-load, by construction (labels skip the shock positions).")
print("   You don't choose; the cell carries BOTH: (musical interval, shocks-traversed).")
print()
# live readings — geometry types; myth fills (validator, §26 locked gods)
print("LIVE READINGS (geometry types the cell; myth-content is the validator-skin, §26):")
def read(a,b):
    da=dict((p[0],p) for p in P)
    A=abs(da[b][2]-da[a][2]); sh=shocks_between(da[a][2],da[b][2])
    arrow = "asc" if da[b][2]>da[a][2] else "desc"
    return f"{a}×{b}: {IVL[A+1]} {arrow}, shock-load {len(sh)} [{','.join(sh) or 'none'}]"
for a,b in [("Saturn","Jupiter"),("Jupiter","Saturn"),("Moon","Mars"),("Sun","Saturn")]:
    print("   "+read(a,b))
print()
print("   Saturn×Jupiter (La→Si, 2nd asc, no shock) = Athena→Zeus, adjacent, no crisis —")
print("     the leading-tone handoff. Jupiter×Saturn (desc) = the return-pressure inverted.")
print("   Moon×Mars (Mi→Fa, 2nd asc, CROSSES X3) = the mi→fa shock pair — feeling driven")
print("     through the first crisis into force. The shock-load IS the Ares/Artemis tension.")
print("   (myth fills content; geometry already set interval + shock-load — guardrail held.)")
