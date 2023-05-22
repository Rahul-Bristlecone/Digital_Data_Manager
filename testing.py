import tkinter as tk

def createNewWindow():
    newWindow = tk.Toplevel(app)
    newWindow.grab_set()

app = tk.Tk()
buttonExample = tk.Button(app, text="Create new window", command=createNewWindow)
buttonExample.pack()
app.mainloop()