from tkinter import *
from PIL import Image, ImageTk
from functools import partial

root = Tk()

# STATUS BARS:


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
    status = Label(
        root, text=f'Image {img_number} of {len(img_list)}', bd=1, relief=SUNKEN, anchor=E)

    if img_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


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
    status = Label(
        root, text=f'Image {img_number} of {len(img_list)}', bd=1, relief=SUNKEN, anchor=E)

    if img_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


my_img1 = ImageTk.PhotoImage(Image.open('images/img1.png'))
# my_img2 = ImageTk.PhotoImage(Image.open('images/img2.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/img3.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/img4.png'))
my_img4 = ImageTk.PhotoImage(Image.open('images/img5.png'))

img_list = [my_img1, my_img2, my_img3, my_img4]

status = Label(
    root, text=f'Image 1 of {len(img_list)}', bd=2, relief=SUNKEN, anchor=E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=partial(forward, 2))

label = Label(root, image=my_img1)
label.grid(row=0, column=0, columnspan=3)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
