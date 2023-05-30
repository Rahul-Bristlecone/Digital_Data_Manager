import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# tk._test()
root = tk.Tk()
# root.resizable(False,False)
root.title("Select Alias")
# root.columnconfigure(0,weight=1)
# root.geometry("250x140")
style = ttk.Style()
style.configure("CustomButtonStyle.TButton", font=("Tahoma", 15))
style.map("CustomButtonStyle.TButton",
          underline=[("active",True)]) # for Hover and all
print(style.theme_names())
print(style.theme_use())

test_button = ttk.Button(root, text="Hello", style="CustomeButtonStyle.TButton", underline=True)
test_button.grid()
print(test_button.winfo_class())
print(style.layout("TButton"))
print(style.element_options("TButton.border"))

style.configure("TButton", bordercolor="#f00")
style.configure("TButton", relief="solid")
style.configure("TButton", borderwidth=10)

test_button["style"] = "CustomButtonStyle.TButton"

root.mainloop()

# def select_db():
#     length= len(username.get())
#     print("Database %s selected" %username.get())
#     print(length)
#     # ttk.Label(root,text=username.get())
#
#
# username = tk.StringVar()
#
# # Using snake case PEP8 coding standard
# sps_commerce_logo = ttk.Frame(root)
# sps_commerce_logo.grid(row=0,column=0)
# ttk.Label(sps_commerce_logo,text="SPS commerce", padding=(10,10)).grid()
#
# db_field = ttk.Entry(sps_commerce_logo, textvariable=username)
# db_field.grid(row=1, column=0)
# db_field.focus()
#
# buttons = ttk.Frame(root, padding=(40,10))
# buttons.grid()
# ok_button = ttk.Button(buttons,text="✅OK", command=select_db)
# ok_button.grid(sticky="EW", row=3, column=1)
#
# cancel_button=ttk.Button(buttons,text="❌Cancel",command=root.destroy)
# cancel_button.grid(row=3,column=2)


# root.mainloop()
