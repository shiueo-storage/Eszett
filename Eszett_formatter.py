import os

from tools import clear


PATH = os.path.dirname(__file__)
clear.code_format_and_make_requirements_txt(path=PATH)
