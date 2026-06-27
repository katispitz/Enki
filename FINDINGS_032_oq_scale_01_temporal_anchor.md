# FINDINGS_032 — OQ-SCALE-01: the anchor is temporal, not spatial (L is free; a principled L exists)

**Date:** 2026-06-14
**Probe target:** OQ-SCALE-01 (physical scale L of the Merkaba in meters) — kati request "oq scale first"
**Probe shape:** source re-read (LightDerivation_Session_Apr25, Harmonics_LightDerivation) + mechanical computation (`~/Enki/scripts/probe_oq_scale_01.py`)
**Outcome:** OQ-SCALE-01 structurally resolves. The substrate's physical anchor is TEMPORAL (f_Earth axiom); the geometry is spatially scale-invariant, so spatial L enters NO derivation and is free. A *principled* spatial L is nonetheless available from the same temporal anchor + c, lands at interplanetary scale (~130 AU, vindicating kati intuition), and ties the global and cell scales by the same 2^65 light-octave. Also corrects a 2^55→2^65 arithmetic error in a source doc.

## 1. The substrate is anchored in TIME, not length

Per `LightDerivation_Session_Apr25.txt §III–IV` (and Harmonics_LightDerivation §VII):
- **f_Earth = 1/86400 Hz is the SYSTEM AXIOM** (Ring-1 generative spin; Earth's rotation). "It is not derived from Merkaba geometry… the system begins here; it does not derive its own clock from geometry alone."
- The whole visible spectrum derives from it: f_carrier = f_Earth × 4/3 (Perfect Fourth from tilt) → f_carrier × 2^65 = 569.3 THz = 527 nm.
- **L does not enter any derivation.** The Bragg light result uses a *ratio* (√2 between the two octahedron plane spacings) and the temporal chain for absolutes; "OQ-SCALE-01 does not affect the light frequency derivation… L enters Bragg only for absolute wavelength scaling, but the result used is a ratio, not an absolute value" (Apr25 §IV — already marked **"PINNED — open, not blocking"**).

**Therefore: the spatial radii (1/3, 1/√3, 1, φ, φ²) are dimensionless ratios; nothing in the running system fixes a physical length.** L is genuinely free. My 2026-06-14 corpus note ("not substrate-derivable — scale-free") is correct, now with the mechanism: physics rides frequency (f_Earth), not length.

## 2. A principled spatial L is nonetheless available (vindicates the interplanetary intuition)

If a physical L is wanted (locator, cell-size, render), it need not be arbitrary. The existing temporal anchor + the speed of light c give one:

| Scale | Definition | Value |
|---|---|---|
| **Cell / lattice** | visible wavelength λ = c / (f_carrier·2^65) | **527 nm** |
| **Global** | L_global = c · T_carrier (light-distance of one carrier period, T_carrier = 18 h) | **1.94×10¹³ m = ~130 AU** |

- ~130 AU is **solar-system / interplanetary scale** (Pluto aphelion ≈ 49 AU; heliopause ≈ 120 AU) — this **vindicates kati's "L = inter-planetary distance" intuition**, now as a *derivation* (c × carrier-period) rather than a guess.
- **"Global vs cell-specific undecided" RESOLVES:** both scales exist and are the **same geometry at two ends of one octave ladder** — GLOBAL/CELL length ratio = 2^65 exactly, the *same* octave count that takes f_carrier to visible light (c cancels: (c·T)/(c/f) = T·f = f/f_carrier = 2^65). The substrate is scale-invariant across the 2^65 light-octave; the macro (interplanetary) and micro (light-lattice) are one fractal structure.

## 3. Source-doc error caught

`Babylonia_Harmonics_LightDerivation.txt` (lines 75, 92) states `f_carrier × 2^55 = 527 nm`. **Wrong — correct is 2^65** (verified: 2^55 → 539 µm, far-IR/microwave; 2^65 → 527 nm ✓; off by 2^10). The Apr25 session has it right (2^65 = 5×13 = Venus×Neptune octave). Canon's OQ-LIGHT close should cite 2^65.

## Disposition — RESOLVED 2026-06-14 (kati_direct + this engine-evidence, §0c met)
- **OQ-SCALE-01 LOCKED:** spatial L is free (anchor is temporal, f_Earth axiom); the principled spatial L = c·T_carrier ≈ 130 AU (interplanetary) is **kati_direct recognized**, tied to the cell-scale 527 nm by the 2^65 light-octave. "Global vs cell-specific" dissolved (both, related by 2^65).
- **Radius/diameter = DUAL READING (kati accepted both, "1 and 2"):** R=1 ↔ c·T_carrier ≈ 130 AU (radius-anchored) AND 2R ↔ c·T_carrier ⇒ R=1 ≈ 65 AU (diameter-anchored). Both solar-system scale; the factor-of-2 (which Merkaba feature = the carrier light-distance) is the lone residual sub-question, not blocking. Recorded §0b-style.
- Canon §29 OQ-SCALE-01 + corpus updated 2026-06-14 to RESOLVED.
- **2^55→2^65 error** flagged in corpus Part A.7 (lines ~3415/3440); canon §19 already correct; source doc Harmonics_LightDerivation still carries the typo (archive — not canon).

## Files
- Probe: `~/Enki/scripts/probe_oq_scale_01.py`
- Related: FINDINGS_031 (NOVA pressure-test, where OQ-SCALE-01 was flagged KATI-ONLY)
