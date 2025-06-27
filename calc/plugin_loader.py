import importlib.util
import os

def load_plugins(path="plugins"):
    plugins = {}
    for filename in os.listdir(path):
        if filename.endswith(".py"):
            name = filename[:-3]
            spec = importlib.util.spec_from_file_location(name, os.path.join(path, filename))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            plugins[name] = mod
    return plugins
