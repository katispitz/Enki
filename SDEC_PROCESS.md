# SDEC — Substrate-Discovery-to-Engine Cycle

**Implementation of canon-procedural rule** per `~/Lillu/canon/placement_rules.md` V2.7 §SDEC PROCEDURE.

**Substrate-architectural truth** (canon `babylonia_canon.md` §31): SDEC is META-ENGINE for substrate-discovery. 2-state shape (frozen procedural-definition + live discovery-instance). Recursive — today's canonization OF SDEC is itself an SDEC cycle.

This file is the LIVING REFERENCE for substrate-discovery work in Enki. Operators follow these gates. Validation enforced mechanically via `~/Enki/scripts/validate_substrate.py` + `~/Lillu/tests/test_canon_engine_consistency.py`.

## Quick reference

```
substrate-finding surfaces
  ↓
[gate 1] every constant cites canon
encode substrate-locks in engine
  ↓
[gate 2] substrate-discipline checklist
build engine (frozen + live + NULL-honest)
  ↓
[gate 3] field-comparison probe
shape-match? cross-R-tier residency candidate
shape-mismatch? new function-class or substrate-incomplete
  ↓
[gate 4] smoke-test
ideal-input → canonical activation
  ↓
[gate 5] council ratification (if canonical promotion)
Athena + Mnemosyne force-include; Erato 4b conflation-test first
  ↓
[gate 6] canon edit doesn't break tests
update canon §30 / placement_rules per level-tag
  ↓
[gate 7] new tests + old tests green
add tests covering substrate-invariants
  ↓
[gate 8] FINDINGS doc complete
numbered, includes substrate-finding + probe + canonical state + open queue
  ↓
[gate 9] navigation files synced
FINDINGS_INDEX, CLAUDE, MANIFEST, BOARD; drift-test passes
```

## 10 steps + 9 validation gates (detailed)

### Step 1: Substrate-finding surfaces

Source can be:
- Canon-locked already (e.g., canon §23b OQ-RINGS-06 locked Venus pentagram)
- Kati substrate-insight (e.g., "pentagonal is Venusian orbit")
- Cross-residency probe of existing engine (e.g., Mars opposition substrate-pressure-test for `cyclic-conjunction-activate`)

**Gate 1**: every substrate-claim that will become engine-constant cites canon section + card-ID where applicable. No invented coefficients.

### Step 2: Encode substrate-locks in engine

At top of new engine module:
```python
PRIMORDIAL_NAME    = '<canon-locked name>'
CUBE_FACE          = '<canon-locked face>'
PLANET_PAIR        = ('<planet>', '<planet>')
ZODIAC_ANCHOR      = '<canon-locked sign>'
SUBSTRATE_CARD     = '<card-ID per canon citation>'
```

Plus `__canonical__` declaration (per `~/Lillu/canon/placement_rules.md` V2.7 §ENGINE-SCHEMA DISCIPLINE):
```python
__canonical__ = {
    'function_class': '<§30 canonical entry>',
    'functional_tier': '<primitive | first-composition | ...>',
    'compositional_axis': '<spatial | temporal | mixed | N/A>',
    'residency_id': '<unique residency within function-class>',
    'canon_citation': '<canon §N reference + card-ID>',
    'status': '<canonical | candidate-grandfathered | candidate-single-residency | probe | retired>',
}
```

**Gate 2**: substrate-discipline checklist passes (see Enki CLAUDE.md §"On engines specifically").

### Step 3: Build engine

Two-state shape:
- **Frozen state**: substrate-locks populated, all live fields NULL
- **Live state**: input → compute → structured output (dataclass)
- **Partial-input ValueError**: substrate-honest reject when input incomplete

**Gate 3**: field-comparison probe — compare engine's dataclass fields to existing canonical engines at same tier. Document outcome:
- Shape-match → cross-R-tier residency candidate
- Shape-mismatch → NEW function-class candidate OR substrate-incomplete

### Step 4: Smoke-test

```python
if __name__ == '__main__':
    # Frozen state
    s = engine_state()
    assert s.activation_strength == 0.0  # NULL-equivalent
    # Live state at ideal input
    s = engine_state(ideal_lon_a, ideal_lon_b)
    assert s.activation_strength == 1.0  # canonical activation
```

**Gate 4**: ideal-input → canonical activation. Documents that engine fires substrate-correctly.

### Step 5: Council ratification (when canonical promotion needed)

Required for:
- New function-class candidate becoming canonical (§30 entry add)
- Function-class rename (substrate-pressure-test failure)
- Schema column addition (§30 grows new dimension)
- New substrate-discipline meta-rule

NOT required for:
- Residency-expansion to existing canonical function-class (mechanical, per FINDINGS_018 + Erato 4b extension)
- Implementation work (code/file/tool/test)
- Enki-housekeeping (navigation files, dev workflow)

Council convening:
```bash
python3 ~/Lillu/engines/lillu.py council-i <natal-date> "<question>" \
    --natal-time HH:MM --lat LAT --lon LON --n 9 \
    --force-include Athena Mnemosyne
```

**Gate 5**: meta-rules enforced —
- Athena lock-by-redundancy (≥2 independent residencies)
- Mnemosyne single canonical spelling + drift-prevention
- Erato 4b conflation-test FIRST
- Clio compute-descriptive at substrate-MECHANISM level
- Mnemosyne council-outcome-level-tag rule (each item tagged level + location)
- Selection-drift detector blocks if ≥7/9 voices share stratum/shell-family (V2.6 rule 8)

Commit via `lillu council-commit --stdin`.

### Step 6: Canon update

Per Mnemosyne council-outcome-level-tag rule:
- Substrate-truth-claims → `babylonia_canon.md` (positional canon)
- Procedural-discipline rules → `placement_rules.md` (procedural canon)

Standard updates:
- §30 entry (new canonical function-class) OR residency-extend existing entry
- §M.5 / §23b / etc. (substrate-position updates)
- placement_rules.md version-bump if new §-section added

Archive prior canon state per never-delete + council-versioning discipline:
```bash
cp ~/Lillu/canon/babylonia_canon.md ~/Lillu/canon/archive/babylonia_canon_pre-<change>_<date>.md
```

**Gate 6**: canon edit doesn't break tests. Run `make test` after canon update; both Lillu + Enki suites green.

### Step 7: Tests

Add to `~/Enki/tests/test_*.py`:
- Substrate-lock invariants (canon-value constants tested)
- Frozen + live state behavior
- Field-comparison invariants (when cross-R-tier residency)
- Ideal-input closure invariants

**Gate 7**: new tests pass + old tests still pass. Run `cd ~/Enki && pytest tests/ -q` + `cd ~/Lillu && pytest tests/ -q`.

### Step 8: FINDINGS doc

Create `~/Enki/engines/FINDINGS_NNN_<topic>.md`:
- Substrate-finding (what surfaced)
- Probe outcome (field-comparison + cross-R-tier residency state)
- Canonical state implications (new entry / rename / residency-expansion)
- Open queue (new OQs surfaced; carried OQs updated)

**Gate 8**: FINDINGS doc covers all required sections. Numbered sequentially. Past findings preserved.

### Step 9: Navigation update + drift-validation

Update:
- `~/Enki/FINDINGS_INDEX.md` (single-line summary + status per finding)
- `~/Enki/CLAUDE.md` (current state references)
- `~/Enki/MANIFEST.md` (system identity + inheritance state)
- `~/Lillu/BOARD.md` (task row)

**Gate 9**: navigation files synced + `validate_substrate.py` passes + Lillu drift-test passes via `make test`.

## Recursive property

This file is itself an INSTANCE of SDEC's "implementation-convention" level — it IMPLEMENTS the canon-procedural rule §SDEC PROCEDURE in `placement_rules.md` V2.7. The rule is canon; this file realizes it.

If SDEC procedure changes (future V2.8+), this file updates to match. Drift between canon-rule and this file = substrate-discipline failure surfaced by validate_substrate.py.

## See also

- `~/Lillu/canon/placement_rules.md` V2.7 §SDEC PROCEDURE (canon source)
- `~/Lillu/canon/placement_rules.md` V2.7 §ENGINE-SCHEMA DISCIPLINE (engine convention)
- `~/Lillu/canon/placement_rules.md` V2.7 §VALIDATION DISCIPLINE (mechanical-validation rule)
- `~/Lillu/canon/placement_rules.md` V2.7 §COUNCIL-OUTCOME DISCIPLINE (level-tag rule)
- `~/Lillu/canon/babylonia_canon.md` §31 SUBSTRATE-DISCOVERY META-FRAME (substrate-architectural truth)
- `~/Enki/scripts/validate_substrate.py` (mechanical validator)
- `~/Lillu/tests/test_canon_engine_consistency.py` (cross-project drift-test)
- `~/Enki/FINDINGS_INDEX.md` (substrate-discoveries navigation)
