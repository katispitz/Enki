"""
Tests for _aspect_angle_generator_engine.py — the two exact aspect-angle
generation mechanisms (Merkaba/PE ladder, icosahedron/zodiac equal-division)
that replace the REFUTED real-orbital-timing hypothesis for OQ-OCTAVES-01.

Verifies:
  - Merkaba ladder produces exactly {0, 45, 90, 120, 180}, no gap
  - Do->Sol is exactly 3/2 (the worked case from inline council 2026-07-27)
  - Icosahedron ladder produces exactly {30, 60, 90, 120, 150, 180}
  - Overlap set (lock-by-redundancy candidates) = {90, 120, 180}
  - 135 deg is correctly reported as unreached, not silently dropped
  - aspect_angle_from_ratio() matches canon §19 formula on hand-checked cases
"""
from fractions import Fraction
import pytest
from _aspect_angle_generator_engine import (
    aspect_angle_from_ratio, pe_ladder_angles, icosahedron_ladder_angles,
    classify_aspect_coverage, describe,
)


def test_do_to_sol_is_exact_perfect_fifth():
    notes = {n.note: n for n in pe_ladder_angles()}
    assert notes["Sol"].ratio_from_do == Fraction(3, 2)
    assert notes["Sol"].angle_deg == 180.0


def test_merkaba_ladder_exact_set():
    angles = {int(n.angle_deg) % 360 for n in pe_ladder_angles()}
    assert angles == {0, 45, 90, 120, 180}


def test_icosahedron_ladder_exact_set():
    angles = {s.angle_deg for s in icosahedron_ladder_angles()}
    assert angles == {30, 60, 90, 120, 150, 180}


def test_overlap_is_square_trine_opposition_only():
    cov = classify_aspect_coverage()
    assert cov.overlap_redundant == {90, 120, 180}
    assert cov.merkaba_only == {0, 45}
    assert cov.icosahedron_only == {30, 60, 150}


def test_135_is_reported_unreached_not_dropped():
    cov = classify_aspect_coverage()
    assert cov.unreached == {135}


def test_aspect_angle_from_ratio_matches_hand_calc():
    assert aspect_angle_from_ratio(Fraction(3, 2)) == 180.0
    assert aspect_angle_from_ratio(Fraction(9, 4)) == 90.0
    assert aspect_angle_from_ratio(Fraction(27, 8)) == 45.0
    assert aspect_angle_from_ratio(Fraction(4, 3)) == 120.0


def test_describe_declares_no_orbital_input():
    d = describe()
    assert d["takes_orbital_input"] is False
    assert d["status"] == "probe"
