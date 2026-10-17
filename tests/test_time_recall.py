"""Time-keyed recall (2026-10-16): cards whose arc contains T; cards whose moment lies inside
arc A. Categorical only. Reads a synthetic card list — never the live store."""
import datetime as dt
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "substrate"))
import field_memory as F  # noqa: E402
import card_writer as cw  # noqa: E402  (field_memory puts ~/Nammu/cards on sys.path)

UTC = dt.timezone.utc
APOLLO = {"archetype": "Apollo", "actor": "Sun", "engine": "archetype_events.apollo_arc"}
DIONYSUS = {"archetype": "Dionysus", "actor": "Sun", "engine": "archetype_events.dionysus_arc"}


def _card(cid, **kw):
    return {"id": cid, "created_at": "2026-01-01T00:00:00+00:00", "canon_status": "candidate",
            "text": cid, **kw}


@pytest.fixture
def store(monkeypatch):
    cards = []
    monkeypatch.setattr(cw, "_load", lambda: list(cards))
    return cards


def test_engine_arc_contains(store):
    store += [_card("apollo", event_arcs=[APOLLO]), _card("dionysus", event_arcs=[DIONYSUS]),
              _card("plain")]
    summer = F.recall_arcs_containing("2026-07-01T00:00")
    assert [(h["card"]["id"], h["by"]) for h in summer] == [("apollo", "engine")]
    assert 0 < summer[0]["position"]["fraction"] < 1
    winter = F.recall_arcs_containing("2026-02-01T00:00")
    assert [h["card"]["id"] for h in winter] == ["dionysus"]


def test_pinned_arc_contains(store):
    pinned = dict(APOLLO, start="2026-03-20T00:00:00+00:00", end="2026-03-25T00:00:00+00:00")
    store.append(_card("pinned", event_arcs=[pinned]))
    assert [h["by"] for h in F.recall_arcs_containing("2026-03-22")] == ["pinned"]
    assert F.recall_arcs_containing("2026-07-01") == []      # pinned instance is over


def test_dropped_status_excluded(store):
    store.append(_card("gone", canon_status="retracted", event_arcs=[APOLLO]))
    assert F.recall_arcs_containing("2026-07-01") == []
    assert len(F.recall_arcs_containing("2026-07-01", include_dropped=True)) == 1


def test_moments_in_arc(store):
    store += [_card("about", moment="2026-05-01T00:00:00+00:00", moment_kind="about"),
              _card("written_only", created_at="2026-08-01T00:00:00+00:00"),
              _card("outside", moment="2026-02-01T00:00:00+00:00")]
    arc = F.arc_for("Apollo", "2026-07-01")
    hits = F.recall_moments_in_arc(arc)
    assert [(h["card"]["id"], h["by"]) for h in hits] == [("about", "moment"), ("written_only", "created_at")]
    assert hits[0]["position"] is not None
    span = F.recall_moments_in_arc(("2026-04-30", "2026-05-02"))
    assert [h["card"]["id"] for h in span] == ["about"] and span[0]["position"] is None


def test_no_scores_in_output(store):
    store.append(_card("apollo", event_arcs=[APOLLO], moment="2026-07-01T00:00:00+00:00"))
    for h in F.recall_arcs_containing("2026-07-01") + F.recall_moments_in_arc(F.arc_for("Apollo", "2026-07-01")):
        assert not {"score", "weight", "rank"} & set(h)


def test_density_clock_is_canonical_tithi_clock():
    """density.t_tithis_at = (JD − EPOCH_JD)·30/SYNODIC (canon §17 epoch, §23b tithi unit) —
    the engine path; not calendar days since 2026-01-01 (retired 2026-10-16)."""
    import density
    import locate_entity_v4 as loc
    w = dt.datetime(2026, 10, 16, 20, 0)
    jd = loc._jd(2026, 10, 16, 20, 0, 0)
    assert density.t_tithis_at(w) == pytest.approx((jd - loc.EPOCH_JD) * 30.0 / loc.SYNODIC)
    assert density.t_tithis_at(dt.datetime(2026, 1, 1)) > 1e6          # retired clock read 0 here
    same = [w, w.replace(tzinfo=UTC), "2026-10-16T13:00-07:00", "2026-10-16T20:00Z"]
    assert len({density.helix_coord_at(x)["matrix_pos"] for x in same}) == 1
