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

try:
    import numpy as _np
except Exception:                                     # pragma: no cover
    _np = None


def _jsonable(obj):
    """Recursively convert numpy scalar types (np.float64/np.bool_/np.int64,
    surfaced by several downstream engines — e.g. helix_geometry's k_helix/
    delta_phase, this session's own chart-lon cross-check) into native Python
    types. json.dumps/Flask's jsonify both reject raw numpy scalars outright —
    confirmed the hard way: full_reading()'s output 500'd through Flask before
    this existed. Applied once at full_reading()'s return, not scattered
    per-field, so nothing downstream has to remember to do this."""
    if _np is not None and isinstance(obj, _np.generic):
        return obj.item()
    if isinstance(obj, dict):
        return {k: _jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_jsonable(v) for v in obj]
    return obj

sys.path.insert(0, str(Path.home() / "Nammu" / "engines"))
sys.path.insert(0, str(Path.home() / "Enki" / "substrate"))
sys.path.insert(0, str(Path.home() / "Enki" / "scripts"))

from helix_address import address_of, relation  # noqa: E402
from bounds import ZODIAC_SIGNS  # noqa: E402
from substrate_at import substrate_at  # noqa: E402
from solid_phase import solid_phase as _solid_phase  # noqa: E402
from chart import full_chart as _full_chart  # noqa: E402

# Cross-pipeline honesty check: full_chart()'s planet longitudes come from
# locate_entity_v4.locate() (its own DE441-primary call), a DIFFERENT code path
# from substrate_at()/address_of() (also DE441-primary, via ephem_de441.py
# directly) even though both should agree closely for in-range dates. Flag,
# don't silently trust, if they ever drift apart — same discipline as the
# Sun-sign bug this session started from.
_LON_CROSS_CHECK_TOLERANCE_DEG = 0.05

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
# "unison" (diagonal/conjunction, 0° separation — same row, e.g. Neptune/Pluto/Venus
# collapsing onto one another via the do-boundary) isn't in card 29455a2b's harmonic
# map at all — that table only covers the 6 off-diagonal intervals. Not a lookup miss;
# there's no angle to name for 0° separation. Labeled directly rather than left blank.
_INTERVAL_ASPECT = {
    "unison": ("Conjunction (0°)", "unison"),
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


def body_data(body, addrs, functions=None, chart_substrate=None):
    """Structured per-body reading. Pure data — print_bodies() formats this for
    the terminal; the Navigator route jsonifies it directly. Single computation
    path either way.

    Four provenance-distinct layers, kept in separate keys rather than flattened
    together, because several of them use similar-sounding names for DIFFERENT
    things (e.g. this dict's own "grid_pos" (helix_geometry, from tropical lon)
    vs chart_substrate's "grid" (natal.py's own project(), a different
    computation) — flattening them risks exactly the kind of same-word/
    different-primitive confusion the zodiac-vs-matrix aspect split already
    guards against.

      (top-level)       — zodiac position + helix address (helix_address.address_of)
      correspondence    — static per-planet reference table (card ec79c27d)
      activation        — Wu Xing phase + counter-rotation state for THIS planet
                           at THIS moment (substrate_at().functions[body])
      chart             — dignity/bound/houses(3 systems)/vedic/PE-ring/cell-
                           signature (chart.py's full_chart(), archetype-free
                           'substrate' partition only — output_contract.py's own
                           contract guarantees no myth/figure-name content here)
    """
    a = addrs[body]
    sign, deg = lon_to_sign(a["lon"])
    corr = CORRESPONDENCE[body]
    out = {
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
        "activation": None,
        "chart": None,
        "lon_cross_check": None,
    }
    if functions is not None:
        act = functions.get("activation") or {}
        out["activation"] = {
            "tet_side": functions.get("tet_side"),
            "rotation_angle_deg": act.get("rotation_angle_deg"),
            "arc_direction": act.get("arc_direction"),
            "frame": act.get("frame"),
            "wu_xing_phase": act.get("wu_xing_phase"),
        }
    if chart_substrate is not None:
        out["chart"] = {k: v for k, v in chart_substrate.items() if k != "ecl"}
        chart_lon = (chart_substrate.get("ecl") or [None])[0]
        if chart_lon is not None:
            delta = abs(((chart_lon - a["lon"] + 180) % 360) - 180)
            out["lon_cross_check"] = {
                "chart_lon": round(chart_lon, 4),
                "delta_deg": round(delta, 4),
                "agrees": delta <= _LON_CROSS_CHECK_TOLERANCE_DEG,
            }
    return out


def pair_data(pa, pb, addrs):
    """Structured pair-relation across BOTH of relation()'s axes — they are not
    redundant and can disagree by name (e.g. Sun<->Saturn: matrix-interval says
    "5th"/Trine, real zodiacal angle says square):

      pair_49 (here: interval/aspect/quality/shock_load/...) — the STATIC 49-matrix
        planet-PAIR cell; "aspect" here is a harmonic-interval label from card
        29455a2b's map (matrix-ROW distance, not sky position).
      spatial_60 (here: zodiac_*) — the REAL angular aspect from each body's actual
        ecliptic longitude (conjunction/sextile/square/trine/quincunx/opposition/
        semi-sextile), zero-orb sign-based (aspect_lattice.py, §31c divisor-stars).

    Same source for CLI and Navigator — see body_data()."""
    aa, ab = addrs[pa], addrs[pb]
    rel = relation(aa, ab)
    pc = rel["pair_49"]
    spatial = rel.get("spatial_60") or {}
    out = {
        "a": pa, "b": pb,
        "recall_49": rel["recall_49"],
        "helix_gap_2940": rel["helix_gap_2940"],
        "elements": {pa: CORRESPONDENCE[pa], pb: CORRESPONDENCE[pb]},
        "zodiac_aspect": spatial.get("aspect"),
        "zodiac_sign_offset": spatial.get("sign_offset"),
        "zodiac_line_type": spatial.get("line_type"),
        "zodiac_unavailable": spatial.get("unavailable"),
        # polyhedral-shell relation (real face-graph, not vertex-index arithmetic) —
        # per solid, is this pair co-resident/adjacent/antipodal/disjoint. Same
        # aspect_lattice.aspect() call as zodiac_aspect above, previously unused.
        "shells": spatial.get("shells"),
        "shared_shell_cells": spatial.get("shared_shell_cells"),
        # enneagram (§16 hexad/triangle lines) between the two bodies' PE points
        "enneagram": spatial.get("enneagram"),
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


def print_top_level(result):
    """The stuff that isn't per-body or per-pair: Merkaba orientation, the real
    Fire/Air/Earth/Water/Aether rotation-zone (solid_phase — a DIFFERENT 5-fold
    system than orientation's own Wu Xing clock, don't conflate the two), ASC/
    houses/lots (empty if no lat/lon), PE-node firings, and the cross-ephemeris
    honesty check."""
    print("=" * 100)
    print("MOMENT: Merkaba orientation, rotation-phase zone, angles/houses/lots")
    print("=" * 100)
    o = result["orientation"]
    print(f"  rotation: father={o['father_angle_deg']:.2f}°  mother={o['mother_angle_deg']:.2f}°"
          f"  (axis={o['rotation_axis']})")
    print(f"  Wu Xing clock (Venus 72° symmetry-5, separate from the zone below): "
          f"{o['wu_xing_phase']}  [{o['period_status']}]")
    sp = result["solid_phase"]
    est = " [ESTIMATE]" if sp.get("is_estimate") else ""
    print(f"  rotation-phase zone (canon §8/9, Tet/Oct/Cube/Ico/Dodec -> Fire/Air/Earth/Water/Aether): "
          f"{sp['phase_name']} / {sp['element']}{est}  (tithi {sp['tithi_in_cycle']} of 30, {sp['half']})")
    if result["ascendant"]:
        a = result["ascendant"]
        print(f"  ASC {a['asc_lon']:.3f}°  MC {a['mc_lon']:.3f}°  "
              f"DESC {a['desc_lon']:.3f}°  IC {a['ic_lon']:.3f}°  sect={a['sect']}")
        for mode, houses in result["houses"].items():
            print(f"  houses ({mode}): " + ", ".join(f"{p}=H{h}" for p, h in houses.items() if isinstance(h, int)))
        if result["lots"]:
            print("  lots: " + ", ".join(
                f"{name}={l['sign']} {l['lon_in_sign']:.1f}°" for name, l in result["lots"].items()
                if isinstance(l, dict) and "sign" in l))
    else:
        print("  ASC/houses/lots: unavailable (no lat/lon given)")
    if result["pe_firing"]:
        for f in result["pe_firing"]:
            print(f"  pe_firing: {f['planet']} within {abs(f['deviation_deg']):.2f}° of {f['pe']} (grid {f['grid']})")
    if result["lon_cross_check_mismatches"]:
        print("  ⚠ cross-ephemeris mismatch (substrate_at vs chart.py DE441 paths disagree):")
        for m in result["lon_cross_check_mismatches"]:
            print(f"    {m['body']}: Δ={m['delta_deg']}° (chart_lon={m['chart_lon']})")


def print_bodies(bodies):
    print("\n" + "=" * 100)
    print("PER-BODY: zodiac position, address (spatial/temporal), correspondence-table element/azoth")
    print("=" * 100)
    for body in ALL_PLANETS:
        d = bodies[body]
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
        if d["activation"]:
            act = d["activation"]
            print(f"  activation: tet_side={act['tet_side']}  wu_xing={act['wu_xing_phase']}"
                  + (f"  rotation={act['rotation_angle_deg']:.1f}° ({act['arc_direction']})"
                     if act["rotation_angle_deg"] is not None else ""))
        if d["chart"]:
            c = d["chart"]
            dig = c.get("dignity")
            dig_str = f"score={dig['score']} {'/'.join(dig['dignities']) or 'peregrine'}" if dig else "n/a (modern planet)"
            print(f"  chart: dignity={dig_str}  bound={c.get('bound')}  "
                  f"PE={c.get('pe_pt')}/{c.get('pe_role')}  ring={c.get('ring')} ({c.get('ring_mechanism')})")
            if c.get("house_whole_sign") is not None:
                print(f"    houses: whole-sign=H{c['house_whole_sign']}  porphyry=H{c['house_porphyry']}  "
                      f"placidus=H{c['house_placidus']}")
            v = c.get("vedic") or {}
            nak = v.get("nakshatra") or {}
            if nak:
                print(f"    vedic: sidereal {v['sidereal_lon']:.2f}°  nakshatra={nak.get('name')} "
                      f"pada={nak.get('pada')}  navamsa={((v.get('navamsa') or {}).get('navamsa_sign'))}")
            print(f"    active cell (this planet's row x today's column): "
                  f"{c.get('cell_x_active_col')} / {c.get('cell_x_active_element_pair')} / {c.get('cell_x_active_phase_delta')}")
        if d["lon_cross_check"] and not d["lon_cross_check"]["agrees"]:
            print(f"  ⚠ lon cross-check mismatch: chart_lon={d['lon_cross_check']['chart_lon']}"
                  f" (Δ={d['lon_cross_check']['delta_deg']}°)")


def print_pair(d):
    pa, pb = d["a"], d["b"]
    print(f"\n{pa} <-> {pb}")
    if d["zodiac_unavailable"]:
        print(f"  zodiac aspect (real angle, §31c spatial-60): unavailable — {d['zodiac_unavailable']}")
    else:
        print(f"  zodiac aspect (real angle, §31c spatial-60): {d['zodiac_aspect']}"
              f"  (sign_offset={d['zodiac_sign_offset']}, {d['zodiac_line_type']})")
    if d.get("shells"):
        shell_bits = [f"{name}={rel['relation']}" for name, rel in d["shells"].items()]
        print("    polyhedral shells: " + ", ".join(shell_bits))
    if d.get("enneagram") and d["enneagram"].get("relations"):
        print(f"    enneagram (§16): {d['enneagram']['planet_a']}<->{d['enneagram']['planet_b']} "
              f"{d['enneagram']['relations']}")
    if d["has_cell"]:
        print(f"  pair_49 (static, §31c): {d['cell_label']}"
              f"{' [CONJUNCTION/unison]' if d['is_conjunction'] else ''}")
        if d["do_boundary"]:
            print(f"  do_boundary: {d['do_boundary']} — Pluto/Neptune read via Venus's frame cell")
        print(f"  matrix interval/aspect/quality (harmonic map, NOT the zodiac angle above): "
              f"{d['interval']} / {d['aspect']} / {d['quality']}"
              f"  (shock_load={d['shock_load']}, {d['octave_sense']}, {d['arm_relation']})")
    else:
        print(f"  pair_49: no-cell — {d['reason']}")
    print(f"  recall_49 (motion, is this pair-aspect lit right now): {d['recall_49']}")
    print(f"  helix_gap_2940 (cyclic distance of joint addresses): {d['helix_gap_2940']}")
    sa, sb = d["elements"][pa], d["elements"][pb]
    print(f"  elements in play: {pa}={sa['sign_element']}(sign)/{sa['own_element']}(own)   "
          f"{pb}={sb['sign_element']}(sign)/{sb['own_element']}(own)")
    print(f"  azoth ops in play: {pa}={sa['azoth']}   {pb}={sb['azoth']}")


def print_pairs(pairs):
    print("\n" + "=" * 100)
    print("PAIR RELATIONS: T(49,60) closure — static pair-cell + motion recall + interval/aspect/quality")
    print("=" * 100)
    if not pairs:
        print("\n(no pairs — check --pair planet names against ALL_PLANETS)")
        return
    for d in pairs:
        print_pair(d)


def full_reading(when, lat=None, lon=None, focus=None, only_pair=None):
    """Top-level: one JSON-serializable dict, the single source both the CLI
    formatter and the Navigator /api/reading route consume.

    Composes THREE substrate-true (archetype-free) sources for one moment:
      1. helix_address.address_of()/relation() — the T(49,60) joint address +
         pair relations (both aspect axes: zodiac angle + matrix interval).
      2. substrate_at() — Merkaba orientation (father/mother counter-rotation +
         Wu Xing phase), per-planet activation, PE-node firings. Time-only,
         no location needed.
      3. chart.py's full_chart() — dignity, bound, houses (whole-sign/porphyry/
         placidus), vedic (sidereal/nakshatra/navamsa), lots, karana, PE/ring/
         cell-signature. Runs with or without lat/lon (houses+lots need it,
         everything else doesn't); output_contract.py's partition() guarantees
         its 'substrate' block carries no archetype/myth content — that's the
         ONLY block used here, matching the explicit scope of this tool (card
         29455a2b: "no archetype/myth content included anywhere... by design").
    """
    addrs = {body: address_of(body, when) for body in ALL_PLANETS}

    sub_state = substrate_at(when)
    orientation = sub_state["orientation"]
    phase = _solid_phase(sub_state["helix"]["cumul_tithi"])
    pe_firing = sub_state["pe_firing"]

    chart_result = _full_chart(when.year, when.month, when.day,
                                when.hour, when.minute, when.second,
                                birth_lat=lat, birth_lon=lon)
    chart_planets = chart_result["planets"]

    bodies = {
        body: body_data(
            body, addrs,
            functions=sub_state["functions"].get(body),
            chart_substrate=chart_planets.get(body, {}).get("substrate"),
        )
        for body in ALL_PLANETS
    }

    lon_mismatches = [
        {"body": b, **d["lon_cross_check"]}
        for b, d in bodies.items()
        if d["lon_cross_check"] and not d["lon_cross_check"]["agrees"]
    ]

    if only_pair:
        pairs = [pair_data(*only_pair, addrs)] if all(p in ALL_PLANETS for p in only_pair) else []
    else:
        pairs = [
            pair_data(pa, pb, addrs)
            for i, pa in enumerate(ALL_PLANETS)
            for pb in ALL_PLANETS[i + 1:]
            if not focus or focus in (pa, pb)
        ]

    asc_lon = chart_result["meta"].get("asc_lon")
    ascendant = None
    if asc_lon is not None:
        ascendant = {
            "asc_lon": asc_lon,
            "mc_lon": chart_result["meta"].get("mc_lon"),
            "desc_lon": chart_result["meta"].get("desc_lon"),
            "ic_lon": chart_result["meta"].get("ic_lon"),
            "sect": chart_result["meta"]["sect"],
        }

    return _jsonable({
        "when_utc": when.isoformat(),
        "bodies": bodies,
        "pairs": pairs,
        "ascendant": ascendant,
        "houses": chart_result["houses"],       # {} if no lat/lon
        "lots": chart_result["lots"],           # {} if no lat/lon
        "temporal": chart_result["temporal"],   # karana + solid_phase (chart.py's own copy)
        "orientation": orientation,             # Merkaba rotation state (Wu Xing clock)
        "solid_phase": phase,                   # Fire/Air/Earth/Water/Aether rotation-zone (canon §8/9)
        "pe_firing": pe_firing,                 # planets currently within orb of a PE node
        "lon_cross_check_mismatches": lon_mismatches,  # empty list = the two ephemeris paths agree
    })


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="YYYY-MM-DD (wall-clock local if --tz given, else UTC)")
    ap.add_argument("--time", default="12:00:00", help="HH:MM[:SS] (wall-clock local if --tz given, else UTC; default 12:00:00)")
    ap.add_argument("--tz", default="UTC",
                     help="timezone for --date/--time: IANA name (e.g. America/Los_Angeles, "
                          "DST-aware) or raw UTC offset (e.g. -7, +5:30, not DST-aware). Default UTC.")
    ap.add_argument("--natal", action="store_true", help="shortcut: Kati's natal (1988-03-31 15:21 UTC / 7:21 AM PST)")
    ap.add_argument("--lat", type=float, default=None, help="birth latitude (unlocks ASC/houses/lots/dignity-sect)")
    ap.add_argument("--lon", type=float, default=None, help="birth longitude")
    ap.add_argument("--label", default=None, help="free-text label for the header")
    ap.add_argument("--focus", help="only show pairs involving this planet")
    ap.add_argument("--pair", nargs=2, metavar=("PLANET_A", "PLANET_B"), help="only show this one pair")
    args = ap.parse_args()

    local_repr = None
    lat, lon = args.lat, args.lon
    if args.natal:
        when = NATAL_KATI
        if lat is None and lon is None:
            lat, lon = 33.7879, -117.8531   # Orange, CA — same natal reference as live_reading.py
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

    only_pair = tuple(args.pair) if args.pair else None
    result = full_reading(when, lat=lat, lon=lon, focus=args.focus, only_pair=only_pair)

    print_top_level(result)
    print_bodies(result["bodies"])
    print_pairs(result["pairs"])


if __name__ == "__main__":
    main()
