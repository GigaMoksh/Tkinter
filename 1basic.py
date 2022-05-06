from tkinter import *

root = Tk()  # creates a new window (the main window)

# to create anything in tkinetr, we have a 2 step process. First we have to define the
# thing and create it and then you have to put it on the screen.

mylabel = Label(root, text='Hello World')
# creates a label widget into the root window

mylabel.pack()
# pack puts it on the screen.
# pack says pack this in just as big as the stuff inside is.
# because of pack the label will stay right in the middle of the window.

root.mainloop()
# creates a event loop. When we have a program running it's always looping constantly
# and that's how it figures out what's going on the screen.
