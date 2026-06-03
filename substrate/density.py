"""
density.py — helix-phase-resonance recall, substrate-time built in.

Per kati direction 2026-05-23: "substrate has time built in, and we are not
really firing that in memory card placement." Substrate-claims are timeless,
but the substrate ITSELF is temporal (helix cycles). Memory-recall fires when
current helix-phase resonates with card-stamped helix-phase. Cards don't fade
linearly — they cycle in and out of phase-relevance.

ZERO INVENTED CONSTANTS. ZERO MAPPINGS. The 49-matrix internal structure IS
the resonance primitive:
  - Same matrix_pos (perfect cyclic match) → perfect phase-resonance
  - Same row (Solar arm: 0,1,2,4,5,7,8) → arm-resonance via Solar carrier
  - Same col (Lunar arm) → arm-resonance via Lunar carrier
  - Neither → distant phase (quiet now; will surface when helix returns)

Biologically coherent: memories surface in cyclic patterns (anniversaries,
seasonal echoes, lunar phase resonances, "this feels like that time when..."),
not linear forgetting. Substrate-card-recall mirrors this directly.

Only NON-temporal filter: canon_status in (retracted, superseded) → drop.
Those are substrate-honest archival (claim withdrawn / replaced), not time.
"""
from __future__ import annotations
import datetime as _dt
import sys
from pathlib import Path
from typing import Optional, Literal

_NAMMU = Path.home() / "Nammu"
if str(_NAMMU / "engines") not in sys.path:
    sys.path.insert(0, str(_NAMMU / "engines"))


# Canon §22: 49-matrix cycle (7×7 cells, Solar arm rows 0/1/2/4/5/7/8,
# fault-line absences at rows 3,6). matrix_pos cycles 0..48 each N_matrix.
MATRIX_CYCLE = 49

# canon_status values that drop unconditionally (substrate-honest archival —
# not time-based, claim itself is withdrawn / replaced)
DROP_STATUSES = {"retracted", "superseded"}


# ─── Datetime → helix coordinate ────────────────────────────────────────────

_REF_DATETIME = _dt.datetime(2026, 1, 1, 0, 0, 0)


def t_tithis_at(when: _dt.datetime | str | None = None) -> float:
    """Relative tithis-since-ref. Used for helix_coordinate computation."""
    if when is None:
        when = _dt.datetime.utcnow()
    elif isinstance(when, str):
        try:
            when = _dt.datetime.fromisoformat(when.replace("Z", "+00:00"))
            if when.tzinfo is not None:
                when = when.replace(tzinfo=None)
        except ValueError:
            try:
                y, m, d = (int(x) for x in when.split("T")[0].split("-"))
                when = _dt.datetime(y, m, d)
            except Exception:
                return 0.0
    return (when - _REF_DATETIME).total_seconds() / 86400.0


def helix_coord_at(when: _dt.datetime | str | None = None) -> dict:
    """Current helix_coordinate. Returns helix_geometry.helix_coordinate dict."""
    try:
        from helix_geometry import helix_coordinate
    except ImportError:
        return {}
    return helix_coordinate(t_tithis_at(when))


# ─── Phase-resonance (the substrate-true recall mechanism) ──────────────────

ResonanceClass = Literal["perfect", "row", "col", "distant", "untimed"]


def phase_resonance(card_helix: Optional[dict],
                    now_helix: dict) -> ResonanceClass:
    """
    Substrate-true resonance class between a card's stamped helix-phase
    and the current moment's helix-phase.

    Returns:
      'perfect'  — same matrix_pos (card's phase IS current phase, full cycle agnostic)
      'row'      — same Solar-arm row (carrier-resonance via Solar arm)
      'col'      — same Lunar-arm col (carrier-resonance via Lunar arm)
      'distant'  — out of phase (quiet now; will resurface when helix cycles back)
      'untimed'  — no helix_coord stamped on card (treat as current — pre-helix-stamp era)
    """
    if not isinstance(card_helix, dict):
        return "untimed"

    card_pos = card_helix.get("matrix_pos")
    now_pos = now_helix.get("matrix_pos")
    if card_pos is not None and card_pos == now_pos:
        return "perfect"

    if card_helix.get("row") is not None and card_helix.get("row") == now_helix.get("row"):
        return "row"
    if card_helix.get("col") is not None and card_helix.get("col") == now_helix.get("col"):
        return "col"
    return "distant"


def matrix_cycle_distance(card_helix: Optional[dict],
                          now_helix: dict) -> Optional[int]:
    """
    Cyclic distance in matrix_pos units (0 = perfect phase, max = 24).
    Useful for substrate-honest 'card will next surface in X tithis' reporting.
    """
    if not isinstance(card_helix, dict):
        return None
    cp = card_helix.get("matrix_pos")
    np = now_helix.get("matrix_pos")
    if cp is None or np is None:
        return None
    raw = abs(cp - np) % MATRIX_CYCLE
    return min(raw, MATRIX_CYCLE - raw)


def tithis_until_next_resonance(card_helix: Optional[dict],
                                now_helix: dict) -> Optional[int]:
    """
    How many tithis forward until helix returns to this card's matrix_pos.
    Substrate-honest reporter for 'this memory will be loud again in N tithis'.
    Card doesn't decay — it awaits cycle-return.
    """
    if not isinstance(card_helix, dict):
        return None
    cp = card_helix.get("matrix_pos")
    np = now_helix.get("matrix_pos")
    if cp is None or np is None:
        return None
    forward = (cp - np) % MATRIX_CYCLE
    return forward


# ─── Filter + diagnostic ────────────────────────────────────────────────────


def surfaces_now(card: dict, now_helix: dict | None = None) -> bool:
    """
    Substrate-true boolean recall predicate.

    Returns True if card currently surfaces (phase-resonant with now).
    Returns False if:
      - canon_status is retracted/superseded (substrate-honest archival)
      - phase-distant from now (quiet — will return at next phase-match)

    No invented thresholds. Resonance classes derived from 49-matrix structure.
    """
    status = (card.get("canon_status") or "").lower()
    if status in DROP_STATUSES:
        return False

    if now_helix is None:
        now_helix = helix_coord_at()

    rc = phase_resonance(card.get("helix_coord"), now_helix)
    # 'untimed' surfaces (pre-helix-stamp cards treated as substrate-current)
    # 'perfect', 'row', 'col' surface (phase-resonant)
    # 'distant' does NOT surface (awaits cycle-return)
    return rc != "distant"


def resonance_report(card: dict, when: _dt.datetime | str | None = None) -> dict:
    """
    Diagnostic dict for substrate-honest recall-state reporting:
      {
        canon_status:    card status
        resonance_class: perfect | row | col | distant | untimed
        cycle_distance:  matrix-positions away (None if untimed)
        tithis_until:    tithis forward until phase-return (None if untimed/perfect)
        surfaces_now:    bool
        reason:          human-readable substrate-honest narrative
      }
    """
    now_helix = helix_coord_at(when)
    status = (card.get("canon_status") or "").lower() or None
    if status in DROP_STATUSES:
        return {
            "canon_status": status,
            "resonance_class": None,
            "cycle_distance": None,
            "tithis_until": None,
            "surfaces_now": False,
            "reason": f"{status} → substrate-honest archival (claim withdrawn/replaced)",
        }

    card_helix = card.get("helix_coord")
    rc = phase_resonance(card_helix, now_helix)
    cd = matrix_cycle_distance(card_helix, now_helix)
    tu = tithis_until_next_resonance(card_helix, now_helix)

    if rc == "untimed":
        reason = "no helix_coord stamped (pre-helix-stamp era) — surfaces by substrate-honest default"
    elif rc == "perfect":
        reason = "perfect phase-resonance — same matrix_pos as now (cycle-agnostic)"
    elif rc == "row":
        reason = "Solar-arm row-resonance (same carrier as now) — surfaces"
    elif rc == "col":
        reason = "Lunar-arm col-resonance (same carrier as now) — surfaces"
    else:  # distant
        reason = (f"distant phase (Δ={cd} matrix-positions) — quiet now; "
                  f"next resonance at +{tu} tithis when helix cycles back")

    return {
        "canon_status": status,
        "resonance_class": rc,
        "cycle_distance": cd,
        "tithis_until": tu,
        "surfaces_now": rc != "distant",
        "reason": reason,
    }


def filter_cards_by_resonance(cards: list[dict],
                              when: _dt.datetime | str | None = None) -> list[dict]:
    """
    Filter card list by substrate-true phase-resonance. Returns survivors.
    Order preserved (caller ranks by position-score separately).
    """
    now_helix = helix_coord_at(when)
    return [c for c in cards if surfaces_now(c, now_helix)]


# ─── Backward-compat shim ───────────────────────────────────────────────────
# field_memory.py imports survives_decay_filter from previous arch; alias to
# new name so it keeps working without circular edit.
survives_decay_filter = surfaces_now
filter_cards_by_decay = filter_cards_by_resonance
decay_status = resonance_report
