from tkinter import *

root = Tk()
root.geometry("444x222")
root.title("Title")
root.wm_iconbitmap("notepad_icon.ico")

root.configure(background="skyblue")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command=root.destroy).pack()

root.mainloop()