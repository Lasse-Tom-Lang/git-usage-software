import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import subprocess, os


def main():
  def openProject():
    global selectedProject
    home = Path.home()
    selectedProject = filedialog.askdirectory(title="Choose project", initialdir=home)
    if (selectedProject != ""):
      os.chdir(selectedProject)
      result = subprocess.run(['git', 'status'], capture_output=True, text=True)
      if result.returncode == 0:
        selectedProjectLabel.config(text=f'{selectedProject} opened')
      else:
        selectedProjectLabel.config(text=f'{selectedProject} opened, not a git project')


  selectedProject = ""
  

  window = tk.Tk()
  window.geometry("700x500")
  selectedProjectLabel = tk.Label(text="No project selected")
  projectSelectionButton = tk.Button(text="Open project", command=openProject)
  selectedProjectLabel.pack(side="left", anchor='n', padx=5, pady=5)
  projectSelectionButton.pack(side="right", anchor='n', padx=5, pady=5)
  window.mainloop()


if __name__ == "__main__":
  main()