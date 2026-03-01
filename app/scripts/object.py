import json

class ScriptObj:
    def __init__(self, json_path):
        with open(json_path, 'r') as file:
            self.data = json.load(file)

        self.name = self.data['name']