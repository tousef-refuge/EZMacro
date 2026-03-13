from PySide6 import QtCore, QtWidgets

import pyautogui

def get_edit_subscript(instruct):
    match instruct["type"]:
        case "mouse":
            return MouseEdit(instruct)

        case "key":
            return KeyEdit(instruct)

        case "write":
            return WriteEdit(instruct)

        case _:
            raise NameError("Invalid instruction type")

class EditSubscript(QtWidgets.QDialog):
    def __init__(self, instruct):
        super().__init__()
        self.instruct = instruct
        self.setWindowTitle(f"Edit {instruct["type"].capitalize()} Instruction")

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
        self.frame_layout = QtWidgets.QFormLayout(frame)
        self.frame_layout.setSpacing(4)

        #this one is always here
        self.sleep = QtWidgets.QSpinBox()
        self.sleep.setMinimum(1)
        self.sleep.setMaximum(1000000)
        self.sleep.setValue(self.instruct["sleep"])
        self.frame_layout.addRow("Sleep time (in milliseconds)", self.sleep)

        self.main_layout.addWidget(frame)

    def _build_buttons(self):
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.setSpacing(1)

        self.save_button = QtWidgets.QPushButton("Exit and Save")
        self.save_button.clicked.connect(self._on_save)
        button_layout.addWidget(self.save_button)

        self.delete_button = QtWidgets.QPushButton("Delete Instruction")
        self.delete_button.clicked.connect(self._on_delete)
        self.delete_button.setStyleSheet("color:red")
        button_layout.addWidget(self.delete_button)

        self.main_layout.addLayout(button_layout)

    def _on_save(self):
        pass

    def _on_delete(self):
        delete_dialog = QtWidgets.QMessageBox()
        delete_dialog.setWindowTitle(' ')
        delete_dialog.setText("Are you sure?")
        delete_dialog.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes |
            QtWidgets.QMessageBox.StandardButton.No
        )

        if delete_dialog.exec_() == QtWidgets.QMessageBox.StandardButton.Yes:
            self.instruct = {}
            self.accept()

    # noinspection PyUnresolvedReferences
    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            event.ignore()
            return
        super().keyPressEvent(event)

class MouseEdit(EditSubscript):
    def __init__(self, instruct):
        super().__init__(instruct)

    def _build_options(self):
        super()._build_options()
        width, height = pyautogui.size()

        self.hold = QtWidgets.QSpinBox()
        self.hold.setMinimum(1)
        self.hold.setMaximum(1000000)
        self.hold.setValue(self.instruct["hold"])
        self.frame_layout.addRow("Hold time (in milliseconds)", self.hold)

        self.button = QtWidgets.QComboBox()
        self.button.addItems(["Left", "Middle", "Right"])
        self.button.setCurrentText(self.instruct["button"].capitalize())
        self.frame_layout.addRow("Mouse Button", self.button)

        self.x = QtWidgets.QSpinBox()
        self.x.setMinimum(1)
        self.x.setMaximum(width)
        self.x.setValue(self.instruct["x"])
        self.frame_layout.addRow("X position", self.x)

        self.y = QtWidgets.QSpinBox()
        self.y.setMinimum(1)
        self.y.setMaximum(height)
        self.y.setValue(self.instruct["y"])
        self.frame_layout.addRow("Y position", self.y)

    def _on_save(self):
        self.instruct["hold"] = self.hold.value()
        self.instruct["sleep"] = self.sleep.value()
        self.instruct["button"] = self.button.currentText().lower()
        self.instruct["x"] = self.x.value()
        self.instruct["y"] = self.y.value()

        self.accept()

class KeyEdit(EditSubscript):
    def __init__(self, instruct):
        super().__init__(instruct)

    def _build_options(self):
        super()._build_options()
        self.hold = QtWidgets.QSpinBox()
        self.hold.setMinimum(1)
        self.hold.setMaximum(1000000)
        self.hold.setValue(self.instruct["hold"])
        self.frame_layout.addRow("Hold time (in milliseconds)", self.hold)

        self.key = QtWidgets.QKeySequenceEdit()
        self.key.keySequenceChanged.connect(self._keyseq_limit)
        self.key.setKeySequence(self.instruct["key"])
        self.frame_layout.addRow("Key pressed", self.key)

    def _on_save(self):
        self.instruct["hold"] = self.hold.value()
        self.instruct["sleep"] = self.sleep.value()
        self.instruct["key"] = self.key.keySequence().toString()

        self.accept()

    def _keyseq_limit(self, seq):
        if seq.count() > 1:
            self.key.setKeySequence(seq[0])

class WriteEdit(EditSubscript):
    def __init__(self, instruct):
        super().__init__(instruct)

    def _build_options(self):
        super()._build_options()

        self.line = QtWidgets.QLineEdit()
        self.line.setText(self.instruct["line"])
        self.frame_layout.addRow("Sentence", self.line)

    def _on_save(self):
        self.instruct["sleep"] = self.sleep.value()
        self.instruct["line"] = self.line.text()

        self.accept()
