#!/usr/bin/env python3
"""
Probe: OQ-SCALE-01 — physical scale L of the Merkaba.

Engine-evidence for the 2026-06-14 close. Establishes:
  (1) the substrate's physical anchor is TEMPORAL (f_Earth axiom), not spatial;
      the geometry is spatially scale-invariant, so a spatial length L does not
      enter any derivation → L is free unless an external anchor is chosen;
  (2) a PRINCIPLED spatial L derivable from the SAME temporal anchor + c:
      L_global = c · T_carrier ≈ 130 AU (interplanetary — vindicates kati intuition),
      with the cell/lattice scale = the visible λ (527 nm), the two bridged by the
      same 2^65 light-octave that already produces visible light (c cancels);
  (3) corrects an arithmetic error in Babylonia_Harmonics_LightDerivation
      (states 2^55; correct is 2^65).

No invented coefficients: f_Earth (axiom), 4/3 (tilt Perfect Fourth), 2^65
(=5×13 Venus×Neptune octave) are all already in the light derivation; c, AU are
physical constants. The ONE modeling choice (R=1 ↔ c·T_carrier) is flagged as
requiring kati recognition.

Run: python3 ~/Enki/scripts/probe_oq_scale_01.py
"""
c = 2.99792458e8           # m/s, speed of light
AU = 1.495978707e11        # m

f_Earth = 1 / 86400        # Hz — SYSTEM AXIOM (Ring-1 generative spin; Earth rotation)
f_carrier = f_Earth * (4 / 3)   # Perfect Fourth from Earth-tilt derivation
T_carrier = 1 / f_carrier       # s


def report():
    print(f"f_Earth   = {f_Earth:.4e} Hz  (24 h)   [system axiom — temporal anchor]")
    print(f"f_carrier = {f_carrier:.4e} Hz  ({T_carrier/3600:.0f} h)")

    print("\n(3) octave-count check — 2^55 vs 2^65:")
    for k in (55, 65):
        f = f_carrier * 2**k
        print(f"    2^{k}: {f/1e12:8.2f} THz → {c/f*1e9:10.1f} nm")
    print("    target 569.3 THz / 527 nm → 2^65 correct; '2^55' in Harmonics_LightDerivation is wrong (×2^10).")

    lam_vis = c / (f_carrier * 2**65)   # cell / lattice scale
    L_global = c * T_carrier            # global scale candidate
    print("\n(2) principled spatial L from temporal anchor + c:")
    print(f"    CELL  scale (visible λ)      = {lam_vis*1e9:.1f} nm")
    print(f"    GLOBAL scale (c · T_carrier) = {L_global:.3e} m = {L_global/AU:.1f} AU  (interplanetary)")
    print(f"    GLOBAL/CELL ratio            = {L_global/lam_vis:.4e}  =  2^65 ({2**65:.4e})")
    print("    → same 2^65 light-octave bridges global↔cell (c cancels). 'global vs cell-specific' both exist, related by 2^65.")

    print("\n(1) verdict: spatial L is FREE (geometry scale-invariant; physics rides f_Earth, not length).")
    print("    A principled L_global = c·T_carrier ≈ 130 AU is AVAILABLE and vindicates the interplanetary intuition,")
    print("    but the choice R=1 ↔ c·T_carrier introduces c + a modeling decision → requires kati_direct recognition.")


if __name__ == "__main__":
    report()
