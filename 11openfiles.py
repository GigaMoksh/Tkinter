from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# OPEN FILES DIALOG BOX

root = Tk()
root.title('Image Viewer')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="C:\\Users\\Dell_Owner\\Desktop\\MY DOCUMENTS\\python\\images", title="Select A File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()


root.mainloop()
