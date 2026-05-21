# FINDINGS 006 — First canonical entry in §30: `planet-aspect-activate`

**Build**: conflation-test council (9 voices, --force-include Athena Mnemosyne) ratified the function-name graduated by Enki cross-R-tier residency probe.
**Status**: `planet-aspect-activate` is now the FIRST canonical entry in canon §30 FUNCTION-NAMES REGISTRY.

## What landed

- **§30 canonical promotion**: `planet-aspect-activate`. Function takes 2 planet longitudes, computes their angular separation + midpoint, checks aspect within V2.6 G4 ignition orb (6°), emits activation 0..1.
- **Residencies confirming** (2 independent primitive-classes):
  - R=1 cube-face Primordials (6 instances)
  - R=φ icosidodec-midpt Bridges (3 V2.5-locked instances)
- **4 candidates retired as conflated**:
  - `axis-bound` — residency-binding ("axis" R=1-flavor)
  - `axis-generate` — residency-binding
  - `axis-arm-emit` — pair-class-binding
  - `pair-aspect-activate` — secondary conflation ("pair" ambiguous primordial-pair-class vs planet-pair-input)
- **Erato gate**: 0/3 → 1/3 toward audit-pass unblock. 2 more canonical entries needed.
- **Cross-R-tier residency probe pattern**: templated for future canonical promotions.

## What the council substrate-confirmed (beyond §30 entry)

### Selection-drift cross-check operating mechanically

9-voice selection: 8 olympian / 1 titan, 7 shock_node / 2 non-shock, 7 inner / 2 outer shell-family. Drift detector fired warning at prep-time. Force-include `Athena Mnemosyne` operating as cross-check. Both pinned voices were structurally decisive — Athena's residency-binding rejection + Mnemosyne's pair-ambiguity tighten between them determined the final canonical name. **Without force-include cross-check, the Muse-heavy default selection would NOT have caught either substrate-failure mode.**

### Conflation-test FIRST (Erato rule 4b) worked end-to-end

The council did NOT proceed to residency-test on any candidate until conflation-test ran first:
1. Candidates 1-3 (axis-flavored) — conflated, retired
2. Candidate 4 (`pair-aspect-activate`) — secondary conflation flagged, tightened to `planet-aspect-activate`
3. Tightened candidate — passed conflation, residency pre-confirmed by Enki build, graduates

Erato process-learning rule operated as designed. Substrate-discipline guard intact.

### Nammu validator gap surfaced + fixed

Council commit hit `ValueError: face_type='shock' must be one of {Father,Mother}`. Root cause: `card_writer.VALID_FACE_TYPE = {Father,Mother}` was incomplete relative to canonical `TET_POLARITY` in `voice_instructions.py` which includes `bridge` and `shock` per canon §M.5 4-polarity tet structure. Patched to `{Father,Mother,shock,bridge}`. 308/308 Nammu tests green post-fix.

This is a substrate-discipline win: free-text would have silently accepted any string, but enum validation surfaced the canon/code inconsistency. NULL-honesty + enum-locked-values prevents future silent drift; the fix is small and substrate-honest.

### Bridge engine-class confirmed via canonical promotion

Per FINDINGS_005, bridges were proposed as engine-class. The conflation-test council ratified by accepting the cross-R-tier match as substrate-honest. Implicit acceptance: bridge stratum agent-shape = engine.

Agent-typology now has 2 engine-class strata confirmed:
- Primordial (R=1 cube-face)
- Bridge (R=φ icosidodec-midpt)

3 of 7 strata locked (Olympian as subagent confirmed in Nammu). 4 strata pending: Titan (Carrier), PE planet (Operator), shock-resident (Threshold-Marker), Muse (Activator).

## What's now unblocked

### Other §30 candidates can follow same pattern

The cross-R-tier residency probe template:
1. Build engine instances at candidate's primary primitive-class
2. Build engine instances at second R-tier primitive-class plausibly sharing function
3. Field-by-field shape comparison
4. Council conflation-test on naming (shell-agnostic preferred)
5. Promote to canonical

Candidates queued for this pattern:
- `transmit-force` (proposed R=1 cube-edge Titans). Probe: does same function operate at another R-tier? Maybe R=φ² ico-edges (Hesiod-descendants). But those have `descent-transmit` candidate — possible function-name MERGE or both subsumed.
- `deliberate` (proposed R=φ² ico-vertex Olympians). Probe: does deliberation as a function operate elsewhere? Maybe shock-residents at threshold (`threshold-mark`).
- `threshold-mark` (proposed R=1/3 shock nodes). Probe: do other primitives mark thresholds?

### Erato gate progress: 1/3

Audit-pass backfill of existing locks remains BLOCKED. Need 2 more canonical entries. Each requires its own cross-R-tier probe + council. Going forward, recommend building per-stratum engine prototypes (Titans/Operators/Threshold/Muses) AND probing each for cross-R-tier residency simultaneously.

### Schema enforcement now strict + accurate

After Nammu VALID_FACE_TYPE fix: card-write validation now rejects free-text/variant function_class spellings AND accepts canonical-tier polarity values. Schema-evolution drift-prevention operating.

## Open queue update

| OQ | Status | Notes |
|---|---|---|
| ~~OQ-AXIS-BOUND-NAME-CHECK~~ | **RESOLVED 2026-05-12** | All 4 candidates retired. `planet-aspect-activate` canonical. |
| ~~OQ-CROSS-R-TIER-RESIDENCY~~ | **RESOLVED 2026-05-12** | First cross-R-tier residency probe complete; pattern templated. |
| ~~OQ-FUNCTION-NAME-FRAMING~~ | **RESOLVED 2026-05-12** | Shell-agnostic naming wins (per Athena residency-binding rejection). Future function-names must avoid shell/residency-flavor prefixes. |
| OQ-ENGINE-GENERALIZATION | OPEN (carried) | Substrate-discipline favors named-per-residency engine files over parameterized lookup. Decision deferred. |
| OQ-CASCADE-PATTERN-AT-OTHER-RTIERS | OPEN (carried) | Does face→pair→trine→system cascade emerge at R=1/√3 inner-oct? Bridges at R=φ have cardinality 3 (too few for full cascade); inner-oct has cardinality 8 faces. |
| OQ-FACE-AS-POSITION-VS-FUNCTION | RESOLVED-IMPLICITLY | Shell-agnostic name (`planet-aspect-activate`) IS the function; position-anchors are metadata. Position ≠ function; both are substrate-locked. |
| OQ-PLUTO-NEPTUNE-PARTITION | SUBSTANTIATED (carried) | Canon §M.5b extension candidate pending council. |
| OQ-ANTIPODE-ASYMMETRY | OPEN (carried) | Erebus-Nyx unique zodiac-180°-coincidence. |
| OQ-PRIMORDIAL-PAIR-LEVEL-FUNCTION | DEFERRED | Pair-level proposed `polarity-define` still candidate; not graduated until cross-R-tier probe. |

## What to build next (substrate-emergent)

Per Kati directive (substrate build-out before functionality), highest-value moves:

1. **Cascade-pattern probe at R=1/√3 inner-oct** — 6V / 12E / 8F. Does face→pair→trine cascade emerge? Inner-oct face count (8) ≠ cube face count (6), so cascade structure may differ. Tests OQ-CASCADE-PATTERN-AT-OTHER-RTIERS.

2. **Carrier (Titan) engine prototype at R=1 cube-edge** — different primitive-type (edge vs face). 12 Titans. Tests whether engine-shape generalizes across primitive-type (edge vs face vs midpoint). Likely surfaces a NEW function-name candidate (`transmit-force` or similar). May or may not be same function as `planet-aspect-activate` — cross-R-tier probe will tell.

3. **Persephone bridge** — 4th bridge per V2.5, NOT midpoint-compound (seasonal Pluto-anchored). Different shape. Tests whether ALL bridges are engines or whether seasonal-bridges break the engine-class pattern.

4. **Pair-level cross-R-tier probe** — does `polarity-define` (pair-class at R=1 cube-face) operate at any other R-tier? If yes, second canonical entry possible. Less obvious where it operates — maybe R=1/√3 inner-oct face-pairs (4 antipodal pairs of 8 faces)?

Recommend (1) — directly tests substrate-cascade generality at a different shell, would likely surface candidates for canonical promotion in inner-oct primitive-classes.

Or (2) — switches primitive-type for the first time, validates engine-shape across the broadest substrate-axis.

Either advances the §30 canonical count toward Erato gate (≥3).
