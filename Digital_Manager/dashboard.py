# On clicking the submit button POST request "/stores/create_store" end-point is hit
# Database table optimizations
# Create logs
import tkinter as tk
from tkinter import ttk
from Utilities import send_email_sms
import json
import MySQLdb

from PIL import ImageTk, Image

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

dashboard = tk.Tk()
dashboard.title("PERSONAL DIGITAL MANAGER")
dashboard.iconbitmap("C:\\Users\\Rahul.Sharma4\\PycharmProjects\\pythonProject1\\Icons\\briefcase.ico")
dashboard.geometry('337x600')
dashboard.resizable(False, False)

dashboard_image = ImageTk.PhotoImage(Image.open('../Icons/dashboard_image.png').resize((65, 65)))
new_user_image = ImageTk.PhotoImage(Image.open('../Icons/add-user.png').resize((23, 23)))
exist_user_image = ImageTk.PhotoImage(Image.open('../Icons/existing-user.png').resize((25, 25)))

db = MySQLdb.connect('localhost', 'rsshrma92', 'rsshrma92', 'document_manager')

print("Connection successful")
cursor = db.cursor()


def reset():
    name.set("")
    new_username.set("")
    email.set("")
    new_password.set("")
    phone.set("")
    otp_code.set("")
    username.set("")
    password.set("")


def send_email():
    if len(email.get()) > 4 and '@' in email.get() and '.' in email.get():
        passw = 'MTGrHWd3m61hZYFV'
        sender = 'rsshrma.92@gmail.com'
        new_user = email.get()
        send_email.send_email_otp(passw, sender, new_user)

        message = ttk.Label(dashboard, font=("Aharoni", 10, "bold"), text="Email sent, Check your inbox")
        message.pack(pady=20)
        dashboard.after(1600, message.destroy)
    else:
        message = ttk.Label(dashboard, font=("Aharoni", 10, "bold"), text="Incorrect email id")
        message.pack(pady=20)
        dashboard.after(1600, message.destroy)


def otp_validation():
    if send_email_sms.otp_extraction() == otp_code.get():
        message = ttk.Label(dashboard, font=("Aharoni", 10, "bold"), text="OTP Verified")
        message.pack(pady=20)
        dashboard.after(1000, message.destroy)
        return True
    else:
        message = ttk.Label(dashboard, font=("Aharoni", 10, "bold"), text="Wrong OTP")
        message.pack(pady=20)
        dashboard.after(800, message.destroy)
        return False


def submit_details():
    if not (new_name_entry.get() and new_username_entry.get() and new_password_entry.get() and new_email_entry.get() and
            otp_entry.get()):
        message = ttk.Label(dashboard, font=("Aharoni", 10, "bold"), text="Fields are empty")
        message.pack(pady=20)
        dashboard.after(800, message.destroy)
    elif not (new_phone_entry.get() and new_phone_entry.get().isdigit() and len(new_phone_entry.get()) == 10):
        message = ttk.Label(dashboard, font=("Aharoni", 10, "bold"), text="Incorrect Phone number")
        message.pack(pady=20)
        dashboard.after(800, message.destroy)
    else:
        while otp_validation():
            data = {"status_flag": "S",
                    "name": new_name_entry.get(),
                    "username": new_username_entry.get(),
                    "email_details": {
                        "email": new_email_entry.get(),
                        "OTP": otp_entry.get()
                    },
                    "password": new_password_entry.get(),
                    "mobile": new_phone_entry.get(), }
            json_data = json.dumps(data)
            print(json_data)
            cursor.execute('INSERT INTO new_user VALUES (%s,%s,%s,%s,%s)',
                           (name.get(), new_username.get(), email.get(), new_password.get(), phone.get()))
            db.commit()
            reset()


# ------------------------- Tabs creation and Tab style ---------------------
notebookStyle = ttk.Style()
notebookStyle.configure('Custom.TNotebook.Tab', padding=(30, 4), font=("Calibri", 10, "bold"))

dashboard_tabs = ttk.Notebook(dashboard, style="Custom.TNotebook")
dashboard_tabs.pack(expand=1, fill="both")

# -------------------- NEW USER TAB ---------------------------------
new_user_tab = ttk.Frame(dashboard_tabs)
dashboard_tabs.add(new_user_tab, text=" NEW USER", image=new_user_image, compound="left")

display_image = ttk.Label(new_user_tab, image=dashboard_image)
display_image.grid(padx=(136, 0), pady=(20, 0), sticky='w')

new_name_label = ttk.Label(new_user_tab, font=("Aharoni", 10, "bold"), text="Enter your name")
new_name_label.grid(column=0, pady=(10, 0), padx=62)
name = tk.StringVar()
new_name_entry = ttk.Entry(new_user_tab, textvariable=name, font=("Calibri", 11, "bold"), width=30)
new_name_entry.grid(column=0, pady=(5, 0), padx=62)
new_name_entry.focus()

new_username_label = ttk.Label(new_user_tab, font=("Aharoni", 10, "bold"), text="Enter Username")
new_username_label.grid(column=0, pady=(10, 0), padx=62)
new_username = tk.StringVar()
new_username_entry = ttk.Entry(new_user_tab, textvariable=new_username, font=("Calibri", 11, "bold"), width=30)
new_username_entry.grid(column=0, pady=(5, 0), padx=62)

new_email_label = ttk.Label(new_user_tab, font=("Aharoni", 10, "bold"), text="Enter E-mail address")
new_email_label.grid(column=0, pady=(10, 0), padx=62)
send_button = ttk.Button(new_user_tab, text="Send OTP", width=10, command=send_email)
send_button.grid(row=5, pady=(10, 0), padx=208)
email = tk.StringVar()
new_email_entry = ttk.Entry(new_user_tab, textvariable=email, font=("Calibri", 11, "bold"), width=30)
new_email_entry.grid(column=0, pady=(5, 0), padx=62)

new_password_label = ttk.Label(new_user_tab, font=("Aharoni", 10, "bold"), text="Enter Password")
new_password_label.grid(column=0, pady=(10, 0), padx=62)
new_password = tk.StringVar()
new_password_entry = ttk.Entry(new_user_tab, textvariable=new_password, font=("Calibri", 11, "bold"), show="*",
                               width=30)
new_password_entry.grid(column=0, pady=(5, 0), padx=62)

new_phone_label = ttk.Label(new_user_tab, font=("Aharoni", 10, "bold"), text="Enter Phone number")
new_phone_label.grid(column=0, pady=(10, 0), padx=62)
phone = tk.StringVar()
new_phone_entry = ttk.Entry(new_user_tab, textvariable=phone, font=("Calibri", 11, "bold"), width=30)
new_phone_entry.grid(column=0, pady=(5, 0), padx=62)

otp_label = ttk.Label(new_user_tab, font=("Aharoni", 10, "bold"), text="Enter OTP", )
otp_label.grid(column=0, pady=(10, 0), padx=62)
verify_button = ttk.Button(new_user_tab, text="Verify", width=10, command=otp_validation)
verify_button.grid(row=11, pady=(10, 0), padx=208)
otp_code = tk.StringVar()
otp_entry = ttk.Entry(new_user_tab, textvariable=otp_code, font=("Calibri", 11, "bold"), width=30)
otp_entry.grid(column=0, pady=(5, 0), padx=62)

submit_button = ttk.Button(new_user_tab, text="Submit", width=10, command=submit_details)
submit_button.grid(row=13, pady=(15, 0), padx=62)
reset_button = ttk.Button(new_user_tab, text="Reset", width=10, command=reset)
reset_button.grid(row=13, pady=(15, 0), padx=135)

for child in new_user_tab.winfo_children():
    child.grid_configure(sticky='w')

# ------------------------- EXISTING USER TAB -------------------------------
existing_user_tab = ttk.Frame(dashboard_tabs)
dashboard_tabs.add(existing_user_tab, text=" EXISTING USER", image=exist_user_image, compound="left")

display_image = ttk.Label(existing_user_tab, image=dashboard_image)
display_image.grid(padx=(136, 0), pady=(20, 0))

exist_username_label = ttk.Label(existing_user_tab, font=("Aharoni", 10, "bold"), text="Enter Username")
exist_username_label.grid(pady=(10, 0), padx=62)
username = tk.StringVar()
username_entry = ttk.Entry(existing_user_tab, textvariable=username, font=("Calibri", 11, "bold"), width=30)
username_entry.grid(pady=(5, 0), padx=62)
username_entry.focus()

exist_password_label = ttk.Label(existing_user_tab, font=("Aharoni", 10, "bold"), text="Enter Password")
exist_password_label.grid(pady=(20, 0), padx=62)
password = tk.StringVar()
password_entry = ttk.Entry(existing_user_tab, textvariable=password, font=("Calibri", 11, "bold"), show="*", width=30)
password_entry.grid(pady=(5, 0), padx=62)

login_button = ttk.Button(existing_user_tab, text="Login", width=10, command=submit_details)
login_button.grid(row=7, pady=20, padx=62)
reset_button = ttk.Button(existing_user_tab, text="Reset", width=10, command=reset)
reset_button.grid(row=7, pady=20, padx=135)

for child in existing_user_tab.winfo_children():
    child.grid_configure(column=0, sticky='w')

dashboard.mainloop()
