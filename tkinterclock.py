from tkinter import *
from time import strftime

root = Tk()
root.title('Clock')


def time():
    string = strftime('%I: %M: %S %p')
    # %H for 24 hours time and %I for 12 hours time
    label.config(text=string)
    label.after(1000, time)


label = Label(root, bg='black', fg='cyan', font=('ds-digital', 80))
label.pack()

time()

root.mainloop()
