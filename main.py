import PySimpleGUI as sg
import WindowManager
import git
import os

def main():
  mainWindow = WindowManager.mainWindow()
  while True:
    event, values = mainWindow.read(5000)
    match event:
      case sg.WIN_CLOSED:
        break
      case "-NEWREPO-":
        newRepoWindow = WindowManager.newRepoWindow()
        while True:
          event, values = newRepoWindow.read()
          match event:
            case sg.WIN_CLOSED:
              break
            case "-CREATE-":
              if values["-REPONAME-"] != "" and values["-LOCATION-"] != "":
                try:
                  repo = git.Repo.init(f"{values['-LOCATION-']}/{values['-REPONAME-']}")
                  repo.index.commit('Initial commit.')
                  mainWindow["-OPENREPO-"].update(f"{values['-LOCATION-']}/{values['-REPONAME-']}")
                  mainWindow["-REPONAME-"].update(values['-REPONAME-'])
                  break
                except:
                  WindowManager.errorWindow("Couldn't create repo.")
        newRepoWindow.close()
      case "-OPENREPO-":
        try:
          repo = git.Repo(values["-OPENREPO-"])
          mainWindow["-REPONAME-"].update(values["-OPENREPO-"].split("/")[-1])
        except:
          WindowManager.errorWindow("Can't open repo.")
          mainWindow["-OPENREPO-"].update("")
  mainWindow.close()

if __name__ == "__main__":
  global repo
  main()