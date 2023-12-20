from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

from pymysql import NULL

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    Textarea.delete(1.0, END)
def openFile():
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Test Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad ")
        Textarea.delete(1.0,END)
        f = open(file, "r")
        Textarea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt", filetypes=[("All files", "*.*"), ("Test Documents", "*.txt")])

        if file == "":
            file = None
        else:
            # save as a new file

            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file)  + " - Notepad")
            print("File Saved")
    
    else:
        #save the file
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by SAGAR")


if  __name__ == '__main__':
    #Basic tkinter satup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad_icon.ico")    
    root.geometry("500x300")

    #add text area
    Textarea = Text(root, font="timesnewroman, 12")
    file = None
    Textarea.pack(expand=True, fill=BOTH,)


    #lets create a menubar

    Menubar = Menu(root)

    #file menu starts
    Filemenu = Menu(Menubar, tearoff=0)

    #To open new file
    Filemenu.add_command(label="New", command=newFile)

    #To Open already existing file

    Filemenu.add_command(label="Open", command=openFile)

    # To save the current file
    Filemenu.add_command(label="Save", command=saveFile)
    Filemenu.add_separator()

    Filemenu.add_command(label="Exit", command=quitApp)

    Menubar.add_cascade(label="File", menu=Filemenu)
    #file menu starts


    
    #Edit Menu starts

    Editmenu = Menu(Menubar, tearoff=0)

    # to give a feature of cut,copy,paste

    Editmenu.add_command(label="Cut", command=cut)
    Editmenu.add_command(label="Copy", command=copy)
    Editmenu.add_command(label="Paste", command=paste)

    Menubar.add_cascade(label="Edit", menu=Editmenu)
    #Edit Menu Ends


    #Help menu starts
    Helpmenu = Menu(Menubar, tearoff=0)
    Helpmenu.add_command(label="About Notepad", command=about)
    Menubar.add_cascade(label="Help", menu=Helpmenu)

    #adding scrollbar

    Scroll = Scrollbar(Textarea) 
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=Scroll.set)

    root.config(menu=Menubar)

    #help menu Ends    

    root.mainloop()