from tkinter import * 
import tkinter.messagebox as msg 
root = Tk()
root.geometry("455x233")
root.title("Radio Button")


# var = IntVar()
var = StringVar()
var.set("Dosa")

Label(root, text="Whaat would you like to have?", font="timesnewroman 19 bold", justify=LEFT, padx=14).pack()

radio = Radiobutton(root, text="Dosa", padx=14,variable=var,value="Dosa").pack(anchor="w" )
radio = Radiobutton(root, text="Idli", padx=14,variable=var,value="Idli").pack(anchor="w" )
radio = Radiobutton(root, text="Paratha", padx=14,variable=var,value="Paratha").pack(anchor="w")
radio = Radiobutton(root, text="Paneer Makhhani", padx=14,variable=var,value="Paneer Makhhani").pack(anchor="w")

def order():
    msg.showinfo("Order Recieved",f"We have recieved your order for {var.get()}, thanks for ordering.")


Button(text="Order now", command=order).pack()

root.mainloop()