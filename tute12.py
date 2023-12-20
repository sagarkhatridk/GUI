from tkinter import *



root = Tk()
root.geometry("644x344")

def getvals():
    print("Submitting form")
    print(f"{namevalue.get()},{phonevalue.get()},{gendervalue.get()},{contactvalue.get()},{paymentvalue.get()}, {foodservicevalue.get()}")
    with open("records_tute_12.txt", "a") as f:
        f.write(f"{namevalue.get()},{phonevalue.get()},{gendervalue.get()},{contactvalue.get()},{paymentvalue.get()}, {foodservicevalue.get()}\n")


# heading 
Label(root,text="Welcome to Travel", font="timesnewroman 13 bold", padx=25).grid(row=0, column=3)

# text for form
name= Label(root, text="Name")
phone= Label(root, text="phone")
gender= Label(root, text="gender")
contact= Label(root, text="contact")
payment= Label(root, text="payment")


# pack text for a form by grid
name.grid(row=1, column=1)
phone.grid(row=2, column=1)
gender.grid(row=3, column=1)
contact.grid(row=4, column=1)
payment.grid(row=5, column=1)


# tkinter variable for string entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
contactvalue = StringVar()
paymentvalue = StringVar()

foodservicevalue = IntVar()   #if check box is checked then value is 1 either value is 0 thats why IntVar()

# entry for a form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
contactentry = Entry(root, textvariable=contactvalue)
paymententry = Entry(root, textvariable=paymentvalue)


# packing Entry
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
contactentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

# checkbox

foodserive = Checkbutton(text="Want to prebook your meals", variable=foodservicevalue)
foodserive.grid(row=6, column=3)

# Button and packing it and assign command

Button(text="Submit", command=getvals).grid(row=7,column=3)



root.mainloop()