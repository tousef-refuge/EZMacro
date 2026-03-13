from PySide6 import QtCore, QtGui, QtWidgets

import pyautogui

# noinspection PyUnresolvedReferences
class InputRecord(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' ')

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.adjustSize()
        self.setFixedSize(self.size())

# noinspection PyUnresolvedReferences
class MouseRecord(InputRecord):
    def __init__(self):
        super().__init__()
        info_label = QtWidgets.QLabel("Your next mouse position will be recorded\nand stored once you press ENTER.")
        self.main_layout.addWidget(info_label)
        self.pos = None

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self.pos = pyautogui.position() #stored mouse pos
            self.accept()

class KeyRecord(InputRecord):
    def __init__(self):
        super().__init__()
        info_label = QtWidgets.QLabel("Your next keyboard press will\nbe recorded and stored.")
        self.main_layout.addWidget(info_label)
        self.key = None

    def keyPressEvent(self, event):
        self.key = QtGui.QKeySequence(event.key()) #stored key sequence
        self.accept()

class WriteRecord(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()