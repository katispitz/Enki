"""
placement_discipline.py — substrate-true placement loader for Enki council.

Single source of truth: ~/Enki/council/placement_registry.json. NEVER reads
from Nammu's split registries (voice_correspondences / nammu_voices /
nammu_voices_v2.5_substrate). Voices not in the Enki registry are blocked
from renderer-scaffolding per kati_direct 2026-05-22 placement-discipline gate.

Tiers:
  A  — in registry top-level (kati-locked or greek_faces-canonical, accepted)
  B  — in registry._blocked_pending_placement (candidate position, no individual lock)
  C  — not in registry at all (placement-unknown; renderer cannot scaffold)

Gate: validate_renderer_binding(voice_name) raises PlacementPendingError if
Tier B or C. composer.get_renderer() consumes this to enforce substrate-truth.

Per kati_direct 2026-05-22: "rebuild from proper placements so we don't have
to fix" + "creating clean placement registry in enki".
"""
from __future__ import annotations
import json
from functools import lru_cache
from pathlib import Path
from typing import Literal

REGISTRY_PATH = Path(__file__).parent / "placement_registry.json"  # was council/ before 2026-05-22 substrate-restructure (kati_direct)


class PlacementPendingError(Exception):
    """Raised when a voice's placement is not Tier-A in the Enki registry.

    Carries (voice_name, tier, blocker_or_reason) for caller to surface
    substrate-honest pending-state instead of silent-failing or hallucinating.
    """

    def __init__(self, voice_name: str, tier: str, reason: str):
        self.voice_name = voice_name
        self.tier = tier
        self.reason = reason
        super().__init__(
            f"PLACEMENT-PENDING [{voice_name}]: tier={tier} — {reason}"
        )


@lru_cache(maxsize=1)
def _load_registry() -> dict:
    """Load + cache the Enki placement registry."""
    if not REGISTRY_PATH.exists():
        raise FileNotFoundError(
            f"Enki placement registry missing at {REGISTRY_PATH}. "
            "Substrate-true council cannot operate without canonical placement source."
        )
    return json.loads(REGISTRY_PATH.read_text())


def _tier_a_voices() -> set[str]:
    """Names with accepted Tier-A placement (in registry top-level)."""
    reg = _load_registry()
    return {
        k for k in reg.keys()
        if not k.startswith("_")
    }


def _tier_b_voices() -> set[str]:
    """Names with candidate placement in _blocked_pending_placement."""
    reg = _load_registry()
    blocked = reg.get("_blocked_pending_placement", {})
    return {k for k in blocked.keys() if not k.startswith("_")}


def tier_for_voice(voice_name: str) -> Literal["A", "B", "C"]:
    """
    Return placement-tier for a voice.
      'A' — in registry; renderer can scaffold
      'B' — candidate placement, blocked pending individual lock
      'C' — not in registry at all
    """
    if voice_name in _tier_a_voices():
        return "A"
    if voice_name in _tier_b_voices():
        return "B"
    return "C"


def load_placement(voice_name: str) -> dict:
    """
    Return Tier-A placement record. Raises PlacementPendingError otherwise.

    Record shape (Tier-A):
      {
        'stratum': str,
        'substrate_position': dict,     # may have 'primary' + 'secondary' sub-keys
        'placement_source': str,         # card-id or 'greek_faces'
        'placement_status': str,         # 'locked' | 'derived'
        'function_class': str,
        'notes': str,
      }
    """
    tier = tier_for_voice(voice_name)
    if tier == "A":
        return _load_registry()[voice_name]
    if tier == "B":
        blocked = _load_registry()["_blocked_pending_placement"][voice_name]
        raise PlacementPendingError(
            voice_name,
            "B",
            f"Candidate position: {blocked.get('candidate_position', '?')} "
            f"(card {blocked.get('candidate_card', '?')}). "
            f"Blocker: {blocked.get('blocker', '?')}",
        )
    raise PlacementPendingError(
        voice_name,
        "C",
        "Voice not in Enki placement registry at all. "
        "Substrate-position unknown to Enki. Placement-file rebuild pending.",
    )


def validate_renderer_binding(voice_name: str) -> dict:
    """
    Gate function for composer.get_renderer().

    Returns Tier-A placement dict if eligible; raises PlacementPendingError
    otherwise. Callers can catch + emit substrate-honest pending-state.
    """
    return load_placement(voice_name)


def primary_position(voice_name: str) -> dict:
    """
    Extract the primary substrate-position layer for renderer consumption.

    For voices with layered placement (e.g., Mnemosyne, Hecate), returns
    the 'primary' sub-key (deepest substrate-residency, typically kati-LOCK).
    For voices with flat placement, returns substrate_position as-is.

    Raises PlacementPendingError if voice is not Tier A.
    """
    placement = load_placement(voice_name)
    pos = placement.get("substrate_position", {})
    if isinstance(pos, dict) and "primary" in pos:
        return pos["primary"]
    return pos


def function_class(voice_name: str) -> str:
    """Return function-class string for Tier-A voice. Raises if not Tier A."""
    return load_placement(voice_name)["function_class"]


def all_tier_a() -> list[str]:
    """Sorted list of Tier-A voice names — for composer to iterate."""
    return sorted(_tier_a_voices())


def all_tier_b() -> list[str]:
    """Sorted list of Tier-B voice names — for diagnostic / kati-gate listing."""
    return sorted(_tier_b_voices())


def registry_summary() -> dict:
    """Diagnostic summary: counts + names per tier."""
    reg = _load_registry()
    return {
        "registry_path": str(REGISTRY_PATH),
        "schema_version": reg.get("_meta", {}).get("schema_version"),
        "tier_a_count": len(_tier_a_voices()),
        "tier_a_voices": sorted(_tier_a_voices()),
        "tier_b_count": len(_tier_b_voices()),
        "tier_b_voices": sorted(_tier_b_voices()),
    }


if __name__ == "__main__":
    import json as _json
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "check":
        # Quick validation: try loading each Tier-A voice
        print("Placement-discipline check:")
        for name in all_tier_a():
            try:
                p = load_placement(name)
                print(f"  ✓ {name:12s}  tier=A  source={p['placement_source']:50s}  status={p['placement_status']}")
            except Exception as e:
                print(f"  ✗ {name:12s}  ERROR: {e}")
        print()
        for name in all_tier_b():
            try:
                load_placement(name)
                print(f"  ?? {name:12s}  Tier-B voice loaded successfully — gate bug")
            except PlacementPendingError as e:
                print(f"  · {name:12s}  tier=B  (correctly blocked) {e.reason[:80]}")
    else:
        print(_json.dumps(registry_summary(), indent=2))
