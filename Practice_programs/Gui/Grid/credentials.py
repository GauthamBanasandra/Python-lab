from tkinter import *

__author__ = 'gauth_000'


def login():
    print(name.get(), '\n' + passw.get())


def enter(event):
    print('entered at', event.x, event.y)


root = Tk()
Label(root, text='First name:').grid(sticky=E)
Label(root, text='Last name:').grid(sticky=E)
chk = Checkbutton(root, text='Remember me', onvalue='yes', offvalue='no')
chk.grid(columnspan=2)
name = StringVar()
passw = StringVar()
Entry(root, textvariable=name).grid(row=0, column=1, sticky=W)
Entry(root, textvariable=passw, show='*').grid(row=1, column=1, sticky=W)
button_login = Button(root, text='Login', command=login)
button_login.grid(columnspan=2, sticky=E + W)
button_login.bind('<Enter>', enter)
# button_login.config(relief=SUNKEN)
mainloop()
