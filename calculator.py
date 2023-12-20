from tkinter import *



root = Tk()
root.geometry("644x900")
root.title("Calculator")
root.wm_iconbitmap("calculator_icon.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="timesnewroman 40 bold", relief=SUNKEN)
screen.pack(fill=X, ipadx=8, padx=10, pady=10)

def click(event):
    # print("Hello")
    global scvalue
    text = event.widget.cget("text")
    print(text)
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()



f = Frame(root, bg="grey")


b = Button(f, text="9", padx=28, pady=15,font="timesnewroman 35 bold ")
b.bind("<Button-1>",click)

b.pack(side=LEFT, padx=18, pady=5) 
b = Button(f, text="8", padx=28, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=28, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()


# ===============================

f = Frame(root, bg="grey")


b = Button(f, text="6", padx=28, pady=15,font="timesnewroman 35 bold ")
b.bind("<Button-1>",click)

b.pack(side=LEFT, padx=18, pady=5) 
b = Button(f, text="5", padx=28, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=28, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()

# ==================================

f = Frame(root, bg="grey")


b = Button(f, text="3", padx=28, pady=15,font="timesnewroman 35 bold ")
b.bind("<Button-1>",click)

b.pack(side=LEFT, padx=18, pady=5) 
b = Button(f, text="2", padx=28, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=28, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()

# ======================================


f = Frame(root, bg="grey")


b = Button(f, text="0", padx=30, pady=15,font="timesnewroman 35 bold ")
b.bind("<Button-1>",click)

b.pack(side=LEFT, padx=18, pady=5) 
b = Button(f, text="-", padx=32, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=31, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()

# ========================================


f = Frame(root, bg="grey")


b = Button(f, text="/", padx=32, pady=15,font="timesnewroman 35 bold ")
b.bind("<Button-1>",click)

b.pack(side=LEFT, padx=18, pady=5) 
b = Button(f, text="%", padx=25, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=25, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()
# =============================

f = Frame(root, bg="grey")


b = Button(f, text="C", padx=28, pady=15,font="timesnewroman 35 bold ")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

# b.pack(side=LEFT, padx=18, pady=5) 
# b = Button(f, text="%", padx=28, pady=15,font="timesnewroman 35 bold ")
# b.pack(side=LEFT,padx=18, pady=5)
# b.bind("<Button-1>", click)

# b = Button(f, text="=", padx=28, pady=15,font="timesnewroman 35 bold ")
# b.pack(side=LEFT,padx=18, pady=5)
# b.bind("<Button-1>",click)
f.pack()

root.mainloop()