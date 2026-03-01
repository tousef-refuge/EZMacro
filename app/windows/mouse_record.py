from PySide6 import QtCore, QtWidgets

# noinspection PyUnresolvedReferences
class MouseRecord(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' ')

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        info_label = QtWidgets.QLabel("Your next mouse click will\nbe recorded and stored.")
        self.main_layout.addWidget(info_label)

        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.adjustSize()
        self.setFixedSize(self.size())