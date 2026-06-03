# FINDINGS_027 — Octave-Shift Mechanism Residency Probe (SDEC)

**Date:** 2026-05-22
**Probe target:** card `e3f55016` (§00a concentration-octave partial-lock)
**Probe shape:** residency-count enumeration per Athena lock-by-redundancy
**Outcome:** PASS — 3 qualified residencies (≥2 threshold met)

## Probe design

Per canon §00a candidate-extension and kati_direct recognition 2026-05-22, the octave-shift mechanism (same structure, different observer-anchor frequency) extends the PE octave operator from planetary-position-axis to observer-axis. Athena lock-by-redundancy requires ≥2 independent substrate-residencies for canonical promotion.

Enumerate observer-anchor pairs admitting octave-shift; validate each meets the substrate-pattern (same coprime structure, different anchor frequency, observer-frame change).

## Qualifying residencies

### ✓ Residency 1 — helix-mode-duality (PRIMARY)

- **Pair:** universal mode (Venus drives `grid_pos`, no surface observer) ↔ personal mode (ASC drives `grid_pos`, specific observer at lat/lon/t)
- **Same structure:** identical coprime 49×60 cycle structure, ring-tiers, matrix-positions, helix-LCM 2940
- **Different anchor:** carrier identity changes (Venus barycenter ↔ ASC at specific moment)
- **Observer levels:** lvl 1 ↔ lvl 2 per canon §00 concentration recursion
- **Engine evidence:** `~/Nammu/engines/helix_trajectory.py` G5 LOCKED 2026-05-11
- **Status:** kati_direct precedent (originating recognition 2026-05-22 "we already kind of addressed this with personal merkebe")

### ✓ Residency 2 — natal-vs-return

- **Pair:** natal chart at t0 ↔ solar return chart at t0 + N·solar_year (or lunar/saturn/etc. returns at their periods)
- **Same structure:** identical 12-house/12-sign chart structure, same observer location, same physical bodies
- **Different anchor:** time-anchor shifts. Sun returns to natal position; the chart phase-locks at the return-moment instead of birth-moment.
- **Observer levels:** lvl 2 ↔ lvl 2 (same observer, different time-anchor; intra-level octave-shift via temporal-period sweep)
- **Engine evidence:** `natal.py` supports arbitrary date; solar return = same engine called at return-moment with same lat/lon
- **Status:** canon-derivable per §00a per-concentration fixed-point hierarchy — lvl-2 entries explicitly enumerate planetary returns (solar 1yr, lunar 27d, Venus 8yr, Jupiter 12yr, Saturn 29.5yr) as fixed-points

This is the more interesting residency: it surfaces that lvl-2 has its OWN intra-level octave structure indexed by per-planet return period. Each return = one octave of that planet's anchor.

### ✓ Residency 3 — tropical-vs-sidereal (CANDIDATE-COMPATIBLE)

- **Pair:** tropical zodiac (vernal-equinox-anchored) ↔ sidereal zodiac (star-position-anchored)
- **Same structure:** identical 12-fold sign structure projected on Merkaba
- **Different anchor:** frame reference shifts (Earth-Sun seasonal ↔ deep-sky fixed-star reference); ayanamsa offset = the shift parameter
- **Observer levels:** lvl 1 ↔ lvl 1 (same Earth-observer, different anchor-frame)
- **Status:** canon-compatible, not explicitly canonized as octave-shift instance
- **Engine evidence:** standard astronomy; not in Nammu engines currently

Counts as third residency because it satisfies same-structure-different-anchor pattern within a single observer-level — another *intra-level* octave-shift, this time at lvl 1.

## Rejected candidates

### ✗ whole-sign-vs-equal-house

Equal-house and Placidus rejected per OQ-H03 RESOLVED (whole-sign canonical). Substrate-rejected, cannot count as residency.

### ? ASC-vs-MC-vs-IC-vs-DC

Four cardinal angles offer different "frame views" of one chart but unclear whether this constitutes octave-shift or merely rotation of view. Deferred — would need separate substrate analysis.

## Probe verdict

3 qualified residencies confirmed (≥2 threshold met):
1. helix-mode-duality (lvl 1 ↔ lvl 2, inter-level)
2. natal-vs-return (lvl 2 intra-level via time-anchor)
3. tropical-vs-sidereal (lvl 1 intra-level via frame-anchor)

The mechanism operates **both inter-level (between concentration levels) AND intra-level (within one concentration level via different anchor parameters)**. This is structurally richer than originally framed in card `e3f55016`.

## Recommendation

Promote card `e3f55016` from `derived` + `sdec-pending` → `locked` per canon §0c (recognition + engine-evidence both satisfied).

Update §00a to reflect the inter/intra-level distinction surfaced by this probe:
- inter-level shift: lvl 1 ↔ lvl 2 (helix-mode-duality)
- intra-level shift: same lvl, different anchor parameter (natal-vs-return at lvl 2; tropical-vs-sidereal at lvl 1)

Status: **PASS** → promote per §0c.
