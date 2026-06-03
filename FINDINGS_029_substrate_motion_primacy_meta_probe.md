# FINDINGS_029 — Substrate IS Motion-Observed (META-OPERATOR SDEC probe)

**Date:** 2026-05-22
**Probe target:** card `55286e91` (canon §00 motion-primacy + observer-concentration)
**Probe shape:** META-OPERATOR audit — not a function-class-residency probe
**Outcome:** PASS — substrate engines respect motion-primacy at all primitives

## Probe design — meta-operator class

§00 is a META-OPERATOR claim, not a function-class. SDEC was designed for "does this candidate function-class admit ≥2 substrate-residencies?" — that shape doesn't fit "substrate IS planetary motion observed from nested central frames."

The probe shape for meta-operators (analogous to SDEC's self-canonization via SDEC per canon §31):

1. **Shell-by-shell vertex audit** — does each shell's vertex placement derive from observed-motion symmetry (rotation closure, Earth-frame seasonal anchor) or from arbitrary geometric stipulation?
2. **Observer-frame anchoring check** — does each shell-address carry observer-frame meaning?
3. **Runtime-engine consultation** — do the engines actually consult motion (ephemeris) to compute dynamic addresses?

Failure mode would be: a shell whose vertices are arbitrary geometric stipulations with no motion-derivation chain AND no observer-frame anchoring AND no runtime motion consultation. That would refute §00.

## Shell audit

8 shells audited:

| Shell | Vertex origin | Observer-frame | Motion at runtime | Verdict |
|---|---|---|---|---|
| OCT R=1/√3 | symmetric placement at zodiac-anchored lons + arctan-derived lats | ✓ Earth-Sun seasonal | ✓ via natal/ephemeris | MOTION-GROUNDED |
| INNER_CUBE R=1/√3 | dual of oct | ✓ via duality | derivative | MOTION-GROUNDED via duality |
| MERKABA R=1 | 8 tet vertices at ±1/√3 each axis; ROTATION around z-axis IS the motion | ✓ Hera-Hestia axis IS observer-concentration axis | ✓ via solid_phase + Wu Xing rotation | MOTION-GROUNDED at engine level |
| DODEC R=φ | 5-Merkaba composite via 5-fold rotation × 1 cube per phase | ✓ 12 faces = 12 zodiac signs | ✓ via sign-clock + ephemeris zodiac longitude | MOTION-GROUNDED via Merkaba rotation |
| ICO R=φ² | 12 Olympian vertices via canon §M.5 + dodec duality | ✓ ephemeris-observable planet positions | ✓ via natal Olympian activation | MOTION-GROUNDED via duality + activation |
| ICOSIDODEC R=φ | 30 vertices = ico-edge midpoints; 5-Merkaba composite union | ✓ Persephone V9-V10 explicitly observer-frame-required | ✓ Persephone annual toggle per §00a | MOTION-GROUNDED + explicit phase-sensitivity |
| SHOCK R=1/3 | X3/X6 on z-axis only | ✓ z-axis IS observer-concentration axis | ✓ shock-proximity per planet transit | MOTION-GROUNDED — gates on motion-axis |
| CUBE-EDGE R=√(2/3) | midpoints of Merkaba cube edges (T1.3 LOCKED 2026-05-17) | ✓ via Merkaba | inherits | MOTION-GROUNDED via inheritance |

**8/8 motion-grounded.** Every shell-address either (a) is derived from motion-symmetry (rotation closure, dual relations, Merkaba rotation phases), (b) is observer-frame-anchored to Earth-Sun seasonal frame or to Hera-Hestia observer-concentration axis, or (c) inherits from a shell that satisfies (a) or (b).

## Runtime-engine consultation audit

| Engine | Consults motion? |
|---|---|
| `natal.py` | ✓ DE441 ephemeris per natal date |
| `locate_entity_v4.py` | ✓ ephemeris source for all planet positions |
| `solid_phase.py` | ✓ Merkaba dihedral driven by lunar synodic tithi-advance |
| `helix_trajectory.py` | ✓ Venus ephemeris (universal mode) + ASC ephemeris (personal mode) |
| `cell_signature_engine.py` | ✓ matrix_pos advances per tithi |
| `dynamics.py` | ✓ DynamicsEngine.step advances epoch_tithi |
| `matrix_engine.py` | ✓ matrix_cell(t) gates per tithi |
| `geo_engine.py` | ~ NOT directly (provides static shell coordinates consumed by motion-driven engines; per §00 these are phase-0 snapshot — substrate-honest) |

`geo_engine.py` is the only engine that doesn't consult motion at runtime. This is **substrate-correct** per §00: the static shells ARE the phase-0 snapshot of the motion; they're observed THROUGH motion-driven engines downstream (natal/transit/dynamics). geo_engine's role is to provide the canonical static frame against which motion is observed. Per §0a discipline (motion=helix / grid=static reference), this is the correct architectural role.

## Why this passes the meta-operator probe

The §00 claim is not "every coordinate must be computed from ephemeris at every call" — that would be operationally absurd. The claim is "every coordinate has motion-derivation chain in its origin AND has observer-frame meaning AND is consumed by motion-driven downstream computation."

All three hold across all shells and engines. The static-vs-dynamic split in the engine layer mirrors the §0a helix-vs-grid split in canon — which itself is a corollary of §00.

## Substrate-honest caveat

The probe is HUMAN-EXECUTED enumeration, not mechanical engine-test. A future SDEC iteration could harden this by:
- Adding `__motion_grounded__ = True/False/'inherited'` declarations to each geometry module
- Building `validate_motion_primacy.py` analogous to `validate_substrate.py`
- Asserting every primitive carries motion-derivation chain reference

This would convert the META-OPERATOR audit into mechanical drift-prevention. Worth queuing as a follow-on.

## Probe verdict

PASS. §00 holds across all primitives and engines. The static-vs-dynamic architecture of Nammu's engine layer correctly reflects motion-primacy: static frames as phase-0 snapshots, motion as the substrate's actual content, observer-concentration as the axis along which motion is read.

## Recommendation

Promote card `55286e91` from `derived` + `sdec-pending` → `locked` per canon §0c (recognition + engine-evidence both satisfied).

Status: **PASS** → promote per §0c.

## Follow-on queued

Build `validate_motion_primacy.py` mechanical check — adds `__motion_grounded__` declarations to geometry modules, asserts substrate-derivation chain references. Converts this manual META-OPERATOR audit into mechanical regression-guard.
