
from tkinter import *

def print_1():
    print("Button-1 Pressed")


def print_2():
    print("Button-2 Pressed")


def print_3():
    print("Button-3 Pressed")

def print_4():
    print("Button-4 Pressed")


root = Tk()
root.geometry("500x100")

name = Label(text="This is Buttons", bg="blue", fg="white", font="timesnewroman 12 bold")
name.pack()

f1 = Frame(root, borderwidth=5, bg="grey", relief=SUNKEN)
f1.pack(side=LEFT, padx=50)

b1 = Button(f1, text="Button-1", fg="red", command=print_1)
b1.pack(side=LEFT,padx=20 )

b2 = Button(f1, text="Button-2", fg="red", command=print_2)
b2.pack(side=LEFT,padx=20 )

b3 = Button(f1, text="Button-3", fg="red", command=print_3)
b3.pack(side=LEFT,padx=20 )

b4 = Button(f1, text="Button-4", fg="red", command=print_4)
b4.pack(side=LEFT,padx=20 )


root.mainloop()