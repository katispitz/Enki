#!/usr/bin/env python3
"""
probe_orbital_harmonic_generation.py — OQ-OCTAVES-01 (renamed from working
label "OQ-H01" per Mnemosyne, inline council 2026-07-27, card 8dd649f9 — see
ID COLLISION note below). Deferred question from Babylonia_Octaves.docx,
"PENDING — next major work layer" in source; taken up 2026-07-26 per kati
explicit request, sibling to OQ-H02..H06 same session 2026-07-25 (those
labels are session shorthand only, never canon-written, no collision risk).

ID COLLISION (why renamed): canon §22 already has a RESOLVED OQ-H01..OQ-H07
set (Ascendant/houses derivation, LOCKED). This probe's question is a
DIFFERENT question from a different source doc (Babylonia_Octaves.docx, not
Houses docs) that originally reused the same short-form label same session
2026-07-25. Renamed to OQ-OCTAVES-01 before any card-write under the
colliding ID.

QUESTION: do REAL sidereal orbital periods, mapped by ratio, GENERATE (a) the
already-LOCKED Ptolemaic PE/solfège interval sequence (canon §19, lines
~1013-1016) and/or (b) the already-LOCKED 30°-multiple aspect-angle system
(canon §0 / §19 "aspect angle = 360°/ratio denominator")? Or do real orbital
ratios only sparsely CO-SIGN isolated points in those systems, the way Venus
(OQ-RINGS-06-PRECISION) and Neptune:Pluto (canon §23b) already do?

Discipline: same generation-vs-coincidence test as probe_octave_comma_magnitude.py.
A numerical lock needs ONE rigorous chain; substrate-forced counts != orbital
(observation-calibrated) counts (OQ-RINGS-06-PRECISION).
"""
from math import log2

CENTS = lambda ratio: 1200.0 * log2(ratio)

# ── Real sidereal orbital periods (years), NASA/JPL values ───────────────────
PERIOD_YR = {
    "Mercury": 87.969 / 365.25,
    "Venus":   224.701 / 365.25,
    "Earth":   1.000000,
    "Moon_synodic": 29.5306 / 365.25,   # canon Ring 2 basis (~30t)
    "Mars":    686.980 / 365.25,
    "Jupiter": 4332.59 / 365.25,
    "Saturn":  10759.22 / 365.25,
    "Uranus":  30688.5 / 365.25,
    "Neptune": 60182.0 / 365.25,
    "Pluto":   90560.0 / 365.25,
}

print("=" * 78)
print("OQ-OCTAVES-01 — does real orbital timing GENERATE the locked PE/aspect structure?")
print("=" * 78)

# ── TEST A — PE flow-order note assignment vs LOCKED Ptolemaic intervals ─────
# Flow order (canon §23b ring table, pt0..pt9; matches §19 solfège LOCK):
# Do(Pluto,pt0) Re(Sun/Earth,pt1) Mi(Moon,pt2) [X3 shock=Venus] Fa(Mars,pt4)
# Sol(Mercury,pt5) [X6 shock=Uranus] La(Saturn,pt7) Si(Jupiter,pt8) Do-ret(Neptune,pt9)
pe_notes = [
    ("Do",  "Pluto",   PERIOD_YR["Pluto"]),
    ("Re",  "Earth",   PERIOD_YR["Earth"]),
    ("Mi",  "Moon",    PERIOD_YR["Moon_synodic"]),
    ("Fa",  "Mars",    PERIOD_YR["Mars"]),
    ("Sol", "Mercury", PERIOD_YR["Mercury"]),
    ("La",  "Saturn",  PERIOD_YR["Saturn"]),
    ("Si",  "Jupiter", PERIOD_YR["Jupiter"]),
    ("Do'", "Neptune", PERIOD_YR["Neptune"]),
]
locked_ptolemaic = [("Do-Re", 9/8), ("Re-Mi", 10/9), ("Mi-Fa", 16/15),
                     ("Fa-Sol", 9/8), ("Sol-La", 10/9), ("La-Si", 9/8), ("Si-Do'", 16/15)]

print("\n(A) PE-note orbital-period ratio vs LOCKED Ptolemaic interval (canon §19):\n")
print(f"{'step':<8}{'planets':<18}{'period ratio':>14}{'cents':>10}{'mod-oct cents':>16}{'Ptolemaic (locked)':>20}{'gap (mod-oct)':>16}")
degrees_cents = [0, 203.9, 386.3, 498.0, 702.0, 884.4, 1088.3, 1200.0]
a_gaps = []
for i in range(7):
    n1, p1, t1 = pe_notes[i]
    n2, p2, t2 = pe_notes[i + 1]
    ratio = max(t1, t2) / min(t1, t2)
    c = CENTS(ratio)
    c_mod = c % 1200
    target_c = CENTS(locked_ptolemaic[i][1])
    gap = min(abs(c_mod - degrees_cents[i]), abs(c_mod - degrees_cents[i+1]))
    a_gaps.append(gap)
    print(f"{locked_ptolemaic[i][0]:<8}{p1+'-'+p2:<18}{ratio:>14.3f}{c:>10.0f}{c_mod:>16.1f}{target_c:>20.1f}{gap:>16.1f}")
print(f"\nVERDICT A: mean mod-octave gap = {sum(a_gaps)/len(a_gaps):.1f} cents (vs Ptolemaic step sizes")
print("of 111.7-203.9 cents) — gaps are the SAME ORDER OF MAGNITUDE as the steps")
print("themselves. No systematic alignment. REFUTED: real orbital periods do NOT")
print("generate the locked PE/solfège note sequence (periods are non-monotonic —")
print("Moon < Mercury < Earth < Mars < Jupiter < Saturn < Neptune < Pluto in reality,")
print("but the LOCKED flow order is Pluto,Earth,Moon,Mars,Mercury,Saturn,Jupiter,Neptune —")
print("a geometric/grid ordering, not a period-magnitude ordering. The mismatch is")
print("structural, not a measurement gap.")

# ── TEST B — heliocentric-adjacent pairs vs named just-intonation consonances ─
print("\n" + "-" * 78)
print("(B) Heliocentric-adjacent period ratio vs named just-intonation consonances:\n")
chain = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
named = {0: "unison", 203.9: "M2 (9:8)", 315.6: "m3 (6:5)", 386.3: "M3 (5:4)",
         498.0: "P4 (4:3)", 600.0: "tritone", 702.0: "P5 (3:2)", 884.4: "M6 (5:3)",
         1017.6: "m7 (16:9)", 1088.3: "M7 (15:8)", 1200.0: "octave (2:1)"}
b_hits = []
for i in range(len(chain) - 1):
    p1, p2 = chain[i], chain[i + 1]
    t1, t2 = PERIOD_YR[p1], PERIOD_YR[p2]
    ratio = t2 / t1
    c = CENTS(ratio)
    nearest_c = min(named, key=lambda x: abs(x - (c % 1200 if c > 1200 else c)))
    c_ref = c if c <= 1200 else c % 1200
    gap = abs(c_ref - nearest_c)
    pct = abs(ratio / (2 ** (nearest_c / 1200) * (1 if c <= 1200 else (2 ** (c // 1200)))) - 1) * 100 if False else gap / max(nearest_c,1) * 100
    tight = "  <-- TIGHT" if gap < 10 else ("  <-- moderate" if gap < 20 else "")
    b_hits.append((p1, p2, ratio, c, nearest_c, gap, tight))
    print(f"{p1:<9}:{p2:<9} ratio={ratio:>8.4f}  cents={c:>8.1f}  nearest={named[nearest_c]:<14} gap={gap:>6.1f}c{tight}")

print("\nStandout precise hits (<10 cents / <0.5% ratio gap):")
for p1, p2, ratio, c, nearest_c, gap, tight in b_hits:
    if gap < 10:
        exact = 2 ** (nearest_c / 1200)
        pct = abs(ratio - exact) / exact * 100
        print(f"  {p1}:{p2} = {ratio:.5f} vs {named[nearest_c]} = {exact:.5f}  ({pct:.2f}% gap)")

# ── TEST C — synodic conjunction-drift angle vs 30°-multiple aspect system ───
print("\n" + "-" * 78)
print("(C) Synodic conjunction-longitude-drift angle vs LOCKED aspect angles (canon §0):")
print("    Delta-lambda = 360 deg x (S / T_outer), S = synodic period. Real celestial-")
print("    mechanics formula (successive-conjunction longitude advance), NOT invented.\n")
aspect_angles = {0: "conjunction", 30: "semi-sextile", 45: "semi-square(shock)",
                  60: "sextile", 90: "square", 120: "trine", 135: "sesquiquadrate(shock)",
                  150: "quincunx", 180: "opposition"}
for i in range(len(chain) - 1):
    p1, p2 = chain[i], chain[i + 1]
    t1, t2 = PERIOD_YR[p1], PERIOD_YR[p2]
    synodic = 1.0 / abs(1.0 / t1 - 1.0 / t2)
    dlam = (360.0 * synodic / t2) % 360.0
    short = min(dlam, 360 - dlam)
    nearest = min(aspect_angles, key=lambda a: abs(a - short))
    gap = abs(short - nearest)
    tight = "  <-- TIGHT" if gap < 5 else ("  <-- moderate" if gap < 10 else "")
    print(f"{p1:<9}:{p2:<9} synodic={synodic:>7.2f}yr  drift={dlam:>7.1f}deg  short-way={short:>6.1f}deg  "
          f"nearest={aspect_angles[nearest]:<20}({nearest}deg) gap={gap:>5.1f}deg{tight}")

print("\n" + "=" * 78)
print("OVERALL VERDICT")
print("=" * 78)
print("""
TEST A (PE-order note-ratio -> Ptolemaic solfège steps): REFUTED.
  Real periods are non-monotonic across the locked flow order; ratios miss the
  Ptolemaic step sizes by an order of magnitude. The PE solfège assignment is
  geometric (grid-position-derived), not orbital-period-derived. No chain exists.

TEST B (adjacent-pair ratio -> named just-intonation interval): SPARSE CO-SIGN.
  Two tight hits (Earth:Mars ~= 15:8 major-seventh, Neptune:Pluto ~= 3:2 fifth —
  the latter already canon-locked, §23b), five misses (Mercury:Venus, Venus:Earth,
  Mars:Jupiter, Saturn:Uranus, Uranus:Neptune all land 15-90 cents off any named
  consonance). No systematic chain across the full planetary sequence.

TEST C (synodic conjunction-drift -> 30-degree aspect multiples): SPARSE CO-SIGN.
  Jupiter:Saturn drift ~= 120 deg (trine) at ~3 deg gap — this is the real,
  independently-documented "Great Conjunction trigon" astronomical phenomenon.
  Earth:Mars drift ~= 45 deg (locked shock aspect) at ~4 deg gap. Mercury:Venus
  drift lands near BOTH 120 deg and the 135 deg shock aspect (~7-9 deg gaps).
  Saturn:Uranus and Uranus:Neptune show NO clean alignment (14-16 deg gaps,
  near-null drift instead — expected for adjacent slow giants in near-resonance).

TIER CLASSIFICATION (per OQ-RINGS-06-PRECISION schema: structural-parameter-
substrate vs structural-parameter-empirical): every hit in B and C is
observation-calibrated (orbital), not substrate-forced. None derives from
49-geometry, PE-grid structure, or any coprime/integer substrate mechanism —
they are properties of THIS solar system's actual masses/distances. Per the
same discipline already applied to Venus and Neptune:Pluto: these are
VALIDATION-tier correspondences (real, non-random-looking, worth recording),
not GENERATION-tier derivations. Real orbital timing does not produce the
30-degree aspect system or the Ptolemaic octave from a forcing mechanism —
it lands near a handful of its landmarks, at the same 0.2-3% precision
already established as this system's empirical (not substrate) tier.
""")
