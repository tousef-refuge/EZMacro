from threading import Thread
import keyboard

class ListenThread(Thread):
    def __init__(self, window):
        super().__init__(target=lambda: keyboard.wait(), daemon=True)
        self.window = window
        self._previous = None

    def update_keybind(self, keybind):
        self.close()
        self._previous = keyboard.add_hotkey(keybind, self._on_keybind)

    def close(self):
        if self._previous is not None:
            keyboard.remove_all_hotkeys()

    def _on_keybind(self):
        #its a toggle now
        self.window.is_running ^= True