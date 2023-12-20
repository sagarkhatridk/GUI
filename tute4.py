from tkinter import *

root = Tk()

# Width x Height
root.geometry("444x234")

# Width, Height
root.minsize(200,100)

root.maxsize(1200,700)

name = Label(text="This is Label")
name.pack()

# name = Label(root,text="This is Label").place(x=20,y=20)



root.mainloop()