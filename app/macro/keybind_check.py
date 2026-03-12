from PySide6 import QtWidgets, QtCore

import time

class KeybindCheck(QtCore.QTimer):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.timeout.connect(self.run_script)

    def run_script(self):
        if not self.window.is_running:
            self.window.overlay.hide()
            return

        self.window.overlay.show()
        QtWidgets.QApplication.processEvents()

        time.sleep(1) #temp
        self.window.is_running = False