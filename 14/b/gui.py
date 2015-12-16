from tkinter import *

__author__ = 'gauth_000'


def on_click():
    global count
    count += 1
    l1.config(font=('times', 20, 'bold'))
    if count % 2:
        l1.config(bg='green')
    else:
        l1.config(bg='purple')
    l1.config(text=str(count) + ' click')


count = 0
root = Tk()
root.geometry('250x250+100+100')
b1 = Button(root, text='click me', bg='red', command=on_click)
b1.pack()
l1 = Label(root, text='not yet clicked', bg='blue')
l1.pack()
b2 = Button(root, text='exit', command=exit)
b2.pack()
mainloop()
