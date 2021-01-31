from tkinter import *
from frames import *

BACKGROUND_COLOR = "#2e2e2e"

root = Tk()
root.title("Sorting Application")
root.resizable(width=False, height=False)
root.configure(background=BACKGROUND_COLOR)

frame = Frames(root)

root.mainloop()