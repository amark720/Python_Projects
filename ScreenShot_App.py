import time
import pyautogui
import tkinter as tk


def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/gsc-30431/PycharmProjects/test1.py/Screenshot_App/{}.png'.format(name)
    # Update the Directory path above where the screenshots will be saved.

    img = pyautogui.screenshot(name)
    img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="Quit",
    command=quit)

close.pack(side=tk.LEFT)

root.mainloop()
