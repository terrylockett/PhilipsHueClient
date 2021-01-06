import tkinter as tk
from ui.phui_colors import PHColors


class Header:
    def __init__(self, root_widgit):
        print("In header constructor")
        self.frame = tk.LabelFrame(root_widgit, padx=5, pady=5, bd=0, bg=PHColors.header_background)
        self.frame.columnconfigure(2, weight=1)
        self.frame.pack(fill='x', side='top')
        self.buttons = []

        createSettingsButton(self, self.frame)
        createHomeButton(self, self.frame)


def createSettingsButton(self, parent_widgit):
    newButton = createHeaderButton(parent_widgit, 'Settings')
    newButton.grid(row=0, column=0, sticky='w')
    self.buttons.append(newButton)


def createHomeButton(self, parent_widgit):
    newButton = createHeaderButton(parent_widgit, 'Home')
    newButton.grid(row=0, column=2, sticky='e')
    self.buttons.append(newButton)


def setButtonBackground(button, color):
    button['background'] = color


def createHeaderButton(parent, text):
    newButton = tk.Button(parent, text=text, padx=2, pady=2, bd=0,
                          #  command=command_,
                          bg=PHColors.header_background, fg=PHColors.header_button_foreground,
                          highlightcolor=PHColors.heaer_button_press_background,
                          #  activebackground=color_button_press_bg, activeforeground=color_button_press_fg,
                          relief="solid", font=("Segoe", 15)
                          )
    newButton.bind('<Enter>', lambda x: setButtonBackground(
        newButton, PHColors.header_button_hover_background))
    newButton.bind('<Leave>', lambda x: setButtonBackground(
        newButton, PHColors.header_background))
    return newButton
