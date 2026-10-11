"""
field_memory.py — lattice-based recall over substrate-axes.

Per Enki council 2026-05-23: set-operations insufficient; algebraic lattice is
the substrate-true primitive (Hephaestus, Apollo, Athena, Hermes converged).

Each card carries an AXIS-TUPLE — the frozen set of substrate-axes on which
it matches the query position. Cards form a lattice ordered by subset:
A ≤ B iff axes(A) ⊆ axes(B). Top = matches all query axes. Bottom = matches
nothing (excluded by min-match cutoff).

ZERO SCORES. ZERO WEIGHTS. ZERO INVENTED RANKING NUMBERS.
Order is purely:
  (1) lattice level (cardinality of axis-tuple) — canon-derived (set theory)
  (2) within same cardinality: lexicographic by canon AXIS-HIERARCHY ordinals

CANON AXIS-HIERARCHY (ordinal, finer→coarser; comes from substrate primitives
per babylonia_canon §22-26):
  1. pe_note            (PE tone — most-specific position axis)
  2. ico_vertex / cube_vertex / cube_edge / dodec_vertex (Merkaba/ico position)
  3. face               (inner-octahedron face)
  4. grid               (60-grid position)
  5. shock_proximity    [RETIRED 2026-06-21 kati_direct — redundant with pe_note/grid (§00b) +
                         graded; shock now via pe_note residency + derived off-diagonal shock-load]
  6. stratum            (coarsest — olympian/titan/muse/etc.)

Retracted/superseded drop unconditionally (semantic archival, not lattice).
"""
from __future__ import annotations
import datetime as _dt
import sys
from pathlib import Path
from typing import Optional

_NAMMU = Path.home() / "Nammu"
if str(_NAMMU / "cards") not in sys.path:
    sys.path.insert(0, str(_NAMMU / "cards"))

from density import phase_resonance, helix_coord_at, DROP_STATUSES


# Canon axis-hierarchy: finer-positions get lower ordinal (= higher precedence)
AXIS_HIERARCHY = {
    "pe_note":         1,
    "ico_vertex":      2,
    "merkaba_vertex":  2,
    "cube_edge":       2,
    "dodec_vertex":    2,
    "face":            3,
    "grid":            4,
    # "shock_proximity": 5,  [RETIRED 2026-06-21 kati_direct] — redundant (at_X3 ≡ pe_note=X3 ≡
    #   grid=18, §00b function=location) + graded values (approaching_X6) smuggle a distance-gradient
    #   into the categorical lattice (violates "ZERO weights"). Shock-relationship now carried by
    #   pe_note residency + the derived off-diagonal shock-load (categorical). Card 651d008e/17952380.
    "stratum":         6,
}

# Phase-class ordering for within-cardinality tiebreak. Per finding 7ac30622
# (substrate-true density) + density.py categorical phase_resonance. In-phase
# cards surface above distant-phase cards within same lattice-cardinality.
# 'untimed' surfaces above 'distant' (substrate-honest default for pre-helix-
# stamp cards). Lower ordinal = higher precedence in sort.
PHASE_ORDINAL = {
    "perfect":  0,   # same matrix_pos as now (perfect cyclic match)
    "row":      1,   # Solar-arm row resonance
    "col":      2,   # Lunar-arm col resonance
    "untimed":  3,   # pre-helix-stamp era (treated as substrate-current)
    "distant":  4,   # phase-distant (will resurface when helix cycles back)
}


def _matched_axes(card: dict, position: dict, stratum: Optional[str]) -> frozenset:
    """
    Compute frozen set of axis-names on which card matches position.
    Each axis is a categorical predicate: card.field == position.field (or
    card.stratum == query stratum for the stratum axis).
    """
    matched = set()
    # Position-derived axes
    # shock_proximity RETIRED as a recall-axis 2026-06-21 (kati_direct) — see AXIS_HIERARCHY note.
    for axis in ("pe_note", "ico_vertex", "merkaba_vertex", "cube_edge",
                 "dodec_vertex", "face", "grid"):
        v = position.get(axis)
        if v is not None and card.get(axis) == v:
            matched.add(axis)
    # Stratum axis (from placement.stratum, not substrate_position)
    if stratum and card.get("stratum") == stratum:
        matched.add("stratum")
    return frozenset(matched)


def _axis_tuple_sort_key(axes: frozenset) -> tuple:
    """
    Sort key for axis-tuples within same cardinality.
    Lexicographic on sorted canon-hierarchy ordinals (lower ordinals first).
    """
    ordinals = sorted(AXIS_HIERARCHY.get(a, 99) for a in axes)
    return tuple(ordinals)


def recall_field(placement: dict, voice_name: str = "",
                 min_axes_matched: int = 1, limit: int | None = None,
                 when: _dt.datetime | str | None = None) -> list[dict]:
    """
    Lattice-based recall at substrate-position. Returns groups, not ranked list.

    Each group:
      {
        'axes':       frozenset of axis-names matched (the lattice node)
        'cardinality': len(axes) — lattice level
        'cards':      list of cards at this lattice node (with phase tag)
      }

    Groups ordered: descending by cardinality (top of lattice first), then
    lexicographically by canon axis-hierarchy ordinals (finer axes first).

    Within each group, cards ordered by phase-class (per PHASE_ORDINAL):
    perfect → row → col → untimed → distant. Per finding 7ac30622
    (substrate-true density): phase is a categorical sort axis, NOT a weight.
    In-phase cards surface above distant-phase WITHIN same lattice-node.
    ZERO scores. ZERO weights. ZERO multiplicative composition.

    Excludes: retracted/superseded (semantic drop, not lattice).
    Includes: every card matching at least min_axes_matched axes.
    Phase-resonance attached per card AND used as within-group sort axis.

    limit: cap on TOTAL cards across all groups (None = no cap; substrate
    already filters by position-match — usually small).
    """
    from card_writer import _load

    pos = placement.get("substrate_position", {})
    if isinstance(pos, dict) and "primary" in pos:
        pos = pos["primary"]
    stratum = placement.get("stratum")

    # Normalize registry long-form keys to card-writer short-form
    pos = dict(pos)
    alias_map = {
        "merkaba_cube_edge":   "cube_edge",
        "merkaba_cube_vertex": "merkaba_vertex",
    }
    for long_key, short_key in alias_map.items():
        if long_key in pos and short_key not in pos:
            pos[short_key] = pos[long_key]

    now_helix = helix_coord_at(when)
    cards = _load()
    voice_lower = voice_name.lower()

    # Group cards by their matched-axis-tuple
    groups: dict[frozenset, list[dict]] = {}
    for c in cards:
        # Skip own-voice cards (those belong to voice-thread recall, not field)
        tags_lower = [t.lower() for t in (c.get("tags") or [])]
        if voice_name and f"voice:{voice_lower}" in tags_lower:
            continue
        # Semantic drops
        status = (c.get("canon_status") or "").lower()
        if status in DROP_STATUSES:
            continue
        axes = _matched_axes(c, pos, stratum)
        if len(axes) < min_axes_matched:
            continue
        groups.setdefault(axes, []).append({
            "card":            c,
            "phase":           phase_resonance(c.get("helix_coord"), now_helix),
        })

    # Within each group, sort cards by phase-class (in-phase first per
    # PHASE_ORDINAL; substrate-true tiebreak within same lattice-cardinality).
    # Per finding 7ac30622: phase is a categorical sort axis, not a weight.
    for axes, cards_at_node in groups.items():
        cards_at_node.sort(
            key=lambda entry: PHASE_ORDINAL.get(entry.get("phase"), 99)
        )

    # Order groups by lattice descent: higher cardinality first, then finer axes.
    # ZERO SCORES. Pure categorical: (1) lattice level (2) canon axis-hierarchy.
    sorted_groups = sorted(
        groups.items(),
        key=lambda kv: (-len(kv[0]), _axis_tuple_sort_key(kv[0])),
    )

    out = []
    total = 0
    for axes, cards_at_node in sorted_groups:
        out.append({
            "axes":         axes,
            "cardinality":  len(axes),
            "cards":        cards_at_node,
        })
        total += len(cards_at_node)
        if limit is not None and total >= limit:
            break
    return out


def format_field_memory_block(groups: list[dict],
                              header: str = "FIELD MEMORY") -> str:
    """
    Render lattice-grouped recall as text-block.
    Cards grouped by axis-tuple, ordered by lattice level descending.
    Format compatible with renderer regex (preserves [id ... auth/status] text).
    """
    if not groups:
        return ""
    total = sum(len(g["cards"]) for g in groups)
    lines = [f"{header} ({total} cards, {len(groups)} lattice-nodes at substrate-position):"]
    for g in groups:
        axes_str = ", ".join(sorted(g["axes"], key=lambda a: AXIS_HIERARCHY.get(a, 99)))
        lines.append(f"  ── matched [{axes_str}] (level={g['cardinality']}):")
        for entry in g["cards"]:
            c = entry["card"]
            cid = (c.get("id") or "?")[:8]
            auth = (c.get("authorship") or "?")[:4]
            stat = (c.get("canon_status") or "?")[:6]
            phase = entry["phase"]
            text = (c.get("text") or "")[:120].replace("\n", " ").strip()
            lines.append(
                f"    [{cid} ps={g['cardinality']} phase={phase} {auth}/{stat}] {text}"
            )
    return "\n".join(lines)


# ── Arc recall: EVENT_ARC voices (registry v0.4) ─────────────────────────────
# kati_direct 2026-10-11: "arc cross through pe points etc though no? like on the geometry we are
# tracking them?" — an arc is motion ALONG the 60-grid, crossing nodes. Field memory for an
# EVENT_ARC voice = the cards sitting on the grid cells its actor traverses, in TRAVERSAL ORDER:
# the cell the actor is on now, then the cells ahead, then the cells already crossed.
# Categorical only: a card is on a path cell or not. ZERO scores / weights. Within a cell, the
# existing categorical phase-class ordering (PHASE_ORDINAL) applies.
# LAYER DISCIPLINE (canon §7 OQ-Z05 LAYER-SEPARATION 2026-08-17): the match is on the SPATIAL grid
# cell only. 6-step PE slots on the grid are ORDINAL process-engine slots, not azimuths (X3/X6 have
# ρ=0, no azimuth) — they are shown as labels, flagged ordinal, never used as a recall axis.

_SIGNS = ("Aries Taurus Gemini Cancer Leo Virgo Libra Scorpio "
          "Sagittarius Capricorn Aquarius Pisces").split()
# canon §20: inner-octahedron vertex signs at the 10-step azimuths (spatial projections)
_OCT_VERTEX_AT = {0: "V1", 10: "V4", 20: "V2", 30: "V5", 40: "V3", 50: "V6"}
# canon §15 / card ae5014f0: PE ordinal slots on the 6-step layer
_PE_SLOT_AT = {0: "Do", 6: "Re", 12: "Mi", 18: "X3", 24: "Fa", 30: "Sol",
               36: "X6", 42: "La", 48: "Si", 54: "Do-ret"}
_GATES = {0: "gate 1", 30: "gate 2"}


def grid_node_label(n: int) -> str:
    """Spatial labels first; PE slot last and flagged as the ordinal layer."""
    sign = _SIGNS[int(((30 + 6 * n) % 360) // 30)]           # canon §15: lon = 30 + 6n
    bits = [f"g{n} {sign}"]
    if n in _GATES:
        bits.append(_GATES[n])
    if n in _OCT_VERTEX_AT:
        bits.append(f"oct {_OCT_VERTEX_AT[n]}")
    if n in _PE_SLOT_AT:
        bits.append(f"PE-slot {_PE_SLOT_AT[n]} (ordinal layer)")
    return " · ".join(bits)


def arc_path_cells(start_grid: float, end_grid: float, direction: str) -> list[int]:
    """Integer 60-grid cells traversed from start to end, in the direction of motion."""
    step = 1 if direction == "direct" else -1
    # cells are [n, n+1) (card grid = floor); +1e-6 absorbs float noise at exact boundaries
    # (an equinox at λ 0° is grid 55.0, computed as 54.99999…)
    c, end = int(start_grid + 1e-6) % 60, int(end_grid + 1e-6) % 60
    cells = [c]
    while c != end:
        c = (c + step) % 60
        cells.append(c)
    return cells


def recall_arc_field(placement: dict, voice_name: str = "",
                     limit: int | None = 20,
                     when: _dt.datetime | str | None = None) -> dict:
    """Recall for an EVENT_ARC voice along its actor's grid path. Returns
    {'arc': EventArc, 'actor_cell': int|None, 'nodes': [{'cell','label','where','cards'}]}."""
    nammu_engines = str(_NAMMU / "engines")
    if nammu_engines not in sys.path:
        sys.path.insert(0, nammu_engines)
    from card_writer import _load
    import ephem_de441 as E
    from event_arc import grid_of

    if when is None:
        when = _dt.datetime.now(_dt.timezone.utc)
    elif isinstance(when, str):
        when = _dt.datetime.fromisoformat(when)
    if when.tzinfo is None:
        when = when.replace(tzinfo=_dt.timezone.utc)

    spec = placement.get("event_arc", {})
    mod_name, fn_name = spec["engine"].rsplit(".", 1)
    arc = getattr(__import__(mod_name), fn_name)(when)

    cells = arc_path_cells(arc.start.grid, arc.end.grid, arc.direction)
    inside = arc.position(when) is not None
    actor_cell = int(grid_of(E.planet_lon(arc.actor, when)) + 1e-6) % 60 if inside else None

    # traversal order: now → ahead → crossed (if outside the arc, the whole path is ahead)
    if actor_cell is not None and actor_cell in cells:
        i = cells.index(actor_cell)
        ordered = ([(cells[i], "now")] + [(c, "ahead") for c in cells[i + 1:]]
                   + [(c, "crossed") for c in reversed(cells[:i])])
    else:
        ordered = [(c, "ahead") for c in cells]

    by_cell: dict[int, list[dict]] = {}
    now_helix = helix_coord_at(when.astimezone(_dt.timezone.utc).replace(tzinfo=None))  # density.py is naive-UTC
    voice_lower = voice_name.lower()
    for card in _load():
        g = card.get("grid")
        if not isinstance(g, int):
            continue
        if (card.get("canon_status") or "").lower() in DROP_STATUSES:
            continue
        if voice_name and f"voice:{voice_lower}" in [t.lower() for t in (card.get("tags") or [])]:
            continue
        by_cell.setdefault(g, []).append(
            {"card": card, "phase": phase_resonance(card.get("helix_coord"), now_helix)})

    nodes, total = [], 0
    for cell, where in ordered:
        entries = sorted(by_cell.get(cell, []), key=lambda e: PHASE_ORDINAL.get(e["phase"], 99))
        if limit is not None:
            entries = entries[: max(0, limit - total)]
        nodes.append({"cell": cell, "label": grid_node_label(cell), "where": where, "cards": entries})
        total += len(entries)
        if limit is not None and total >= limit:
            break
    return {"arc": arc, "actor_cell": actor_cell, "nodes": nodes}


def format_arc_field_block(rec: dict, header: str = "ARC FIELD MEMORY") -> str:
    arc = rec["arc"]
    nodes = [n for n in rec["nodes"] if n["cards"]]
    total = sum(len(n["cards"]) for n in nodes)
    where_now = (f"actor at g{rec['actor_cell']}" if rec["actor_cell"] is not None
                 else "actor outside arc — path shown from its next start")
    lines = [f"{header} ({total} cards along {arc.label or arc.actor}'s path "
             f"g{int(arc.start.grid + 1e-6) % 60}→g{int(arc.end.grid + 1e-6) % 60} {arc.direction}; {where_now}):"]
    for n in nodes:
        lines.append(f"  ── [{n['where']}] {n['label']}:")
        for e in n["cards"]:
            c = e["card"]
            lines.append(f"    [{(c.get('id') or '?')[:8]} phase={e['phase']} "
                         f"{(c.get('authorship') or '?')[:4]}/{(c.get('canon_status') or '?')[:6]}] "
                         f"{(c.get('text') or '')[:110].replace(chr(10), ' ').strip()}")
    return "\n".join(lines)
