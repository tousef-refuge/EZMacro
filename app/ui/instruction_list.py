from PySide6 import QtWidgets

from .subscript import SubScript
from app.scripts import MouseInstruction, KeyInstruction
from app.windows.input_record import MouseRecord, KeyRecord

class InstructionList(QtWidgets.QListWidget):
    def __init__(self, script_obj):
        super().__init__()
        self.setStyleSheet("background-color: rgb(246, 246, 246);")
        self.script_obj = script_obj
        self.add_mouse = None
        self.add_key = None
        self.itemClicked.connect(self._on_item)
        self.refresh_list()

    def _on_item(self, item):
        if item == self.add_mouse:
            mouse_record = MouseRecord()
            if mouse_record.exec():
                instruct = MouseInstruction(mouse_record.pos)
                self.script_obj.append(instruct)

        if item == self.add_key:
            key_record = KeyRecord()
            if key_record.exec():
                instruct = KeyInstruction(key_record.key)
                self.script_obj.append(instruct)

        if type(item) == SubScript:
            item.open_window()

        self.refresh_list()

    def refresh_list(self):
        self.clear()
        script = self.script_obj.get_script()
        for idx, instruct in enumerate(script):
            subscript = SubScript(instruct, idx)
            self.addItem(subscript)

        self.add_mouse = QtWidgets.QListWidgetItem("➕ Add Mouse Instruction")
        self.add_key = QtWidgets.QListWidgetItem("➕ Add Key Instruction")
        self.addItem(self.add_mouse)
        self.addItem(self.add_key)
