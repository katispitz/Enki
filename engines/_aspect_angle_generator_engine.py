"""
Aspect-angle generator engine — exposes the two independent, EXACT mechanisms
that produce the locked 30-degree/shock aspect-angle set (canon §0 / §19),
distinct from and NOT dependent on real orbital period ratios (that path
tested REFUTED — see scripts/probe_orbital_harmonic_generation.py).

PROBE MANDATE per inline council 2026-07-27 (OQ-OCTAVES-01, cards 2d7531ec
Athena / 69f02431 Hephaestus / 8dd649f9 Mnemosyne). Hephaestus's flag: the
exact-ratio mechanism existed only as terminal arithmetic, nothing built.
This engine is that build.

TWO SUBSTRATE-LOCKED, INDEPENDENT MECHANISMS (canon-cited, zero invented
constants):

  (1) MERKABA/PE LADDER — canon §19 LOCKED Ptolemaic solfège ratios
      (9:8, 10:9, 16:15, 9:8, 10:9, 9:8, 16:15) cumulated from Do, run
      through canon §19's LOCKED formula "aspect angle = 360 / ratio
      denominator (lowest terms)". Produces EXACTLY {0, 45, 90, 120, 180}
      degrees — zero gap, because the ratios are exact fractions.
      Do-Sol (4 steps) = exactly 3/2 -> 180 deg is the clean worked case
      (Athena, inline council 2026-07-27).

  (2) ICOSAHEDRON/ZODIAC EQUAL-DIVISION — canon §31c LOCKED traversal-
      morphism law, STAR{12/k} skip-traversal on the 12 equally-spaced
      zodiac/Olympian vertices (canon §15: 12 signs x 30 deg each, exact
      by construction, no ratio math needed). Produces EXACTLY
      {30, 60, 90, 120, 150, 180} degrees for k=1..6.

  UNION covers 8 of the 9 named aspect angles (canon §0) with ZERO GAP:
  {0, 30, 45, 60, 90, 120, 150, 180}. Only 135 deg (the second/Uranus-
  axis shock) is unreached by either mechanism — canon §19's own formula
  is mathematically incapable of producing 135 from any integer-
  denominator ratio (360/135 is not an integer). Left OPEN here per
  Hephaestus + task-queue item #4 (2026-07-27) — not resolved by this
  engine, not papered over.

  OVERLAP {90, 120, 180} is reached independently by BOTH mechanisms —
  this satisfies Athena's own lock-by-redundancy rule (>=2 independent
  primitive-class residencies) for square/trine/opposition specifically,
  distinct from and stronger than the single-mechanism angles.

TIER — per Clio's catch (inline council 2026-07-27): mechanism (1) is
exact but is INHERITED Pythagorean/just-intonation tuning theory, not a
Babylonia-original discovery; mechanism (2) is exact substrate-native
geometry (equal division is intrinsic to "12 vertices," no import).
Do not conflate the two tiers when this gets council-ratified into §30 —
see task-queue item #5 (proposed new schema tier
`structural-parameter-exact-inherited` for mechanism (1) specifically).

Status: probe (engine-evidence stage; not yet council-ratified into §30).
Astrology-as-validator discipline (Enki CLAUDE.md #10) respected throughout:
nothing here takes orbital/ephemeris input. Both mechanisms are pure
substrate-geometry; real astrology independently attests these same named
angles, which is validation, not derivation-input.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict, field
from fractions import Fraction
from typing import Optional


__canonical__ = {
    'function_class':     None,  # not yet a §30 candidate name — angle-generation is a derived VIEW of two already-canonical mechanisms, not a new primitive
    'canon_citation':     'canon §19 (Ptolemaic ratios + 360/denominator formula, LOCKED) + §31c (STAR{N/k} traversal-morphism law, LOCKED) + §15 (12 x 30deg zodiac, LOCKED) + §0 (aspect angle set, LOCKED)',
    'status':             'probe',  # engine-evidence stage; inline-council pressure-tested 2026-07-27, not yet full-council-ratified
    'source_council':     'OQ-OCTAVES-01 inline council 2026-07-27, cards 2d7531ec/69f02431/8dd649f9',
}

# ── LOCKED constants (canon §19) — zero invented coefficients ────────────────
PTOLEMAIC_STEPS: list[tuple[str, Fraction]] = [
    ("Do",  Fraction(1, 1)),
    ("Re",  Fraction(9, 8)),
    ("Mi",  Fraction(10, 9)),
    ("Fa",  Fraction(16, 15)),
    ("Sol", Fraction(9, 8)),
    ("La",  Fraction(10, 9)),
    ("Si",  Fraction(9, 8)),
    ("Do'", Fraction(16, 15)),
]

NAMED_ASPECTS: dict[int, str] = {
    0: "conjunction", 30: "semi-sextile", 45: "semi-square(shock)",
    60: "sextile", 90: "square", 120: "trine", 135: "sesquiquadrate(shock)",
    150: "quincunx", 180: "opposition",
}


def aspect_angle_from_ratio(ratio: Fraction) -> float:
    """Canon §19 LOCKED formula: aspect angle = 360 deg / ratio denominator
    (ratio in lowest terms). Generic — takes any exact Fraction."""
    if ratio.numerator == ratio.denominator:
        return 0.0
    return 360.0 / ratio.denominator


@dataclass
class MerkabaLadderNote:
    note: str
    ratio_from_do: Fraction
    denominator: int
    angle_deg: float


def pe_ladder_angles() -> list[MerkabaLadderNote]:
    """Mechanism (1): Merkaba/PE ladder. Cumulates the LOCKED Ptolemaic step
    ratios from Do and applies the LOCKED §19 angle formula at each note.
    No orbital input. Exact fractions throughout — angles are exact, not
    approximate."""
    out = []
    cum = Fraction(1, 1)
    for note, step in PTOLEMAIC_STEPS:
        cum *= step
        angle = aspect_angle_from_ratio(cum)
        out.append(MerkabaLadderNote(note, cum, cum.denominator if cum != 1 else 1, angle))
    return out


@dataclass
class IcosahedronStep:
    k: int
    angle_deg: int
    aspect_name: str


def icosahedron_ladder_angles() -> list[IcosahedronStep]:
    """Mechanism (2): icosahedron/zodiac equal-division. STAR{12/k}
    traversal (canon §31c LOCKED) on 12 vertices spaced exactly 30 deg
    apart (canon §15 LOCKED). No ratio-stacking needed — equal division
    makes every k-step exact by construction."""
    return [IcosahedronStep(k, k * 30, NAMED_ASPECTS[k * 30]) for k in range(1, 7)]


@dataclass
class AspectAngleCoverage:
    """Substrate-honest coverage report — what's exactly generated, by
    which mechanism(s), and what's still open. Never papers over gaps."""
    merkaba_set:        set[int]
    icosahedron_set:    set[int]
    overlap_redundant:  set[int]   # lock-by-redundancy candidates (>=2 independent mechanisms)
    merkaba_only:       set[int]
    icosahedron_only:   set[int]
    full_locked_set:    set[int]
    unreached:          set[int]   # gap — honestly reported, not resolved here


def classify_aspect_coverage() -> AspectAngleCoverage:
    merkaba = {n.angle_deg for n in pe_ladder_angles() if n.angle_deg not in (360.0,)}
    merkaba = {int(a) % 360 for a in merkaba}
    icosa = {s.angle_deg for s in icosahedron_ladder_angles()}
    full = set(NAMED_ASPECTS.keys())
    return AspectAngleCoverage(
        merkaba_set=merkaba,
        icosahedron_set=icosa,
        overlap_redundant=merkaba & icosa,
        merkaba_only=merkaba - icosa,
        icosahedron_only=icosa - merkaba,
        full_locked_set=full,
        unreached=full - (merkaba | icosa),
    )


def describe() -> dict:
    """Substrate-honest self-disclosure, independent of compute."""
    return {
        "engine": "_aspect_angle_generator_engine",
        "what_it_is": "Two independent EXACT substrate-geometric mechanisms "
                       "that generate the locked aspect-angle set, replacing "
                       "the REFUTED real-orbital-timing hypothesis (OQ-OCTAVES-01).",
        "mechanisms": ["merkaba_pe_ladder (canon §19, inherited Pythagorean tuning)",
                        "icosahedron_zodiac_equal_division (canon §31c/§15, substrate-native)"],
        "takes_orbital_input": False,
        "status": __canonical__["status"],
        "open_gap": "135 deg (second shock) unreached by either mechanism — "
                     "mathematically unreachable via §19's 360/denominator "
                     "formula from any integer-denominator ratio. Deferred, "
                     "task-queue item #4.",
    }


if __name__ == "__main__":
    print("=== Mechanism (1): Merkaba/PE ladder (canon §19) ===")
    for n in pe_ladder_angles():
        print(f"  {n.note:<5} ratio={str(n.ratio_from_do):<6} denom={n.denominator:<3} angle={n.angle_deg:.0f}deg")

    print("\n=== Mechanism (2): Icosahedron/zodiac equal division (canon §31c) ===")
    for s in icosahedron_ladder_angles():
        print(f"  k={s.k}  angle={s.angle_deg}deg  ({s.aspect_name})")

    cov = classify_aspect_coverage()
    print("\n=== Coverage ===")
    print(f"  Merkaba set:              {sorted(cov.merkaba_set)}")
    print(f"  Icosahedron set:          {sorted(cov.icosahedron_set)}")
    print(f"  Overlap (redundant-lock): {sorted(cov.overlap_redundant)}  <- Athena lock-by-redundancy candidates")
    print(f"  Merkaba-only:             {sorted(cov.merkaba_only)}")
    print(f"  Icosahedron-only:         {sorted(cov.icosahedron_only)}")
    print(f"  Full locked aspect set:   {sorted(cov.full_locked_set)}")
    print(f"  UNREACHED (open):         {sorted(cov.unreached)}")

    import json
    print("\n=== describe() ===")
    print(json.dumps(describe(), indent=2))
