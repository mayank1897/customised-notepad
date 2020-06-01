import cx_Freeze
import sys
import os

base=None

if (sys.platform=="win32"):
    base="win32GUI"

os.environ["TCL_LIBRARY"]=r"C:\Users\mayank\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ["TK_LIBRARY"]=r"C:\Users\mayank\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"

executables=[cx_Freeze.Executable("notepad.py",base=base,icon="icon.ico")]

cx_Freeze.setup(
    name="My Notepad",
    options={"build_exe":{"packages":["tkinter","os"],"include_files":["icon.ico","tcl86t.dll","tk86t.dll","icons"]}},
    version="0.01",
    description="Tkinter Application",
    executables=executables
)