from app import SCRIPT_DIR
from .object import ScriptObj

import json
import time

def get_scripts():
    scripts = []
    for item in SCRIPT_DIR.iterdir():
        if item.is_file() and item.suffix == '.json':
            scripts.append(ScriptObj(item))
    return scripts

def add_script():
    scripts = get_scripts()
    script_name = "New Script 1"

    while any(script_name == item.name for item in scripts):
        next_id = int(script_name.lstrip("New Script "))
        script_name = f"New Script {next_id + 1}"

    data = {"name" : script_name, "keybind" : "Ctrl+M"}
    new_path = SCRIPT_DIR / f"{time.time()}.json"
    with open(new_path, 'w') as file:
        json.dump(data, file)
