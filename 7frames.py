from tkinter import *
# FRAMES:

root = Tk()

frame = LabelFrame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

b = Button(frame, text='this is a button')
b.pack()

root.mainloop()
