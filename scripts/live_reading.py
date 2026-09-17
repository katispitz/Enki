#!/usr/bin/env python3
"""
live_reading.py — one real instance through the whole stack: helix_address (spatial+
temporal address) x master correspondence table (element/azoth/macro-phase) x 49-cell
fill (interval/aspect/quality), for a real natal moment.

Instance: Kati Spitz natal, 1988-03-31 15:21 UTC (7:21 AM PST, Orange CA 33.7879N/117.8531W).
Source: Babylonia_Houses_OQ_Derivations.txt / locate_entity_v4.py archive usage — the
already-verified reference tuple used throughout the corpus (ASC 15.5 Taurus matches
astro.com). Not invented for this script.
"""
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path.home() / "Nammu" / "engines"))
sys.path.insert(0, str(Path.home() / "Enki" / "substrate"))
sys.path.insert(0, str(Path.home() / "Enki" / "scripts"))

from helix_address import address_of, relation, pair_cell  # noqa: E402
from bounds import ZODIAC_SIGNS  # noqa: E402

NATAL = datetime(1988, 3, 31, 15, 21, 0, tzinfo=timezone.utc)

# from card ec79c27d TABLE 1 (classical 7-planet scope; Pluto/Neptune/Uranus = apex/shock,
# no derived element/azoth of their own)
CORRESPONDENCE = {
    "Sun":     {"vertex_sign": "Taurus",    "sign_element": "Earth", "own_element": "Fire",
                "azoth": "Calcination",   "macro_phase": "Rubedo"},
    "Moon":    {"vertex_sign": "Cancer",    "sign_element": "Water", "own_element": "Water",
                "azoth": "Dissolution",  "macro_phase": "Albedo"},
    "Venus":   {"vertex_sign": "Leo",       "sign_element": "Fire",  "own_element": "unresolved (shock/centroid)",
                "azoth": "shock — no stable operation", "macro_phase": "Nigredo + Citrinitas"},
    "Mars":    {"vertex_sign": "Virgo",     "sign_element": "Earth", "own_element": "Fire",
                "azoth": "Separation",   "macro_phase": "Rubedo + Albedo"},
    "Mercury": {"vertex_sign": "Scorpio",   "sign_element": "Water", "own_element": "Water",
                "azoth": "Conjunction",  "macro_phase": "Citrinitas + Nigredo"},
    "Uranus":  {"vertex_sign": "Sagittarius", "sign_element": "Fire", "own_element": "unresolved (shock/centroid)",
                "azoth": "shock — no stable operation", "macro_phase": "—"},
    "Saturn":  {"vertex_sign": "Capricorn", "sign_element": "Earth", "own_element": "Earth",
                "azoth": "Fermentation", "macro_phase": "Nigredo + Citrinitas"},
    "Jupiter": {"vertex_sign": "Pisces",    "sign_element": "Water", "own_element": "Air",
                "azoth": "Distillation", "macro_phase": "Rubedo + Albedo"},
    "Neptune": {"vertex_sign": "—apex—",    "sign_element": "unresolved", "own_element": "unresolved",
                "azoth": "Coagulation",  "macro_phase": "—"},
    "Pluto":   {"vertex_sign": "—apex—",    "sign_element": "unresolved", "own_element": "unresolved",
                "azoth": "Coagulation",  "macro_phase": "—"},
}

# from card 29455a2b — TABLE 2 (30 content cells) for non-Venus pairs,
# TABLE 3 (12 frame cells) for Venus pairs (Venus x each of 6, directed both ways;
# "Sun x Venus" = motion direction, planet's own cycle crossing the X3 fault)
PAIR_TABLE = {
    ("Sun", "Venus"): ("2nd (mirrors Re)", "Novile (40°)", "mild — pre-shock (motion dir.)"),
    ("Sun", "Moon"): ("2nd", "Novile (40°)", "mild"),
    ("Mars", "Mercury"): ("2nd", "Novile (40°)", "mild"),
    ("Sun", "Saturn"): ("5th", "Trine (120°)", "most consonant"),
    ("Moon", "Jupiter"): ("5th", "Trine (120°)", "most consonant"),
}

PLANETS = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]


def lon_to_sign(lon):
    idx = int(lon % 360 // 30)
    deg_in_sign = lon % 360 - idx * 30
    return ZODIAC_SIGNS[idx], deg_in_sign


def main():
    print(f"LIVE READING — {NATAL.isoformat()} (Kati Spitz natal, Orange CA)\n")
    print("=" * 100)
    print("PER-BODY: zodiac position, address (spatial/temporal), correspondence-table element/azoth")
    print("=" * 100)

    addrs = {}
    for body in PLANETS:
        a = address_of(body, NATAL)
        addrs[body] = a
        sign, deg = lon_to_sign(a["lon"])
        corr = CORRESPONDENCE[body]
        print(f"\n{body}")
        print(f"  lon {a['lon']:6.2f}°  →  {deg:5.2f}° {sign}")
        print(f"  helix address: grid_pos={a['grid_pos']:2} (spatial/60)  "
              f"matrix_pos={a['matrix_pos']:2} row/col={a['row']}/{a['col']} (temporal/49)  "
              f"helix_pos={a['helix_pos']:4}/2940")
        print(f"  correspondence table (own vertex/shock sign = {corr['vertex_sign']}):")
        print(f"    sign-element (Merkaba residency): {corr['sign_element']}   "
              f"own-element (humoral temperament): {corr['own_element']}")
        print(f"    azoth operation: {corr['azoth']}    macro-phase: {corr['macro_phase']}")

    print("\n" + "=" * 100)
    print("PAIR RELATIONS: T(49,60) closure — static pair-cell + motion recall + interval/aspect/quality")
    print("=" * 100)

    pairs = [("Sun", "Venus"), ("Sun", "Moon"), ("Mars", "Mercury"), ("Sun", "Saturn"), ("Moon", "Jupiter")]
    for pa, pb in pairs:
        aa, ab = addrs[pa], addrs[pb]
        rel = relation(aa, ab)
        pc = rel["pair_49"]
        cell_label = pc.get("cell_label", f"off-matrix: {pc.get('reason')}")
        interval, aspect, quality = PAIR_TABLE.get((pa, pb), ("?", "?", "?"))
        print(f"\n{pa} <-> {pb}")
        print(f"  pair_49 (static, §31c): {cell_label}"
              f"{' [CONJUNCTION/unison]' if pc.get('is_conjunction') else ''}")
        print(f"  interval/aspect/quality (29455a2b): {interval} / {aspect} / {quality}")
        print(f"  recall_49 (motion, is this pair-aspect lit right now): {rel['recall_49']}")
        print(f"  helix_gap_2940 (cyclic distance of joint addresses): {rel['helix_gap_2940']}")
        sa, sb = CORRESPONDENCE[pa], CORRESPONDENCE[pb]
        print(f"  elements in play: {pa}={sa['sign_element']}(sign)/{sa['own_element']}(own)   "
              f"{pb}={sb['sign_element']}(sign)/{sb['own_element']}(own)")
        print(f"  azoth ops in play: {pa}={sa['azoth']}   {pb}={sb['azoth']}")

    print("\n" + "=" * 100)
    print("BOUNDARY BODIES: Pluto/Neptune do-boundary collapse, Uranus fault")
    print("=" * 100)
    for body in ("Neptune", "Pluto", "Uranus"):
        rel = relation(addrs["Sun"], addrs[body])
        pc = rel["pair_49"]
        if "cell_label" in pc:
            print(f"  Sun <-> {body:8s}: {pc['cell_label']}  do_boundary={pc.get('do_boundary')}")
        else:
            print(f"  Sun <-> {body:8s}: no-cell — {pc['reason']}")


if __name__ == "__main__":
    main()
