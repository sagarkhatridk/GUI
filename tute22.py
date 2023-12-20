
from tkinter import *



root = Tk()
root.geometry("455x233")
root.title("Scrollbar")

#for connecting a scrollbar to Widget
# 1. Widget(yscrollcommand = scrollbar.set)
# 2. scollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill="y")

# listbox = Listbox(root,yscrollcommand = scrollbar.set)
# for i in range(344):
#     listbox.insert(END, f"Item - {i}")
# listbox.pack(fill=BOTH, padx=22)
# scrollbar.config(command=listbox.yview)


text = Text(root, yscrollcommand = scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)



root.mainloop()