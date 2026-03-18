from app import SCRIPT_DIR, VERSION
from .scriptobj import ScriptObj

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

    while any(script_name == item["name"] for item in scripts):
        next_id = int(script_name.lstrip("New Script "))
        script_name = f"New Script {next_id + 1}"

    data = {"version" : VERSION, "name" : script_name, "keybind" : "Ctrl+M", "repeat" : 'O', "script" : []}
    new_path = SCRIPT_DIR / f"{new_filename()}.json"
    with open(new_path, 'w') as file:
        json.dump(data, file)

def new_filename():
    #base36 cause its awesome
    name = ''
    n = round(time.time() * 1000)
    while n > 0:
        name += "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[n % 36]
        n //= 36
    return name[::-1].zfill(8)
