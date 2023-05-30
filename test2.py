from tkinter import *
from tkinter import ttk

x = Tk()
x.geometry("400x300")

styl = ttk.Style()
styl.configure('TSeparator', background='grey')

b = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
b.place(relx=0.03, rely=0.1, relheight=0.8, relwidth=0.4)

separator = ttk.Separator(x, orient='vertical')
separator.place(relx=0.47, rely=0, relwidth=1, relheight=0.9)

a = Label(x, bg="#f5f5f5", bd=4, relief=GROOVE, text="With Separator")
a.place(relx=0.5, rely=0.1, relheight=0.8, relwidth=0.4)

mainloop()