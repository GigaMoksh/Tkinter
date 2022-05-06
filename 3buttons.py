from tkinter import *

# CREATING BUTTONS:


def commad():
    mylabel = Label(root, text='hey, you just pressed the button.')
    mylabel.pack()


root = Tk()
root.geometry("500x500")
# mybutton = Button(root, text='this is a button', command=commad, state=DISABLED)
# the button will be disabled.
mybutton = Button(root, text='this is a button', command=commad)
# more functions for BUTTON : padx, pady, fg, bg.

mybutton.pack()

root.mainloop()
