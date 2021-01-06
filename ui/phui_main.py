from ctypes import windll
from ui.phui_colors import PHColors
from ui.header import Header
import tkinter as tk
import util.configLoader as config


def run():
    # fix blurry windows shit...
    windll.shcore.SetProcessDpiAwareness(1)
    root = tk.Tk()
    root.title(config.getProperty('window_title'))
    root.geometry(config.getProperty('window_size'))
    root.iconbitmap(config.getProperty('window_icon'))
    root["bg"] = PHColors.background

    header = Header(root)

    root.mainloop()
