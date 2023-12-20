

from tkinter import *




root = Tk()
root.geometry("455x233")
root.title("Status bar")

statusvar = StringVar()
statusvar.set("Not, Ready")

sbar = Label(root, textvariable=statusvar,relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)


def upload():
    statusvar.set("Busy")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready, Now")




Button(root, text="Upload", command=upload).pack()


root.mainloop()