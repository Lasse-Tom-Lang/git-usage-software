import PySimpleGUI as sg

backgroundColor = "#323232"
elementColor = "#404040"
textColor = "#FFFFFF"

def mainWindow():
  layout = [
    [
      sg.Column(
        [
          [
            sg.Button(
              "New Repo",
              button_color=(textColor,elementColor),
              key="-NEWREPO-",
              font="Arial 14"
            ),
            sg.Button(
              "Clone Repo",
              button_color=(textColor,elementColor),
              key="-CLONEREPO-",
              font="Arial 14"
            ),
            sg.FolderBrowse(
              "Open Repo",
              button_color=(textColor,elementColor),
              target="-OPENREPO-",
              font="Arial 14"
            ),
          ],
          [
            sg.Text(
              "Changed and new files:",
              expand_x=True,
              background_color=backgroundColor,
              text_color=textColor,
              font="Arial 16"
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
        ],
        background_color=backgroundColor,
        expand_x=True,
        expand_y=True
      ),
      sg.Column(
        [
          [
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
            sg.Text(
              "",
              expand_x=True,
              background_color=backgroundColor,
              text_color=textColor,
              key="-REPONAME-",
              font="Arial 20"
            )
          ],
          [
            sg.Text(
              "Commits:",
              expand_x=True,
              background_color=backgroundColor,
              text_color=textColor,
              font="Arial 16"
            )
          ],
          [
            sg.Listbox(
              [],
              key="-COMMITS-",
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
          ],
          [
            sg.In(
              expand_x=True,
              text_color=textColor,
              key="-EMAILADRESS-",
              border_width=0,
              font="Arial 18",
              background_color=elementColor,
              size=(25, 1),
              change_submits=True
            ),
            sg.Button(
              "Change",
              button_color=(textColor,elementColor),
              key="-CHANGEEMAIL-",
              font="Arial 14",
              expand_x=True,
              disabled=True
            )
          ]
        ],
        background_color=backgroundColor,
        expand_x=True,
        expand_y=True
      )
    ],
    [
      sg.In(
        expand_x=True,
        text_color=textColor,
        key="-COMMITMESSAGE-",
        disabled=True,
        border_width=0,
        font="Arial 18",
        background_color=elementColor,
        disabled_readonly_background_color=elementColor
      ),
      sg.Button(
        "Commit",
        button_color=(textColor,elementColor),
        key="-COMMIT-",
        font="Arial 14",
        disabled=True,
        expand_x=True
      ),
      sg.Button(
        "Push",
        button_color=(textColor,elementColor),
        key="-PUSH-",
        font="Arial 14",
        disabled=True,
        expand_x=True
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

def errorWindow(message):
  return sg.PopupError(
    message,
    background_color=backgroundColor,
    text_color=textColor,
    button_color=(textColor, "red")
  )

def newRepoWindow():
  layout = [
    [
      sg.Text(
        "New Repo",
        font="Arial 22",
        text_color=textColor,
        background_color=backgroundColor
      ),
    ],
    [
      sg.Text(
        "Name:",
        font="Arial 14",
        text_color=textColor,
        background_color=backgroundColor
      ),
      sg.In(
        font="Arial 14",
        text_color=textColor,
        background_color=elementColor,
        key="-REPONAME-",
        border_width=0,
        expand_x=True,
        size=(20, 1)
      )
    ],
    [
      sg.FolderBrowse(
        "Location",
        button_color=(textColor,elementColor),
        target="-LOCATION-",
        font="Arial 14"
      ),
      sg.In(
        expand_x=True,
        text_color=textColor,
        key="-LOCATION-",
        change_submits=True,
        readonly=True,
        border_width=0,
        size=(20, 1),
        font="Arial 14",
        disabled_readonly_background_color=elementColor
      )
    ],
    [
      sg.Button(
        "Create",
        button_color=(textColor,elementColor),
        key="-CREATE-",
        font="Arial 14",
        expand_x=True
      )
    ]
  ]
  return sg.Window(
    "New Repo",
    layout,
    background_color=backgroundColor,
    location=(100, 100),
    element_justification="center"
  )

def cloneRepo():
  layout = [
    [
      sg.Text(
        "Clone Repo",
        font="Arial 22",
        text_color=textColor,
        background_color=backgroundColor
      ),
    ],
    [
      sg.Text(
        "SSH:",
        font="Arial 14",
        text_color=textColor,
        background_color=backgroundColor
      ),
      sg.In(
        font="Arial 14",
        text_color=textColor,
        background_color=elementColor,
        key="-REPOURL-",
        border_width=0,
        expand_x=True,
        size=(20, 1)
      )
    ],
    [
      sg.FolderBrowse(
        "Location",
        button_color=(textColor,elementColor),
        target="-LOCATION-",
        font="Arial 14"
      ),
      sg.In(
        expand_x=True,
        text_color=textColor,
        key="-LOCATION-",
        change_submits=True,
        readonly=True,
        border_width=0,
        size=(20, 1),
        font="Arial 14",
        disabled_readonly_background_color=elementColor
      )
    ],
    [
      sg.Button(
        "Create",
        button_color=(textColor,elementColor),
        key="-CREATE-",
        font="Arial 14",
        expand_x=True
      )
    ]
  ]
  return sg.Window(
    "Clone Repo",
    layout,
    background_color=backgroundColor,
    location=(100, 100),
    element_justification="center"
  )