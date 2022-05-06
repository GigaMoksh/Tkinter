# CHECKBOXES:
from tkinter import *


root = Tk()
root.title('Codemy.com - Learn To Code!')
root.geometry("400x400")


def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Would you like to SuperSize your order? Check Here!",
                variable=var, onvalue="Off", offvalue="On")
c.deselect()
c.pack()


myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()
