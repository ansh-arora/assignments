#Q1
from tkinter import *

root = Tk()
f2=Frame(root)
f2.pack()
d={'ansh':9898989898,'dhruv':8787878787}
lab=Label(f2)
lab.pack(side=BOTTOM)
lab1=Label(f2)
lab1.pack(side=BOTTOM)

def selected():

    lab.after(200,selected)
    all=mylist.get(0,END)
    sel=mylist.curselection()
    if len(sel)>0:
        n=all[sel[0]]
        lab1.config(text='Phone number:')
        lab.config(text=d[n])

s=list(d)

scrollbar = Scrollbar(f2)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(f2, yscrollcommand = scrollbar.set)
for names in s :
   mylist.insert(END, names)
mylist.pack( fill = BOTH )
scrollbar.config( command = mylist.yview )

selected()
mainloop()

#Q2
# from tkinter import *
#
# root = Tk()
# f2=Frame(root)
# f2.pack()
# d={'ansh':9898989898,'dhruv':8787878787}
# lab=Label(f2)
# lab.pack(side=BOTTOM)
# lab1=Label(f2)
# lab1.pack(side=BOTTOM)
#
# def ins():
#     x=input('enter new name:')
#     y=input('enter phone number:')
#     d[x]=y
#     d1=d
#     print(d)
#
# def selected():
#
#     lab.after(200,selected)
#     all=mylist.get(0,END)
#     sel=mylist.curselection()
#     if len(sel)>0:
#         n=all[sel[0]]
#         lab1.config(text='Phone number:')
#         lab.config(text=d[n])
#
# s=list(d)
#
# scrollbar = Scrollbar(f2)
# scrollbar.pack( side = RIGHT, fill = Y )
# mylist = Listbox(f2, yscrollcommand = scrollbar.set)
# for names in s :
#    mylist.insert(END, names)
# mylist.pack( fill = BOTH )
# scrollbar.config( command = mylist.yview )
# f=Frame(root)
# f.pack()
# Button(f, text='Enter New Details', command=ins).pack()
# selected()
# mainloop()

