from PySide6 import QtWidgets

class InstructionList(QtWidgets.QListWidget):
    def __init__(self, script):
        super().__init__()
        self.script = script
        self.add_button = None
        self.itemClicked.connect(self._on_item)
        self.refresh_list()

    def _on_item(self, item):
        pass

    def refresh_list(self):
        self.clear()

        self.add_button = QtWidgets.QListWidgetItem("➕ Add Script")
        self.addItem(self.add_button)
