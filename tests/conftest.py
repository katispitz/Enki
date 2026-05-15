"""
Enki pytest config — engine import path setup.

Each Enki engine module sits in ~/Enki/engines/. Tests import via direct
module name (e.g., `from _axis_engine import compute_axis_state`).
"""
import sys
from pathlib import Path

# Make Enki/engines/ importable from any test module
ENGINES_DIR = Path(__file__).parent.parent / "engines"
sys.path.insert(0, str(ENGINES_DIR))
