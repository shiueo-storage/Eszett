from PySide6 import QtGui
from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import *
from utils import global_path
from src.GUI import Eszett_preferences
from src.GUI import Eszett_build_settings


class ESZETT_GUI(QMainWindow):
    def __init__(self, ESZETT_MANAGER):
        super().__init__(parent=None)
        self.GRID = QGridLayout(parent=None)
        self.UPDATE_TIMER = QTimer()
        self.ESZETT_MANAGER = ESZETT_MANAGER

        # MENU BAR
        self.MENUBAR = self.menuBar()
        self.MENUBAR_FILE = self.MENUBAR.addMenu("&File")
        self.MENUBAR_EDIT = self.MENUBAR.addMenu("&Edit")
        self.MENUBAR_BUILD = self.MENUBAR.addMenu("&Build")

        # ACTION
        ### EXIT
        self.MENUBAR_FILE_EXIT_ACTION = QAction(
            QIcon(global_path.get_proj_abs_path("assets/ionicons/exit.svg")), "Exit"
        )
        self.MENUBAR_FILE_EXIT_ACTION.triggered.connect(lambda: self.close())
        self.MENUBAR_FILE.addAction(self.MENUBAR_FILE_EXIT_ACTION)

        ### SETTINGS
        self.MENUBAR_EDIT_PREFERENCES_ACTION = QAction(
            QIcon(global_path.get_proj_abs_path("assets/ionicons/settings.svg")),
            "Preferences",
        )
        self.MENUBAR_EDIT_PREFERENCES_ACTION.triggered.connect(
            lambda: self.ACTION_ACTIVATED_MENUBAR_EDIT_PREFERENCES_ACTION()
        )
        self.MENUBAR_EDIT.addAction(self.MENUBAR_EDIT_PREFERENCES_ACTION)

        ### BUILD
        self.MENUBAR_BUILD_ACTION = QAction(
            QIcon(global_path.get_proj_abs_path("assets/ionicons/build.svg")),
            "Build",
        )
        self.MENUBAR_BUILD_ACTION.triggered.connect(
            lambda: self.ACTION_ACTIVATED_MENUBAR_BUILD_ACTION()
        )
        self.MENUBAR_BUILD.addAction(self.MENUBAR_BUILD_ACTION)

        ### BUILD SETTINGS
        self.MENUBAR_BUILD_SETTINGS_ACTION = QAction(
            QIcon(global_path.get_proj_abs_path("assets/ionicons/settings.svg")),
            "Build settings",
        )
        self.MENUBAR_BUILD_SETTINGS_ACTION.triggered.connect(
            lambda: self.ACTION_ACTIVATED_MENUBAR_BUILD_SETTINGS_ACTION()
        )
        self.MENUBAR_BUILD.addAction(self.MENUBAR_BUILD_SETTINGS_ACTION)

        # WINDOW SET
        self.setWindowTitle(
            f"ESZETT - {ESZETT_MANAGER.RETURN_PROJECT_DEV_NAME()} - {ESZETT_MANAGER.RETURN_PROJECT_NAME()}"
        )
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

    def ACTION_ACTIVATED_MENUBAR_EDIT_PREFERENCES_ACTION(self):
        ESZETT_PREFERENCES = Eszett_preferences.ESZETT_preferences(
            ESZETT_MANAGER=self.ESZETT_MANAGER
        )
        ESZETT_PREFERENCES.showMaximized()

    def ACTION_ACTIVATED_MENUBAR_BUILD_ACTION(self):
        pass

    def ACTION_ACTIVATED_MENUBAR_BUILD_SETTINGS_ACTION(self):
        ESZETT_BUILD_SETTINGS = Eszett_build_settings.ESZETT_build_settings(
            ESZETT_MANAGER=self.ESZETT_MANAGER
        )
        ESZETT_BUILD_SETTINGS.showMaximized()
