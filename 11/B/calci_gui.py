from tkinter import *

__author__ = 'gauth_000'


def compute():
    op = int(v.get())
    v1 = eval(i1.get())
    v2 = eval(i2.get())
    if op == 1:
        res = v1 + v2
    elif op == 2:
        res = v1 * v2
    elif op == 3:
        res = v1 - v2
    elif op == 4:
        res = v1 / v2
    i3.set(res)


root = Tk()
root.geometry('300x200')
v = IntVar()
i1 = StringVar()
i2 = StringVar()
i3 = StringVar()
ip1 = Entry(root, textvariable=i1)
ip1.pack()
ip2 = Entry(root, textvariable=i2)
ip2.pack()
add = Radiobutton(root, text='add', variable=v, value=1, command=compute)
add.pack()
mul = Radiobutton(root, text='mul', variable=v, value=2, command=compute)
mul.pack()
sub = Radiobutton(root, text='sub', variable=v, value=3, command=compute)
sub.pack()
div = Radiobutton(root, text='div', variable=v, value=4, command=compute)
div.pack()
res = Entry(root, textvariable=i3)
res.pack()
mainloop()
