'''
Python | Create a digital clock using Tkinter

As we know Tkinter is used to create a variety of GUI (Graphical User Interface) applications.
In this project I will create a Digital clock using Tkinter.
We'll Use Label widget from Tkinter and time module :
In the following application, we are going to use Label widget and also going to use time module which we will use to retrieve system’s time.
'''

# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Amar\'s Clock')


# This function is used to display time on the label
def time():
    string = strftime('%I:%M:%S %p')
    # To make the clock format 24 hrs. Simply change the strftime('%I:%M:%S %p') to strftime('%H:%M:%S %p').
    lbl.config(text=string)
    lbl.after(1000, time)  # It will update the time after every (1000 milliseconds i.e. after 1 second)


# Styling the label widget so that clock will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')


# Placing clock at the centre of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()
