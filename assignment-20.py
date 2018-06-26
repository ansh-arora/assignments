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
# #
# root = Tk()
# f2=Frame(root)
# f2.pack()
# d={'ansh':9898989898,'dhruv':8787878787}
# set1=set(d)
# lab=Label(f2)
# lab.pack(side=BOTTOM)
# lab1=Label(f2)
# lab1.pack(side=BOTTOM)
#
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
#
#
# scrollbar = Scrollbar(f2)
# scrollbar.pack( side = RIGHT, fill = Y )
# mylist = Listbox(f2, yscrollcommand = scrollbar.set)
# mylist.pack( fill = BOTH )
# scrollbar.config( command = mylist.yview )
#
# def ins():
#
#     f=Frame(root)
#     f.pack()
#     Label(f,text='Name:').grid(row=0)
#     n=Entry(f)
#     n.grid(row=0,column=1)
#     Label(f, text='Phone:').grid(row=1)
#     p = Entry(f)
#     p.grid(row=1, column=1)
#     Button(f,text='Submit',command=lambda :add1(n.get(),p.get())).grid(row=2,column=1)
# def add():
#     s = list(d)
#     for names in s:
#         mylist.insert(END, names)
#
# def add1(n1,p1):
#     if n1:
#         d[n1]=p1
#         global set1
#     print(d)
#     set2=set(d)
#     set3=set2-set1
#     set1=set2
#     s=list(set3)
#     for names in s :
#         mylist.insert(END, names)
# add()
# f=Frame(root)
# f.pack()
# Button(f, text='Enter New Details', command=ins).pack()
# selected()
# mainloop()









