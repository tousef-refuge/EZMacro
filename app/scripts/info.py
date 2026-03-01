from app import SCRIPT_DIR
from app.scripts import ScriptObj

def get_scripts():
    scripts = []
    for item in SCRIPT_DIR.iterdir():
        if item.is_file() and item.suffix == '.json':
            scripts.append(ScriptObj(item))
    return scripts