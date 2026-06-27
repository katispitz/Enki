# FINDINGS_034 — Tarot operator reconcile: TWO ERRORS I made, corrected (azoth=nodes; hexad=§16)

**Date:** 2026-06-15 (corrected same day)
**Trigger:** kati — "read [Tarot Engine v3], correct, then document," then two direct corrections: "there was an error in your original hexad application" + "azoth attaches to nodes though.... ugh."
**Status:** This finding initially documented a WRONG "fix." Rewritten to record the actual corrections. Root cause of both errors: **I let the MGW tarot PDF override canon.** Substrate-first discipline (CLAUDE.md: MythOS = archive/validator, NOT generator; canon is authoritative) was violated.

## Error 1 — Azoth: I moved it to EDGES; it attaches to NODES
**What I did wrong:** reading the MGW spec ("Azoth attaches to Kairos edges, not nodes"), I "corrected" the operator to emit azoth on the 7 Kairos edges. **Wrong direction.**
**Substrate truth (kati_direct 2026-06-15 + canon §30 functor):** azoth is a **per-PE-pt NODE attribute** — the §30 tarot functor emits "(planet + sign + **azoth** + face + platonic + archetype + hexad-role) at each PE-pt address." Azoth is one channel of the per-node emission. The MGW spec's "edges" claim **diverges from substrate**; canon wins.
**Fix:** reverted the edge-fix; `azoth_at_node(r) = AZOTH_AT_R[r]` (the canon PE-node azoth, = substrate_address azoth). Regenerated `tarot_correspondences.json` (78/78). Node azoth verified r0..r9: Solve/Coagula, Calcination, Dissolution, Separation, Conjunction, Fermentation, Distillation, Sublimation, Coagulation, Coagula Re-entry.
**Note:** the ORIGINAL code (`azoth_edge_entering`) was ALSO wrong — it built node→node edges along the Cronus adjacency. Neither edge form was right; azoth is simply the node value. Backup of pre-meddling state: `scripts/archive_run_tarot_operator_pre_azoth_edge_fix_20260615.py`.

## Error 2 — Hexad: I used the MGW ascending loop; the canonical hexad is §16's 1→4→2→8→5→7
**What I did wrong:** in FINDINGS_033 (and the azoth work) I called the MGW Kairos loop **9→1→2→4→5→7→8→9** (node order 1,2,4,5,7,8) "the supervision hexad," and placed the shocks at 2→4 and 5→7.
**Substrate truth (canon §16 SUPERVISION — HEXAD, LOCKED):** the supervision hexad is **Sun→Mars→Moon→Jupiter→Mercury→Saturn→Sun = `1→4→2→8→5→7→1`** (the real enneagram law-of-seven 1/7 circulation), with the cross-body shocks at:
- **4→2 (Mars→Moon)** through **X3/Venus** (mi→fa shock)
- **5→7 (Mercury→Saturn)** through **X6/Uranus** (si→do shock)
The triangle is Venus→Uranus→Neptune/Pluto→Venus (the shock/axis nodes 3,6,9). The MGW tarot Kairos loop (1,2,4,5,7,8 ascending) is a **MythOS divergence** from this; canon §16 is authoritative.
**Internal tell:** even the operator's own `kairos_position()` describes the shocks as "Mars→Moon" (X3) and "Mercury→Saturn" (X6) — i.e. the §16 4→2 and 5→7 directions — while labeling the loop in the contradictory MGW 1→2→4→5→7→8 order. So the operator was internally inconsistent on this point already.
**Fix (docs):** corrected the hexad/cronus labeling in FINDINGS_033/034 (see Error 3).

## Error 3 — Cronos/Kairos confusion (kati_direct 2026-06-15)
Underneath both errors above: I attached **sequential** structures to **Kairos**, but sequence is **Cronus**. Per canon §25 (LOCKED) the three line-types are three TRAVERSALS of the enneagram nodes:
- **CRONUS** — chronological, SEQUENTIAL (`0→5→10…` / numeric `0→9`). Saturn, "lord of chronological sequential time."
- **KAIROS = the HEXAD** — NON-sequential PE leaps `1→4→2→8→5→7`. Process transformation.
- **TRIANGLE** — the 3·6·9 shock/axis nodes (Venus/Uranus/Neptune-Pluto), 3-point intervention.

My mistakes: (a) I called the ascending node-listing `1→2→4→5→7→8` "Kairos" — that ascending order is CRONUS (sequential); true Kairos is the non-sequential `1→4→2→8→5→7`. (b) The azoth 7-stage alchemical progression (Calcination→…→Coagulation) is a SEQUENTIAL process → it rides CRONUS, not Kairos; I'd put it on "Kairos edges."

**Correct statement:** azoth attaches to the **NODES** (the PE points). Those nodes are traversed three ways (Cronus / Kairos / Triangle). Azoth is not on any traversal's edges — it is on the points, sequenced chronologically (Cronus). The node-SET of the hexad is {1,2,4,5,7,8} regardless of listing order; the KAIROS quality is the non-sequential leap-order through them.

## Kairos loop — CORRECTED (kati confirmed the order 2026-06-15)
kati ratified: **Kairos = `1→4→2→8→5→7→1` = Sun→Mars→Moon→Jupiter→Mercury→Saturn, cross-body shocks at 4→2 (X3/Venus) and 5→7 (X6/Uranus)** (= the §16 supervision hexad). The operator's `kairos_position()` had strung the loop in ascending CRONUS order (`9→1→2→4→5→7→8→9`), whose edges are NOT the Kairos edges — internally inconsistent with its own shock lines. Fixed: `KAIROS_LOOP_NODES = (1,4,2,8,5,7)`; `kairos_position()` now emits the §16 leap-order + planets; shock lines name the 4→2 / 5→7 cross-body edges; docstring L8 updated. Verified r0..r9. (My earlier "leave it alone" was wrong — once the order was confirmed, the ascending string was simply incorrect.)

## Lesson (procedural)
Both errors came from treating the MGW tarot PDF as authoritative over canon. The PDF is a MythOS rendering — a validator/source to cross-check, never a generator. **Canon §16/§30 first; PDF second.** Added to the pattern: when a source doc and canon disagree, canon wins and the divergence gets flagged, not silently adopted.

## v3.1 PDF full read (2026-06-15) — confirms the divergences, nothing new
Read all 12 pp of `Tarot Engine v3_1 (FINAL).pdf`. It CONFIRMS the cronos/kairos confusion is in the MGW spec itself:
- **§7B "Kairos carrier loop" = `9→1→2→4→5→7→8→9`** = the ascending/chronological order = CRONUS, mislabeled "Kairos." True Kairos = §16 `1→4→2→8→5→7`. Already corrected in our operator.
- **§7C "Azoth edge map"** attaches azoth to those loop EDGES (Sun/Moon/Mars/Mercury/Jupiter/Venus/Saturn). Substrate = azoth at NODES. Already corrected.
- **§7B shock "2→4"** — §16 directs it `4→2` (X3/Venus). Already corrected.
No NEW canon-divergence beyond these. Notes (not bugs): (a) v3.1 r-spine uses FUNCTION names (r1 Agency / r2 Polarity / r3 Synthesis / r4 Structure / r5 Adjustment / r6 Relatedness / r7 Presentation / r8 Equilibrium / r9 Integration) — third label scheme alongside the operator's exemplar-names and canon's substrate_address. (b) v3.1 separates `carrier_k` (lane: k0/k1/k2 shadow/octave) from `k_state` (orientation: upright/reversed/integrated) as distinct controls; the operator's k-handling is lighter (engine-completeness, not canon).

## Files
- `~/Nammu/scripts/run_tarot_operator.py` — azoth reverted to node; docstring + emit labels corrected. Regenerated `tarot_correspondences.json`.
- Backup: `~/Nammu/scripts/archive_run_tarot_operator_pre_azoth_edge_fix_20260615.py`
- Related: FINDINGS_033 (hexad order corrected there too), canon §16 (supervision hexad), §30 functor (azoth-at-node).
