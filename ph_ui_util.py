import tkinter as tk
from ph_util import getLightsInfo
from ph_util import getGroupsInfo
from ph_util import toggleLight
from ph_util import toggleGroup

color_bg = '#151515'
color_header_bg = '#242424'

color_button_fg = '#ffffff'
color_button_hover_bg = '#404040'
color_button_press_bg = '#323232'
color_button_press_fg = '#eeeeee'

color_tile_bg = color_header_bg
color_tile_bg_enabled = '#cccccc'
color_tile_fg = color_button_fg
color_tile_fg_enabled = '#111111'
tile_height = 5


def getChildren(widget):
    list = widget.winfo_children()
    for item in list:
        if item.winfo_children():
            list.extend(item.winfo_children())
    return list


def setTileBg(label_frame, color, recursive):
    label_frame['background'] = color
    if(recursive):
        for child in getChildren(label_frame):
            child['background'] = color


def addSettingTiles(parent_widget):
    for child in getChildren(parent_widget):
        child.destroy()


def addGroupTiles(parent_widget):
    for child in getChildren(parent_widget):
        child.destroy()
    groups = getGroupsInfo()
    for id in groups.keys():
        makeGroupTile(parent_widget, groups[id]["name"], id, groups[id]["lights"])


def showLights(parent_widget, lightList):
    for child in getChildren(parent_widget):
        child.destroy()
    lights = getLightsInfo()
    for id in lights.keys():
        if(id in lightList):
            makeTile(parent_widget, lights[id]["name"], id, {}, lights[id]['state']['on'])


def toggleButtonPress(widgit_main, widgit_toggle, id):
    if(widgit_main["bg"] == color_tile_bg_enabled):
        toggleLight(id, False)
        widgit_main["bg"] = color_tile_bg
        widgit_main["fg"] = color_tile_fg
        widgit_toggle['text'] = 'Turn On'
        widgit_main.bind('<Enter>', lambda x: setTileBg(widgit_main, color_button_hover_bg, True))
        widgit_main.bind('<Leave>', lambda x: setTileBg(widgit_main, color_tile_bg, True))
    else:
        toggleLight(id, True)
        widgit_main['bg'] = color_tile_bg_enabled
        widgit_main['fg'] = color_tile_fg_enabled
        widgit_toggle['text'] = 'Turn Off'
        widgit_main.bind('<Enter>', lambda x: setTileBg(widgit_main, color_button_hover_bg, True))
        widgit_main.bind('<Leave>', lambda x: setTileBg(widgit_main, color_tile_bg_enabled, True))


def makeTile(parent_widget, labelText, id, list, is_enabled):
    temp_bg_color = color_tile_bg
    temp_fg_color = color_tile_fg
    if(is_enabled):
        temp_bg_color = color_tile_bg_enabled
        temp_fg_color = color_tile_fg_enabled

    # Frame
    frame = tk.LabelFrame(parent_widget, height=40, bg=color_bg, pady=1,
                          borderwidth=5, relief='flat')
    frame.grid(row=id, column=0, sticky='ew')
    frame.columnconfigure(0, weight=1)

    # main buttn
    main_button = tk.Button(frame, text=labelText, height=tile_height,
                            command=lambda: showLights(parent_widget, list),
                            bg=temp_bg_color, fg=temp_fg_color, activebackground='green', relief='flat')
    main_button.grid(row=0, column=0, sticky='ew')
    main_button.bind('<Enter>', lambda x: setTileBg(main_button, color_button_hover_bg, True))
    main_button.bind('<Leave>', lambda x: setTileBg(main_button, temp_bg_color, True))

    # toggle
    toggle_button = tk.Button(frame, text='Turn Off', height=tile_height,
                              command=lambda: toggleButtonPress(main_button, toggle_button, id),
                              bg=color_tile_bg, fg=color_tile_fg)
    toggle_button.grid(row=0, column=1)
    toggle_button.bind('<Enter>', lambda x: setTileBg(toggle_button, color_button_hover_bg, True))
    toggle_button.bind('<Leave>', lambda x: setTileBg(toggle_button, color_tile_bg, True))

    # slider
    tile_slider = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=0, width=20)
    tile_slider.grid(row=1, column=0, columnspan=2, sticky='we')

    return frame


def createHeaderButton(parent, text, command_):
    newButton = tk.Button(parent, text=text, padx=2, pady=2, bd=0, command=command_,
                          bg=color_header_bg, fg=color_button_fg, highlightcolor=color_button_press_bg,
                          activebackground=color_button_press_bg, activeforeground=color_button_press_fg,
                          relief="solid", font=("Segoe", 15))
    newButton.bind('<Enter>', lambda x: setTileBg(newButton, color_button_hover_bg, False))
    newButton.bind('<Leave>', lambda x: setTileBg(newButton, color_header_bg, False))
    return newButton


def makeGroupTile(parent_widget, labelText, row_, lightList):
    makeTile(parent_widget, labelText, row_, lightList, False)
