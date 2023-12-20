
from tkinter import *



root = Tk()
root.title("GOOD GUI ")

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# the line goes from the point x1, y1 to x2, y2
can_widget.create_line(0,0,800,400, fill="red")
can_widget.create_line(0,400,800,0, fill="red")


# to create a ractangle spacify parameters in this order  top,left, bottom,right
can_widget.create_rectangle(3,5,700,300, fill="blue")


can_widget.create_text(200,200, text="Python", font="20")


can_widget.create_oval(344,233,244,350)


root.mainloop()