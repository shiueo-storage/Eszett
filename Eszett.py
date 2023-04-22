import os
import sys

from PySide6 import QtGui
from utils import global_path
from src.GUI import Eszett_GUI
from src.Engine.Structure import Eszett_manager
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import *

global_path.set_proj_abs_path(os.path.abspath(__file__))


class ESZETT(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.GRID = QGridLayout(parent=None)
        self.UPDATE_TIMER = QTimer()

        # PROJECT_NAME
        self.PROJECT_NAME_LAYOUT = QHBoxLayout()
        self.PROJECT_NAME_LINEEDIT = QLineEdit()
        self.PROJECT_NAME_LABEL = QLabel("Project Name:")

        # PROJECT_DEV_NAME
        self.PROJECT_DEV_NAME_LAYOUT = QHBoxLayout()
        self.PROJECT_DEV_NAME_LINEEDIT = QLineEdit()
        self.PROJECT_DEV_NAME_LABEL = QLabel("Dev Name:")

        # PROJECT_LOCATION SELECTION
        self.PROJECT_LOCATION_LAYOUT = QHBoxLayout()
        self.PROJECT_LOCATION_LINEEDIT = QLineEdit()
        self.PROJECT_LOCATION_LABEL = QLabel("Location:")

        # PROJECT_LOCATION DIALOG
        self.PROJECT_LOCATION_FILE_DIALOG = QFileDialog()
        self.PROJECT_LOCATION_FILE_DIALOG_BUTTON = QPushButton("Find Location")
        self.PROJECT_LOCATION_FILE_DIALOG_BUTTON.clicked.connect(
            lambda: self.BUTTON_CLICKED_PROJECT_LOCATION_FILE_DIALOG()
        )

        # APPLY
        self.APPLY_BUTTON = QPushButton("Apply")
        self.APPLY_BUTTON.clicked.connect(lambda: self.BUTTON_CLICKED_APPLY_BUTTON())

        # OPEN_EXISTING_PROJECT_LOCATION SELECTION
        self.OPEN_EXISTING_PROJECT_LAYOUT = QHBoxLayout()
        self.OPEN_EXISTING_PROJECT_LINEEDIT = QLineEdit()
        self.OPEN_EXISTING_PROJECT_LABEL = QLabel("Location:")

        # OPEN_EXISTING_PROJECT_LOCATION DIALOG
        self.OPEN_EXISTING_PROJECT_FILE_DIALOG = QFileDialog()
        self.OPEN_EXISTING_PROJECT_FILE_DIALOG_BUTTON = QPushButton(
            "Open Existing Project"
        )
        self.OPEN_EXISTING_PROJECT_FILE_DIALOG_BUTTON.clicked.connect(
            lambda: self.BUTTON_CLICKED_OPEN_EXISTING_PROJECT_FILE_DIALOG()
        )

        # OTHERS
        self.HLINE = QFrame()
        self.HLINE.setFrameShape(QFrame.HLine)
        self.HLINE.setFrameShadow(QFrame.Sunken)

        self.HLINE_2 = QFrame()
        self.HLINE_2.setFrameShape(QFrame.HLine)
        self.HLINE_2.setFrameShadow(QFrame.Sunken)

        self.setWindowTitle("ESZETT")
        self.setWindowIcon(
            QtGui.QIcon(global_path.get_proj_abs_path("assets/icon.png"))
        )
        self.setMinimumSize(600, 200)
        self.initUI()

    def initUI(self):
        # Update Timer
        self.UPDATE_TIMER.setInterval(1000 / 10)
        self.UPDATE_TIMER.timeout.connect(lambda: self.updateUI())
        self.UPDATE_TIMER.start()

        # PROJECT_NAME
        self.PROJECT_NAME_LAYOUT.addWidget(self.PROJECT_NAME_LABEL)
        self.PROJECT_NAME_LAYOUT.addWidget(self.PROJECT_NAME_LINEEDIT)

        # PROJECT_DEV_NAME
        self.PROJECT_DEV_NAME_LAYOUT.addWidget(self.PROJECT_DEV_NAME_LABEL)
        self.PROJECT_DEV_NAME_LAYOUT.addWidget(self.PROJECT_DEV_NAME_LINEEDIT)

        # PROJECT LOCATION / DIALOG
        self.PROJECT_LOCATION_LAYOUT.addWidget(self.PROJECT_LOCATION_LABEL)
        self.PROJECT_LOCATION_LAYOUT.addWidget(self.PROJECT_LOCATION_LINEEDIT)
        self.PROJECT_LOCATION_LAYOUT.addWidget(self.PROJECT_LOCATION_FILE_DIALOG_BUTTON)

        # OPEN EXISTING PROJECT / DIALOG
        self.OPEN_EXISTING_PROJECT_LAYOUT.addWidget(self.OPEN_EXISTING_PROJECT_LABEL)
        self.OPEN_EXISTING_PROJECT_LAYOUT.addWidget(self.OPEN_EXISTING_PROJECT_LINEEDIT)
        self.OPEN_EXISTING_PROJECT_LAYOUT.addWidget(
            self.OPEN_EXISTING_PROJECT_FILE_DIALOG_BUTTON
        )

        # GUI
        self.GRID.addLayout(self.PROJECT_NAME_LAYOUT, 0, 0, 1, 1)
        self.GRID.addLayout(self.PROJECT_DEV_NAME_LAYOUT, 1, 0, 1, 1)
        self.GRID.addLayout(self.PROJECT_LOCATION_LAYOUT, 2, 0, 1, 1)
        self.GRID.addWidget(self.HLINE, 3, 0, 1, 1)
        self.GRID.addLayout(self.OPEN_EXISTING_PROJECT_LAYOUT, 4, 0, 1, 1)
        self.GRID.addWidget(self.HLINE_2, 5, 0, 1, 1)
        self.GRID.addWidget(self.APPLY_BUTTON, 6, 0, 1, 1)
        self.setLayout(self.GRID)

    def updateUI(self):
        if self.OPEN_EXISTING_PROJECT_LINEEDIT.text():
            self.PROJECT_NAME_LINEEDIT.setEnabled(False)
            self.PROJECT_DEV_NAME_LINEEDIT.setEnabled(False)
            self.PROJECT_LOCATION_LINEEDIT.setEnabled(False)
            self.PROJECT_LOCATION_FILE_DIALOG_BUTTON.setEnabled(False)

        else:
            self.PROJECT_NAME_LINEEDIT.setEnabled(True)
            self.PROJECT_DEV_NAME_LINEEDIT.setEnabled(True)
            self.PROJECT_LOCATION_LINEEDIT.setEnabled(True)
            self.PROJECT_LOCATION_FILE_DIALOG_BUTTON.setEnabled(True)

        if (
            self.PROJECT_NAME_LINEEDIT.text()
            or self.PROJECT_DEV_NAME_LINEEDIT.text()
            or self.PROJECT_LOCATION_LINEEDIT.text()
        ):
            self.OPEN_EXISTING_PROJECT_LINEEDIT.setEnabled(False)
            self.OPEN_EXISTING_PROJECT_FILE_DIALOG_BUTTON.setEnabled(False)

        else:
            self.OPEN_EXISTING_PROJECT_LINEEDIT.setEnabled(True)
            self.OPEN_EXISTING_PROJECT_FILE_DIALOG_BUTTON.setEnabled(True)

        if (
            self.PROJECT_NAME_LINEEDIT.text()
            and self.PROJECT_LOCATION_LINEEDIT.text()
            and self.PROJECT_DEV_NAME_LINEEDIT.text()
            and not self.OPEN_EXISTING_PROJECT_LINEEDIT.text()
        ):
            self.APPLY_BUTTON.setEnabled(True)
        elif (
            not self.PROJECT_NAME_LINEEDIT.text()
            and not self.PROJECT_LOCATION_LINEEDIT.text()
            and not self.PROJECT_DEV_NAME_LINEEDIT.text()
            and self.OPEN_EXISTING_PROJECT_LINEEDIT.text()
        ):
            self.APPLY_BUTTON.setEnabled(True)
        else:
            self.APPLY_BUTTON.setEnabled(False)

    def BUTTON_CLICKED_PROJECT_LOCATION_FILE_DIALOG(self):
        location = self.PROJECT_LOCATION_FILE_DIALOG.getExistingDirectory(
            self, "Select Directory"
        )

        if location:
            self.PROJECT_LOCATION_LINEEDIT.setText(location)

    def BUTTON_CLICKED_OPEN_EXISTING_PROJECT_FILE_DIALOG(self):
        location = self.OPEN_EXISTING_PROJECT_FILE_DIALOG.getOpenFileName(
            self, "Select Project File", filter="*.eszett"
        )
        if location:
            self.OPEN_EXISTING_PROJECT_LINEEDIT.setText(location[0])

    def BUTTON_CLICKED_APPLY_BUTTON(self):
        ESZETT_MANAGER = Eszett_manager.ESZETT_ENGINE_MANAGER()

        if self.OPEN_EXISTING_PROJECT_LINEEDIT.text():
            PROJECT_PATH = self.OPEN_EXISTING_PROJECT_LINEEDIT.text()
            ESZETT_MANAGER.load_from_file(PATH=PROJECT_PATH)

            ESZETT_GUI = Eszett_GUI.ESZETT_GUI(ESZETT_MANAGER=ESZETT_MANAGER)

            ESZETT_GUI.showMaximized()

        else:
            PROJECT_PATH = self.PROJECT_LOCATION_LINEEDIT.text()
            PROJECT_NAME = self.PROJECT_NAME_LINEEDIT.text()
            PROJECT_DEV_NAME = self.PROJECT_DEV_NAME_LINEEDIT.text()
            ESZETT_MANAGER.save(
                PROJECT_PATH=PROJECT_PATH,
                PROJECT_NAME=PROJECT_NAME,
                PROJECT_DEV_NAME=PROJECT_DEV_NAME,
                WINDOW_WIDTH=1280,
                WINDOW_HEIGHT=720,
                WINDOW_FULLSCREEN=False,
                WINDOW_TITLE=PROJECT_NAME,
                WINDOW_MONITOR=None,
                WINDOW_SHARE=None,
                WINDOW_ICON_PATH=None,
                BUILD_MAIN_FILE=None,
            )
            ESZETT_MANAGER.save_to_file()
            ESZETT_GUI = Eszett_GUI.ESZETT_GUI(ESZETT_MANAGER=ESZETT_MANAGER)

            ESZETT_GUI.showMaximized()
        self.close()


if __name__ == "__main__":
    ESZETT_APP = QApplication()
    ESZETT_APP_GUI = ESZETT()
    ESZETT_APP_GUI.show()
    sys.exit(ESZETT_APP.exec())

"""
ESZETT_ENGINE = Eszett_engine.ESZETT_ENGINE_ENGINE(
    width=1280,
    height=720,
    fullscreen=False,
    title="ESZETT_ENGINE",
    monitor=None,
    share=None,
    icon=Image.open(global_path.get_proj_abs_path("assets/icon.png"))
)
ESZETT_ENGINE.close()
"""
