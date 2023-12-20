
from tkinter import *


root = Tk()
root.geometry("733x566")
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


root.mainloop()
