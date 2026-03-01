from PySide6 import QtWidgets

from app.scripts import ScriptObj

class EditScript(QtWidgets.QDialog):
    def __init__(self, path):
        super().__init__()
        self.setWindowTitle("Edit Script")

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self.adjustSize()
        self.setFixedSize(self.size())

        self.script = ScriptObj(path)