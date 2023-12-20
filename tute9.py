from tkinter import *

def hello():
    print("Hello tkinter Buttons")

def name():
    print ("Name is sagar")

root = Tk()
root.geometry("655x333")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red",text="Submit", command=hello)
b1.pack(side=LEFT, padx=23)


b2 = Button(frame, fg="red",text="Tell me name", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red",text="Submit") 
b3.pack(side=LEFT, padx=23)

root.mainloop() 