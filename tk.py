from tkinter import *
from random import randint

root = Tk()
root.title('Guess The Number!')
root.geometry("500x500")

num_label = Label(root, text="Pick A Number Between 1 and 10!",
                  font=("Brush Script MT", 32))
num_label.pack(pady=20)


def guesser():
    if guess_box.get().isdigit():
        if int(guess_box.get()) > 50:
            num_label.config(text='Hey! Pick a number below 10')
            guess_box.delete(0, END)
        else:
            # Find out how far away our pick was from the actual number
            dif = abs(num - int(guess_box.get()))

            # Check to see if correct
            if int(guess_box.get()) == num:
                bc = "SystemButtonFace"
                num_label.config(text="Correct!!")
            elif dif == 25:
                # Set background color to white
                bc = "white"
            elif dif < 25 and dif > 20:
                bc = f'#ff{dif}{dif}{dif}{dif}'
            else:
                bc = f'#{dif}{dif}{dif}{dif}ff'
            # Change the background of the app
            root.config(bg=bc)
            # Change bg of label
            num_label.config(bg=bc)

    else:
        # Delete entry and throw error message
        guess_box.delete(0, END)
        num_label.config(text="Hey! That's Not A Number!")


def rando():
    global num
    num = randint(1, 10)
    # Clear the guess box
    guess_box.delete(0, END)
    # Change the colors back to normal
    num_label.config(bg="SystemButtonFace",
                     text="Pick A Number Between 1 and 50!")
    root.config(bg="SystemButtonFace")


guess_box = Entry(root, font=("Helvetica", 70), width=2)
guess_box.pack(pady=20)

guess_button = Button(root, text="Submit", command=guesser)
guess_button.pack(pady=20)

rand_button = Button(root, text="New Number", command=rando)
rand_button.pack(pady=20)

# Generate a random number on start
rando()

root.mainloop()
