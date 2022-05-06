from tkinter import *

# GRID SYSTEM:

root = Tk()

mylabel1 = Label(root, text='hey, what are you doing?')
mylabel2 = Label(root, text='Hello World')

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)
# Position a widget in the parent widget in a grid.

root.mainloop()

# the window will be just as big as the text.
labex = Label(root, text='hey, what are you doing?')