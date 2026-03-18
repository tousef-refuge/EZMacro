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
            repeat = subscript["repeat"]
            while repeat > 0:
                match subscript["type"]:
                    case "key":
                        keyboard.press(subscript["key"])
                        QtCore.QThread.msleep(subscript["hold"])
                        keyboard.release(subscript["key"])

                    case "mouse":
                        button = subscript["button"]
                        mouse.move(subscript["x"], subscript["y"])
                        mouse.press(button=button)
                        QtCore.QThread.msleep(subscript["hold"]) #im sorry.
                        mouse.release(button=button)

                    case "write":
                        keyboard.write(subscript["line"])
                QtCore.QThread.msleep(subscript["sleep"])
                repeat -= 1
