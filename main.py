from tkinter import E
import PySimpleGUI as sg
import WindowManager
import git
import os

def main():
  repo = None
  mainWindow = WindowManager.mainWindow()
  while True:
    event, values = mainWindow.read(5000)
    if repo != None:
      changedFiles = []
      for item in repo.index.diff(None):
        changedFiles.append(item.a_path)
      for elements in repo.untracked_files:
        if elements not in [".DS_Store", ".gitignore"]:
          changedFiles.append(elements)
      mainWindow["-REPOFILES-"].update(changedFiles)
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
      case "-CLONEREPO-":
        cloneWindow = WindowManager.cloneRepo()
        while True:
          event, values = cloneWindow.read()
          match event:
            case sg.WIN_CLOSED:
              break
            case "-CREATE-":
              if values["-REPOURL-"] != "" and values["-LOCATION-"] != "":
                try:
                  repo = git.Repo.clone_from(values["-REPOURL-"], f"{values['-LOCATION-']}/{values['-REPOURL-'].split('/')[-1][0:-4]}")
                  mainWindow["-OPENREPO-"].update(f"{values['-LOCATION-']}/{values['-REPOURL-'].split('/')[-1][0:-4]}")
                  mainWindow["-REPONAME-"].update(values['-REPOURL-'].split('/')[-1][0:-4])
                  break
                except:
                  WindowManager.errorWindow("Can't clone repo.")
        cloneWindow.close()
  mainWindow.close()

if __name__ == "__main__":
  main()