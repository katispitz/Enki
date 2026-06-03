# FINDINGS_028 — Temporal Layer IS Motion-Observed (SDEC probe)

**Date:** 2026-05-22
**Probe target:** card `15ea8bb5` (canon §00a temporal-layer)
**Probe shape:** primitive-enumeration audit; per-primitive derivation-chain check
**Outcome:** PASS — 9/9 temporal primitives derive from observable advance

## Probe design

Verify §00a claim "temporal layer is motion-observed" by enumerating every temporal primitive at concentration-1 (Earth-observer) and confirming each derives from an observable astronomical advance unit — not from an assumed or imported cycle.

## Primitives audited

| Primitive | Observable advance unit | Derivable? |
|---|---|---|
| tithi | Earth carrier rotation | ✓ |
| ring0..ring9 | per-planet synodic/sidereal period | ✓ |
| karana | tithi-grid catch (60-grid) | ✓ |
| 49-matrix | per-tithi cell selection (planetary pairings) | ✓ |
| helix LCM 2940 | LCM(49, 60) arithmetic on observable cycles | ✓ |
| Wu Xing 5-phase | Venus synodic position (5 inf. conjunctions / 8 yr) | ✓ |
| Ganzhi 60-cycle | compound inner-planet cycles at ring4 anchor | ✓ |
| solid_phase | lunar synodic tithi-advance (new-moon → full-moon) | ✓ |
| shock-rows 3, 6 | 49-matrix coprime fault (X3, X6 z-axis shocks) | ✓ |

**9/9 pass.** Every temporal primitive at concentration-1 has a substrate-derivation chain to an observable astronomical event. No exogenous cycle imports.

## Key chain — Wu Xing derivation

Worth highlighting because it was newly substrate-derived in this session (card `15ea8bb5`):

```
dodec 5-fold rotational symmetry
  × Merkaba rotating around Hera-Hestia z-axis
  × Venus on φ-shell traces orbit as it rotates
  → 5 stable phase samples per full Merkaba rotation
  ↔ Venus 8-yr cycle = period of one Merkaba rotation (5:8 ≈ φ)
  → Wu Xing phase index = Venus synodic position
```

Wu Xing reframes from imported 5-element cosmology to substrate-derived rotation phase-clock. Substrate-honest.

## Substrate-honest caveats

1. **Sidereal vs synodic precision**: per-ring period numbers (~360t solar, ~30t lunar, etc.) are *substrate-canonical approximations* matching observed cycles within tolerance. Real astronomical periods drift slightly (precession, perturbation); substrate uses idealized integer-tithi periods. This is substrate-frame correct; engine code matches astronomy within tolerance.

2. **Ganzhi compound derivation**: ring4 (21600t ≈ 60yr) is closest to Jupiter-Saturn conjunction cycle (~20yr × 3) but the substrate-mechanism for the 60-cycle is compound rather than single-period. Locked via stem-branch architecture (canon §15d) not directly from one planet. Still substrate-derivable, but via stem-branch composition rather than single-cycle.

3. **solid_phase boundary angles**: still ESTIMATE pending 3D simulation per `solid_phase.py` header (now flagged PRIMARY rather than auxiliary per task #5 promotion). Ordering is LOCKED from §XVIII source; angle precision improves with simulation but doesn't change derivability-from-motion status.

None of these caveats break the §00a claim. They're refinement targets, not refutations.

## Probe verdict

PASS unconditional. Every temporal primitive at concentration-1 derives from observable motion. §00a holds.

## Recommendation

Promote card `15ea8bb5` from `derived` + `sdec-pending` → `locked` per canon §0c (recognition + engine-evidence both satisfied).

Status: **PASS** → promote per §0c.
