from PySide6 import QtCore, QtWidgets

import pyautogui

# noinspection PyUnresolvedReferences
class MouseRecord(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' ')

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        info_label = QtWidgets.QLabel("Your next mouse position will be recorded\nand stored once you press ENTER.")
        self.main_layout.addWidget(info_label)

        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.adjustSize()
        self.setFixedSize(self.size())

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            pos = pyautogui.position() #stored mouse pos
            self.accept()