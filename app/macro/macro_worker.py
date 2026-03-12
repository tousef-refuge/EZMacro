from PySide6 import QtWidgets, QtCore

import time

#well took you long enough bro
class MacroWorker(QtCore.QObject):
    trigger = QtCore.Signal()

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.trigger.connect(self.run)

    @QtCore.Slot()
    def run(self):
        while self.window.is_running:
            self.window.overlay.show()
            self._macro()
            if self.window.script_obj["repeat"] == 'O':
                break
        self.window.overlay.hide()
        self.window.is_running = False

    def _macro(self):
        time.sleep(1)
        print("ts temporary")
