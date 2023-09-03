from pathlib import Path
import os
import sys
import importlib

sys.path.append("Decompiler2")
from Decompiler2.Falcom.ED85 import scena2py
from Falcom.ED85.Parser.scena_writer_helper import *


def dat2py(filename: str):
    scena2py.main(filename)


def py2dat(filename: str):
    current_dir = Path.cwd()
    filepath = Path(filename)
    new_path = filepath.resolve().parent

    package = str(new_path.relative_to(Path.cwd())).replace("\\", ".")
    os.chdir(new_path)

    if not package or package.startswith("."):
        sys.path.append(".")
        filemodule = importlib.import_module(f"{filepath.name[:-3]}")
    else:
        sys.path.append(new_path)
        filemodule = importlib.import_module(f"{package}.{filepath.name[:-3]}")
    filemodule.main()
    os.chdir(current_dir)
