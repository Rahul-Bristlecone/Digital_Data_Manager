import tkinter as tk
from tkinter import ttk, DISABLED

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Set basic attributes
root = tk.Tk()
root.title("Calculator")
root.geometry("300x520")


# root.resizable(False,False)

# calculator function
def btn_click(item):
    expression = value.get()+str(item)
    value.set(expression)
def calculator():
    result = str(eval(value.get()))
    value.set(result)

def selection_result():
    print(select_checkbox.get())
    print(select_radiobutton.get())


def handle_selection(event):
    print("Today is", select_combobox.get())


# textfield
value = tk.StringVar()
entry_field = ttk.Entry(root, font=("Arial", 12), textvariable=value)
# entry_field.place(x=40,y=60,height=19,width=78)
entry_field.grid(padx=40, sticky="w")
entry_field.focus()

# textbox
text_entry = tk.Text(root, width=22, height=8, insertborderwidth=2)
text_entry.grid(padx=40, pady=10, sticky="w")
text_entry.insert("1.0", "Content here")
# text_entry ["state"] = "normal"

# Scrollbar
text_scroll = tk.Scrollbar(root, orient="vertical", command=text_entry.yview)
text_scroll.grid(row=1, column=0, pady=10, sticky="ns")
text_entry["yscrollcommand"] = text_scroll.set

# buttons
select_button = tk.StringVar()
addition = tk.StringVar()
plus_button = ttk.Button(root, text="+", width="5", command = lambda: btn_click("+"))
plus_button.grid(padx=10, row=2, column=0, sticky="W")
minus_button = ttk.Button(root, text="-", width="5", command = lambda: btn_click("-"))
minus_button.grid(padx=55, row=2, column=0, sticky="W")
multiply_button = ttk.Button(root, text="x", width="5", command = lambda: btn_click("*"))
multiply_button.grid(padx=105, row=2, column=0, sticky="W")
divide_button = ttk.Button(root, text="/", width="5", command = lambda: btn_click("/"))
divide_button.grid(padx=155, row=2, column=0, sticky="W")
equal_button = ttk.Button(root, text="=", width="5", command=calculator)
equal_button.grid(padx=205, row=2, column=0, sticky="W")
# Button row 2
modulus_button = ttk.Button(root, text="%", width="5", command = lambda: btn_click("%"))
modulus_button.grid(padx=10, pady=10, row=3, column=0, sticky="W")

# Checkbox
select_checkbox = tk.StringVar()
ttk.Checkbutton(root,
                text="Print",
                variable=select_checkbox,
                command=selection_result,
                onvalue="Print Selected",
                offvalue="Print unselected").grid()

# RadioButtons
select_radiobutton = tk.StringVar()
ttk.Radiobutton(root,
                text="as pdf",
                variable=select_radiobutton,
                value="as pdf1").grid()

ttk.Radiobutton(root,
                text="as pdf",
                variable=select_radiobutton,
                value="as pdf2").grid()

ttk.Radiobutton(root,
                text="as pdf",
                variable=select_radiobutton,
                value="as pdf3").grid()

# Combobox
select_combobox = tk.StringVar()
combo_values = ttk.Combobox(root, textvariable=select_combobox)
combo_values["values"] = ("AADHAR", "PAN", "VOTERID CARD", "DRIVING LICENCE")
combo_values["state"] = "readonly"
combo_values.grid()
combo_values.bind("<<ComboboxSelected>>", handle_selection)

# List values
options = ("8786","89787")
select_listbox = tk.StringVar(value=options)
list_values = tk.Listbox(root, listvariable=options, height=7)
list_values["selectmode"] = "extended" #browse
list_values.grid()

def handle_selection_change(event):
    selected_indices = list_values.curselection()
    for i in selected_indices:
        print(list_values.get(i))


list_values.bind("<<ListboxSelect>>", handle_selection_change)

initial_value = tk.IntVar(value=0)
spin_box = ttk.Spinbox(root,values=(0,5,10,15,20,25), textvariable=initial_value,wrap=False)
spin_box.grid()

def handle_scale_change(event):
    print(scale.get())

initial_value_scale = tk.DoubleVar()
scale = ttk.Scale(root, from_=1,to=5, command=handle_scale_change, variable=initial_value_scale)
scale.grid()

root.mainloop()

print("Today is", select_combobox.get())
