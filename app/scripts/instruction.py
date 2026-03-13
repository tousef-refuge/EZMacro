class Instruction:
    def getdata(self):
        pass

class MouseInstruction(Instruction):
    def __init__(self, record):
        self.x = record.pos.x
        self.y = record.pos.y

    def getdata(self):
        return {"type": "mouse", "hold": 1, "sleep": 1, "button" : "left", "x": self.x, "y": self.y}

class KeyInstruction(Instruction):
    def __init__(self, record):
        self.key = record.key.toString()

    def getdata(self):
        return {"type": "key", "hold": 1, "sleep": 1, "key": self.key}

class WriteInstruction(Instruction):
    def __init__(self, record):
        self.line = record.line

    def getdata(self):
        return {"type": "write", "sleep": 1, "line": self.line}
