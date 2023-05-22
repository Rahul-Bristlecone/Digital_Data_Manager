import tkinter as tk
from tkinter import ttk
import MySQLdb
from PIL import ImageTk, Image

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

main = tk.Tk()
main.title("DOCUMENT MANAGER")
main.iconbitmap("../Icons/briefcase.ico")
main.geometry('320x450')
main.resizable(False, False)

db = MySQLdb.connect('localhost', 'rsshrma92', 'rsshrma92', 'document_manager')
print("Connection successful")
cursor = db.cursor()


def auto_capitalize(*args):
    select_number.set(select_number.get().upper())


def save_details():
    while len(select_number.get()) > 1 and len(select_name.get()) > 1:
        cursor.execute('INSERT INTO doc_manager VALUES (%s,%s,%s)',
                       (select_combobox.get(), select_name.get(), select_number.get()))
        db.commit()

        message = ttk.Label(main, font=("Aharoni", 10, "bold"), text="Database entry successful")
        message.grid(row=8, column=0, pady=(10, 0), padx=60, sticky='w')
        select_number.set("")
        select_name.set("")
        main.after(600, message.destroy)


def reset():
    select_number.set("")
    select_name.set("")


def pop_up():
    pop_window = tk.Tk()

    pl = ttk.Label(pop_window, text="Success")
    pl.grid()


doc_image = ImageTk.PhotoImage(Image.open('../Icons/doc_image.png').resize((85, 85)))
doc_image_label = ttk.Label(main, image=doc_image, compound="left")
doc_image_label.grid(padx=(110, 0), pady=(30, 0), sticky='w')

document_type = ttk.Label(main, font=("Aharoni", 10, "bold"), text="Choose your document type")
document_type.grid(column=0, pady=(20, 0), padx=50, sticky='w')

select_combobox = tk.StringVar()
combo_values = ttk.Combobox(main, textvariable=select_combobox, font=("Calibri", 10, "bold"), width=27)
combo_values["values"] = ("AADHAR", "PAN", "VOTER ID CARD", "DRIVING LICENCE")
combo_values["state"] = "readonly"
combo_values.current(0)
combo_values.grid(column=0, pady=(5, 0), padx=50, sticky='w')

document_name = ttk.Label(main, font=("Aharoni", 10, "bold"), text="Enter name of the document holder")
document_name.grid(column=0, pady=(20, 0), padx=50, sticky='w')
select_name = tk.StringVar()
name_entry = ttk.Entry(main, textvariable=select_name, font=("Calibri", 11, "bold"), width=30)
name_entry.grid(column=0, pady=(5, 0), padx=50, sticky='w')

document_number = ttk.Label(main, font=("Aharoni", 10, "bold"), text="Enter Document number")
document_number.grid(column=0, pady=(20, 0), padx=50, sticky='w')
select_number = tk.StringVar()
select_number.trace("w", auto_capitalize)
number_entry = ttk.Entry(main, textvariable=select_number, font=("Calibri", 11, "bold"), width=30)
number_entry.grid(column=0, pady=(5, 0), padx=50, sticky='w')

save_button = ttk.Button(main, text="Save", width=10, command=save_details)
save_button.grid(row=7, pady=20, padx=50, sticky='w')

# boldStyle = ttk.Style ()
# boldStyle.configure("Bold.TButton", font = ('Sans','10','bold'))
reset_button = ttk.Button(main, text="Reset", width=10, command=reset)
reset_button.grid(row=7, pady=20, padx=123, sticky="w")

cancel_button = ttk.Button(main, text="Cancel", width=10, command=main.destroy)
cancel_button.grid(row=7, pady=20, padx=196, sticky="w")

main.mainloop()
