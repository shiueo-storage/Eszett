from PySide6 import QtGui
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import *
from utils import global_path


class ESZETT_build_settings(QWidget):
    def __init__(self, ESZETT_MANAGER):
        super().__init__(parent=None)
        self.GRID = QGridLayout(parent=None)
        self.UPDATE_TIMER = QTimer()
        self.ESZETT_MANAGER = ESZETT_MANAGER

        # WINDOW SET
        self.setWindowTitle("Build Settings")
        self.setMinimumSize(600, 200)
        self.setWindowIcon(
            QtGui.QIcon(global_path.get_proj_abs_path("assets/icon.png"))
        )
        self.initUI()

    def initUI(self):
        # Update Timer
        self.UPDATE_TIMER.setInterval(1000 / 10)
        self.UPDATE_TIMER.timeout.connect(lambda: self.updateUI())
        self.UPDATE_TIMER.start()

        # GUI

        self.setLayout(self.GRID)

    def updateUI(self):
        pass
