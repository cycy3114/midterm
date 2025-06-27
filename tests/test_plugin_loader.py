import os
from calc.plugin_loader import load_plugins

def test_plugin_loader(tmp_path):
    # Create a dummy plugin
    plugin_file = tmp_path / "square.py"
    plugin_file.write_text("def run(x): return float(x) * float(x)")
    
    # Load plugin from this temp directory
    plugins = load_plugins(path=str(tmp_path))
    
    assert "square" in plugins
    assert plugins["square"].run(4) == 16.0
