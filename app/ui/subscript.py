from PySide6 import QtWidgets

class SubScript(QtWidgets.QListWidgetItem):
    def __init__(self, data, idx):
        super().__init__(data["type"].capitalize())
        self.idx = idx

    def open_window(self):
        pass