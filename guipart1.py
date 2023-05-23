#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      91982
#
# Created:     18-05-2023
# Copyright:   (c) 91982 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
root=Tk()
root.title("quiz")
root.geometry("500x400")

classes = ["Class","1","2","3","4","5"]
first = ["a","b"]
second = ["c","d"]
third = ["e","f"]
fourth = ["g","h"]
fifth = ["i","j"]
i=0
def pick_chapter(e):
    if classmb.get()=="1":
        chaptermb.config(value=first)
    elif classmb.get()=="2":
        chaptermb.config(value=second)
    elif classmb.get()=="3":
        chaptermb.config(value=third)
    elif classmb.get()=="4":
        chaptermb.config(value=fourth)
    elif classmb.get()=="5":
        chaptermb.config(value=fifth)
    else:
        i=1


classmb = ttk.Combobox(root,value=classes,state="readonly")
classmb.current(0)
classmb.pack(pady=20)


classmb.bind("<<ComboboxSelected>>",pick_chapter)

chaptermb = ttk.Combobox(root,value=[" "],state="readonly")
chaptermb.current(0)
chaptermb.pack(pady=20)

root.mainloop()
