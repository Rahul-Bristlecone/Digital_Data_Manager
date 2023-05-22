# Take help from testing.py for opening a new window

import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

if __name__ == '__main__':
    from Digital_Manager import unit_converter


class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.onclick = None
        self.converter_image = None
        self.title("Home Page")
        self.geometry("320x400")

        def open_converter():
            objconveter = tk.Toplevel(unit_converter.ConverterWindow())
            objconveter.grab_set()

        self.converter_image = ImageTk.PhotoImage(Image.open('../Icons/converter.png').resize((75, 75)))
        converter_image = ttk.Button(self, image=self.converter_image, text="converter", compound="top",
                                     command=open_converter)
        converter_image.grid(padx=(35, 0), pady=(35, 0), sticky='w')


main = HomePage()
main.mainloop()
