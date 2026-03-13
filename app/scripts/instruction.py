class Instruction:
    @staticmethod
    def _basedata():
        return {"type" : ' ', "hold" : 1, "sleep" : 1}

    def getdata(self):
        pass

class MouseInstruction(Instruction):
    def __init__(self, record):
        self.x = record.pos.x
        self.y = record.pos.y

    def getdata(self):
        data = self._basedata()
        data["type"] = "mouse"
        data["x"] = self.x
        data["y"] = self.y
        return data

class KeyInstruction(Instruction):
    def __init__(self, record):
        self.key = record.key.toString()

    def getdata(self):
        data = self._basedata()
        data["type"] = "key"
        data["key"] = self.key
        return data

class WriteInstruction(Instruction):
    def __init__(self, record):
        self.line = record.line

    def getdata(self):
        data = self._basedata()
        data["type"] = "write"
        data["line"] = self.line
        return data
