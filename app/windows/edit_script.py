from PySide6 import QtCore, QtGui, QtWidgets

from app.scripts import ScriptObj
from app.ui.instruction_list import InstructionList
from app.ui.overlay import Overlay

class EditScript(QtWidgets.QDialog):
    def __init__(self, path):
        super().__init__()
        self.setWindowTitle("Edit Script")
        self.script_obj = ScriptObj(path)
        self.is_running = False

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_options()
        self._build_buttons()

        self.adjustSize()
        self.setFixedSize(self.size())

        self.overlay = Overlay(self, "Running script...")

    def _build_options(self):
        frame = QtWidgets.QFrame(frameShape=QtWidgets.QFrame.Shape.StyledPanel)
        frame_layout = QtWidgets.QFormLayout(frame)
        frame_layout.setSpacing(4)

        self.name = QtWidgets.QLineEdit()
        self.name.setText(self.script_obj.name)
        self.name.editingFinished.connect(
            lambda: self.script_obj.write("name", self.name.text())
        )
        frame_layout.addRow("Script Name:", self.name)

        self.keybind = QtWidgets.QKeySequenceEdit()
        self.keybind.setKeySequence(self.script_obj.keybind)
        self.keybind.editingFinished.connect(self._edit_shortcut)
        frame_layout.addRow("Keybind:", self.keybind)

        self.shortcut = QtGui.QShortcut(self.keybind.keySequence(), self)
        self.shortcut.activated.connect(self.run_script)

        self.repeat = QtWidgets.QComboBox()
        self.repeat.setEditable(False)
        self.repeat.addItems(["Only once", "Until I turn it off"])
        self.repeat.activated.connect(
            lambda: self.script_obj.write("repeat", self.repeat.currentText()[0])
        )
        frame_layout.addRow("Repeat:", self.repeat)

        self.instructions = InstructionList(self.script_obj)
        frame_layout.addRow("Instructions:", self.instructions)

        self.main_layout.addWidget(frame)

    def _build_buttons(self):
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.setSpacing(1)

        self.save_button = QtWidgets.QPushButton("Exit and Save")
        self.save_button.clicked.connect(lambda: self.close())
        button_layout.addWidget(self.save_button)

        self.delete_button = QtWidgets.QPushButton("Delete Script")
        self.delete_button.setStyleSheet("color:red")
        self.delete_button.clicked.connect(self._on_delete)
        button_layout.addWidget(self.delete_button)

        self.main_layout.addLayout(button_layout)

    def _edit_shortcut(self):
        self.script_obj.write("keybind", self.keybind.keySequence().toString())
        self.shortcut.setParent(None)

        self.shortcut = QtGui.QShortcut(self.keybind.keySequence(), self)
        self.shortcut.activated.connect(self.run_script)

    def _on_delete(self):
        delete_dialog = QtWidgets.QMessageBox()
        delete_dialog.setWindowTitle(' ')
        delete_dialog.setText("Are you sure?")
        delete_dialog.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes |
            QtWidgets.QMessageBox.StandardButton.No
        )

        if delete_dialog.exec_() == QtWidgets.QMessageBox.StandardButton.Yes:
            self.script_obj.unlink()
            self.close()

    def run_script(self):
        if self.is_running:
            return

        self.is_running = True
        self.overlay.show()
        QtWidgets.QApplication.processEvents()
        QtCore.QTimer.singleShot(1000, self.finish_script)

    def finish_script(self):
        self.is_running = False
        self.overlay.hide()

    # noinspection PyUnresolvedReferences
    #ignore Enter button
    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            event.ignore()
            return
        super().keyPressEvent(event)