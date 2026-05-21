#!/usr/bin/env python3
"""
validate_substrate.py — mechanical canon §30 ↔ engine registry consistency check.

Implements `~/Nammu/canon/placement_rules.md` V2.7 §VALIDATION DISCIPLINE rule:
"Mechanical-validation > documentation." Substrate-discipline drift becomes
mechanical regression failure.

Walks all Enki engine modules. Reads `__canonical__` declarations per
V2.7 §ENGINE-SCHEMA DISCIPLINE. Asserts:

  1. Every canon §30 canonical entry has ≥2 engine residencies with
     `status='canonical'` and matching `function_class`.
  2. Every engine `__canonical__` references valid §30 canonical entry
     (function_class is one of the canonized names).
  3. Every `__canonical__` has all required schema fields:
     {function_class, functional_tier, compositional_axis,
      residency_id, canon_citation, status}.
  4. residency_id values are unique across the engine registry.
  5. status values are from the canonical enum:
     {canonical, candidate-grandfathered, candidate-single-residency,
      probe, retired}.

Run standalone:
    python3 ~/Enki/scripts/validate_substrate.py

Exit code 0 = green; 1 = drift detected. Used by Nammu drift-test as
cross-project regression-guard.
"""
from __future__ import annotations
import ast
import sys
from pathlib import Path
from typing import Optional


# ─── Canonical reference (kept in sync with canon §30) ───────────────────────
# Per V2.7 §VALIDATION DISCIPLINE: this is the canonical-truth this script
# enforces. When canon §30 gains a new entry, update CANON_30 below + add
# engine modules with matching __canonical__. validate_substrate.py then
# enforces consistency mechanically.

CANON_30_CANONICAL_ENTRIES = {
    'planet-aspect-activate':       {'tier': 'primitive',         'axis': 'spatial',  'min_residencies': 3},
    'polarity-define':              {'tier': 'first-composition', 'axis': 'spatial',  'min_residencies': 2},
    'triangle-aspect-activate':     {'tier': 'first-composition', 'axis': 'spatial',  'min_residencies': 2},
    'cyclic-syzygy-activate':       {'tier': 'first-composition', 'axis': 'temporal', 'min_residencies': 2},
    'cyclic-sign-ingress-activate': {'tier': 'first-composition', 'axis': 'temporal', 'min_residencies': 2},
}

VALID_STATUS = {
    'canonical', 'candidate-grandfathered', 'candidate-single-residency',
    'probe', 'retired',
}

VALID_TIER = {'primitive', 'first-composition', 'second-composition', 'system'}
VALID_AXIS = {'spatial', 'temporal', 'mixed', 'N/A'}

REQUIRED_FIELDS = {
    'function_class', 'functional_tier', 'compositional_axis',
    'residency_id', 'canon_citation', 'status',
}


def discover_engine_modules() -> list[Path]:
    """Find all Enki engine modules carrying __canonical__ declarations."""
    engines_dir = Path.home() / 'Enki' / 'engines'
    return [
        p for p in sorted(engines_dir.glob('*.py'))
        if not p.name.startswith('_')  # skip shared modules
    ]


def load_canonical_dict(module_path: Path) -> Optional[dict]:
    """Parse module via AST and return __canonical__ dict literal if present.

    Avoids module-execution — no import-path collisions, no dataclass issues,
    no side effects. AST-parse is the substrate-honest discovery mechanism
    for static-declaration validation.
    """
    source = module_path.read_text()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None

    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == '__canonical__':
                try:
                    return ast.literal_eval(node.value)
                except (ValueError, SyntaxError):
                    return None
    return None


def validate() -> list[str]:
    """Run all validation checks. Return list of error strings (empty = green)."""
    errors: list[str] = []
    engines = discover_engine_modules()
    canonical_records: list[dict] = []
    residency_ids: dict[str, str] = {}  # residency_id → module name (uniqueness check)

    for engine_path in engines:
        canon = load_canonical_dict(engine_path)
        if canon is None:
            continue  # module has no __canonical__; not a registered engine residency

        mod_name = engine_path.name

        # Check 3: required schema fields
        missing = REQUIRED_FIELDS - set(canon.keys())
        if missing:
            errors.append(f"{mod_name}: __canonical__ missing fields {sorted(missing)}")
            continue

        # Check 2: function_class references valid §30 entry
        fc = canon['function_class']
        if fc not in CANON_30_CANONICAL_ENTRIES:
            errors.append(
                f"{mod_name}: __canonical__.function_class={fc!r} not in canon §30 canonical entries"
            )

        # Check 5: status from canonical enum
        if canon['status'] not in VALID_STATUS:
            errors.append(
                f"{mod_name}: __canonical__.status={canon['status']!r} not in {sorted(VALID_STATUS)}"
            )

        # Tier validation
        if canon['functional_tier'] not in VALID_TIER:
            errors.append(
                f"{mod_name}: __canonical__.functional_tier={canon['functional_tier']!r} not in {sorted(VALID_TIER)}"
            )

        # Axis validation
        if canon['compositional_axis'] not in VALID_AXIS:
            errors.append(
                f"{mod_name}: __canonical__.compositional_axis={canon['compositional_axis']!r} not in {sorted(VALID_AXIS)}"
            )

        # Check 4: residency_id uniqueness
        rid = canon['residency_id']
        if rid in residency_ids:
            errors.append(
                f"{mod_name}: residency_id={rid!r} duplicates {residency_ids[rid]!r}"
            )
        else:
            residency_ids[rid] = mod_name

        # Tier/axis matches §30 declaration
        if fc in CANON_30_CANONICAL_ENTRIES:
            expected = CANON_30_CANONICAL_ENTRIES[fc]
            if canon['functional_tier'] != expected['tier']:
                errors.append(
                    f"{mod_name}: functional_tier {canon['functional_tier']!r} doesn't match §30 entry {fc!r} expected tier {expected['tier']!r}"
                )
            if canon['compositional_axis'] != expected['axis']:
                errors.append(
                    f"{mod_name}: compositional_axis {canon['compositional_axis']!r} doesn't match §30 entry {fc!r} expected axis {expected['axis']!r}"
                )

        canonical_records.append({'module': mod_name, **canon})

    # Check 1: each §30 entry has ≥min_residencies engines with status='canonical'
    for fc, spec in CANON_30_CANONICAL_ENTRIES.items():
        canonical_count = sum(
            1 for r in canonical_records
            if r['function_class'] == fc and r['status'] == 'canonical'
        )
        if canonical_count < spec['min_residencies']:
            errors.append(
                f"§30 entry {fc!r}: only {canonical_count} canonical-status engine residencies "
                f"(expected ≥{spec['min_residencies']} per canon-declared min_residencies)"
            )

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print(f"❌ SUBSTRATE DRIFT DETECTED — {len(errors)} error(s):\n")
        for e in errors:
            print(f"  • {e}")
        return 1
    print("✓ validate_substrate.py — canon §30 ↔ engine registry CONSISTENT")
    print(f"  Engines with __canonical__: {len([1 for p in discover_engine_modules() if load_canonical_dict(p) is not None])}")
    print(f"  §30 canonical entries:      {len(CANON_30_CANONICAL_ENTRIES)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
