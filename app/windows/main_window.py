from PySide6 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EZ Macro")

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self._build_title()
        self._build_list()

        self.adjustSize()
        self.setFixedSize(self.size())

    def _build_title(self):
        layout = QtWidgets.QHBoxLayout()
        layout.setSpacing(20)

        logo_pixmap = QtGui.QPixmap("textures/logo.svg").scaled(
            75, 75,
            QtCore.Qt.AspectRatioMode.KeepAspectRatio,
            QtCore.Qt.TransformationMode.SmoothTransformation
        )
        logo = QtWidgets.QLabel()
        logo.setPixmap(logo_pixmap)
        layout.addWidget(logo)

        title = QtWidgets.QLabel("EZ Macro")
        title.setFont(QtGui.QFont("Courier", 25))
        layout.addWidget(title)

        self.main_layout.addLayout(layout)

    def _build_list(self):
        frame = QtWidgets.QFrame(frameShape=QtWidgets.QFrame.Shape.StyledPanel)
        frame_layout = QtWidgets.QVBoxLayout(frame)

        text = QtWidgets.QLabel("List of scripts:")
        frame_layout.addWidget(text)

        self.script_list = QtWidgets.QListWidget()
        self.add_script = QtWidgets.QListWidgetItem("➕ Add Script")
        self.script_list.addItem(self.add_script)

        self.script_list.itemClicked.connect(self._list_button)
        frame_layout.addWidget(self.script_list)
        self.main_layout.addWidget(frame)

    def _list_button(self, item):
        pass
