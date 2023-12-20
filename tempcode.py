from tkinter import *
# from tkinter import Image
from PIL import Image,ImageTk


root = Tk()
root.geometry("433x244")
root.title("Hello")

photo = ImageTk.PhotoImage(file="image_1.jpg")
Label(root,image=photo).pack()


root.mainloop()


