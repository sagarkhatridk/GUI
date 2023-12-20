from tkinter import *
from tkinter import font
from turtle import left, title

root = Tk()
root.geometry("444x233")
root.title("My Gui With Harry")


# importand Label Options


#=========== text = adds the text ==========


# bg - background
# fg - foreground
# font - sets the font
    # 1. font=("times new roman",20, "bold")
    # 2. font="timesnewroman 20 bold"
# padx - x padding
# pady - y padding
# relief - bordeer styling - SUNKEN, RAISED,  GROOVE, RIDGE

title_label = Label(text='''Abdul Rashid Salim Salman Khan ; 27 December 1965)[2] is an Indian actor, film producer, and\n television personality who works in Hindi films. In a film\n career spanning over thirty years, Khan has received numerous\n awards, including two National Film Awards as a film producer, and two Filmfare Awards for acting.[3] He is cited in the media\n as one of the most commercially successful actors of Indian cinema.[4][5] Forbes\n included him in their 2015 list of Top-Paid 100 Celebrity Entertainers in the world;\n Khan tied with Amitabh Bachchan for No. 71 on the list, both with earnings of $33.5 million.\n[6][7] According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world,\n Khan was the highest-ranked Indian with 82nd rank with earnings of \n$37.7 million.[8][9] He is also known as the host of the reality show, Bigg Boss since 2010.[10]''',bg="red",fg="white", padx=23, pady=94, font="timesnewroman 12 bold", borderwidth=3, relief=SUNKEN)

# Important pack option 
# 1. anchor nw           # nw means north west
# side = top,bottom,left, right

# title_label.pack(anchor="nw")
# title_label.pack(anchor="ne")    # north east

 
# title_label.pack(side=BOTTOM , anchor="se")  
# title_label.pack(side=BOTTOM, anchor="sw", fill=X)  
title_label.pack(side=LEFT, fill=Y, padx=34,pady=34)  


title_label.pack()

root.mainloop()