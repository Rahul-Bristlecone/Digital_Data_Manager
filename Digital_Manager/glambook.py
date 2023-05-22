import tkinter as tk
from tkinter import ttk
import json

import requests
from PIL import ImageTk, Image

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class GlamWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PERSONAL CARE MANAGER")
        self.geometry("380x520")
        self.iconbitmap("../Icons/briefcase.ico")

        glam_frame = GlamBookFrame(self)
        glam_frame.grid()


class GlamBookFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        main_frame = ttk.Frame(self)
        main_frame.grid()

        self.product_image = ImageTk.PhotoImage(Image.open('../Icons/business-case.png').resize((75, 75)))
        pimage_label = ttk.Label(main_frame, image=self.product_image, compound="left")
        pimage_label.grid(padx=(152, 10), pady=(30, 10), sticky='w')

        # ------------------------------ Store Header ---------------------------------

        store_label = ttk.Label(main_frame, text="Choose your Brand Store", font=("Aharoni", 10, "bold"))
        store_label.grid(row=1, padx=(25, 5), pady=(10, 5), sticky='w')
        self.store = tk.StringVar()
        store_name = ttk.Combobox(main_frame, width=25,
                                  values=['Select from here', "OrganicHarvest", "Plum", "Organique"],
                                  textvariable=self.store)
        store_name.grid(row=2, padx=(25, 5), pady=(5, 5), sticky='w')

        made_for_label = ttk.Label(main_frame, text="Suitable for", font=("Aharoni", 10, "bold"))
        made_for_label.grid(row=1, column=1, pady=(10, 0), sticky='w')
        self.gender = tk.StringVar()
        made_for_name = ttk.Radiobutton(main_frame, value="Men", text="Men", variable=self.gender)
        made_for_name.grid(row=2, column=1, pady=(0, 0), sticky='w')
        made_for_name = ttk.Radiobutton(main_frame, value="Women", text="Women", variable=self.gender)
        made_for_name.grid(row=3, column=1, pady=(0, 5), sticky='w')
        made_for_name = ttk.Radiobutton(main_frame, value="Unisex", text="Unisex", variable=self.gender)
        made_for_name.grid(row=4, column=1, pady=(0, 5), sticky='w')

        range_label = ttk.Label(main_frame, text="Choose range of product", font=("Aharoni", 10, "bold"))
        range_label.grid(padx=(25, 5), pady=(5, 5), sticky='w')
        self.range = tk.StringVar()
        range_name = ttk.Combobox(main_frame, width=25,
                                  values=['Select from here', "Vitamin C", "Aloe vera", "Honey Milk", "Kumkumadi"],
                                  textvariable=self.range)
        range_name.grid(padx=(25, 5), pady=(5, 5), sticky='w')

        # ------------------------------ Product Details -------------------------------

        category_label = ttk.Label(main_frame, text="Choose category of product", font=("Aharoni", 10, "bold"))
        category_label.grid(padx=(25, 5), pady=(5, 5), sticky='w')
        self.category = tk.StringVar()
        category_name = ttk.Combobox(main_frame, width=25,
                                     values=['Select from here', "Body", "Face", "Hair", "Make-Up"],
                                     textvariable=self.category)
        category_name.grid(padx=(25, 5), pady=(5, 5), sticky='w')

        ptype_label = ttk.Label(main_frame, text="Choose your product type", font=("Aharoni", 10, "bold"))
        ptype_label.grid(padx=(25, 5), pady=(5, 5), sticky='w')
        self.ptype = tk.StringVar()
        ptype_name = ttk.Combobox(main_frame, width=25,
                                  values=['Select from here', "Moisturizer", "Face Cream", "Body Lotion", "Serum"],
                                  textvariable=self.ptype)
        ptype_name.grid(padx=(25, 5), pady=(5, 5), sticky='w')

        price_label = ttk.Label(main_frame, text="Enter price", font=("Aharoni", 10, "bold"))
        price_label.grid(row=7, column=1, pady=(0, 5), sticky='w')
        self.price = tk.IntVar()
        price_value = ttk.Entry(main_frame, textvariable=self.price, width=10)
        price_value.grid(row=8, column=1, pady=(0, 5), sticky='w')

        qty_label = ttk.Label(main_frame, text="Enter quantities", font=("Aharoni", 10, "bold"))
        qty_label.grid(row=9, column=1, pady=(0, 5), sticky='w')
        self.qty = tk.IntVar()
        qty_value = ttk.Entry(main_frame, textvariable=self.qty, width=10)
        qty_value.grid(row=10, column=1, pady=(0, 5), sticky='w')

        submit_button = ttk.Button(main_frame, text="Submit", command=self.submit_details)
        submit_button.grid(row=11, padx=(25, 5), pady=(20, 5), sticky='w')
        reset_button = ttk.Button(main_frame, text="Reset")
        reset_button.grid(row=11, padx=(125, 5), pady=(20, 5), sticky='w')

    def submit_details(self):
        data = {"name": self.store.get(),
                "products":
                    [
                        {
                            "range": self.range.get(),
                            "details":
                            [
                                {
                                    "category": self.category.get(),
                                    "Description":
                                    {
                                        "gender": self.gender.get(),
                                        "product_type": self.ptype.get(),
                                        "price": self.price.get(),
                                        "quantity": self.qty.get()
                                    }
                                }
                            ]
                        }
                    ]
                }
        json_data = json.dumps(data)

        # if a store (i.e. data["name"]) exists in the database, then add products - hit the create product API
        url_item = 'http://127.0.0.1:5000/store/' + data["name"] + '/item'
        response_item = requests.post(url_item, json=data["products"][0])
        print(url_item, response_item, data["products"][0])

        # if store does not exist then hit the create store API
        url = 'http://127.0.0.1:5000/store'
        response = requests.post(url, json=data)
        print(url, response, data)

        # cursor.execute('INSERT INTO new_user VALUES (%s,%s,%s,%s,%s)',
        #                (name.get(), new_username.get(), email.get(), new_password.get(), phone.get()))
        # db.commit()
        # return json_data


app = GlamWindow()
app.mainloop()
