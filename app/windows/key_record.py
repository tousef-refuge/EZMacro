from PySide6 import QtCore, QtGui, QtWidgets

class KeyRecord(QtWidgets.QDialog):
    # noinspection PyUnresolvedReferences
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' ')
        self.sequence = None

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        info_label = QtWidgets.QLabel("Your next keyboard press will\nbe recorded and stored.")
        self.main_layout.addWidget(info_label)

        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.adjustSize()
        self.setFixedSize(self.size())

    def keyPressEvent(self, event):
        self.sequence = QtGui.QKeySequence(event.key()) #stored key sequence
        self.accept()