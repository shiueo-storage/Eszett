import os

from tools import builder
from utils import global_path

global_path.set_proj_abs_path(os.path.abspath(__file__))

builder.build(
    withconsole=True,
    path=os.path.abspath("Eszett.py"),
    file_dict=["assets"],
    companyname="Cshtarn",
    product_version="0.0.1",
    icon=global_path.get_proj_abs_path("assets/icon.png"),
    plugin_dict=["pyside6"],
    include_package_dict=["PIL"],
)
