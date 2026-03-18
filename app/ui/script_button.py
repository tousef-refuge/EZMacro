from PySide6 import QtGui, QtWidgets
from app import VERSION, VersionObj

from app.windows.edit_script import EditScript #direct import cause circular imports SUCK
from app.scripts import ScriptObj

class ScriptButton(QtWidgets.QListWidgetItem):
    def __init__(self, script_obj, parent):
        super().__init__(script_obj["name"])
        self.parent = parent
        self.path = script_obj.path

        self.version = VersionObj(script_obj["version"])
        self.is_old = self.version < VERSION
        if self.is_old:
            self.setForeground(QtGui.QColor("red"))

    def open_window(self):
        confirm = not self.is_old
        if self.is_old:
            dialog = QtWidgets.QMessageBox.question(
                self.parent,
                "Warning",
                f"This script is on version {self.version} while\nyou are currently running version {VERSION}.\nRunning this script may crash the program.\nDo you want to open it?",
                QtWidgets.QMessageBox.StandardButton.Yes |
                QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No
            )
            confirm = dialog == QtWidgets.QMessageBox.StandardButton.Yes

        if confirm:
            dialog = EditScript(self.path)
            dialog.exec()
        else:
            delete = QtWidgets.QMessageBox()
            delete.setWindowTitle(' ')
            delete.setText("Do you want to delete this script instead?")
            delete.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Yes |
                QtWidgets.QMessageBox.StandardButton.No
            )

            if delete.exec_() == QtWidgets.QMessageBox.StandardButton.Yes:
                ScriptObj(self.path).unlink()