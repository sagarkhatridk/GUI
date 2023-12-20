from tkinter import *

import tkinter.messagebox as msg
root = Tk()
root.geometry("455x233")
root.title("Slider Tutorial")

# vertical
# myslider = Scale(root, from_=0, to=100)
# myslider.pack()
def getdollar():
    print(f"We will credit {myslider2.get()} dollars in your Bank account")
    msg.showinfo("Amount Credited",f"We will credit {myslider2.get()} dollars in your Bank account")

Label(root, text="How many Dollars you want").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=25)  # tik interval will take value in the multiplication of given value
myslider2.set(20)
myslider2.pack()
Button(root, text="Get Dollars",pady=10,command=getdollar).pack()


root.mainloop()