import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image


class ConverterWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("UNIT CONVERTER")
        self.geometry("280x360")
        self.iconbitmap("C:\\Users\\Rahul.Sharma4\\PycharmProjects\\pythonProject1\\Icons\\briefcase.ico")
        self.resizable(False, False)

        self.converter_frames = dict()

        main_frame = ttk.Frame(self)
        main_frame.grid(padx=60, pady=30, sticky="EW")

        feet2meter_frame = Feet2Meter(main_frame, self)
        feet2meter_frame.grid(row=0, column=0, sticky="NSEW")

        meter2feet_frame = Meter2Feet(main_frame, self)
        meter2feet_frame.grid(row=0, column=0, sticky="NSEW")

        self.converter_frames[Feet2Meter] = feet2meter_frame
        self.converter_frames[Meter2Feet] = meter2feet_frame

        # for selectframe in (Feet2Meter, Meter2Feet):
        #     frame = selectframe(main_frame,self)
        #     self.converter_frames[selectframe] = frame
        #     frame.grid()

    def show_frames(self, container):
        frame = self.converter_frames[container]
        frame.tkraise()


class Feet2Meter(ttk.Frame):
    # Kwargs takes keyword arguments like grid and all, controller will take an argument needed for switch
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.converter_image = ImageTk.PhotoImage(Image.open('../Icons/converter.png').resize((75, 75)))
        converter_label = ttk.Label(self, image=self.converter_image, compound="top")
        converter_label.grid(padx=(40, 0), pady=(10, 0), sticky='w')

        self.select_type = tk.StringVar()
        conversion_type = ttk.Combobox(self, textvariable=self.select_type, font=("Calibri", 10, "bold"))
        conversion_type["values"] = ("Length", "Area", "Volume", "Weight", "Temperature")
        conversion_type["state"] = "readonly"
        conversion_type.current(0)
        conversion_type.grid(pady=(5, 5), padx=(5, 0), sticky='w')

        self.meters = tk.StringVar()
        meter_entry = ttk.Entry(self, textvariable=self.meters)
        meter_entry.grid(pady=(5, 5), padx=(5, 0), sticky='w')

        meters_label = ttk.Label(self, text="Meters")
        meters_label.grid(row=2, pady=(5, 5), padx=(135, 0), sticky='w')

        self.feets = tk.StringVar()
        feets_entry = ttk.Entry(self, textvariable=self.feets)
        feets_entry.grid(pady=(5, 5), padx=(5, 0), sticky='w')

        feet_label = ttk.Label(self, text="Feets")
        feet_label.grid(row=3, pady=(5, 5), padx=(135, 0), sticky='w')

        click = ttk.Button(self, text="Convert", command=self.convert)
        click.grid(row=5, pady=(5, 5), padx=(5, 0), sticky='w')

        switch = ttk.Button(self, text="Switch", command=lambda: controller.show_frames(Meter2Feet))
        switch.grid(row=5, pady=(5, 5), padx=(95, 0), sticky='w')

    def convert(self):
        meter_value = float(self.meters.get())
        feet_value = meter_value * 3.2808
        self.feets.set(f"{feet_value:.2f}")


class Meter2Feet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):  # takes keyword arguments like grid and all
        super().__init__(container, **kwargs)

        self.converter_image = ImageTk.PhotoImage(Image.open('../Icons/converter.png').resize((75, 75)))
        converter_label = ttk.Label(self, image=self.converter_image, compound="top")
        converter_label.grid(padx=(40, 0), pady=(10, 0), sticky='w')

        self.select_type = tk.StringVar()
        conversion_type = ttk.Combobox(self, textvariable=self.select_type, font=("Calibri", 10, "bold"))
        conversion_type["values"] = ("Length", "Area", "Volume", "Weight", "Temperature")
        conversion_type["state"] = "readonly"
        conversion_type.current(0)
        conversion_type.grid(pady=(5, 5), padx=(5, 0), sticky='w')

        self.feets = tk.StringVar()
        feets_entry = ttk.Entry(self, textvariable=self.feets)
        feets_entry.grid(pady=(5, 5), padx=(5, 0), sticky='w')

        feet_label = ttk.Label(self, text="Feets")
        feet_label.grid(row=2, pady=(5, 5), padx=(135, 0), sticky='w')

        self.meters = tk.StringVar()
        meter_entry = ttk.Entry(self, textvariable=self.meters)
        meter_entry.grid(pady=(5, 5), padx=(5, 0), sticky='w')

        meters_label = ttk.Label(self, text="Meters")
        meters_label.grid(row=3, pady=(5, 5), padx=(135, 0), sticky='w')

        click = ttk.Button(self, text="Convert", command=self.convert)
        click.grid(row=5, pady=(5, 5), padx=(5, 0), sticky='w')

        switch = ttk.Button(self, text="Switch", command=lambda: controller.show_frames(Feet2Meter))
        switch.grid(row=5, pady=(5, 5), padx=(95, 0), sticky='w')

    def convert(self):
        feet_value = float(self.feets.get())
        meter_value = feet_value * 0.3048
        self.meters.set(f"{meter_value:.2f}")


track = ConverterWindow()
track.mainloop()
