import this
from tkinter import *

root = Tk()
root.geometry("300x250")
root.title("Window Resize")
root.resizable(False,False)



window_title = Label(root, text="GUI Resizer", font="tilesnewroman 20 bold").grid(row=2, column=2)
width_1 = Label(root, text="Width: ", font="timesnewroman 12 bold").grid(row=3, column=1)
height_1 = Label(root, text="Height: ", font="timesnewroman 12 bold").grid(row=4, column=1)

width_input = Entry()
width_input.grid(row=3, column=2)


height_input = Entry()
height_input.grid(row=4, column=2, pady=10)


def resize():


    width_value = width_input.get()
    height_value = height_input.get()
    root.geometry(f"{width_value}x{height_value}")




Btb = Button(root, text="Apply", command=resize, font="timesnewroman 8 bold").grid(row=5,column=2)

root.mainloop()