from PySide6 import QtWidgets

import pyautogui

class EditSubscript(QtWidgets.QDialog):
    def __init__(self, instruct, idx):
        super().__init__()
        self.instruct = instruct
        self.idx = idx
        self.setWindowTitle(f"Edit {instruct["type"].capitalize()} Instruction")

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_options()
        self._build_buttons()

        self.adjustSize()
        self.setFixedSize(self.size())

    def _build_options(self):
        frame = QtWidgets.QFrame(frameShape=QtWidgets.QFrame.Shape.StyledPanel)
        frame_layout = QtWidgets.QFormLayout(frame)
        frame_layout.setSpacing(4)

        #these are always here
        self.hold = QtWidgets.QSpinBox()
        self.hold.setMinimum(1)
        self.hold.setMaximum(1000000)
        self.hold.setValue(self.instruct["hold"])
        frame_layout.addRow("Hold time (in milliseconds)", self.hold)

        self.delay = QtWidgets.QSpinBox()
        self.delay.setMinimum(1)
        self.delay.setMaximum(1000000)
        self.delay.setValue(self.instruct["delay"])
        frame_layout.addRow("Delay time (in milliseconds)", self.delay)

        #lowkey depends on the type
        self.x = None
        self.y = None
        self.key = None

        if self.instruct["type"] == "mouse":
            width, height = pyautogui.size()

            self.x = QtWidgets.QSpinBox()
            self.x.setMinimum(1)
            self.x.setMaximum(width)
            self.x.setValue(self.instruct["x"])
            frame_layout.addRow("X position", self.x)

            self.y = QtWidgets.QSpinBox()
            self.y.setMinimum(1)
            self.y.setMaximum(height)
            self.y.setValue(self.instruct["y"])
            frame_layout.addRow("Y position", self.y)

        else:
            self.key = QtWidgets.QKeySequenceEdit()
            self.key.keySequenceChanged.connect(self._keyseq_limit)
            self.key.setKeySequence(self.instruct["key"])
            frame_layout.addRow("Key pressed", self.key)

        self.main_layout.addWidget(frame)

    def _build_buttons(self):
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.setSpacing(1)

        self.save_button = QtWidgets.QPushButton("Exit and Save")
        button_layout.addWidget(self.save_button)

        self.delete_button = QtWidgets.QPushButton("Delete Instruction")
        self.delete_button.setStyleSheet("color:red")
        button_layout.addWidget(self.delete_button)

        self.main_layout.addLayout(button_layout)

    def _keyseq_limit(self, seq):
        if seq.count() > 1:
            self.key.setKeySequence(seq[0])