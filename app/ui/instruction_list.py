from PySide6 import QtWidgets

from app.windows.key_record import KeyRecord
from app.windows.mouse_record import MouseRecord

class InstructionList(QtWidgets.QListWidget):
    def __init__(self, script):
        super().__init__()
        self.setStyleSheet("background-color: rgb(246, 246, 246);")
        self.script = script
        self.add_mouse = None
        self.add_key = None
        self.itemClicked.connect(self._on_item)
        self.refresh_list()

    def _on_item(self, item):
        if item == self.add_mouse:
            mouse_record = MouseRecord()
            mouse_record.exec()

        if item == self.add_key:
            key_record = KeyRecord()
            key_record.exec()

        self.refresh_list()

    def refresh_list(self):
        self.clear()

        self.add_mouse = QtWidgets.QListWidgetItem("➕ Add Mouse Instruction")
        self.add_key = QtWidgets.QListWidgetItem("➕ Add Key Instruction")
        self.addItem(self.add_mouse)
        self.addItem(self.add_key)
