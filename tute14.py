from tkinter import * 


root = Tk()
root.title("Events in tkinter")
root.geometry("644x334")


widget = Button(root, text="Click")
widget.pack()

def harry(event):
    print(f"You clicked the button at {event.x}, {event.y}")

widget.bind('<Button-1>', harry)
widget.bind('<Double-1>', quit)



root.mainloop()