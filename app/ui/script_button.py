from PySide6 import QtWidgets

from app.windows.edit_script import EditScript #direct import cause circular imports SUCK

class ScriptButton(QtWidgets.QListWidgetItem):
    def __init__(self, script_obj):
        super().__init__(script_obj["name"])
        self.path = script_obj.path

    def open_window(self):
        dialog = EditScript(self.path)
        dialog.exec()