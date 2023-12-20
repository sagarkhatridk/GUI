

from tkinter import *


class GUI(Tk):
    #here root is self
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
    
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def create_btn(self):
        Button(text="Click", command=self.click).pack()

    def click(self):
        print("Button Clicked")


if __name__ == '__main__':
    #here root is window
    window = GUI()
    window.status()
    window.create_btn()
    window.mainloop()
    
