#!/usr/bin/env python3
"""
enumerate_offdiagonal_30.py — the 30 content cells of the 49-matrix, fully typed.
GEOMETRY is computed by helix_address (interval, shock-load, octave-sense, arm).
MYTH-CONTENT is a SEPARATE candidate data layer (validator-skin, §26 locked gods) —
kati validates/refines. Guardrail visible: geometry never reads from the content dict.
"""
from datetime import datetime, timezone
import helix_address as h

GOD = {"Sun":"Apollo","Moon":"Artemis","Mars":"Ares","Mercury":"Hermes","Saturn":"Athena","Jupiter":"Zeus"}
PLANETS = ["Sun","Moon","Mars","Mercury","Saturn","Jupiter"]

# CANDIDATE myth-content (outer-phase WITH inner-quality operating inside it). §26 gods. kati validates.
READ = {
 ("Sun","Moon"):"solar will carrying lunar instinct — clarity softened by protective reflex (twins)",
 ("Sun","Mars"):"illumination driven to a point — the plague-arrow; will weaponized",
 ("Sun","Mercury"):"radiance carried as signal — light translated to speech (Hermes' lyre-gift)",
 ("Sun","Saturn"):"illumination given strategic structure — prophecy made law (allied order)",
 ("Sun","Jupiter"):"the favored son's light under sovereign expansion — radiance at sky-scale",
 ("Moon","Sun"):"the wild/instinct phase lit by solar aim — the hunt made precise (twins)",
 ("Moon","Mars"):"instinct driven by force — protective fury, the huntress's kill",
 ("Moon","Mercury"):"instinct given threshold/language — the psychopomp feel, wild crossing",
 ("Moon","Saturn"):"instinct disciplined into strategy — the hunt made wise (two virgin powers)",
 ("Moon","Jupiter"):"instinct under sovereign expansion — the king's wild daughter amplified",
 ("Mars","Sun"):"force illuminated — strife given righteous aim/clarity",
 ("Mars","Moon"):"force carrying instinct — the warrior's protective rage",
 ("Mars","Mercury"):"force translated — the herald of war; speech that strikes",
 ("Mars","Saturn"):"raw force seeking wisdom — brute war reaching for strategy (Ares→Athena)",
 ("Mars","Jupiter"):"force under sovereignty — strife legitimated or restrained by law (Zeus' scorn)",
 ("Mercury","Sun"):"translation illuminated — the message made clear/true",
 ("Mercury","Moon"):"translation by instinct — boundary-crossing on feel",
 ("Mercury","Mars"):"translation driven by force — the message as weapon",
 ("Mercury","Saturn"):"cunning given structure — trickery made wise (two cleverness-gods)",
 ("Mercury","Jupiter"):"the messenger under sovereignty — Zeus's will carried into decree",
 ("Saturn","Sun"):"structure illuminated — strategy made radiant, wisdom given prophecy",
 ("Saturn","Moon"):"structure carrying instinct — strategy guided by protective feel",
 ("Saturn","Mars"):"strategy deploying force — wisdom wielding the war-machine (Athena masters Ares)",
 ("Saturn","Mercury"):"structure made articulate — strategy communicated as cunning",
 ("Saturn","Jupiter"):"wisdom under sovereign expansion — Athena sprung from Zeus's head; the sovereign's mind",
 ("Jupiter","Sun"):"sovereign expansion lit by the favored son — law illuminated",
 ("Jupiter","Moon"):"sovereignty carrying instinct — the king's domain protected by feel",
 ("Jupiter","Mars"):"sovereignty driven by force — expansion through war; the thunderbolt's wrath",
 ("Jupiter","Mercury"):"sovereignty translated — the king's will disseminated as law",
 ("Jupiter","Saturn"):"sovereign expansion given wisdom — authority made strategic (Athena from his head)",
}

when = datetime(2026,6,20,12,0,0,tzinfo=timezone.utc)
HEXAD = {("Sun","Mars"),("Mars","Moon"),("Moon","Jupiter"),("Jupiter","Mercury"),("Mercury","Saturn"),("Saturn","Sun")}
addrs = {p: h.address_of(p, when) for p in PLANETS}

rows=[]
for po in PLANETS:
    for pi in PLANETS:
        if po==pi: continue
        s = h.relation(addrs[po], addrs[pi])["pair_49"]["skeleton"]
        rows.append((po,pi,s))

lines=["# 49-Matrix Off-Diagonal — 30 Content Cells (GEOMETRY derived · MYTH candidate)",
       "",
       "Geometry: helix_address skeleton. Myth: §26 locked gods, CANDIDATE (kati validates).",
       "Guardrail: geometry generates type; myth fills content; never reverse.","",
       "| cell (po×pi) | gods | interval | dir/octave | arm | shock-load | candidate myth-content |",
       "|---|---|---|---|---|---|---|"]
for po,pi,s in rows:
    hexmark = " ⟡hexad" if (po,pi) in HEXAD else ""
    sc = ",".join(x.split()[0] for x in s["shocks_crossed"]) or "—"
    lines.append(f"| {po}×{pi}{hexmark} | {GOD[po]}×{GOD[pi]} | {s['interval']} | "
                 f"{s['direction']}/{s['octave_sense']} | {s['arm_relation']} | "
                 f"{s['shock_load']} [{sc}] | {READ.get((po,pi),'(owed)')} |")

out="/Users/kati/Nammu/drafts/offdiagonal_30cells_2026-06-21.md"
open(out,"w").write("\n".join(lines)+"\n")
print(f"WROTE {out}  ({len(rows)} cells)\n")
# show the structurally notable ones
print("STRUCTURAL STANDOUTS:")
print("  shock-load 2 (must cross BOTH octave-crises — hardest relationships):")
for po,pi,s in rows:
    if s["shock_load"]==2: print(f"    {GOD[po]}×{GOD[pi]:8} ({po}×{pi}, {s['interval']}, {s['octave_sense']}): {READ[(po,pi)]}")
print("\n  the Ares/Athena directional pair (force↔wisdom, both ways):")
for po,pi in [("Mars","Saturn"),("Saturn","Mars")]:
    s=h.relation(addrs[po],addrs[pi])["pair_49"]["skeleton"]
    print(f"    {GOD[po]}×{GOD[pi]} ({s['direction']}/{s['octave_sense']}, {s['arm_relation']}): {READ[(po,pi)]}")
