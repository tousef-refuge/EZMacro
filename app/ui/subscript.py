from PySide6 import QtWidgets

from app.windows.edit_subscript import EditSubscript

def subscript_name(instruct):
    itype = instruct["type"].capitalize()
    if itype == "Key":
        info = instruct["key"]
    else:
        info = f"{instruct["x"]}, {instruct["y"]}"
    return f"{itype} ({info})"

class SubScript(QtWidgets.QListWidgetItem):
    def __init__(self, instruct, idx):
        super().__init__(subscript_name(instruct))
        self.instruct = instruct
        self.idx = idx

    def open_window(self):
        dialog = EditSubscript(self.instruct)
        if dialog.exec():
            self.instruct = dialog.instruct