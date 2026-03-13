from PySide6 import QtWidgets

from app.windows.edit_subscript import get_edit_subscript

def subscript_name(instruct):
    itype = instruct["type"].capitalize()
    info = None
    match itype:
        case "Key":
            info = instruct["key"]

        case "Mouse":
            info = f"{instruct["x"]}, {instruct["y"]}"

        case "Write":
            info = instruct["line"]
    return f"{itype} ({info})"

class SubScript(QtWidgets.QListWidgetItem):
    def __init__(self, instruct, idx):
        super().__init__(subscript_name(instruct))
        self.instruct = instruct
        self.idx = idx

    def open_window(self):
        dialog = get_edit_subscript(self.instruct)
        if dialog.exec():
            self.instruct = dialog.instruct