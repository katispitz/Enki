# FINDINGS_031 — NOVA patches pressure-test

**Date:** 2026-06-14
**Probe target:** all NOVA-sourced claims flagged "pressure-test required" in BABYLONIA_CORPUS_v1 (§A.8, §29 PATCH, NOVA-material table) + `~/Nammu/session/universal_operator.md`
**Probe shape:** canon-precedent cross-check (does current canon already adjudicate / supersede the claim?) + substrate-derivability check
**Outcome:** NONE of the NOVA patches survive as "integrate as new canon." Each is already-absorbed-in-refined-form, already-reconciled, reject-as-figure-placement, or canon-open-by-design. NOVA was a seed; substrate work has overtaken it.

## Method

NOVA = archive-only per CLAUDE.md (excluded from canon until pressure-tested + ratified). For each claim: (1) does current canon already address it, and in what form? (2) is it substrate-derivable, or external/figure-placement? Verdict ∈ {ABSORBED-REFINED, RECONCILED, REJECT, CANON-OPEN, KATI-ONLY}.

## Claim-by-claim

### 1. Universal Operator — "operator = self-reference; L1–L8 ladder; L7 self-reference is the FLOOR; L8=⊥" (§A.8 / session/universal_operator.md, Nova 2026-04-19)

**Verdict: ABSORBED-REFINED (core) + CANON-OPEN (floor) + REJECT (architectural claim).**

- **Core ABSORBED, in stronger form.** Canon §00 fractal frame already names the operator as "self-reference — the thing that points at itself," and §00/§27 ground it geometrically as the **Lawvere fixed-point** `f(x)=x` at observer × Merkaba-center (§27 L1407), with a full per-concentration fixed-point hierarchy (lvl0 cycle-closure / lvl1 2940-helix close / lvl2 natal-return / lvl3 Lawvere identity). This is more rigorous than NOVA's Spencer-Brown re-entry hand-wave — the substrate gives a *computable* fixed-point ladder, and it even substrate-derives astrology's return-chart tradition as the lvl-2 case. NOVA's contribution (name the operator self-reference) is real but already in canon, improved.
- **Floor-claim CANON-OPEN by design.** NOVA asserts "L7 self-reference IS the floor, L8=⊥ null." Canon deliberately keeps this OPEN: the fractal frame states "whether self-reference is the floor or emerges from something more primitive (distinction, fold-as-move, fixed-point) is OPEN." Do NOT lock L7-as-floor — canon already considered and declined.
- **T²-sampling claim ≠ canon's T².** NOVA: "two self-references → torus T²; sampling T² → tarot(78)/I-Ching(64)/astrology." Canon's locked torus is **T(49,60)** (matrix_pos × grid_pos, CRT, OQ-TOPOS-01) — a *different* torus (49-cycle × 60-grid), not NOVA's (cycle-phase × substrate-axis). The "same manifold, three samplings, those counts" rendering claim is exactly **OQ-OPERATOR-SAMPLING-MODES** (open per 2026-05-22 audit; build-scales count NOT substrate-derived). Keep candidate; do not conflate the two tori.
- **REJECT: "Architect ↔ Magistrate bridge is reflexive / Babylonia is built on L7."** Figure-placement + architectural claim with no substrate-derivation chain; not in §26. MythOS framing.

### 2. Nova intrinsic cell (0,0) = Venus×Venus = epoch/void cell (§29 PATCH)

**Verdict: VINDICATED — NOT a stale label. [CORRECTED 2026-06-14 after re-check of the v8 49-matrix doc at kati request.]**

My first pass called this "a stale v8 label, reconciled to Pluto×Pluto." That was WRONG. Re-reading the actual source — `Babylonia 49Matrix Derivation v8.docx` (the "49-pointed-star" doc) — and the engine that implements it (`matrix_engine.py`):

- The v8 doc's **culminating derived conclusion** (§XXIII "OQ-49-03 Extended: Venus Is the Structure of the Matrix, Not Its Content") is that **Venus IS the frame**, derived three ways: (1) Venus begins every row AND every column (col 0 = reset column); (2) Venus uniquely appears as both flow-position 0 AND shock-position 3/X3, governing the fault line from outside; (3) **Venus×Venus is null, not pure — "the origin meeting itself… the system at rest before any process begins."** Diagonal asymmetry = 6 shadow cells + 1 VOID cell (Venus×Venus). The epoch (grid 0 = Venus/Taurus, Merkaba spine) is derived three independent ways (geometric + karana + lunar zero converge).
- `matrix_engine.py` IMPLEMENTS this: index 0 = `('Venus','Do',…,'frame/epoch/void')`, spatial-epoch ordering, citing 49Matrix_Derivation_v8.docx §II/§XXIII.

So the NOVA claim "(0,0) = Venus×Venus = epoch/void cell = system at rest" is **exactly the v8 doc's derived position and a live engine convention** — vindicated, not stale.

**The real structure is a §0b dual-ORDERING (not a label trick):**
| Ordering | index 0 | engine | purpose |
|---|---|---|---|
| spatial-epoch | **Venus** (frame/epoch/void) | `matrix_engine.py` + v8 doc | matrix navigation, epoch, void cell |
| PE-sequence | **Pluto** (Do carrier) | `cell_signature_engine.py` | harmonic/frequency signature |

Reconciled via Do-boundary co-residency (Venus/Pluto/Neptune all converge at Do/grid 0). Both correct, function-selected — §0b dispatch.

**Flag:** canon §28b L1825 frames this as "engine retains Pluto as canonical row-0; Venus×Venus = alternate label." That UNDERSTATES the v8 doc, whose primary derived finding is *Venus is the frame*. The honest statement is the co-equal dual-ordering above, not "Pluto canonical / Venus label." Recommend upgrading the §28b prose to the §0b dual-ordering framing. (`test_pluto_row_0_canon_lock` locks Pluto@0 for cell_signature_engine; `matrix_engine.py` runs Venus@0 — operationally consistent, but the canon wording leans against the source.)

### 3. Ananke = Merkaba center (Observer/Axis stratum) (§29 PATCH, Nova MythLayer_Map)

**Verdict: REJECT-as-placement / SUSPEND (function-first).** The Merkaba center (R=0 origin) is canonically the **Lawvere fixed-point / frame-anchor**, explicitly "frame anchor, NOT a residency shell except for the X3+X6-cancel position" (§3). Assigning a named figure (Ananke) to a non-residency frame-anchor is MythOS narrative without substrate residency. Also barred by the function-first suspension of all myth-layer placement + §0d (placement-implies-voice requires a real residency). The *center's function* (identity fixed-point / necessity-of-self-reference) is canonical; the *figure-name* is not derived.

### 4. OQ-SCALE-01 "L = inter-planetary distance" (kati intuition)

**Verdict: KATI-ONLY / not substrate-derivable.** The substrate is **scale-free** — all radii are ratios (Q(√3), Q(√5)); nothing in the geometry fixes a physical length L in meters. So this cannot be pressure-tested *from* the substrate; it requires an external physical-anchor choice. Stays OPEN as kati-intuition, correctly marked "intuition not derivation." Not blocking (geometry is dimensionless). Honest status: needs a kati calibration decision, not a derivation.

### 5. Myth-traversal test cases (Cronus/Titanomachy/Prometheus) (§29 PATCH)

**Verdict: REJECT-as-narrative / SUSPEND.** Agent-synthesized narrative interpretations, not substrate-derived; blocked by function-first myth-layer suspension. No substrate content to pressure-test.

### 6. Council 12-seat light/shadow structure (§29 / NOVA table)

**Verdict: already RETRACTED 2026-05-11** (MythOS import; archive only). No action.

## Summary table

| NOVA patch | Verdict | Action |
|---|---|---|
| Universal Operator — self-reference operator | ABSORBED-REFINED (canon §00/§27 Lawvere) | mark §A.8 superseded-by-canon |
| — self-reference as FLOOR / L8=⊥ | CANON-OPEN (floor-primitive open) | do not lock |
| — T²-sampling → tarot/IChing/astrology counts | CANON-OPEN (OQ-OPERATOR-SAMPLING-MODES; ≠ T(49,60)) | keep candidate |
| — Architect↔Magistrate reflexive bridge | REJECT (figure-placement, no derivation) | retract |
| (0,0) = Venus×Venus epoch/void cell | **VINDICATED** [corrected] — v8 doc: "Venus IS the frame"; live in matrix_engine.py; §0b dual-ordering w/ Pluto@0 PE-sequence | upgrade §28b prose to dual-ordering; do NOT call it stale |
| Ananke = Merkaba center | REJECT/SUSPEND (frame-anchor ≠ residency; function-first) | retract-as-placement |
| OQ-SCALE-01 L = interplanetary | KATI-ONLY (substrate is scale-free) | stays kati-intuition |
| Myth-traversal cases | REJECT/SUSPEND (narrative) | hold |
| Council 12-seat light/shadow | already RETRACTED 2026-05-11 | none |

## Disposition
- **No NOVA patch integrates as new canon.** The sound part (self-reference operator) is already canonical in refined form; the rest is reconciled, open-by-design, or figure-placement that fails function-first.
- Recommended canon/corpus cleanup (requires kati go — supersede+archive, never delete): mark §A.8 "superseded-by-canon §00/§27; residual claims rejected/open"; mark the §29 (0,0) and Ananke PATCH lines superseded/rejected with this finding cited; leave OQ-SCALE-01 as kati-intuition with "not substrate-derivable (scale-free)" note.
