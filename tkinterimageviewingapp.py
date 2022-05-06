from tkinter import *
from PIL import Image, ImageTk
from functools import partial

root = Tk()


def forward(img_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label = Label(root, image=img_list[img_number - 1])
    label.grid(row=0, column=0, columnspan=3)

    button_forward = Button(
        root, text=">>", command=partial(forward, img_number + 1))
    button_back = Button(
        root, text="<<", command=partial(back, img_number - 1))

    if img_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(img_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label = Label(root, image=img_list[img_number - 1])
    label.grid(row=0, column=0, columnspan=3)

    button_forward = Button(
        root, text=">>", command=partial(forward, img_number + 1))
    button_back = Button(
        root, text="<<", command=partial(back, img_number - 1))

    if img_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


my_img1 = ImageTk.PhotoImage(Image.open('python/images/img1.png'))
# my_img2 = ImageTk.PhotoImage(Image.open('images/img2.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('python/images/img3.png'))
my_img3 = ImageTk.PhotoImage(Image.open('python/images/img4.png'))
my_img4 = ImageTk.PhotoImage(Image.open('python/images/img5.png'))

img_list = [my_img1, my_img2, my_img3, my_img4]

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=partial(forward, 2))

label = Label(root, image=my_img1)
label.grid(row=0, column=0, columnspan=3)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
