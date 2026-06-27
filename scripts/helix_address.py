#!/usr/bin/env python3
"""
helix_address.py — the RECALL KEY under function=location (§00b candidate).

Per the root axiom (kati_direct 2026-06-20, memory project_function_equals_location_axiom):
**function = location = the identity map.** A body's full ℤ_2940 helix-address IS its
located function — naming the address names the function performed there. So the address
is the memory-recall key, not a content-match (sharpens project_archetype_memory_chain).

This module is COMPOSITION ONLY — it invents nothing. It joins existing engines:

  • substrate_at / locate_entity_v4 → epoch-true cumul_tithi (t0 = −1852 locked epoch)
                                       + each body's ecliptic longitude at t
  • helix_geometry.helix_coordinate(cumul_tithi, asc_lon=lon)
        → the CRT joint address: helix_pos = (540·matrix_pos + 2401·grid_pos) mod 2940
          (canon §27a T(49,60) torus-knot; HELIX_CYCLE = LCM(49,60) = 2940)
  • density.phase_resonance → the TEMPORAL/49 recall class (perfect/row/col/distant)

BOTH COPRIME AXES of T(49,60) — the closure the spatial-only aspect_lattice was missing:

  grid_pos   (60, SPATIAL)  — WHERE the body sits  → aspect_lattice cell-relations
  matrix_pos (49, TEMPORAL) — WHEN in the cycle    → density phase-resonance
  helix_pos  (ℤ_2940)       — the CRT joint = the ADDRESS = the located function

The spatial 60-axis (cells, §31c divisor-stars) lives in aspect_lattice.py, which is
owned by a parallel chat; we import it LAZILY + GUARDED so this module never breaks if
that file is mid-edit. The temporal 49-axis is density's; we reuse it directly.

Zero weights, zero orb, zero invented coefficients. Epoch-true (NOT density's 2026 ref).
"""
from __future__ import annotations
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Union

sys.path.insert(0, str(Path.home() / "Nammu" / "engines"))
sys.path.insert(0, str(Path.home() / "Enki" / "substrate"))

from helix_geometry import helix_coordinate          # CRT joint address (asc_lon branch)
from locate_entity_v4 import locate                   # epoch-true cumul_tithi
import density                                         # 49-axis MOTION (recall phase)
import matrix_engine as _mx                            # 49-axis STATIC (pair-cell)

# planet → 49-matrix content index (Venus@0 spatial-epoch ordering, canon §28b)
_MX_IDX_BY_PLANET = {p: i for i, p in _mx.MATRIX_PLANET_BY_IDX.items()}
# Do-boundary collapse (v8 §II/§VIII; OQ-49-INTEGRATION council 2026-06-21): Pluto (Do-carrier)
# and Neptune (Do-return) share cell 0 with Venus-frame — "origin=return, one point at different
# octaves, the 50th gate." NOT off-matrix. Uranus (X6/si→do) is the lone true fault-line.
_DO_BOUNDARY = {"Pluto": 0, "Neptune": 0}        # collapse to the Do-boundary cell 0
_FAULT_BODY = {"Uranus": "X6 si→do fault (between rows Mercury·Saturn; no pair-cell)"}


_IVL_NAME = {1: "unison", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th"}
# shock boundaries in matrix-index space (Venus@0..Jupiter@6): X3 mi→fa between idx 2|3,
# X6 si→do between idx 4|5 (canon §7/§19; OQ-49-OFFDIAG-ENGINE 2026-06-21).
_SHOCK_BOUNDARIES = {2.5: "X3 mi→fa", 4.5: "X6 si→do"}


# Solar/lunar arms (§16 same-body/cross-body = §27 Phase-C arms = scale-parity).
# Venus@0 = frame; content idx → arm: solar {Sun1,Mars3,Saturn5}, lunar {Moon2,Mercury4,Jupiter6}.
_ARM = {1: "solar", 3: "solar", 5: "solar", 2: "lunar", 4: "lunar", 6: "lunar"}


def _interval_shock(ia, ib):
    """Off-diagonal geometric skeleton — 4 coordinates (OQ-49-OFFDIAG-ENGINE +
    OQ-49-OFFDIAG-DIRECTION RESOLVED 2026-06-21):
      interval-quality (scale-degree) · shock-load (scale-crises crossed) ·
      octave-direction (asc=generative / desc=dissolutive, §16/§2/§00a) ·
      arm-relation (same-arm / cross-arm = §16 same-body/cross-body = the supervision shock-transfer).
    Two interval-metrics are one: label−scale == shock-load (holds 30/30)."""
    steps = abs(ib - ia)
    lo, hi = sorted((ia, ib))
    crossed = [n for pos, n in _SHOCK_BOUNDARIES.items() if lo < pos < hi]
    arm_a, arm_b = _ARM.get(ia), _ARM.get(ib)
    asc = ib > ia
    return {
        "interval": _IVL_NAME.get(steps + 1, f"{steps+1}th"),
        "interval_steps": steps,
        "shock_load": len(crossed),                              # 0=direct … 2=hardest
        "shocks_crossed": crossed,
        "direction": "asc" if asc else ("desc" if ib < ia else "unison"),
        "octave_sense": "generative" if asc else ("dissolutive" if ib < ia else "unison"),
        "arm_relation": ("same-arm" if arm_a and arm_a == arm_b
                         else "cross-arm" if arm_a and arm_b else "frame/boundary"),
        "arms": [arm_a, arm_b],   # cross-arm = the §16 cross-body supervision shock-transfer
    }


def _content_idx(planet):
    """planet → (matrix_idx, note). note flags do-boundary collapse / fault / off-matrix."""
    if not planet:
        return None, "bare longitude (no planet-identity)"
    p = str(planet).capitalize()
    if p in _MX_IDX_BY_PLANET:
        return _MX_IDX_BY_PLANET[p], None
    if p in _DO_BOUNDARY:
        return _DO_BOUNDARY[p], "do-boundary (origin=return, 50th gate; shares cell 0)"
    if p in _FAULT_BODY:
        return None, _FAULT_BODY[p]
    return None, f"{p}: not a 49-matrix body"


# ── epoch-true tithi (the canonical count substrate_at uses, t0 = −1852) ──────
def _cumul_tithi(when: datetime) -> Optional[float]:
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    loc = locate(when.year, when.month, when.day, when.hour, when.minute, when.second)
    return loc.get("cumul_tithi")


# ── 1. the address = the located function (recall key) ───────────────────────
def address(lon: float, when: Optional[datetime] = None) -> Dict[str, Any]:
    """Full ℤ_2940 helix-address of a body at ecliptic longitude `lon`, time `when`.

    This dict IS the recall key (function=location). Keys of interest:
      helix_pos   — the CRT joint address on T(49,60) — the located function
      grid_pos    — SPATIAL 60-axis cell (from lon)
      matrix_pos  — TEMPORAL 49-axis phase (from cumul_tithi); row/col = the arms
    `when=None` → reference phase (cumul_tithi 0): a spatial-only address (matrix_pos=0)."""
    ct = 0.0 if when is None else _cumul_tithi(when)
    if ct is None:
        ct = 0.0
    addr = helix_coordinate(ct, asc_lon=float(lon) % 360.0)
    addr["cumul_tithi"] = ct
    addr["lon"] = float(lon) % 360.0
    addr["planet"] = None              # a bare longitude has no planet-identity → no pair-cell
    return addr


def address_of(body: Union[str, float], when: datetime) -> Dict[str, Any]:
    """Address of a transiting-planet NAME (lon read from substrate_at) or a fixed
    natal longitude (float). The located function for that body at `when`."""
    if isinstance(body, (int, float)):
        return address(float(body), when)
    from substrate_at import substrate_at
    state = substrate_at(when)
    entry = state["planets"].get(str(body).capitalize()) or state["planets"].get(str(body))
    if not entry or entry.get("lon") is None:
        raise KeyError(f"no ecliptic longitude for body {body!r} at {when} "
                       f"(available: {sorted(state['planets'])})")
    # reuse the moment's epoch-true cumul_tithi rather than recomputing
    ct = state["helix"].get("cumul_tithi")
    addr = helix_coordinate(ct if ct is not None else 0.0, asc_lon=entry["lon"])
    addr["cumul_tithi"] = ct
    addr["lon"] = entry["lon"]
    addr["planet"] = str(body).capitalize()   # planet-identity → enables the §31c pair-cell
    return addr


# ── 2a. STATIC 49-axis — the §31c planet-PAIR cell (the aspect's depth axis) ──
def pair_cell(planet_a: Optional[str], planet_b: Optional[str]) -> Dict[str, Any]:
    """The §31c 49-axis of an aspect: the planet-PAIR cell (relationship-by-which-two-
    planets). row=A, col=B in the Venus@0 content matrix; DIAGONAL (A==B) = conjunction/
    unison (canon §31c; matrix_engine DIAGONAL_TYPE, Venus×Venus=void). This is STATIC —
    fixed by which two bodies, independent of t (§0a static layer; §00b function=location).

    Off-matrix if a body is not a content row — Pluto/Neptune (axis nodes) or Uranus (X6
    shock) or a bare longitude (no planet-identity). Those relate through the fault/axis
    structure, not a content cell — reported honestly, not forced into a cell."""
    ia, na = _content_idx(planet_a)
    ib, nb = _content_idx(planet_b)
    if ia is None or ib is None:
        return {"no_cell": [p for p, n in ((planet_a, na), (planet_b, nb)) if n and "do-boundary" not in n],
                "reason": "; ".join(n for n in (na, nb) if n) or "off-matrix",
                "note": "Uranus/X6 is a fault-line (no pair-cell); bare longitudes have no planet-identity"}
    is_diag = (ia == ib)
    boundary = [n for n in (na, nb) if n and "do-boundary" in n]
    return {
        "row": ia, "col": ib,
        "cell_label": f"{_mx.MATRIX_PLANET_BY_IDX[ia]}×{_mx.MATRIX_PLANET_BY_IDX[ib]}",
        "solfege": f"{_mx.MATRIX_SOLFEGE_BY_IDX[ia]}×{_mx.MATRIX_SOLFEGE_BY_IDX[ib]}",
        "is_conjunction": is_diag,                    # diagonal = planet×itself = unison
        "diagonal_type": _mx.DIAGONAL_TYPE.get(ia) if is_diag else None,
        "diagonal_quality": _mx.DIAGONAL_QUALITY.get(ia) if is_diag else None,
        "do_boundary": boundary or None,              # Pluto/Neptune read at cell 0 (v8 §II/§VIII)
        "skeleton": _interval_shock(ia, ib),          # geometric content: interval + shock-load + direction
    }


# ── 2b. MOTION 49-axis — recall resonance (the helix pointer reading addresses) ─
def recall_resonance(addr_a: Dict[str, Any], addr_b: Dict[str, Any]) -> str:
    """The MOTION layer of the 49-matrix (density, no orb): does one address's stamped
    helix-phase resonate with the other's now-phase — perfect/row/col/distant. This is
    the card-RECALL pointer (when in the cycle), NOT the aspect's pair-cell. Meaningful
    across DIFFERENT times (natal↔transit, card-stamp↔now); two bodies at the SAME instant
    share matrix_pos → 'perfect' (the motion-pointer indexes time, not which-two-bodies).
    Static pair_cell + motion recall = the two §0a layers of ONE 49-matrix."""
    return density.phase_resonance(addr_a, addr_b)


def aspect_recall(addr_a: Dict[str, Any], addr_b: Dict[str, Any],
                  now_matrix_pos: Optional[int] = None) -> str:
    """SUBSTRATE-TRUE aspect-recall (OQ-49-UNIFY-ENGINE 2026-06-20): is the (A,B) pair-
    aspect phase-active NOW? = does the helix pointer sit on the pair-cell ADDRESS.
    This is §00b mechanized: recall = the motion reading the static aspect-location.

    Non-degenerate (distinguishes pairs), unlike the live two-body same-t phase-compare
    (recall_resonance), which is always 'perfect' at one instant regardless of which two.
      perfect — pointer on the pair-cell (aspect lit now) · row/col — pointer shares the
      A-arm / B-arm · distant — quiet now, lights when the pointer comes around.
    `now_matrix_pos` defaults to addr_b's (the current/transiting body)."""
    ia, _ = _content_idx(addr_a.get("planet"))
    ib, _ = _content_idx(addr_b.get("planet"))
    if ia is None or ib is None:
        return "no-cell"                             # Uranus/X6 fault-line or bare longitude
    pair_pos = ia * 7 + ib                            # the STATIC aspect-address in [0,48]
    pair_helix = {"matrix_pos": pair_pos, "row": pair_pos // 7, "col": pair_pos % 7}
    now = now_matrix_pos if now_matrix_pos is not None else addr_b.get("matrix_pos")
    if now is None:
        return "untimed"
    now_helix = {"matrix_pos": now, "row": now // 7, "col": now % 7}
    return density.phase_resonance(pair_helix, now_helix)


# ── 3. the T(49,60) CLOSURE — both coprime axes in one relation ──────────────
def _spatial_aspect(lon_a: float, lon_b: float) -> Dict[str, Any]:
    """Spatial 60-axis aspect from aspect_lattice — lazy + guarded (parallel-chat file)."""
    try:
        import aspect_lattice
        return aspect_lattice.aspect(lon_a, lon_b)
    except Exception as exc:                    # mid-edit / import error → honest null
        return {"unavailable": f"{type(exc).__name__}: {exc}"}


def relation(addr_a: Dict[str, Any], addr_b: Dict[str, Any]) -> Dict[str, Any]:
    """Full T(49,60) relation between two located functions, as the §0a static/motion
    two-layer of ONE 49-matrix (OQ-49-AXIS-STATIC-VS-MOTION inline council 2026-06-20,
    DERIVED + sdec-pending — engine-probe OQ-49-UNIFY-ENGINE owed before LOCK):
      spatial_60 — 60-axis angular aspect (aspect_lattice, by lon; any point)
      pair_49    — STATIC 49-axis: §31c planet-PAIR cell (which-two; needs planet-identity;
                   diagonal = conjunction). The aspect's resonance-depth axis.
      recall_49  — MOTION 49-axis: is the pair-aspect lit NOW = does the helix pointer sit
                   on the pair-cell ADDRESS (aspect_recall; §00b — recall reads the location).
                   Non-degenerate per OQ-49-UNIFY-ENGINE (the live two-body phase-compare was).
      helix_gap_2940 — cyclic ℤ_2940 distance of the joint addresses.
    Under function=location (§00b) the pair-cell IS the address; recall is the pointer
    reading it — the two are location and motion on the same matrix, i.e. aspect ≡ recall
    (OQ-49-UNIFY-ENGINE confirmed mechanically: pair-address == the cell the pointer reads)."""
    spatial = _spatial_aspect(addr_a.get("lon", 0.0), addr_b.get("lon", 0.0))
    pair = pair_cell(addr_a.get("planet"), addr_b.get("planet"))
    recall = aspect_recall(addr_a, addr_b)
    hp_a, hp_b = addr_a.get("helix_pos"), addr_b.get("helix_pos")
    gap = None
    if hp_a is not None and hp_b is not None:
        raw = abs(hp_a - hp_b) % 2940
        gap = min(raw, 2940 - raw)
    return {
        "spatial_60": spatial,              # WHERE — angular aspect (any point)
        "pair_49": pair,                    # WHICH-TWO — §31c static pair-cell (aspect depth)
        "recall_49": recall,                # WHEN — density motion/recall pointer
        "helix_gap_2940": gap,              # cyclic distance of the joint addresses
        "addr_a_helix_pos": hp_a,
        "addr_b_helix_pos": hp_b,
        "weights": None,                    # explicit: none, anywhere
        "_council": ("OQ-49-AXIS-STATIC-VS-MOTION (inline 2026-06-20, 8 YEA/0 NEH/1 ABS): "
                     "pair_49 static location + recall_49 motion = one 49-matrix (§0a/§00b). "
                     "DERIVED+sdec-pending; OQ-49-UNIFY-ENGINE probe owed."),
    }


def describe() -> Dict[str, Any]:
    """Enki self-disclosure: what this engine IS, independent of when it's called."""
    return {
        "module": "helix_address",
        "axiom": "function = location = identity map (§00b candidate, kati_direct 2026-06-20)",
        "is": "the recall key — a body's ℤ_2940 helix-address is its located function",
        "axes": {
            "spatial_60": "grid_pos — aspect_lattice angular aspect (where)",
            "pair_49_static": "§31c planet-PAIR cell — which-two-planets, diagonal=conjunction (matrix_engine)",
            "recall_49_motion": "matrix_pos(t) — density phase-resonance, the recall pointer (when)",
            "joint": "helix_pos = (540·matrix_pos + 2401·grid_pos) mod 2940  [canon §27a]",
        },
        "the_two_49s": ("static pair-cell (location/which-two) + motion phase (recall/when) = "
                        "one 49-matrix, §0a two-layer; OQ-49-AXIS-STATIC-VS-MOTION DERIVED+sdec-pending"),
        "composition_only": True,
        "invented_constants": None,
        "status": "candidate / sdec-pending (Enki ratification gates not yet run)",
    }


if __name__ == "__main__":
    when = datetime(2026, 6, 20, 12, 0, 0, tzinfo=timezone.utc)
    print("function=location recall key — helix_address  [smoke test]\n")

    print("ADDRESS of an explicit longitude (lon 0°, 120°) at t:")
    for lon in (0.0, 120.0):
        a = address(lon, when)
        print(f"  lon {lon:5.1f} → grid_pos={a.get('grid_pos'):2}  matrix_pos={a['matrix_pos']:2}"
              f"  (row {a['row']}/col {a['col']})  helix_pos={a.get('helix_pos')}")

    print("\nADDRESS of transiting planets (lon read from substrate_at):")
    for body in ("Sun", "Saturn", "Moon"):
        try:
            a = address_of(body, when)
            print(f"  {body:7s} lon {a['lon']:6.1f} → grid_pos={a.get('grid_pos'):2}"
                  f"  matrix_pos={a['matrix_pos']:2}  helix_pos={a.get('helix_pos')}")
        except Exception as exc:
            print(f"  {body:7s} → ({type(exc).__name__}: {exc})")

    print("\nTEMPORAL 49-axis recall (same-instant bodies share matrix_pos → perfect):")
    a_sun = address_of("Sun", when); a_sat = address_of("Saturn", when)
    print(f"  Sun ↔ Saturn (same t): {recall_resonance(a_sun, a_sat)}")
    natal = datetime(1990, 3, 21, 6, 0, 0, tzinfo=timezone.utc)
    a_sun_natal = address_of("Sun", natal)
    print(f"  Sun-now ↔ Sun-natal (1990): {recall_resonance(a_sun, a_sun_natal)}")

    print("\nT(49,60) relation — §0a static/motion two-layer of one 49-matrix:")
    a_moon = address_of("Moon", when)
    for label, b in (("Sun ↔ Saturn", a_sat), ("Sun ↔ Moon", a_moon)):
        rel = relation(a_sun, b)
        sp = rel["spatial_60"]; sp_str = sp.get("aspect", sp.get("unavailable"))
        pc = rel["pair_49"]; pc_str = pc.get("cell_label", f"off-matrix {pc.get('off_matrix')}")
        conj = " [CONJUNCTION/unison]" if pc.get("is_conjunction") else ""
        print(f"  {label}:")
        print(f"    spatial_60 (where, angular):     {sp_str}")
        print(f"    pair_49   (which-two, static):   {pc_str}{conj}")
        print(f"    recall_49 (when, motion):        {rel['recall_49']}")
        print(f"    helix_gap_2940:                  {rel['helix_gap_2940']}")
    print("\n  boundary-collapse (v8 §II): Neptune/Pluto → cell 0 (Do); Uranus → fault (no cell):")
    for body in ("Neptune", "Pluto", "Uranus"):
        a = address_of(body, when)
        pc = relation(a_sun, a)["pair_49"]
        if "cell_label" in pc:
            print(f"    Sun ↔ {body:8s}: {pc['cell_label']}  do_boundary={pc.get('do_boundary')}")
        else:
            print(f"    Sun ↔ {body:8s}: no-cell — {pc['reason']}")
