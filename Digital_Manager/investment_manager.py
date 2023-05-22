# category of Investment - EMIs, Policy, SIPs
# reference number
# Amount
# Table will contain name, username and above details, export that table in report format, date added (system default)
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image


class InvestmentTrackerWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("INVESTMENT TRACKER")
        self.geometry("320x460")
        self.iconbitmap("../Icons/briefcase.ico")

        main_frame = InvestmentTrackerFrame(self)
        main_frame.grid()


class InvestmentTrackerFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.investment_image = ImageTk.PhotoImage(Image.open('../Icons/business-case.png').resize((120, 120)))
        investment_label = ttk.Label(self, image=self.investment_image)
        investment_label.grid(padx=(100, 0), pady=(10, 0), sticky='w')

        category_label = ttk.Label(self, text="Choose category of Investment", font=("Aharoni", 10, "bold"))
        category_label.grid(padx=(72, 5), pady=(10, 5), sticky='w')
        self.category = tk.StringVar()
        category_name = ttk.Combobox(self, width=25,
                                     values=["Bonds", "Mutual Funds", "Stocks", "Policy"],
                                     textvariable=self.category)
        category_name.grid(padx=(75, 5), pady=(5, 5), sticky='w')


main = InvestmentTrackerWindow()
main.mainloop()
