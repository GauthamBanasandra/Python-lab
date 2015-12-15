import tkinter as tk

__author__ = 'gauth_000'

root = tk.Tk()
listBox = tk.Listbox(root)
listBox.pack(fill=tk.BOTH, expand=1)
for i in range(10):
    listBox.insert(tk.END, i)
tk.mainloop()
