
from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("433x266")
root.title("Pycharm")


def myfunc():
    print("My Function")


# =========# use this to create none-dropdown menu=======
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)   # tearoff=0 will not show line in file menu
m1.add_command(label="New", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save as", command=myfunc)
m1.add_command(label="Print", command=myfunc)
mainmenu.add_cascade(label="File", menu=m1)
root.config(menu=mainmenu)


m2 = Menu(mainmenu, tearoff=0)   # tearoff=0 will not show line in file menu
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
mainmenu.add_cascade(label="Edit", menu=m2)
root.config(menu=mainmenu)

def help():
    print("I will help you")
    msg.showinfo("Help", "Harry will help you")

def rate():
    print("Rate us")
    value = msg.askquestion("was your experiance Good?", "You used this GUI,was your experiance Good?")
    print(value)

    if value == "yes":
        msg_1 = "Great. Rate us on appstore please"
    else:
        msg_1 = "Tell us, What went Wrong?" 
    msg.showinfo("Experiance", msg_1)
        

def divya():
    ans = msg.askretrycancel("Divya se Dosti karlo", "Sorry, Divya nahi banegi aapki dost")

    if ans:
        print("Retry karne pr bhi kuch nahi hoga")   
    else:
        print("Bahut badhiya bhai, cencel kardiya.. Warna maar padni thi aaj")

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Befriend Divya", command=divya)
mainmenu.add_cascade(label="Help", menu=m3,)
root.config(menu=mainmenu)


root.mainloop()
