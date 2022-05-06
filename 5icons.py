from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Adding Icons, Images and Exit buttons...

root.iconbitmap('custom.ico')
# changing the icon of our window

root.title('window')
# changing the title of the window

button_quit = Button(root, text="Exit Program", command=root.quit).pack()
# adding a exit button to our program

my_img = ImageTk.PhotoImage(Image.open('Dell.jpg'))
label = Label(root, image=my_img).pack()
# this is a 3 step process. We define the image then we put the image into something
# else and then we put that something else on the screen.

root.mainloop()
