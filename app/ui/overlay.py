from PySide6 import QtCore, QtWidgets

class Overlay(QtWidgets.QWidget):
    def __init__(self, parent, text):
        super().__init__(parent)

        self.setStyleSheet("background-color: rgba(255,255,255,150);")
        self.setGeometry(parent.rect())
        self.hide()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)

        label = QtWidgets.QLabel(text)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(label)