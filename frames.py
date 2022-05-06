from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

l1 = Label(frame,
           text="Player            ",
           font=10)

l2 = Label(frame,
           text="VS             ",
           font="normal 10 bold")

l3 = Label(frame, text="Computer", font=10)

l1.pack()
l2.pack()
l3.pack()

root.mainloop()
