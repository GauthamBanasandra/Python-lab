from tkinter import *

__author__ = 'gauth_000'
root = Tk('colours')
red = Label(root, text='red', bg='red', fg='white')
red.pack(side=LEFT, fill=BOTH, expand=1)
blue = Label(root, text='blue', bg='blue', fg='white')
blue.pack(side=RIGHT, fill=BOTH, expand=1)
mainloop()
