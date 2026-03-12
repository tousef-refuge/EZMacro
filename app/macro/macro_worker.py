from PySide6 import QtWidgets, QtCore

import time

#well took you long enough bro
class MacroWorker(QtCore.QObject):
    trigger = QtCore.Signal()

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.running = False
        self.trigger.connect(self.run)

    @QtCore.Slot()
    def run(self):
        if self.running or not self.window.is_running: #extra condition so i lowkey dont start spamming
            return
        self.running = True

        self.window.overlay.show()
        QtWidgets.QApplication.processEvents()

        time.sleep(1)
        print("ts temporary")

        self.window.overlay.hide()
        self.running = False
        self.window.is_running = False
