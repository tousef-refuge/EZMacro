from PySide6 import QtCore, QtWidgets

from app.macro import ListenThread, StatusCheck
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

        self.status_check = StatusCheck(self)
        self.status_check.start()

        self.listen_thread = ListenThread(self)
        self.listen_thread.start()

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
        self.name.setText(self.script_obj["name"])
        self.name.editingFinished.connect(
            lambda: self.script_obj.write("name", self.name.text())
        )
        frame_layout.addRow("Script Name:", self.name)

        self.keybind = QtWidgets.QKeySequenceEdit()
        self.keybind.setKeySequence(self.script_obj["keybind"])
        self.keybind.editingFinished.connect(self._on_keybind_edit)
        self._on_keybind_edit() #run it one time for good luck
        frame_layout.addRow("Keybind:", self.keybind)

        self.repeat = QtWidgets.QComboBox()
        self.repeat.setEditable(False)
        self.repeat.addItems(["Only once", "Until I turn it off"])
        self.repeat.setCurrentIndex(self.script_obj["repeat"] == 'U')
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

    #renews the thread but idk if naming it _renew_thread is a good idea
    def _on_keybind_edit(self):
        keybind = self.keybind.keySequence().toString()
        self.script_obj.write("keybind", keybind)
        self.listen_thread.update_keybind(keybind)

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

    # noinspection PyUnresolvedReferences
    #ignore Enter button
    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            event.ignore()
            return
        super().keyPressEvent(event)