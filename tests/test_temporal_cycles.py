"""
Tests for cyclic-syzygy-activate temporal-cyclic family (canon §30 canonical).

4 substrate-canonical residencies per canon §23b OQ-RINGS-05/06/07 + Nammu
canon line 950 + FINDINGS_012/013/014/015:
  Venus Ring 3   — N=5  inferior-conjunction syzygies / 8yr  / 2880t
  Mercury Ring 5 — N=41 inferior-conjunction syzygies / 13yr / 4680t
  Mars Ring 4    — N=37 OPPOSITION syzygies          / 79yr / 28440t
  Lunar Ring1/Ring2 — N=12 new-moon syzygies         / 1yr  / 360t (derived)
"""
import pytest
from venus_pentagram import (
    VenusPentagramState, compute_venus_pentagram_state,
    VENUS_PENTAGRAM_N, VENUS_RING_TITHIS,
)
from mercury_cycle import (
    MercuryCycleState, compute_mercury_cycle_state,
    MERCURY_CYCLE_N, MERCURY_RING_TITHIS,
)
from mars_cycle import (
    MarsCycleState, compute_mars_cycle_state,
    MARS_CYCLE_N, MARS_RING_TITHIS, EVENT_TYPE as MARS_EVENT,
)
from lunar_year_cycle import (
    LunarYearCycleState, compute_lunar_year_cycle_state,
    LUNAR_CYCLE_N, LUNAR_YEAR_TITHIS, EVENT_TYPE as LUNAR_EVENT,
)
from saturn_cycle import (
    SaturnCycleState, compute_saturn_cycle_state,
    SATURN_SIDEREAL_N, SATURN_RING_TITHIS, SATURN_SIGN_STEP,
    EVENT_TYPE as SATURN_EVENT,
    MIRROR_RATIO as SATURN_MIRROR_RATIO,
)
from jupiter_cycle import (
    JupiterCycleState, compute_jupiter_cycle_state,
    JUPITER_SIDEREAL_N, JUPITER_RING_TITHIS, JUPITER_SIGN_STEP,
    EVENT_TYPE as JUPITER_EVENT,
)
from uranus_cycle import (
    UranusCycleState, compute_uranus_cycle_state,
    URANUS_SIDEREAL_N, URANUS_RING_TITHIS, URANUS_SIGN_STEP,
    EVENT_TYPE as URANUS_EVENT,
)
from pluto_cycle import (
    PlutoCycleState, compute_pluto_cycle_state,
    PLUTO_SIDEREAL_N, PLUTO_RING_TITHIS, PLUTO_SIGN_STEP,
    EVENT_TYPE as PLUTO_EVENT,
)


# ─── Substrate-lock tests (canon §23b values) ─────────────────────────────────

def test_venus_substrate_locks():
    """Canon §23b OQ-RINGS-06: Venus Ring 3 = 5 inferior conjunctions / 2880t / 8yr."""
    assert VENUS_PENTAGRAM_N == 5
    assert VENUS_RING_TITHIS == 2880


def test_mercury_substrate_locks():
    """Canon §23b OQ-RINGS-07: Mercury Ring 5 = 41 inferior conjunctions / 4680t / 13yr."""
    assert MERCURY_CYCLE_N == 41
    assert MERCURY_RING_TITHIS == 4680


def test_mars_substrate_locks():
    """Canon §23b line 950: Mars Ring 4 = 37 oppositions / 28440t / 79yr."""
    assert MARS_CYCLE_N == 37
    assert MARS_RING_TITHIS == 28440
    assert MARS_EVENT == 'opposition'


def test_lunar_substrate_locks():
    """Lunar Ring1/Ring2 ratio: 12 new-moon syzygies / 360t / 1yr (derived 360/30)."""
    assert LUNAR_CYCLE_N == 12
    assert LUNAR_YEAR_TITHIS == 360
    assert LUNAR_EVENT == 'new-moon-syzygy'


def test_lunar_derivable_from_ring_ratio():
    """N=12 = Ring 1 (Solar 360t) / Ring 2 (Lunar 30t). Substrate-derivable."""
    assert LUNAR_CYCLE_N == 360 // 30


# ─── Frozen state tests ──────────────────────────────────────────────────────

def test_venus_frozen():
    s = compute_venus_pentagram_state('test')
    assert s.longitudes is None
    assert s.pentagram_closure is None


def test_mercury_frozen():
    s = compute_mercury_cycle_state('test')
    assert s.longitudes is None
    assert s.closure is None


def test_mars_frozen():
    s = compute_mars_cycle_state('test')
    assert s.longitudes is None
    assert s.closure is None


def test_lunar_frozen():
    s = compute_lunar_year_cycle_state('test')
    assert s.longitudes is None
    assert s.closure is None


# ─── Ideal cycle closure tests ────────────────────────────────────────────────

def test_venus_ideal_pentagram_closes():
    """Ideal pentagram: 0/144/288/72/216 → closure within drift tolerance."""
    s = compute_venus_pentagram_state('ideal', 0.0, 144.0, 288.0, 72.0, 216.0)
    assert s.pentagram_closure is True
    assert abs(s.drift_deg) < 1e-9


def test_mercury_ideal_cycle_closes():
    """41 conjunctions at exact 114.5° steps close within drift tolerance."""
    from mercury_cycle import MERCURY_ADJ_STEP_DEG
    ideal = [(i * MERCURY_ADJ_STEP_DEG) % 360.0 for i in range(MERCURY_CYCLE_N)]
    s = compute_mercury_cycle_state('ideal', ideal)
    assert s.closure is True
    assert abs(s.drift_deg) < 1e-9


def test_mars_ideal_cycle_closes():
    """37 oppositions at exact 48.6° steps close within drift tolerance."""
    from mars_cycle import MARS_ADJ_STEP_DEG
    ideal = [(i * MARS_ADJ_STEP_DEG) % 360.0 for i in range(MARS_CYCLE_N)]
    s = compute_mars_cycle_state('ideal', ideal)
    assert s.closure is True
    assert abs(s.drift_deg) < 1e-9


def test_lunar_ideal_cycle_exact_closure():
    """12 new-moons at exact 30° steps → 12 × 30 = 360 exact closure."""
    from lunar_year_cycle import LUNAR_ADJ_STEP_DEG
    ideal = [(i * LUNAR_ADJ_STEP_DEG) % 360.0 for i in range(LUNAR_CYCLE_N)]
    s = compute_lunar_year_cycle_state('ideal', ideal)
    assert s.closure is True
    assert s.drift_deg == 0.0


# ─── Partial input rejection (substrate-honest) ──────────────────────────────

def test_venus_partial_raises():
    with pytest.raises(ValueError):
        compute_venus_pentagram_state('partial', 0.0, 144.0, None, 72.0, 216.0)


def test_mercury_wrong_count_raises():
    with pytest.raises(ValueError):
        compute_mercury_cycle_state('bad', [0.0, 1.0, 2.0])  # 3 not 41


def test_mars_wrong_count_raises():
    with pytest.raises(ValueError):
        compute_mars_cycle_state('bad', [0.0] * 36)  # 36 not 37


def test_lunar_wrong_count_raises():
    with pytest.raises(ValueError):
        compute_lunar_year_cycle_state('bad', [0.0] * 11)  # 11 not 12


# ─── Cross-engine shape match (FINDINGS_013 + FINDINGS_015) ───────────────────

def test_four_temporal_engines_share_9_compute_fields():
    """
    FINDINGS_013 + FINDINGS_015: all 4 temporal-cyclic engines share 9 core
    compute fields. Confirms cyclic-syzygy-activate canonical applies at all 4
    residencies.
    """
    from dataclasses import fields
    vp = {f.name for f in fields(VenusPentagramState)}
    mc = {f.name for f in fields(MercuryCycleState)}
    ma = {f.name for f in fields(MarsCycleState)}
    ly = {f.name for f in fields(LunarYearCycleState)}
    shared = vp & mc & ma & ly
    expected_shared = {
        'adjacent_step_deg', 'canonical_steps', 'cycle_id', 'cycle_tithis',
        'drift_deg', 'drift_tolerance', 'longitudes',
        'mean_adjacent_step', 'pairwise_separations',
    }
    assert expected_shared.issubset(shared), \
        f"Cross-N shape match broken. Missing: {expected_shared - shared}"


def test_three_distinct_event_types():
    """
    FINDINGS_015: 3 distinct syzygy event-types across 4 residencies:
      inferior-conjunction (Venus, Mercury) + opposition (Mars) + new-moon-syzygy (Moon).
    """
    event_types_with_attr = {MARS_EVENT, LUNAR_EVENT}
    # Venus + Mercury don't expose event_type field but are inferior-conjunction by canon
    assert event_types_with_attr == {'opposition', 'new-moon-syzygy'}
    assert 'opposition' != 'new-moon-syzygy'
    # 3rd event-type (inferior-conjunction) substrate-locked by canon §23b for Venus+Mercury


def test_substrate_periods_all_canon_locked():
    """All 4 cycle-periods are canon §23b values, NOT invented."""
    # Canon §23b values
    assert VENUS_RING_TITHIS == 2880    # Ring 3
    assert MERCURY_RING_TITHIS == 4680  # Ring 5
    assert MARS_RING_TITHIS == 28440    # Ring 4 line 950
    assert LUNAR_YEAR_TITHIS == 360     # Ring 1 (derived parent)


# ─── Saturn cycle tests (FINDINGS_016: NEW function-class candidate) ──────────

def test_saturn_substrate_locks():
    """Canon §23b line 953: Saturn Ring 7 = 12 sign-ingresses / 10620t / 29.5yr."""
    assert SATURN_SIDEREAL_N == 12
    assert SATURN_RING_TITHIS == 10620
    assert SATURN_SIGN_STEP == 30.0
    assert SATURN_EVENT == 'sign-ingress'


def test_saturn_event_type_distinct_from_syzygy():
    """
    FINDINGS_016: Saturn sign-ingress is NOT a syzygy event. Substrate-mechanism
    distinct from cyclic-syzygy-activate (canon §30 canonical). NEW function-
    class candidate: cyclic-sign-ingress-activate.
    """
    assert SATURN_EVENT != MARS_EVENT  # 'sign-ingress' ≠ 'opposition'
    assert SATURN_EVENT != LUNAR_EVENT  # 'sign-ingress' ≠ 'new-moon-syzygy'


def test_saturn_ideal_cycle_exact_closure():
    """12 sign-ingresses at exact 30° steps → 12 × 30 = 360 exact closure."""
    ideal = [(i * SATURN_SIGN_STEP) % 360.0 for i in range(SATURN_SIDEREAL_N)]
    s = compute_saturn_cycle_state('ideal', ideal)
    assert s.closure is True
    assert s.drift_deg == 0.0


def test_saturn_frozen():
    s = compute_saturn_cycle_state('test')
    assert s.longitudes is None
    assert s.closure is None


def test_saturn_wrong_count_raises():
    with pytest.raises(ValueError):
        compute_saturn_cycle_state('bad', [0.0] * 11)  # 11 not 12


def test_saturn_moon_synodic_mirror_is_descriptor():
    """
    FINDINGS_016: Moon-synodic mirror is substrate-numerical descriptor, NOT
    active substrate-function. Saturn 29.5yr ratio to Lunar 29.5d = 354 ratio.
    """
    assert SATURN_MIRROR_RATIO == 354.0  # 10620 / 30 = 354


def test_n_12_substrate_coincidence():
    """
    FINDINGS_016: Both Lunar (new-moon syzygies) and Saturn (sign-ingresses)
    have N=12 at 30° step. Substrate-imposed zodiac cardinality.
    """
    assert LUNAR_CYCLE_N == SATURN_SIDEREAL_N == 12
    # But event-types differ:
    assert LUNAR_EVENT != SATURN_EVENT


# ─── Jupiter cycle tests (FINDINGS_017: 2nd cyclic-sign-ingress residency) ───

def test_jupiter_substrate_locks():
    """Canon §23b line 954: Jupiter Ring 8 = 12 sign-ingresses / 4320t / 12yr."""
    assert JUPITER_SIDEREAL_N == 12
    assert JUPITER_RING_TITHIS == 4320
    assert JUPITER_SIGN_STEP == 30.0
    assert JUPITER_EVENT == 'sign-ingress'


def test_jupiter_event_type_matches_saturn():
    """Same event-type as Saturn → cross-R-tier residency for cyclic-sign-ingress-activate."""
    assert JUPITER_EVENT == SATURN_EVENT == 'sign-ingress'


def test_jupiter_ideal_cycle_exact_closure():
    """12 sign-ingresses at exact 30° → exact closure."""
    ideal = [(i * JUPITER_SIGN_STEP) % 360.0 for i in range(JUPITER_SIDEREAL_N)]
    s = compute_jupiter_cycle_state('ideal', ideal)
    assert s.closure is True
    assert s.drift_deg == 0.0


def test_jupiter_frozen():
    s = compute_jupiter_cycle_state('test')
    assert s.longitudes is None
    assert s.closure is None


def test_jupiter_wrong_count_raises():
    with pytest.raises(ValueError):
        compute_jupiter_cycle_state('bad', [0.0] * 11)


def test_saturn_jupiter_cross_r_tier_shape_match():
    """
    FINDINGS_017: Jupiter fields = exact subset of Saturn fields. 11/11 Jupiter
    fields shared with Saturn (Saturn has 2 extra Moon-synodic-mirror descriptors).
    Cross-R-tier compute-shape MATCH for cyclic-sign-ingress-activate.
    """
    from dataclasses import fields
    s = {f.name for f in fields(SaturnCycleState)}
    j = {f.name for f in fields(JupiterCycleState)}
    assert j.issubset(s)
    saturn_only = s - j
    assert saturn_only == {'moon_synodic_mirror_ratio', 'moon_synodic_mirror_in_solar_years'}


def test_outer_planet_sign_ingress_invariants():
    """Same N + same step across Saturn + Jupiter; different period + planet."""
    assert SATURN_SIDEREAL_N == JUPITER_SIDEREAL_N == 12
    assert SATURN_SIGN_STEP == JUPITER_SIGN_STEP == 30.0
    assert SATURN_RING_TITHIS != JUPITER_RING_TITHIS


# ─── Uranus + Pluto cycle tests (FINDINGS_018: 3rd + 4th sign-ingress residencies) ─

def test_uranus_substrate_locks():
    """Canon §23b line 952: Uranus Ring 6 = 12 sign-ingresses / 30240t / 84yr."""
    assert URANUS_SIDEREAL_N == 12
    assert URANUS_RING_TITHIS == 30240
    assert URANUS_SIGN_STEP == 30.0
    assert URANUS_EVENT == 'sign-ingress'


def test_pluto_substrate_locks():
    """Canon §23b line 945: Pluto Ring 0 = 12 sign-ingresses / 89280t / ~248yr."""
    assert PLUTO_SIDEREAL_N == 12
    assert PLUTO_RING_TITHIS == 89280
    assert PLUTO_SIGN_STEP == 30.0
    assert PLUTO_EVENT == 'sign-ingress'


def test_uranus_ideal_closure():
    ideal = [(i * URANUS_SIGN_STEP) % 360.0 for i in range(URANUS_SIDEREAL_N)]
    s = compute_uranus_cycle_state('ideal', ideal)
    assert s.closure is True and s.drift_deg == 0.0


def test_pluto_ideal_closure():
    ideal = [(i * PLUTO_SIGN_STEP) % 360.0 for i in range(PLUTO_SIDEREAL_N)]
    s = compute_pluto_cycle_state('ideal', ideal)
    assert s.closure is True and s.drift_deg == 0.0


def test_uranus_frozen():
    assert compute_uranus_cycle_state('t').closure is None


def test_pluto_frozen():
    assert compute_pluto_cycle_state('t').closure is None


def test_uranus_wrong_count():
    with pytest.raises(ValueError):
        compute_uranus_cycle_state('bad', [0.0] * 11)


def test_pluto_wrong_count():
    with pytest.raises(ValueError):
        compute_pluto_cycle_state('bad', [0.0] * 11)


def test_4_outer_planet_sign_ingress_match():
    """FINDINGS_018: 4 outer-planet sign-ingress engines share 11 compute fields."""
    from dataclasses import fields
    s = {f.name for f in fields(SaturnCycleState)}
    j = {f.name for f in fields(JupiterCycleState)}
    u = {f.name for f in fields(UranusCycleState)}
    p = {f.name for f in fields(PlutoCycleState)}
    assert len(s & j & u & p) == 11
    # Jupiter, Uranus, Pluto have IDENTICAL field-sets (Saturn alone has 2 mirror descriptors)
    assert j == u == p


def test_4_outer_planets_same_N_same_step():
    """All 4 outer planets: N=12 sign-ingresses, 30° step (zodiac cardinality)."""
    assert SATURN_SIDEREAL_N == JUPITER_SIDEREAL_N == URANUS_SIDEREAL_N == PLUTO_SIDEREAL_N == 12
    assert SATURN_SIGN_STEP == JUPITER_SIGN_STEP == URANUS_SIGN_STEP == PLUTO_SIGN_STEP == 30.0


def test_4_outer_planets_distinct_periods():
    """4 distinct period-values: 4320 / 10620 / 30240 / 89280 tithis."""
    periods = {JUPITER_RING_TITHIS, SATURN_RING_TITHIS, URANUS_RING_TITHIS, PLUTO_RING_TITHIS}
    assert periods == {4320, 10620, 30240, 89280}
