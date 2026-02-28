import sys
from app.windows import MainWindow
from PySide6 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())