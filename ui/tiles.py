import tkinter as tk
from ui.phui_colors import PHColors
from util.ph_util import getLightsInfo
from util.ph_util import getGroupsInfo
from util.ph_util import toggleLightOn
from util.ph_util import toggleGroupOn

tile_height = 5


class Tiles:

    def __init__(self, parent_widgit):
        print("In tiles constructor")
        _tiles_frame = tk.LabelFrame(parent_widgit, bg=PHColors.background, bd=0, padx=5, pady=5)
        _tiles_frame.pack(fill="x",  side="top")
        _tiles_frame.columnconfigure(0, weight=1)
        self.tiles_frame = _tiles_frame
        self.tiles = addGroupTiles(self, _tiles_frame)

    def goHome(self):
        self.tiles_frame.clearTiles()
        self.tiles = addGroupTiles(self, self.tiles_frame)

    def goLights(self, light_list):
        self.tiles_frame.clearTiles()
        self.tiles = addLightTiles(self.tiles_frame, light_list)


def toggleLightPressed(id):
    toggleLightOn(id)


def makeToggleLightFunc(id):
    return lambda: toggleLightPressed(id)


def lightTileButtonPressed(parent_widget):
    pass


def makeLightTileFunc(parent_widget):
    return lambda: lightTileButtonPressed(parent_widget)


def addLightTiles(parent_widget, light_list):
    lights = getLightsInfo()
    tiles = []
    print('lights list: ', light_list)
    for id in lights.keys():
        if(id in light_list):
            tiles.append(makeTile(parent_widget, lights[id]["name"], id,
                                  lights[id]['state']['on'], False,
                                  makeLightTileFunc(parent_widget), makeToggleLightFunc(id)))
    return tiles


def toggleGroupPressed(id):
    toggleGroupOn(id)


def makeToggleGroupFunc(id):
    return lambda: toggleGroupOn(id)


def groupTileButtonPressed(parent_widget, light_list):
    clearTiles(parent_widget)
    addLightTiles(parent_widget, light_list)


def makeGroupTileFunc(parent_widget, light_list):
    return lambda: groupTileButtonPressed(parent_widget, light_list)


def addGroupTiles(self, parent_widget):
    clearTiles(parent_widget)
    groups = getGroupsInfo()
    tiles = []
    for id in groups.keys():
        print('group light list', groups[id]["lights"])
        tiles.append(makeTile(parent_widget, groups[id]["name"], id,
                              groups[id]['state']['any_on'],
                              True, makeGroupTileFunc(parent_widget, groups[id]["lights"]), makeToggleGroupFunc(id)))
    return tiles


def getChildren(widget):
    list = widget.winfo_children()
    for item in list:
        if item.winfo_children():
            list.extend(item.winfo_children())
    return list


def clearTiles(parent_widget):
    for child in getChildren(parent_widget):
        child.destroy()


def makeTile(parent_widget, labelText, id, is_enabled, is_group, _command, _toggle_command):
    # get tile colors
    temp_bg_color = PHColors.tile_background_off
    temp_fg_color = PHColors.tile_foreground_off
    if(is_enabled):
        temp_bg_color = PHColors.tile_background_on
        temp_fg_color = PHColors.tile_foreground_on

    # make tile Frame
    frame = tk.LabelFrame(parent_widget, height=40, bg=PHColors.background, pady=1,
                          borderwidth=5, relief='flat')
    frame.grid(row=id, column=0, sticky='ew')
    frame.columnconfigure(0, weight=1)

    # main button

    main_button = tk.Button(frame, text=labelText, height=tile_height,
                            command=_command,
                            bg=temp_bg_color, fg=temp_fg_color, relief='flat',
                            )
    main_button.grid(row=0, column=0, sticky='ew')
    # main_button.bind('<Enter>', lambda x: setTileBg(main_button, color_button_hover_bg, True))
    # main_button.bind('<Leave>', lambda x: setTileBg(main_button, temp_bg_color, True))

    # toggle button
    toggle_button = tk.Button(frame, text='Turn On', height=tile_height,
                              command=_toggle_command,
                              bg=PHColors.tile_background_off, fg=PHColors.tile_foreground_off)
    toggle_button.grid(row=0, column=1)
    # toggle_button.bind('<Enter>', lambda x: setTileBg(toggle_button, color_button_hover_bg, True))
    # toggle_button.bind('<Leave>', lambda x: setTileBg(toggle_button, color_tile_bg, True))

    # slider
    tile_slider = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=0, width=20)
    tile_slider.grid(row=1, column=0, columnspan=2, sticky='we')

    return frame
