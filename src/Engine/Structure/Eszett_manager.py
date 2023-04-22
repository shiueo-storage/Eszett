import json
import os


class ESZETT_ENGINE_MANAGER:
    def __init__(self):
        self.PROJECT_PATH = None
        self.PROJECT_NAME = None
        self.PROJECT_DEV_NAME = None

        self.WINDOW_WIDTH = None
        self.WINDOW_HEIGHT = None
        self.WINDOW_FULLSCREEN = None
        self.WINDOW_TITLE = None
        self.WINDOW_MONITOR = None
        self.WINDOW_SHARE = None
        self.WINDOW_ICON_PATH = None

        self.BUILD_MAIN_FILE = None

    def save(
        self,
        PROJECT_PATH,
        PROJECT_NAME,
        PROJECT_DEV_NAME,
        WINDOW_WIDTH,
        WINDOW_HEIGHT,
        WINDOW_FULLSCREEN,
        WINDOW_TITLE,
        WINDOW_MONITOR,
        WINDOW_SHARE,
        WINDOW_ICON_PATH,
        BUILD_MAIN_FILE,
    ):
        self.PROJECT_PATH = PROJECT_PATH
        self.PROJECT_NAME = PROJECT_NAME
        self.PROJECT_DEV_NAME = PROJECT_DEV_NAME

        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.WINDOW_FULLSCREEN = WINDOW_FULLSCREEN
        self.WINDOW_TITLE = WINDOW_TITLE
        self.WINDOW_MONITOR = WINDOW_MONITOR
        self.WINDOW_SHARE = WINDOW_SHARE
        self.WINDOW_ICON_PATH = WINDOW_ICON_PATH

        self.BUILD_MAIN_FILE = BUILD_MAIN_FILE

    def save_to_file(self):
        save_dict = {
            "PROJECT_PATH": self.PROJECT_PATH,
            "PROJECT_NAME": self.PROJECT_NAME,
            "PROJECT_DEV_NAME": self.PROJECT_DEV_NAME,
            "WINDOW_WIDTH": self.WINDOW_WIDTH,
            "WINDOW_HEIGHT": self.WINDOW_HEIGHT,
            "WINDOW_FULLSCREEN": self.WINDOW_FULLSCREEN,
            "WINDOW_TITLE": self.WINDOW_TITLE,
            "WINDOW_MONITOR": self.WINDOW_MONITOR,
            "WINDOW_SHARE": self.WINDOW_SHARE,
            "WINDOW_ICON_PATH": self.WINDOW_ICON_PATH,
            "BUILD_MAIN_FILE": self.BUILD_MAIN_FILE,
        }

        with open(
            f"{os.path.join(self.PROJECT_PATH, self.PROJECT_NAME)}.eszett", "w"
        ) as save_file:
            json.dump(save_dict, save_file)

    def load_from_file(self, PATH):
        with open(PATH, "r") as load_file:
            obj = json.load(load_file)

        self.PROJECT_PATH = str(obj["PROJECT_PATH"])
        self.PROJECT_NAME = str(obj["PROJECT_NAME"])
        self.PROJECT_DEV_NAME = str(obj["PROJECT_DEV_NAME"])
        self.WINDOW_WIDTH = int(obj["WINDOW_WIDTH"])
        self.WINDOW_HEIGHT = int(obj["WINDOW_HEIGHT"])

        if str(obj["WINDOW_FULLSCREEN"]).lower() == "true":
            self.WINDOW_FULLSCREEN = True
        else:
            self.WINDOW_FULLSCREEN = False

        self.WINDOW_TITLE = str(obj["WINDOW_TITLE"])

        if str(obj["WINDOW_MONITOR"]).lower() == "none":
            self.WINDOW_MONITOR = None
        else:
            pass

        if str(obj["WINDOW_SHARE"]).lower() == "none":
            self.WINDOW_SHARE = None
        else:
            pass

        if str(obj["WINDOW_ICON_PATH"]).lower() == "none":
            self.WINDOW_ICON_PATH = None
        else:
            pass

        self.BUILD_MAIN_FILE = str(obj["BUILD_MAIN_FILE"])

    def RETURN_PROJECT_PATH(self):
        return self.PROJECT_PATH

    def RETURN_PROJECT_NAME(self):
        return self.PROJECT_NAME

    def RETURN_PROJECT_DEV_NAME(self):
        return self.PROJECT_DEV_NAME

    def RETURN_WINDOW_WIDTH(self):
        return self.WINDOW_WIDTH

    def RETURN_WINDOW_HEIGHT(self):
        return self.WINDOW_HEIGHT

    def RETURN_WINDOW_FULLSCREEN(self):
        return self.WINDOW_FULLSCREEN

    def RETURN_WINDOW_TITLE(self):
        return self.WINDOW_TITLE

    def RETURN_WINDOW_MONITOR(self):
        return self.WINDOW_MONITOR

    def RETURN_WINDOW_SHARE(self):
        return self.WINDOW_SHARE

    def RETURN_WINDOW_ICON_PATH(self):
        return self.WINDOW_ICON_PATH

    def RETURN_BUILD_MAIN_FILE(self):
        return self.BUILD_MAIN_FILE
