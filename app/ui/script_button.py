from PySide6 import QtWidgets

class ScriptButton(QtWidgets.QListWidgetItem):
    def __init__(self, script_obj):
        super().__init__(script_obj.name)
        self.path = script_obj.path

    def open_window(self):
        pass