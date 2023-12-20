
from tkinter import *



root = Tk()
root.geometry("655x333")

user = Label(root, text="Username")
password = Label(root, text="Password")

user.grid()  #there is bydefault row=0 column=0   
password.grid(row=1)


# Classes in tkinter

# BooleanVarn DoubleVar, IntVar,StringVar

def getvals():
    print(f"The value of user name is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")
    


uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable= uservalue)
passentry = Entry(root, textvariable= passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)


Button(text="Submit", command=getvals).grid()


root.mainloop()