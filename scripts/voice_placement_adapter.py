#!/usr/bin/env python3
"""
voice_placement_adapter.py — the missing Layer-A piece (audit 2026-06-20 step 1 blocker).
Maps a council voice's position-schema → field_memory's axis-tuple placement, so
field_memory.recall_field matches on FINE axes (tight, lattice-true recall) instead of
collapsing to stratum-only 500+-card over-recall.

Reliable mappings only (verified against card field-forms 2026-06-21):
  voice pe_note            → pe_note   (direct)
  voice face_id  (F2)      → face      (cards store F-form)
  voice pe_note            → grid      (canonical PE→grid; more reliable than zodiac_deg)
  voice pe_note X3/X6      → shock_proximity at_X3/at_X6
  voice stratum            → stratum   (coarse level-6 axis; lattice ordering handles it)
Dropped (schema-unreliable): vertex_id (inner-oct V-form ≠ card merkaba_vertex U/L/X);
ico_vertex (unused in cards). Honest: do not invent a mapping we can't verify.
"""
_PE_GRID = {"Do":0,"Re":6,"Mi":12,"X3":18,"Fa":24,"Sol":30,"X6":36,"La":42,"Si":48,"Do-ret":54}

def voice_to_placement(v: dict) -> dict:
    """voice dict (with 'position','stratum') → field_memory placement dict."""
    pos = v.get("position") or {}
    sub = {}
    pe = pos.get("pe_note")
    if pe:
        sub["pe_note"] = pe
        if pe in _PE_GRID:
            sub["grid"] = str(_PE_GRID[pe])          # cards store grid as str
        # shock_proximity RETIRED 2026-06-21 (kati_direct) — being at a shock IS pe_note=X3/X6
        # + grid=18/36 (§00b); a separate proximity axis re-encodes the location and is graded.
    if pos.get("face_id"):
        sub["face"] = pos["face_id"]                  # F-form, matches cards
    return {"substrate_position": sub, "stratum": v.get("stratum")}


if __name__ == "__main__":
    import sys, json, glob
    sys.path.insert(0, "/Users/kati/Enki/substrate")
    import field_memory as fm
    d = json.load(open(glob.glob("/Users/kati/Nammu/**/voice_correspondences.json", recursive=True)[0]))
    voices = list(d.values()) if isinstance(d, dict) else d
    print("Layer-A adapter — does it narrow the over-recall?  (before: stratum-only 500+)\n")
    for v in voices[:6]:
        plc = voice_to_placement(v)
        g = fm.recall_field(plc, v.get("name",""), limit=8)
        nodes = [(sorted(x["axes"]), x["cardinality"], len(x["cards"])) for x in g]
        top = nodes[0] if nodes else None
        print(f"  {v.get('name'):11} pe={plc['substrate_position'].get('pe_note')!s:6} "
              f"placement-axes={sorted(k for k in plc['substrate_position'])} ")
        print(f"               top lattice-node: {top}   (groups: {len(g)})")
