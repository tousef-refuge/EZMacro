from PySide6 import QtWidgets

from app.windows.edit_subscript import EditSubscript

class SubScript(QtWidgets.QListWidgetItem):
    def __init__(self, instruct, idx):
        super().__init__(instruct["type"].capitalize())
        self.instruct = instruct
        self.idx = idx

    def open_window(self):
        dialog = EditSubscript(self.instruct)
        if dialog.exec():
            self.instruct = dialog.instruct