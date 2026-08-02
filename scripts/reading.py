#!/usr/bin/env python3
"""
reading.py — general-purpose reading CLI: full stack (helix_address x master
correspondence table x dynamic interval/aspect/quality) for ANY date/time, not
just one fixed instance.

Generalizes live_reading.py (which stays put as the fixed, validated Kati-natal
reference instance / smoke-test — not touched by this script; same engines,
parametrized here).

pair_49's interval/shock/direction/arm are computed live by
helix_address.relation() from each planet's fixed 49-matrix row — not a
hardcoded per-pair table. The only static lookup here is interval-number ->
(aspect angle name, quality), from card 29455a2b's harmonic map (2nd=Novile,
3rd=Quintile, ... 7th=Sesquiquadrate) — a 6-entry universal mapping, not
per-planet-pair data.

Usage:
  python3 reading.py --natal                             # Kati's natal, exact
  python3 reading.py                                     # right now (UTC)
  python3 reading.py --date 2026-08-01 --time 14:30:00    # explicit UTC moment
  python3 reading.py --date 2026-08-01 --time 14:30:00 --tz America/Los_Angeles
                                                          # same moment, wall-clock local
  python3 reading.py --date 2026-08-01 --time 14:30:00 --tz -7
                                                          # local time via raw UTC offset
  python3 reading.py --date 2026-08-01 --focus Venus      # only pairs involving Venus
  python3 reading.py --date 2026-08-01 --pair Sun Saturn  # just one pair

--date/--time are UTC by default. Pass --tz (an IANA zone name, e.g.
America/Los_Angeles, or a raw UTC offset like -7 / +5:30) to type wall-clock
local time instead — it's converted to UTC internally before any ephemeris
call. IANA names are DST-aware (correct offset for the actual date given);
raw offsets are not (you supply the exact offset for that moment yourself).
"""
import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path.home() / "Nammu" / "engines"))
sys.path.insert(0, str(Path.home() / "Enki" / "substrate"))
sys.path.insert(0, str(Path.home() / "Enki" / "scripts"))

from helix_address import address_of, relation  # noqa: E402
from bounds import ZODIAC_SIGNS  # noqa: E402
from locate_entity_v4 import locate as _locate  # noqa: E402

NATAL_KATI = datetime(1988, 3, 31, 15, 21, 0, tzinfo=timezone.utc)

_OFFSET_RE = re.compile(r"^([+-]?\d{1,2})(?::?(\d{2}))?$")


def _resolve_tz(tz_str):
    """--tz argument -> tzinfo. Accepts an IANA zone name (DST-aware, e.g.
    'America/Los_Angeles') or a raw UTC offset ('-7', '-7:00', '+5:30', not
    DST-aware — the offset given is used exactly as-is for that moment)."""
    if tz_str is None or tz_str.upper() == "UTC":
        return timezone.utc
    m = _OFFSET_RE.match(tz_str)
    if m:
        hours = int(m.group(1))
        minutes = int(m.group(2) or 0)
        sign = -1 if hours < 0 or tz_str.strip().startswith("-") else 1
        return timezone(timedelta(hours=hours, minutes=sign * minutes))
    try:
        return ZoneInfo(tz_str)
    except Exception as exc:
        raise ValueError(
            f"Unrecognized --tz {tz_str!r}: not a UTC offset (e.g. -7, +5:30) "
            f"and not a known IANA zone name (e.g. America/Los_Angeles). ({exc})"
        ) from exc

# from card ec79c27d TABLE 1 (classical 7-planet scope; Pluto/Neptune/Uranus = apex/
# shock, no derived element/azoth of their own — cards 561b4d97/05cbdc1c record a
# proposed-then-retracted attempt to resolve "unresolved"; it stands as written here)
#
# Mercury's own_element ("Water") is its correct Babylonia-derived value (dry/wet x
# hot/cold composition) but has no classical counterpart to validate against — Ptolemy
# (Tetrabiblos I.6) gives Mercury no fixed quality at all, it explicitly alternates.
# See card e784a1e0 (corrects the "6-for-6 classical match" overclaim in card 1a093d6a).
CORRESPONDENCE = {
    "Sun":     {"vertex_sign": "Taurus",    "sign_element": "Earth", "own_element": "Fire",
                "azoth": "Calcination",  "macro_phase": "Rubedo"},
    "Moon":    {"vertex_sign": "Cancer",    "sign_element": "Water", "own_element": "Water",
                "azoth": "Dissolution", "macro_phase": "Albedo"},
    "Venus":   {"vertex_sign": "Leo",       "sign_element": "Fire",  "own_element": "unresolved (shock/centroid)",
                "azoth": "shock — no stable operation", "macro_phase": "Nigredo + Citrinitas"},
    "Mars":    {"vertex_sign": "Virgo",     "sign_element": "Earth", "own_element": "Fire",
                "azoth": "Separation",  "macro_phase": "Rubedo + Albedo"},
    "Mercury": {"vertex_sign": "Scorpio",   "sign_element": "Water", "own_element": "Water",
                "azoth": "Conjunction", "macro_phase": "Citrinitas + Nigredo"},
    "Uranus":  {"vertex_sign": "Sagittarius", "sign_element": "Fire", "own_element": "unresolved (shock/centroid)",
                "azoth": "shock — no stable operation", "macro_phase": "—"},
    "Saturn":  {"vertex_sign": "Capricorn", "sign_element": "Earth", "own_element": "Earth",
                "azoth": "Fermentation", "macro_phase": "Nigredo + Citrinitas"},
    "Jupiter": {"vertex_sign": "Pisces",    "sign_element": "Water", "own_element": "Air",
                "azoth": "Distillation", "macro_phase": "Rubedo + Albedo"},
    "Neptune": {"vertex_sign": "—apex—",    "sign_element": "unresolved", "own_element": "unresolved",
                "azoth": "Coagulation", "macro_phase": "—"},
    "Pluto":   {"vertex_sign": "—apex—",    "sign_element": "unresolved", "own_element": "unresolved",
                "azoth": "Coagulation", "macro_phase": "—"},
}

# card 29455a2b harmonic map: interval-number -> (aspect angle name, quality).
# Universal (not per-pair) — the per-pair interval itself comes from
# helix_address.relation()'s pair_49.skeleton.
_INTERVAL_ASPECT = {
    "2nd": ("Novile (40°)",        "mild"),
    "3rd": ("Quintile (72°)",      "consonant"),
    "4th": ("Square (90°)",        "dissonant"),
    "5th": ("Trine (120°)",        "most consonant"),
    "6th": ("Biquintile (144°)",   "consonant"),
    "7th": ("Sesquiquadrate (135°)", "strong dissonance"),
}

ALL_PLANETS = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]


def lon_to_sign(lon):
    idx = int(lon % 360 // 30)
    deg_in_sign = lon % 360 - idx * 30
    return ZODIAC_SIGNS[idx], deg_in_sign


def body_data(body, addrs):
    """Structured per-body reading: zodiac position, helix address, correspondence
    table. Pure data — print_bodies() formats this for the terminal; the Navigator
    route jsonifies it directly. Single computation path either way."""
    a = addrs[body]
    sign, deg = lon_to_sign(a["lon"])
    corr = CORRESPONDENCE[body]
    return {
        "body": body,
        "lon": a["lon"],
        "sign": sign,
        "deg_in_sign": deg,
        "grid_pos": a["grid_pos"],
        "matrix_pos": a["matrix_pos"],
        "row": a["row"],
        "col": a["col"],
        "helix_pos": a["helix_pos"],
        "correspondence": corr,
    }


def pair_data(pa, pb, addrs):
    """Structured pair-relation: pair_49 cell (or honest no-cell), interval/aspect/
    quality, recall_49, helix_gap, elements/azoth in play. Same source for CLI and
    Navigator — see body_data()."""
    aa, ab = addrs[pa], addrs[pb]
    rel = relation(aa, ab)
    pc = rel["pair_49"]
    out = {
        "a": pa, "b": pb,
        "recall_49": rel["recall_49"],
        "helix_gap_2940": rel["helix_gap_2940"],
        "elements": {pa: CORRESPONDENCE[pa], pb: CORRESPONDENCE[pb]},
    }
    if "cell_label" in pc:
        skel = pc["skeleton"]
        interval = skel["interval"]
        aspect, quality = _INTERVAL_ASPECT.get(interval, ("?", "?"))
        out.update({
            "has_cell": True,
            "cell_label": pc["cell_label"],
            "is_conjunction": pc.get("is_conjunction", False),
            "do_boundary": pc.get("do_boundary"),
            "interval": interval, "aspect": aspect, "quality": quality,
            "shock_load": skel["shock_load"],
            "octave_sense": skel["octave_sense"],
            "arm_relation": skel["arm_relation"],
        })
    else:
        out.update({"has_cell": False, "reason": pc.get("reason")})
    return out


def print_bodies(addrs):
    print("=" * 100)
    print("PER-BODY: zodiac position, address (spatial/temporal), correspondence-table element/azoth")
    print("=" * 100)
    for body in ALL_PLANETS:
        d = body_data(body, addrs)
        corr = d["correspondence"]
        print(f"\n{body}")
        print(f"  lon {d['lon']:6.2f}°  →  {d['deg_in_sign']:5.2f}° {d['sign']}")
        print(f"  helix address: grid_pos={d['grid_pos']:2} (spatial/60)  "
              f"matrix_pos={d['matrix_pos']:2} row/col={d['row']}/{d['col']} (temporal/49)  "
              f"helix_pos={d['helix_pos']:4}/2940")
        print(f"  correspondence table (own vertex/shock sign = {corr['vertex_sign']}):")
        print(f"    sign-element (Merkaba residency): {corr['sign_element']}   "
              f"own-element (humoral temperament): {corr['own_element']}")
        print(f"    azoth operation: {corr['azoth']}    macro-phase: {corr['macro_phase']}")


def print_pair(pa, pb, addrs):
    d = pair_data(pa, pb, addrs)
    print(f"\n{pa} <-> {pb}")
    if d["has_cell"]:
        print(f"  pair_49 (static, §31c): {d['cell_label']}"
              f"{' [CONJUNCTION/unison]' if d['is_conjunction'] else ''}")
        if d["do_boundary"]:
            print(f"  do_boundary: {d['do_boundary']} — Pluto/Neptune read via Venus's frame cell")
        print(f"  interval/aspect/quality: {d['interval']} / {d['aspect']} / {d['quality']}"
              f"  (shock_load={d['shock_load']}, {d['octave_sense']}, {d['arm_relation']})")
    else:
        print(f"  pair_49: no-cell — {d['reason']}")
    print(f"  recall_49 (motion, is this pair-aspect lit right now): {d['recall_49']}")
    print(f"  helix_gap_2940 (cyclic distance of joint addresses): {d['helix_gap_2940']}")
    sa, sb = d["elements"][pa], d["elements"][pb]
    print(f"  elements in play: {pa}={sa['sign_element']}(sign)/{sa['own_element']}(own)   "
          f"{pb}={sb['sign_element']}(sign)/{sb['own_element']}(own)")
    print(f"  azoth ops in play: {pa}={sa['azoth']}   {pb}={sb['azoth']}")


def print_pairs(addrs, focus=None, only_pair=None):
    print("\n" + "=" * 100)
    print("PAIR RELATIONS: T(49,60) closure — static pair-cell + motion recall + interval/aspect/quality")
    print("=" * 100)
    if only_pair:
        pa, pb = only_pair
        for p in (pa, pb):
            if p not in ALL_PLANETS:
                print(f"\n{p!r} is not a known body (known: {', '.join(ALL_PLANETS)})")
                return
        print_pair(pa, pb, addrs)
        return
    for i, pa in enumerate(ALL_PLANETS):
        for pb in ALL_PLANETS[i + 1:]:
            if focus and focus not in (pa, pb):
                continue
            print_pair(pa, pb, addrs)


def ascendant_data(when, lat, lon):
    """ASC + whole-sign houses via locate_entity_v4.locate() — the same engine
    natal.py uses. None if lat/lon not supplied (locate() needs both)."""
    loc = _locate(when.year, when.month, when.day, when.hour, when.minute, when.second,
                  birth_lat=lat, birth_lon=lon)
    return loc.get("ascendant")


def full_reading(when, lat=None, lon=None, focus=None, only_pair=None):
    """Top-level: one JSON-serializable dict, the single source both the CLI
    formatter and the Navigator /api/reading route consume."""
    addrs = {body: address_of(body, when) for body in ALL_PLANETS}
    bodies = {body: body_data(body, addrs) for body in ALL_PLANETS}

    if only_pair:
        pairs = [pair_data(*only_pair, addrs)] if all(p in ALL_PLANETS for p in only_pair) else []
    else:
        pairs = [
            pair_data(pa, pb, addrs)
            for i, pa in enumerate(ALL_PLANETS)
            for pb in ALL_PLANETS[i + 1:]
            if not focus or focus in (pa, pb)
        ]

    ascendant = ascendant_data(when, lat, lon) if (lat is not None and lon is not None) else None

    return {
        "when_utc": when.isoformat(),
        "bodies": bodies,
        "pairs": pairs,
        "ascendant": ascendant,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="YYYY-MM-DD (wall-clock local if --tz given, else UTC)")
    ap.add_argument("--time", default="12:00:00", help="HH:MM[:SS] (wall-clock local if --tz given, else UTC; default 12:00:00)")
    ap.add_argument("--tz", default="UTC",
                     help="timezone for --date/--time: IANA name (e.g. America/Los_Angeles, "
                          "DST-aware) or raw UTC offset (e.g. -7, +5:30, not DST-aware). Default UTC.")
    ap.add_argument("--natal", action="store_true", help="shortcut: Kati's natal (1988-03-31 15:21 UTC / 7:21 AM PST)")
    ap.add_argument("--label", default=None, help="free-text label for the header")
    ap.add_argument("--focus", help="only show pairs involving this planet")
    ap.add_argument("--pair", nargs=2, metavar=("PLANET_A", "PLANET_B"), help="only show this one pair")
    args = ap.parse_args()

    local_repr = None
    if args.natal:
        when = NATAL_KATI
        label = args.label or "Kati Spitz natal, Orange CA"
    elif args.date:
        time_str = args.time if args.time.count(":") == 2 else args.time + ":00"
        naive = datetime.strptime(f"{args.date} {time_str}", "%Y-%m-%d %H:%M:%S")
        tz = _resolve_tz(args.tz)
        local_dt = naive.replace(tzinfo=tz)
        when = local_dt.astimezone(timezone.utc)
        if args.tz.upper() != "UTC":
            local_repr = f"{naive.isoformat()} {args.tz}"
        label = args.label or ""
    else:
        when = datetime.now(timezone.utc)
        label = args.label or "now"

    header = f"READING — {when.isoformat()} UTC"
    if local_repr:
        header += f"  ({local_repr} local)"
    if label:
        header += f" ({label})"
    print(header + "\n")

    addrs = {body: address_of(body, when) for body in ALL_PLANETS}

    print_bodies(addrs)
    print_pairs(addrs, focus=args.focus, only_pair=args.pair)


if __name__ == "__main__":
    main()
