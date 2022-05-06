from tkinter import *
from PIL import ImageTk, Image

# CREATING NEW WINDOWS

root = Tk()
root.title('Learn To Code')


def open():
    global my_img
    # global is important otherwise the image wont appear.
    top = Toplevel()
    top.title('My Second Window')
    my_img = ImageTk.PhotoImage(Image.open("images/img3.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


button = Button(root, text="Open Second Window", command=open).pack()


mainloop()
