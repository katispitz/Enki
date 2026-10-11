"""Arc recall along the actor's 60-grid path (EVENT_ARC, kati_direct 2026-10-11)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "substrate"))
import field_memory as F  # noqa: E402


def test_path_cells_direct_wraps_and_handles_float_noise():
    cells = F.arc_path_cells(54.99999999, 39.99999999, "direct")     # Apollo: VE → WS
    assert cells[0] == 55 and cells[-1] == 40 and 0 in cells and len(cells) == 46


def test_path_cells_retrograde():
    assert F.arc_path_cells(31.4, 28.8, "retrograde") == [31, 30, 29, 28]


def test_node_labels_keep_layers_separate():
    lab = F.grid_node_label(30)
    assert "Scorpio" in lab and "gate 2" in lab and "oct V5" in lab
    assert "PE-slot Sol (ordinal layer)" in lab
    assert "X3" in F.grid_node_label(18) and "ordinal layer" in F.grid_node_label(18)
    assert F.grid_node_label(0).startswith("g0 Taurus")


def test_recall_order_now_ahead_crossed():
    import placement_discipline as P
    rec = F.recall_arc_field(P.load_placement("Apollo"), "Apollo", limit=None,
                             when="2026-10-11T18:00")
    wheres = [n["where"] for n in rec["nodes"]]
    assert wheres[0] == "now" and "ahead" in wheres and "crossed" in wheres
    assert wheres.index("crossed") > max(i for i, w in enumerate(wheres) if w == "ahead")
    assert rec["nodes"][0]["cell"] == rec["actor_cell"] == 28


def test_moved_deities_are_event_arc_and_activate():
    import datetime as dt
    import activation_gate as G
    import placement_discipline as P
    when = dt.datetime(2026, 10, 11, 18, tzinfo=dt.timezone.utc)
    expect = {"Persephone": True, "Dionysus": False, "Inanna": True, "Lucifer": True, "Apollo": True}
    for name, active in expect.items():
        pl = P.load_placement(name)
        assert pl["placement_class"] == "EVENT_ARC"
        assert G.check_activation(name, pl, when).active is active, name


def test_event_arc_voices_convene_when_inside_arc():
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "council"))
    import composer as C
    oct_ctx = {"q_profile": {}, "transit_date": "2026-10-11"}
    jan_ctx = {"q_profile": {}, "transit_date": "2027-01-15"}
    oct_ = set(C.convene_by_question(oct_ctx)["convened"])
    jan_ = set(C.convene_by_question(jan_ctx)["convened"])
    assert {"Apollo", "Inanna", "Lucifer", "Persephone"} <= oct_ and "Dionysus" not in oct_
    assert {"Dionysus", "Persephone"} <= jan_ and "Apollo" not in jan_
