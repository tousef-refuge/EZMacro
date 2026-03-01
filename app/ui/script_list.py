from PySide6 import QtWidgets

from app.scripts import get_scripts, add_script

class ScriptList(QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()
        self.add_button = None
        self.refresh_list()

    def _on_item(self, item):
        if item == self.add_button:
            add_script()
            self.refresh_list()

    def refresh_list(self):
        self.clear()
        scripts = get_scripts()
        for script in scripts:
            button = QtWidgets.QListWidgetItem(script.name)
            self.addItem(button)

        self.add_button = QtWidgets.QListWidgetItem("➕ Add Script")
        self.addItem(self.add_button)
        self.itemClicked.connect(self._on_item)