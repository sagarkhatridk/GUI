
from tkinter import *
from PIL import ImageTk, Image  # for .jpg image 

root = Tk()

root.geometry("955x744")
photo =ImageTk.PhotoImage(file="code_image.jpg")


lbl = Label(image=photo)
lbl.pack()


root.mainloop()