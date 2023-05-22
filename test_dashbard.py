import unittest
from tkinter import Tk, ttk


class TestCalculator(unittest.TestCase):
    def setUp(self):
        Dashboard.dashboard = Tk()
        notebookStyle = ttk.Style()
        notebookStyle.configure('Custom.TNotebook.Tab', padding=(30, 4), font=("Calibri", 10, "bold"))
        dashboard_tabs = ttk.Notebook(Dashboard.dashboard, style="Custom.TNotebook")
        dashboard_tabs.pack(expand=1, fill="both")
        Dashboard.existing_user_tab = ttk.Frame(dashboard_tabs)
        Dashboard. dashboard_tabs.add(Dashboard.existing_user_tab, text=" EXISTING USER", image=Dashboard.exist_user_image, compound="left")
        username = ttk.StringVar()
        Dashboard.username_entry = ttk.Entry(Dashboard.existing_user_tab, textvariable=username, font=("Calibri", 11, "bold"), width=30)
        Dashboard.username_entry.grid(pady=(5, 0), padx=62)
        Dashboard.username_entry.focus()

    def tearDown(self):
        Dashboard.username_entry.destroy()

    def reset(self):
        Dashboard.username_entry.delete(0, 'end')

    def test_reset_button(self):
        Dashboard.username_entry.insert(0, '12345')
        Dashboard.reset.invoke()
        self.assertEqual(Dashboard.username_entry.get(), '')


if __name__ == '__main__':
    unittest.main()
