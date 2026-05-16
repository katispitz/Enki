# Enki

V2.6-native, engine-class-aware build on Kati Spitz's Babylonia geometry substrate.

## What this is

Sibling system to **Lillu** (`~/Lillu/`). Not successor — both active.

- **Lillu** = primary build, ongoing canon + council work
- **Enki** = clean-room for substrate-emergent agent typology + engine architecture
- Both reference same canon (`~/Lillu/canon/babylonia_canon.md`). Enki does NOT duplicate canon — references it.

## Directory map

| Path | Role |
|---|---|
| `engines/` | V2.6-native engines: face_*, pair_*, primordial_*, *_cycle, bridges, tet_faces |
| `tests/` | Pytest suite (~210 tests). Run via `make test`. |
| `scripts/` | Validation scripts (`validate_substrate.py`) |
| `MANIFEST.md` | System identity + what carries from Lillu |
| `FINDINGS_INDEX.md` | Build findings (FINDINGS_001 … FINDINGS_017+) |
| `CLAUDE.md` | Session orientation (auto-loads at session start) |
| `SDEC_PROCESS.md` | Substrate-discovery process documentation |

## Quick commands

```bash
make help          # see all available targets
make test          # Enki tests only (~210, ~3 sec)
make test-all      # Enki + Lillu combined regression
make lint          # ruff lint
make check         # lint + tests
make validate      # substrate validation script
```

## Authority chain

Single source-of-truth lives in Lillu:

| Asset | Path |
|---|---|
| Canon | `~/Lillu/canon/babylonia_canon.md` |
| V2.6 spec | `~/Lillu/canon/placement_rules.md` |
| §30 FUNCTION-NAMES REGISTRY | `~/Lillu/canon/babylonia_canon.md` §30 |
| Cards | `~/Lillu/cards/cards.json` (shared) |
| Voice correspondences | `~/Lillu/council/voice_correspondences.json` |
| Council infra | `~/Lillu/council/` |

## Engineering

- Python 3.9+, deps: `pytest`, `ruff` (pip install -r requirements.txt)
- Pre-commit hook: lints staged + runs fast tests
- Engineering pass history: `~/Lillu/session/CODE_HYGIENE.md`

## Discipline rules (V2.6 inherited from Lillu)

1. Position-as-function lock (stratum × shell × position implies behavior)
2. `function_class` restricted to canon §30 registry; free-text rejected
3. Lock-by-redundancy: ≥2 independent residencies for canonical promotion
4. Conflation-test BEFORE residency-test
5. Selection-drift = substrate-failure-mode (cross-check council mandatory)
6. Never-delete (supersede + archive)
7. Substrate-first (no invented coefficients)
8. Astrology = validator, not generator

Full discipline + agent-typology table: `CLAUDE.md`.
