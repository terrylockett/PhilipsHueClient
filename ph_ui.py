from ph_util import toggleGroup
from ph_util import toggleLight
from ph_util import getGroupsInfo
from ph_util import getLightsInfo
from ph_ui_util import addSettingTiles
from ph_ui_util import addGroupTiles
import tkinter as tk
from ctypes import windll
from ph_ui_util import setTileBg
from ph_ui_util import makeTile
from ph_ui_util import createHeaderButton


color_bg = '#151515'
color_header_bg = '#242424'
color_button_fg = '#ffffff'
color_button_hover_bg = '#404040'
color_button_press_bg = '#323232'
color_button_press_fg = '#eeeeee'
color_tile_bg = color_header_bg
color_tile_fg = color_button_fg

# fix blurry windows shit...
windll.shcore.SetProcessDpiAwareness(1)
root = tk.Tk()
root.title("Philips Hue")
root.geometry("400x900")
root.iconbitmap("icon.ico")
root["bg"] = color_bg


# Header frame.
headerFrame = tk.LabelFrame(root, padx=5, pady=5, bd=0, bg=color_header_bg)
headerFrame.pack(fill="x",  side="top")
headerFrame.columnconfigure(2, weight=1)
# tiles frame
tiles_frame = tk.LabelFrame(root, bg=color_bg, bd=0, padx=5, pady=5)
tiles_frame.pack(fill="x",  side="top")
tiles_frame.columnconfigure(0, weight=1)

# header buttons
settingsButton = createHeaderButton(headerFrame, 'Settings', lambda: addSettingTiles(tiles_frame))
settingsButton.grid(row=0, column=0, sticky='w')

homeButton = createHeaderButton(headerFrame, 'Home', lambda: addGroupTiles(tiles_frame))
homeButton.grid(row=0, column=2, sticky='ne')


# Default tiles
addGroupTiles(tiles_frame)


root.mainloop()
