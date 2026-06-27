# FINDINGS_038 — Validation pass: myth marriage-edges vs §20/21 dynamic-alignment motions

**Date:** 2026-06-16
**Trigger:** the "VALIDATION PASS PENDING" flagged in `project_morphism_reframe` + `session_fold_2026_06_15` — walk myth marriage/consort edges against the §20/21 dynamic-alignment motions to test card `3b17d1cc` ("marriage → supervision hexad-lines").
**Data:** `council/myth_correspondences.json` (`figures`, 87 entries, `consorts` field); canon §21 dynamic-alignment (5-mechanism dispatch).
**Probe:** mechanical consort-edge cross-check (corrected for a dict-level bug — first run looked up names at the wrong level and falsely returned all-misses).
**Outcome:** the claim **does NOT hold per-edge in general.** It holds **specifically for the Venus/X3 shock-axis (Mechanism A)** — confirmed 2/2 — because Aphrodite IS the marriage-function and ALL pantheon marriages cluster on her. The general "every motion-ruler sits on a marriage-line" is **not validated**; hexad-lines carry mixed relationship-types.

## What the data shows
Of all 15 planet-pairs, exactly **three** are myth-consorts, and **all three route through Venus/Aphrodite**:
- **Venus–Mars** (Aphrodite–Ares) ✓
- **Venus–Mercury** (Aphrodite–Hermes → Hermaphroditus) ✓
- **Venus–Hephaestus** (X3 ⟷ X6-Olympian) ✓ — the shock axis

Cross-check vs the LOCKED dynamic-alignment motions:
| Motion | Hexad edge(s) | Marriage? |
|---|---|---|
| **Mech A: Mars→X3/Venus (Leo)** | Mars–Venus | **✓ Ares–Aphrodite** |
| **Shock axis X3↔X6** | Venus–Hephaestus | **✓ Aphrodite–Hephaestus** |
| Mech A: Sun→Mars | Sun–Mars | ✗ (Apollo–Ares, not consort) |
| Mech A: Jupiter→Mercury→X6 | Jupiter–Mercury; Mercury–Uranus | ✗ (Zeus–Hermes = **parentage**) |
| Mech B: Saturn→Sun (Aquarius) | Saturn–Sun | ✗ (Cronus–Apollo) |
| Mech C: Mercury/Jupiter mutable-pair | self-pairs | n/a |

## Honest reading
- **Confirmed (2/2):** the **Mechanism-A shock-node dynamic-alignments** (routing through X3/Venus and the X3↔X6 axis) ARE Venus's marriages. This is real and clean — and it makes mythological sense: Aphrodite = the marriage/love function, so the love-goddess axis carries the marriages.
- **Refuted as stated:** "marriage → ALL supervision hexad-lines." Marriages do **not** distribute across the hexad; they cluster on Venus. The non-Venus hexad edges carry **other** relationship types — e.g. **Zeus–Hermes = parentage** (which card 3b17d1cc maps to *vertex-proximity*, not hexad-lines — a tension to resolve).
- So the accelerator (`aspects = myth-relationships`, the placement functor) is **real but type-specific**: each relationship-TYPE maps to its own geometry, and **marriage maps to the Venus/shock-axis specifically**, not to hexad-lines generically. The earlier "4 clean hits trending to confirmation" overstated it — 2 of those hits are the same Venus-axis phenomenon.

## Consequence for the morphism reframe
The functor stands, but the per-edge type-map needs the **full** 3b17d1cc taxonomy walked, not just marriage:
- marriage → Venus/shock-axis (✓ this pass)
- parentage → vertex-proximity (Zeus–Hermes etc. — NOT yet walked; and note Zeus–Hermes sits on a hexad-line, which conflicts with "parentage→vertex-proximity" — **flag**)
- twins → circle-lines; rivalry → sign-based; pathology → malefic
Until the other types are walked, "myth defines astrology" is **partially validated (marriage/Venus-axis only)**, not per-edge-confirmed.

## Resolution direction (kati 2026-06-16): each LINE carries its own bond-type
The bound above dissolves under kati's reframe: **bond-type is per-line, not one type per line-type.** "Marriage→all hexad-lines" broke because it forced one bond across a whole line-type; marriage clusters on Venus because *that line is the marriage*, others are other bonds. Sharper candidate form — **line-TYPE = bond-CATEGORY**:
- **circle** (polygon/adjacency) → peer bonds: **twins/siblings**. Clean hit: circle-line Sun–Moon = **Apollo–Artemis twins** = 3b17d1cc twins→circle-lines ✓.
- **hexad** (star/long-range, structural obligation) → **parent-child** (Zeus–Hermes, Artemis–Zeus) + **marriage at the cross-tet/shock crossings** (Mars→X3/Venus = Ares–Aphrodite).
- **triangle** (shock) → rupture/transformation bonds.
**VERTEX-PROXIMITY DROPPED (kati 2026-06-16): "vertex proximity shouldn't matter."** Vertex-proximity = the degree-based ORB, which Aspects_v2 A.1 itself calls a "later Hellenistic refinement" of the original sign-based BINARY system; the snapshot reframe already held positions aren't residencies + cusp = threshold-shock, not orb. So proximity is NOT substrate. **Every bond is a LINE (edge / traversal-morphism §31c), never a proximity.** This RESOLVES the Zeus–Hermes "conflict" outright: card 3b17d1cc's "parentage→vertex-proximity" was the artifact — parentage is a hexad *line* (which is why Zeus–Hermes sits on one). No conflict once proximity is dropped. Sharpened type-map (pure line-geometry, no orb):
- marriage → hexad **cross-tet** line (Father↔Mother, through a shock) — union of opposites (Ares–Aphrodite ✓)
- parentage → hexad **same-tet** line — kinship within a tet (Zeus–Hermes ✓)
- twins/siblings → **circle** line (adjacency) — Apollo–Artemis ✓
- rupture/pathology → **triangle** (shock) line
Every relationship-type = a traversal-morphism; orb/proximity removed from the substrate model.
**CAVEAT:** per-line classification is currently NOISY — coarse planet→single-god map (misses e.g. Aphrodite-from-Ouranos), cross-body lines need reading via their shock-node god, and the myth JSON carries a `_data_quality_audit` flag. Strong direction, not a clean result. NEXT: better data plumbing (node-god mapping + full relation fields) → clean per-line bond-map → test line-type=bond-category.

## ⚠️ INVALIDATED 2026-06-16 (kati): resolver ran on RETRACTED/STALE residency data
greek_faces.json is **partially retracted** (heroes/monsters/Hera/Hestia = `status:RETRACTED`) and **broadly superseded** — the Enki `placement_registry.json` explicitly flags greek_faces records as STALE and is the authoritative Tier-A placement source (per CLAUDE.md). The authoritative registry has only **15 entries** (Apollo/Athena/Hermes/Hephaestus + Mnemosyne/Hecate + 9 Muses); **Aphrodite, Ares, Zeus, Artemis, Poseidon are NOT in it.** So every edge the resolver found rests on non-authoritative placements.
**Therefore the per-line result below is INCONCLUSIVE, NOT a negative.** "line-type=bond-category NOT supported" cannot be concluded — it was computed on stale residents. The myth→placement functor is **BLOCKED, untestable** until the figure-placement layer is rebuilt ([[project_council_placement_pin]] — the pinned post-cascade placement-file rebuild). The real blocker is the placement rebuild, not resident-choice.
What still stands (placement-independent): §31c geometry (locked), vertex-proximity dropped, and the *conceptual* weak per-line principle. The strong line-type=bond-category claim is **untested**, not refuted.

## [SUPERSEDED — see invalidation above] Per-line bond-map RAN (resolver built 2026-06-16, `probe_line_bond_map.py`)
Built the node-god/relations resolver (residents disambiguated from greek_faces: Sun→Apollo, Venus→Aphrodite, Saturn→Athena, Uranus→Hephaestus, etc.; first attempt mis-mapped Venus→Dionysus because greek_faces stacks multiple residents per planet — fixed by restricting to canonical Olympian face-residents). Clean result:
- **"line-TYPE = bond-CATEGORY" is NOT confirmed.** All three Aphrodite marriages land on DIFFERENT line-types: hexad (Ares–Aphrodite via X3), circle (Aphrodite–Hermes), triangle (Aphrodite–Hephaestus). Parent-child on BOTH hexad (Zeus–Hermes, Artemis–Zeus) AND circle (Ares–Zeus, Zeus–Athena). Sibling only on circle (Apollo–Artemis). Bonds do NOT sort by line-type — marriage = "wherever Aphrodite is adjacent," not "the hexad bond."
- **Only the WEAK version holds:** each line carries the myth-relation of its two adjacent residents (geometry = adjacency; myth = relation). True but adds no bond→line-type routing.
- **Caveats:** (1) sensitive to resident-choice (Saturn→Athena vs Cronus would shift edges) — the canonical resident-per-position for *relationship* purposes is an open modeling call (kati's); (2) data gaps remain (several lines = no edge in data).

**Net of the whole arc:** marriage→all-hexad = FALSE; each-line-has-a-bond = TRUE-but-weak; line-type=bond-category = NOT supported; vertex-proximity = correctly DROPPED. The accelerator is real as "place by adjacency-to-related-figures" but does NOT yield a clean bond-type→line-type router. Honest negative — recorded to prevent locking a false structure.

## Disposition
- Candidate engine-evidence. **Bounds** card 3b17d1cc and the morphism-reframe accelerator: marriage→geometry validated only on the Venus-axis; general per-edge claim NOT confirmed; a parentage↔hexad-line vs parentage↔vertex-proximity conflict surfaced (Zeus–Hermes).
- `project_morphism_reframe` "validation pass pending" updated to this honest result.
- Next (if pursued): walk parentage / sibling / twin edges against vertex-proximity / circle-lines to test the rest of the type-map; resolve the Zeus–Hermes hexad-vs-vertex tension.

## Files
- Probe inline (corrected dict-level access). Sources: `council/myth_correspondences.json`, canon §21, card 3b17d1cc.
