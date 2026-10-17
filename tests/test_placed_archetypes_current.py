"""PLACED_ARCHETYPES.md must match the registry (generated view; kati 2026-10-16 master file)."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location('gen_placed_archetypes', ROOT / 'scripts' / 'gen_placed_archetypes.py')
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)


def test_master_file_matches_registry():
    expected = G.render(json.loads(G.REGISTRY.read_text()))
    assert G.OUT.read_text() == expected, 'stale: run python3 scripts/gen_placed_archetypes.py'


def test_every_event_arc_is_listed():
    reg = json.loads(G.REGISTRY.read_text())
    text = G.OUT.read_text()
    for name, v in reg.items():
        if isinstance(v, dict) and v.get('placement_class') == 'EVENT_ARC':
            assert f'**{name}**' in text
