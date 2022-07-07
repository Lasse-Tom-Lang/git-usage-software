import re
import PySimpleGUI as sg

backgroundColor = "#323232"
elementColor = "#404040"
textColor = "#FFFFFF"

def mainWindow():
  layout = [
    [
      sg.Button(
        "New Repo",
        button_color=(textColor,elementColor),
        key="-NEWREPO-",
        font="Arial 14"
      ),
      sg.FolderBrowse(
        "Open Repo",
        button_color=(textColor,elementColor),
        target="-OPENREPO-",
        font="Arial 14"
      ),
      sg.In(
        expand_x=True,
        text_color=textColor,
        key="-OPENREPO-",
        change_submits=True,
        readonly=True,
        border_width=0,
        size=(10, 1),
        font="Arial 18",
        disabled_readonly_background_color=elementColor
      )
    ],
    [
      sg.Listbox(
        [],
        key="-REPOFILES-",
        expand_x=True,
        expand_y=True,
        background_color=elementColor,
        text_color=textColor,
        sbar_arrow_color=textColor,
        sbar_background_color=backgroundColor,
        enable_events=True,
        font="Arial 14",
        size=(40, 10)
      )
    ]
  ]
  return sg.Window(
    "Git Manager",
    layout,
    background_color=backgroundColor,
    resizable=True,
    location=(100, 100)
  )