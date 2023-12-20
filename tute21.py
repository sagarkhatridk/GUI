
from tkinter import * 

root = Tk()
root.geometry("455x233")
root.title("listbox")


lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First-Item")


i=0
def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i = i + 1


Button(root,text="Add Item", command=add).pack()


root.mainloop()