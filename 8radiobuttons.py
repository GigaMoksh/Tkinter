# RADIO BUTTONS :

from tkinter import *
from functools import partial

root = Tk()

r = IntVar()
r.set('2')


def click(value):
    mylabel = Label(root, text=value)
    mylabel.pack()


Radiobutton(root, text='Option 1', variable=r, value=1,
            command=partial(click, r.get())).pack()
Radiobutton(root, text='Option 2', variable=r, value=2,
            command=partial(click, r.get())).pack()

mylabel = Label(root, text=r.get())
mylabel.pack()

root.mainloop()
