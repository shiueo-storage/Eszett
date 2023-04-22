from PySide6 import QtGui
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import *
from utils import global_path


class ESZETT_preferences(QWidget):
    def __init__(self, ESZETT_MANAGER):
        super().__init__(parent=None)
        self.GRID = QGridLayout(parent=None)
        self.UPDATE_TIMER = QTimer()
        self.ESZETT_MANAGER = ESZETT_MANAGER

        self.PREFERENCES_LIST = [
            "PROJECT_PATH",
            "PROJECT_NAME",
            "PROJECT_DEV_NAME",
            "WINDOW_WIDTH",
            "WINDOW_HEIGHT",
            "WINDOW_FULLSCREEN",
            "WINDOW_TITLE",
            "WINDOW_MONITOR",
            "WINDOW_SHARE",
            "WINDOW_ICON_PATH",
            "BUILD_MAIN_FILE",
        ]

        # TABLE
        self.TABLE = QTableWidget()
        self.TABLE.setRowCount(len(self.PREFERENCES_LIST))
        self.TABLE.setColumnCount(2)
        self.TABLE.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TABLE.setEditTriggers(QAbstractItemView.DoubleClicked)

        # APPLY BUTTON
        self.APPLY_BUTTON = QPushButton("Apply")
        self.APPLY_BUTTON.clicked.connect(lambda: self.BUTTON_CLICKED_APPLY_BUTTON())

        # WINDOW SET
        self.setWindowTitle("Preferences")
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

        for preferences_item in range(len(self.PREFERENCES_LIST)):
            self.TABLE.setItem(
                preferences_item,
                0,
                QTableWidgetItem(self.PREFERENCES_LIST[preferences_item]),
            )

        self.TABLE.setItem(
            0, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_PROJECT_PATH()))
        )
        self.TABLE.setItem(
            1, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_PROJECT_NAME()))
        )
        self.TABLE.setItem(
            2, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_PROJECT_DEV_NAME()))
        )
        self.TABLE.setItem(
            3, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_WINDOW_WIDTH()))
        )
        self.TABLE.setItem(
            4, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_WINDOW_HEIGHT()))
        )
        self.TABLE.setItem(
            5, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_WINDOW_FULLSCREEN()))
        )
        self.TABLE.setItem(
            6, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_WINDOW_TITLE()))
        )
        self.TABLE.setItem(
            7, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_WINDOW_MONITOR()))
        )
        self.TABLE.setItem(
            8, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_WINDOW_SHARE()))
        )
        self.TABLE.setItem(
            9, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_WINDOW_ICON_PATH()))
        )
        self.TABLE.setItem(
            10, 1, QTableWidgetItem(str(self.ESZETT_MANAGER.RETURN_BUILD_MAIN_FILE()))
        )

        # GUI
        self.GRID.addWidget(self.TABLE, 0, 0, 1, 1)
        self.GRID.addWidget(self.APPLY_BUTTON, 1, 0, 1, 1)
        self.setLayout(self.GRID)

    def updateUI(self):
        pass

    def BUTTON_CLICKED_APPLY_BUTTON(self):
        self.ESZETT_MANAGER.save(
            PROJECT_PATH=self.TABLE.item(0, 1).text(),
            PROJECT_NAME=self.TABLE.item(1, 1).text(),
            PROJECT_DEV_NAME=self.TABLE.item(2, 1).text(),
            WINDOW_WIDTH=self.TABLE.item(3, 1).text(),
            WINDOW_HEIGHT=self.TABLE.item(4, 1).text(),
            WINDOW_FULLSCREEN=self.TABLE.item(5, 1).text(),
            WINDOW_TITLE=self.TABLE.item(6, 1).text(),
            WINDOW_MONITOR=self.TABLE.item(7, 1).text(),
            WINDOW_SHARE=self.TABLE.item(8, 1).text(),
            WINDOW_ICON_PATH=self.TABLE.item(9, 1).text(),
            BUILD_MAIN_FILE=self.TABLE.item(10, 1).text(),
        )
        self.ESZETT_MANAGER.save_to_file()
