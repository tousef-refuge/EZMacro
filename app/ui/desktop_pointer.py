from PySide6 import QtWidgets, QtGui, QtCore

class DesktopPointer(QtWidgets.QWidget):
    def __init__(self):
        self.width = 50
        self.height = 50

        super().__init__()
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint |
            QtCore.Qt.WindowType.Tool
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(self.width, self.height)

        pixmap = QtGui.QPixmap("textures/pointer.svg")
        label = QtWidgets.QLabel(self)
        label.setPixmap(
            pixmap.scaled(self.width, self.height,
                          QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                          QtCore.Qt.TransformationMode.SmoothTransformation
            ))
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def move_to(self, x, y):
        screen = QtWidgets.QApplication.primaryScreen()
        dpr = screen.devicePixelRatio()

        px, py = x - self.width * 0.5, y - self.height * 1.2 #this 1.2 helps trust
        self.move(int(px / dpr), int(py / dpr))
