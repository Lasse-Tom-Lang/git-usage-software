import PySimpleGUI as sg
import WindowManager
import git
import os

def main():
  mainWindow = WindowManager.mainWindow()
  while True:
    event, values = mainWindow.read()
    match event:
      case sg.WIN_CLOSED:
        break
  mainWindow.close()

if __name__ == "__main__":
  main()