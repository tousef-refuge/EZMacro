from PySide6 import QtCore

import keyboard
import mouse

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
        script = self.window.script_obj["script"]
        for subscript in script:
            sleep = subscript["sleep"]

            match subscript["type"]:
                case "key":
                    hold = subscript["hold"]
                    keyboard.press(subscript["key"])
                    QtCore.QThread.msleep(hold)
                    keyboard.release(subscript["key"])

                case "mouse":
                    hold = subscript["hold"]
                    mouse.move(subscript["x"], subscript["y"])
                    if hold == 1:
                        mouse.click()  # i mean better safe than sorry
                    else:
                        mouse.press()
                        QtCore.QThread.msleep(hold)
                        mouse.release()

                case "write":
                    keyboard.write(subscript["line"])
            QtCore.QThread.msleep(sleep)
