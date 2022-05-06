from tkinter import *

# CREATING INPUT FIELDS:

root = Tk()

entry1 = Entry(root, width=50)
# some more functions we can use : fg, bg, borderwidth.
entry1.pack()
# entry1.insert(0, 'enter your name:')
# puts enter your name as default text.


def commad():
    mylabel = Label(root, text=entry1.get())
    # e.get() returns what is inside our input field
    mylabel.pack()


button = Button(root, text="Enter your name", command=commad)
button.pack()

root.mainloop()
