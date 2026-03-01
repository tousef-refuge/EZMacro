from PySide6 import QtWidgets

class ScriptList(QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()
        self.add_button = None
        self.refresh_list()

    def _on_item(self, item):
        if item == self.add_button:
            new_item = QtWidgets.QListWidgetItem("New Script")
            self.insertItem(self.count() - 1, new_item)

        else:
            print(item.evil_name)

    def refresh_list(self):
        self.clear()
        self.add_button = QtWidgets.QListWidgetItem("➕ Add Script")
        self.addItem(self.add_button)
        self.itemClicked.connect(self._on_item)