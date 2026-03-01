import json

class ScriptObj:
    def __init__(self, json_path):
        self.path = json_path
        with open(json_path, 'r') as file:
            self.data = json.load(file)

        self.name = self.data['name']
        self.keybind = self.data['keybind']

    def write(self, key, value):
        self.data[key] = value
        self.path.write_text(json.dumps(self.data))

    def unlink(self):
        self.path.unlink()