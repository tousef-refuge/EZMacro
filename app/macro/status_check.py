from PySide6 import QtCore
from .macro_worker import MacroWorker

class StatusCheck(QtCore.QTimer):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.setInterval(50)
        self.timeout.connect(self._check)

        self.thread = QtCore.QThread()
        self.worker = MacroWorker(window)
        self.worker.moveToThread(self.thread)
        self.thread.start()

    def close(self):
        self.thread.quit()
        self.thread.wait()

    def _check(self):
        if self.window.is_running:
            self.worker.trigger.emit()