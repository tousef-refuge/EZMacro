import json

class ScriptObj:
    def __init__(self, json_path):
        self.path = json_path
        with open(json_path, 'r') as file:
            self.data = json.load(file)

        self.name = self.data['name']
        self.keybind = self.data['keybind']

    def get_script(self):
        return self.data['script']

    def append(self, instruction):
        script = self.data['script']
        script.append(instruction.getdata())
        self.data['script'] = script
        self.path.write_text(json.dumps(self.data))

    def write(self, key, value):
        self.data[key] = value
        self.path.write_text(json.dumps(self.data))

    def unlink(self):
        self.path.unlink()