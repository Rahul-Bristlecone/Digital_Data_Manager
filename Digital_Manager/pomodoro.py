import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# This is the main window which will contain the timer frame which has all application related widgets
# Now testing....
# final testing for rebase and remote branch RS_202_dev
class TimerWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TIMER")
        self.geometry("240x360")
        self.iconbitmap("C:\\Users\\Rahul.Sharma4\\PycharmProjects\\pythonProject1\\Icons\\briefcase.ico")
        self.resizable(False, False)

        timer_frame = TimerFrame(self)
        timer_frame.grid()


class TimerFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container)
        self.timer_running = False

        timer_label_frame = ttk.Frame(self)
        timer_label_frame.grid()

        self.time_image = ImageTk.PhotoImage(Image.open('../Icons/timer_watch.png').resize((85, 85)))
        timer_image = ttk.Label(timer_label_frame, image=self.time_image)
        timer_image.grid(padx=(32, 0), pady=(20, 0), sticky='w')

        timer_style = ttk.Style()
        timer_style.configure("CustomLabelStyle.TLabel", font=("Tahoma", 15), padding=(20, 10))

        self.result = tk.StringVar(value="00:00")
        self.timer_label = ttk.Label(timer_label_frame,
                                     textvariable=self.result,
                                     style="CustomLabelStyle.TLabel")
        self.timer_label.grid(padx=(29, 5), sticky='w')

        timer_button_frame = ttk.Frame(self)
        timer_button_frame.grid()

        style = ttk.Style()
        style.configure("CustomLabelStyle.TButton", font=("Tahoma", 10))

        self.minute_value = tk.StringVar()
        start_min_value = ttk.Entry(timer_button_frame, textvariable=self.minute_value, width=4)
        start_min_value.grid(row=0, padx=(35, 5), sticky='w')
        colon = ttk.Label(timer_button_frame, text=":", font=("Tahoma", 15))
        colon.grid(row=0, padx=(65, 5), sticky='w')
        self.second_value = tk.StringVar()
        start_sec_value = ttk.Entry(timer_button_frame, textvariable=self.second_value, width=4)
        start_sec_value.grid(row=0, padx=(75, 5), sticky='w')

        self.start = ttk.Button(timer_button_frame,
                                text="Start",
                                style="CustomLabelStyle.TButton",
                                command=self.start_timer)
        self.start.grid(row=0, padx=(120, 10), pady=(0, 0), sticky='w')
        self.stop = ttk.Button(timer_button_frame,
                               text="Stop",
                               style="CustomLabelStyle.TButton",
                               command=self.stop_timer)
        self.stop.grid(row=1, padx=(120, 10), pady=(5, 0), sticky='w')
        self.reset = ttk.Button(timer_button_frame,
                                text="Reset",
                                style="CustomLabelStyle.TButton",
                                command=self.reset_timer, )
        self.reset.grid(row=2, padx=(120, 10), pady=(5, 0), sticky='w')

    # self.minute_value.get() + ":" + self.second_value.get()
    def timer_time(self):
        self.result.set(self.minute_value.get() + ":" + self.second_value.get())

    def start_timer(self, *args):
        try:
            if not self.timer_running and not self.result.get() == "00:00":
                self.timer_running = True
                self.result.get()
                # self.timer_time()
                self.start["state"] = "disabled"
                self.stop["state"] = "enabled"
                self.dec_sec()
            else:
                self.timer_running = True
                self.result.get()
                self.timer_time()
                self.start["state"] = "disabled"
                self.stop["state"] = "enabled"
                self.dec_sec()
        except:
            self.result.set("00:00")
            timer_error = ttk.Label(self, text=" Please Enter correct values", font=("Aharoni", 10, "bold"))
            timer_error.grid(padx=(25, 5), pady=(20, 5))
            self.after(1000, timer_error.destroy)
            self.start["state"] = "enabled"

    def stop_timer(self):
        self.timer_running = False
        self.stop["state"] = "disabled"
        self.start["state"] = "enabled"
        print(self.result.get())
        print(self.timer_running)
        # self.dec_sec()

    def reset_timer(self):
        self.timer_running = False
        self.start["state"] = "enabled"
        self.stop["state"] = "enabled"
        self.result.set("00:00")
        self.minute_value.set("")
        self.second_value.set("")
        # self.dec_sec()

    def dec_sec(self):
        current_sec = self.result.get()
        if self.timer_running and current_sec != "00:00":
            minutes, seconds = current_sec.split(":")
            if int(seconds) > 0:
                seconds = int(seconds) - 1
                minutes = int(minutes)
            else:
                seconds = 59
                minutes = int(minutes) - 1
            self.result.set(f"{minutes:02d}:{seconds:02d}")
            self.after(1000, self.dec_sec)


# start_time = time.perf_counter()
# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
app = TimerWindow()
app.mainloop()
