from PySide6 import QtWidgets

from .subscript import SubScript
from app.scripts import MouseInstruction, KeyInstruction
from app.windows.input_record import MouseRecord, KeyRecord, WriteRecord

class InstructionList(QtWidgets.QListWidget):
    def __init__(self, script_obj):
        super().__init__()
        self.setStyleSheet("background-color: rgb(246, 246, 246);")
        self.script_obj = script_obj
        self.add_mouse = None
        self.add_key = None
        self.add_write = None
        self.itemClicked.connect(self._on_item)
        self.refresh_list()

    def _on_item(self, item):
        script = self.script_obj["script"]
        match item:
            case self.add_mouse:
                mouse_record = MouseRecord()
                if mouse_record.exec():
                    instruct = MouseInstruction(mouse_record.pos)
                    self.script_obj.append(instruct)

            case self.add_key:
                key_record = KeyRecord()
                if key_record.exec():
                    instruct = KeyInstruction(key_record.key)
                    self.script_obj.append(instruct)

            case self.add_write:
                write_record = WriteRecord()
                if write_record.exec():
                    pass

            case _:
                item.open_window()
                new_instruct = item.instruct
                if new_instruct == {}:
                    script.pop(item.idx)
                else:
                    script[item.idx] = item.instruct
                self.script_obj.write("script", script)

        self.refresh_list()

    def refresh_list(self):
        self.clear()
        script = self.script_obj["script"]
        for idx, instruct in enumerate(script):
            subscript = SubScript(instruct, idx)
            self.addItem(subscript)

        self.add_mouse = QtWidgets.QListWidgetItem("➕ Add Mouse Instruction")
        self.add_key = QtWidgets.QListWidgetItem("➕ Add Key Instruction")
        self.add_write = QtWidgets.QListWidgetItem("➕ Add Writing Instruction")
        self.addItem(self.add_mouse)
        self.addItem(self.add_key)
        self.addItem(self.add_write)
