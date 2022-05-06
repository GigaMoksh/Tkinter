from tkinter import *
import random

root = Tk()

root.geometry("400x300")

root.title("Rock Paper Scissors Game")

computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}


def reset_game():
    
    b1.config(state="active")
    b2.config(state="active")
    b3.config(state="active")
    l1.config(text="Player            ")
    l3.config(text="Computer")
    l4.config(text="")


def button_disable():
    b1.config(state="disable")
    b2.config(state="disable")
    b3.config(state="disable")


def isrock():
    comp_value = computer_value[str(random.randint(0, 2))]
    if comp_value == "Rock":
        match_result = "Match Draw"
    elif comp_value == "Scissor":
        match_result = "Player Wins!"
    else:
        match_result = "Computer Wins!"
    l4.config(text=match_result)
    l1.config(text="Rock            ")
    l3.config(text=comp_value)
    button_disable()


def ispaper():
    comp_value = computer_value[str(random.randint(0, 2))]
    if comp_value == "Paper":
        match_result = "Match Draw"
    elif comp_value == "Scissor":
        match_result = "Computer Wins!"
    else:
        match_result = "Player Wins!"
    l4.config(text=match_result)
    l1.config(text="Paper           ")
    l3.config(text=comp_value)
    button_disable()


def isscissor():
    comp_value = computer_value[str(random.randint(0, 2))]
    if comp_value == "Rock":
        match_result = "Computer Wins!"
    elif comp_value == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Wins!"
    l4.config(text=match_result)
    l1.config(text="Scissor         ")
    l3.config(text=comp_value)
    button_disable()


label_rps = Label(root, text="Rock Paper Scissors", font="normal 20 bold")
label_rps.pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame, text="Player            ", font=10)

l2 = Label(frame, text="VS             ", font="normal 10 bold")

l3 = Label(frame, text="Computer", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)

l4 = Label(root, text="", font="normal 20 bold", bg="white",
           width=15, borderwidth=2, relief=SOLID)
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock", font=10, width=7, command=isrock)

b2 = Button(frame1, text="Paper ", font=10, width=7, command=ispaper)

b3 = Button(frame1, text="Scissors", font=10, width=7, command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

b4 = Button(root, text="Reset Game", font=10,
            fg="red", bg="black", command=reset_game)
b4.pack(pady=20)

root.mainloop()
