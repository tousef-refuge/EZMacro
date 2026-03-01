from PySide6 import QtWidgets

from app.scripts import ScriptObj

class EditScript(QtWidgets.QDialog):
    def __init__(self, path):
        super().__init__()
        self.setWindowTitle("Edit Script")
        self.script = ScriptObj(path)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_options()
        self._build_buttons()

        self.adjustSize()
        self.setFixedSize(self.size())

    def _build_options(self):
        frame = QtWidgets.QFrame(frameShape=QtWidgets.QFrame.Shape.StyledPanel)
        frame_layout = QtWidgets.QFormLayout(frame)
        frame_layout.setSpacing(4)

        self.name = QtWidgets.QLineEdit()
        self.name.setText(self.script.name)
        frame_layout.addRow("Script Name:", self.name)

        self.keybind = QtWidgets.QKeySequenceEdit()
        self.keybind.setKeySequence(self.script.keybind)
        frame_layout.addRow("Keybind:", self.keybind)

        self.main_layout.addWidget(frame)

    def _build_buttons(self):
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.setSpacing(1)

        self.run_button = QtWidgets.QPushButton("Run Script")
        self.run_button.clicked.connect(self._on_run)
        button_layout.addWidget(self.run_button)

        self.save_button = QtWidgets.QPushButton("Save Changes")
        self.save_button.clicked.connect(self._on_save)
        button_layout.addWidget(self.save_button)

        self.delete_button = QtWidgets.QPushButton("Delete Script")
        self.delete_button.setStyleSheet("color:red")
        self.delete_button.clicked.connect(self._on_delete)
        button_layout.addWidget(self.delete_button)

        self.main_layout.addLayout(button_layout)

    def _on_run(self):
        pass

    def _on_save(self):
        self.script.write("name", self.name.text())
        self.script.write("keybind", self.keybind.keySequence().toString())
        self.close()

    def _on_delete(self):
        delete_dialog = QtWidgets.QMessageBox()
        delete_dialog.setWindowTitle("Confirm")
        delete_dialog.setText("Are you sure?")
        delete_dialog.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes |
            QtWidgets.QMessageBox.StandardButton.No
        )

        if delete_dialog.exec_():
            self.script.unlink()
        self.close()