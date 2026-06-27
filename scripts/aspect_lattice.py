#!/usr/bin/env python3
"""
aspect_lattice.py — aspect(A,B) as the §31c LATTICE-RELATION between two bodies'
substrate cells. NO weights, NO orb. Generalizes field_memory's per-axis equality
predicate (= conjunction/co-residency) to the per-axis OFFSET → §31c line-type.

Fork #1 carrier: geo_engine.full_address(lon,lat) (multi-shell face-bary address).
Fork #2 (resolved): aspect = categorical lattice-relation, the field_memory primitive
applied body↔body. Aspect ≡ memory-recall.

§31c traversal-morphism law (canon, FINDINGS_037) — the SAME three line-types on
every substrate node-set, not just the zodiac:
  • POLYGON {N}  adjacency (+1)  → chronological / sequential (Cronus, "circle line")
  • STAR {N/k}   divisor-skip    → qualitative / transformational (Kairos, the aspects)
  • SHOCK/triangle (opposition / 3·6·9) → supervisory intervention (§16)
  • co-residency (offset 0)      → conjunction (shared cell)
  • coprime non-divisor step     → no direct line (disjoint)

Per-axis residency of the law:
  1. ANGULAR (zodiac N=12 / 60-grid)  — sign-offset → divisor-star. Exact, integer.
  2. POLYHEDRAL SHELLS (cube/oct/merkaba/ico/dodec) — the relation is read off each
     solid's REAL face-graph. Co-residency = the CELL a body falls in (its containing
     face, barycentrically determined), NOT the nearest vertex: same face = conjunction;
     faces sharing an EDGE = polygon adjacency; ANTIPODAL faces = opposition/shock-axis;
     else disjoint. Vertex/face idx is an enumeration label, NOT a cyclic position — so
     we use the face-edge + antipode geometry, never index arithmetic, on these shells.

  FRAME: longitudes are SUBSTRATE/grid-frame (lon 0 = Sun's U1 Merkaba home = tropical
  30°), the frame substrate_at() emits and geo_engine was built in. aspect_at() feeds
  this automatically. Pass substrate-frame lon to raw aspect(); not tropical-of-date.
  3. ENNEAGRAM (N=9 hexad/triangle) — DELEGATED to substrate_relationality's canon
     tables (HEXAD_LINES §16 1→4→2→8→5→7, TRIANGLE_LINES X3→X6→Do, Law-of-Three
     3·6·9 membership). Body→PE-pt→planet, then look up the line between the pair.

Zero weights, zero orb anywhere. Sign-based binary (Aspects_v2): the relation holds
by which CELL each body occupies, not by degree-distance.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / "Nammu" / "engines"))
import geo_engine as ge
import substrate_relationality as sr

# ── 1. ANGULAR AXIS — §31c divisor-stars on the 12-fold (5 grid = 1 sign = 30°) ──
# sign-offset → (name, §31c divisor-star description, line_type)
SIGN_ASPECT = {
    0:  ("conjunction",  "co-residency (shared cell)",        "conjunction"),
    1:  ("semi-sextile", "circle / polygon adjacency (+1)",   "polygon"),
    2:  ("sextile",      "divisor-star step-2 (hexagons)",    "star"),
    3:  ("square",       "divisor-star step-3 (4 squares)",   "star"),
    4:  ("trine",        "divisor-star step-4 (3 triangles)", "star"),
    5:  ("quincunx",     "coprime step-5 (no shared edge)",   "disjoint"),
    6:  ("opposition",   "divisor-star step-6 (axis)",        "shock"),
}

def _sign(lon):  # 0..11
    return int((lon % 360) // 30)

def _angular(lon_a, lon_b):
    off = abs(_sign(lon_a) - _sign(lon_b))
    off = min(off, 12 - off)               # fold to 0..6 (aspects are symmetric)
    name, kind, line = SIGN_ASPECT[off]
    return {"sign_offset": off, "aspect": name, "lattice_class": kind, "line_type": line}


# ── 2. POLYHEDRAL SHELLS — relation read off each solid's real edge+antipode graph ──
_SHELL_LOCATORS = {
    "inner_cube":   ge.INNER_CUBE,
    "octahedron":   ge.OCTAHEDRON,
    "merkaba":      ge.MERKABA,
    "icosahedron":  ge.ICOSAHEDRON,
    "dodecahedron": ge.DODECAHEDRON,
}

def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def _unit(v):
    m = (v[0] ** 2 + v[1] ** 2 + v[2] ** 2) ** 0.5 or 1.0
    return (v[0] / m, v[1] / m, v[2] / m)

def _face_centroid(L, f):
    vs = [L.vertices[k][1] for k in f[1:4]]      # f = (label, ia, ib, ic)
    return _unit(tuple(sum(c) / 3.0 for c in zip(*vs)))

def _cell_id(label):
    """Canonical CELL of a face. The locators triangulate square/pentagon faces into
    sub-triangles ('CQ0a'/'CQ0b', 'P5a'/'P5b'); the substrate cell is the whole
    square/pentagon, so collapse a trailing sub-triangle letter (digit+lower-letter).
    Triangular-face shells (oct F1.., ico F14, merkaba Father-..) are already cells."""
    if not label:
        return None
    geo = label.split("/")[0]                       # geometric tag, drop name suffix
    if len(geo) >= 2 and geo[-1].islower() and geo[-2].isdigit():
        geo = geo[:-1]                              # 'P5b' → 'P5', 'CQ0b' → 'CQ0'
    return geo

def _cell_adjacency(L):
    """Canonical-cell adjacency: two cells share an edge if any of their sub-faces
    share an edge (2 vertices). Built once per shell from the real face graph."""
    faces = L.faces
    cell_of = [_cell_id(f[0]) for f in faces]
    vsets = [frozenset(f[1:4]) for f in faces]
    adj = set()
    for i in range(len(faces)):
        for j in range(i + 1, len(faces)):
            if cell_of[i] != cell_of[j] and len(vsets[i] & vsets[j]) == 2:
                adj.add((cell_of[i], cell_of[j])); adj.add((cell_of[j], cell_of[i]))
    return adj

_SHELL_ADJ = {name: _cell_adjacency(L) for name, L in _SHELL_LOCATORS.items()}

def _shell_relation(addr_a, addr_b, addr_a_anti):
    """Per-shell §31c line at canonical-CELL granularity. Co-residency = same cell the
    body falls in (barycentric containment) — NOT nearest vertex. Opposition is exact
    and per-pair: B is opposite A iff B's cell == the cell where A's ANTIPODE lands
    (same locate() for both) — no centroid threshold, no orb. Adjacency = cells edge."""
    out = {}
    for shell, adj in _SHELL_ADJ.items():
        ca = _cell_id((addr_a[shell].get("containing_face") or {}).get("label"))
        cb = _cell_id((addr_b[shell].get("containing_face") or {}).get("label"))
        c_anti = _cell_id((addr_a_anti[shell].get("containing_face") or {}).get("label"))
        if ca is None or cb is None:
            out[shell] = {"relation": "unknown", "line_type": None}
            continue
        if ca == cb:
            rel, line = "conjunction", "conjunction"        # same cell (co-residency)
        elif cb == c_anti:
            rel, line = "opposition", "shock"               # B in A's antipodal cell
        elif (ca, cb) in adj:
            rel, line = "adjacent", "polygon"               # cells share an edge (+1 line)
        else:
            rel, line = "disjoint", "disjoint"              # no shared edge/axis
        out[shell] = {"relation": rel, "line_type": line, "cell_a": ca, "cell_b": cb}
    return out


# ── 3. ENNEAGRAM (N=9) — hexad/triangle line DELEGATED to canon tables (§16) ──────
_PE_ORDER = ["pt0", "pt1", "pt2", "X3", "pt4", "pt5", "X6", "pt7", "pt8", "pt9"]
_TRIANGLE_MEMBERS = {"pt0", "X3", "X6", "pt9"}   # Law of Three (3·6·9 shock axis)

def _lon_to_pe_pt(lon):
    """Nearest PE point on the 10-node law-of-octaves ring (each PE pt = 36°)."""
    return _PE_ORDER[round((lon % 360) / 36) % 10]

def _enneagram_relation(lon_a, lon_b):
    pt_a, pt_b = _lon_to_pe_pt(lon_a), _lon_to_pe_pt(lon_b)
    pl_a = sr.PE_PT_TO_PLANET.get(pt_a)
    pl_b = sr.PE_PT_TO_PLANET.get(pt_b)
    pair = {pl_a, pl_b}
    relations = []
    if pt_a == pt_b:
        relations.append({"line": "conjunction", "line_type": "conjunction", "pe_pt": pt_a})
    # Hexad line (§16 supervision 1→4→2→8→5→7) — the process-octave "star" line
    for fr, to, line_id, cross_tet, via_shock in sr.HEXAD_LINES:
        if {fr, to} == pair and None not in pair:
            relations.append({
                "line": "hexad", "line_type": "star", "line_id": line_id,
                "cross_tet": cross_tet, "via_shock": via_shock,
                "citation": "canon §16 supervision hexad",
            })
    # Z-axis triangle line (X3→X6→Do) — explicit shock-edge between the pair
    for fr, to, label in sr.TRIANGLE_LINES:
        if {fr, to} == pair and None not in pair:
            relations.append({
                "line": "triangle", "line_type": "shock", "label": label,
                "citation": "canon §16 z-axis triangle",
            })
    # Law-of-Three co-membership (both on the 3·6·9 catalytic triangle)
    if pt_a != pt_b and pt_a in _TRIANGLE_MEMBERS and pt_b in _TRIANGLE_MEMBERS:
        relations.append({
            "line": "triangle_comember", "line_type": "shock",
            "set": "Law of Three (3·6·9 catalytic regulation)",
            "citation": "card 1536f214 + canon §16",
        })
    return {
        "pe_a": pt_a, "planet_a": pl_a, "pe_b": pt_b, "planet_b": pl_b,
        "relations": relations,
    }


# ── top-level aspect: all axes of the §31c lattice in one call ────────────────────
def aspect(lon_a, lon_b, lat_a=0.0, lat_b=0.0):
    """Exact §31c lattice-relation (aspect) between two bodies across every axis.
    Zero weights, zero orb. Aspect ≡ memory-recall (field_memory primitive, body↔body)."""
    ang = _angular(lon_a, lon_b)
    addr_a = ge.full_address(lon_a, lat_a)
    addr_b = ge.full_address(lon_b, lat_b)
    addr_a_anti = ge.full_address(lon_a + 180.0, -lat_a)   # A's antipode, for exact opposition
    shells = _shell_relation(addr_a, addr_b, addr_a_anti)
    ennea = _enneagram_relation(lon_a, lon_b)
    # legacy co-residency summary (conjunction-class shells) preserved
    shared = [s for s, r in shells.items() if r["relation"] == "conjunction"]
    return {
        # — angular axis (back-compatible keys) —
        "sign_offset": ang["sign_offset"],
        "aspect": ang["aspect"],
        "lattice_class": ang["lattice_class"],
        "line_type": ang["line_type"],
        # — polyhedral shells (real graph) —
        "shells": shells,
        "shared_shell_cells": shared,
        # — enneagram N=9 (delegated canon tables) —
        "enneagram": ennea,
        "weights": None,                # explicit: there are none, anywhere
    }


# ── ephemeris wiring: aspect_at(A, B, t) = aspect(lon_a(t), lon_b(t)) ─────────────
def _resolve_lon(body, state):
    """A body is either a transiting planet NAME (lon read from substrate_at) or a
    fixed natal longitude (float, e.g. a natal placement / angle)."""
    if isinstance(body, (int, float)):
        return float(body) % 360.0
    name = str(body).capitalize()
    entry = state["planets"].get(name) or state["planets"].get(str(body))
    if not entry or entry.get("lon") is None:
        raise KeyError(f"no ecliptic longitude for body {body!r} at t "
                       f"(available: {sorted(state['planets'])})")
    return entry["lon"]

def aspect_at(body_a, body_b, when):
    """§31c aspect between two bodies AT moment `when` (datetime).
    Each body: a transiting-planet name (Sun, Mars, …) OR a fixed natal longitude
    (float). Real natal/transit aspects fall out of the lattice; the categorical
    relation flips only at cell-crossings — there is no orb. Zero weights."""
    from substrate_at import substrate_at
    state = substrate_at(when)
    lon_a = _resolve_lon(body_a, state)
    lon_b = _resolve_lon(body_b, state)
    r = aspect(lon_a, lon_b)
    r["t"] = when
    r["lon_a"], r["lon_b"] = lon_a, lon_b
    r["body_a"], r["body_b"] = body_a, body_b
    return r


if __name__ == "__main__":
    tests = [
        ("0° vs 120° (exact trine)",        0.0, 120.0),
        ("0° vs 90° (exact square)",        0.0, 90.0),
        ("0° vs 180° (opposition)",         0.0, 180.0),
        ("0° vs 60° (sextile)",             0.0, 60.0),
        ("0° vs 30° (semi-sextile)",        0.0, 30.0),
        ("0° vs 150° (quincunx)",           0.0, 150.0),
        ("15° Tau vs 15° Vir (trine, real)", 45.0, 165.0),
        ("same sign (conjunction)",         5.0, 25.0),
    ]
    print("ANGULAR axis (§31c divisor-stars on the 12-fold):")
    for label, a, b in tests:
        r = aspect(a, b)
        print(f"  {label:34s} → {r['aspect']:13s} [{r['line_type']:11s}] {r['lattice_class']}")

    print("\nPOLYHEDRAL shells (cell co-residency, not nearest-vertex):")
    for label, a, b in [("0° vs 180° (antipode)", 0.0, 180.0), ("0° vs 36°", 0.0, 36.0)]:
        r = aspect(a, b)
        print(f"  {label}")
        for shell, sr_ in r["shells"].items():
            print(f"     {shell:13s} {sr_['relation']:11s} [{sr_['line_type']}]  "
                  f"{sr_['cell_a']}↔{sr_['cell_b']}")

    print("\nENNEAGRAM N=9 (hexad/triangle, delegated to canon §16 tables):")
    ennea_tests = [
        ("Sun pt1 vs Mars pt4 (hexad 1→4)",   36.0, 144.0),
        ("Venus X3 vs Uranus X6 (triangle)",  108.0, 216.0),
        ("Pluto pt0 vs Venus X3 (Law-of-3)",  0.0, 108.0),
        ("Sun pt1 vs Moon pt2 (adjacent, no hexad)", 36.0, 72.0),
    ]
    for label, a, b in ennea_tests:
        e = aspect(a, b)["enneagram"]
        lines = [r["line"] for r in e["relations"]] or ["(no enneagram line)"]
        print(f"  {label:42s} {e['planet_a']}/{e['planet_b']:8s} → {', '.join(lines)}")

    print("\nEPHEMERIS aspect_at(A,B,t) — relation falls out of substrate_at(t):")
    from datetime import datetime, timezone
    when = datetime(2026, 6, 17, 12, 0, 0, tzinfo=timezone.utc)
    for a, b in [("Sun", "Saturn"), ("Mars", "Venus"), ("Sun", 90.0)]:
        try:
            r = aspect_at(a, b, when)
            print(f"  {str(a):7s} ↔ {str(b):7s}  lon {r['lon_a']:6.1f}/{r['lon_b']:6.1f}"
                  f"  → {r['aspect']:12s} [{r['line_type']}]")
        except Exception as exc:
            print(f"  {str(a):7s} ↔ {str(b):7s}  → ({type(exc).__name__}: {exc})")
