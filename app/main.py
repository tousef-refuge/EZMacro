import sys
from app.windows import MainWindow
from PySide6 import QtGui, QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("textures/logo.svg"))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())