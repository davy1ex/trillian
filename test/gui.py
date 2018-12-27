import tkinter as tk
import os


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.init_main()

    def init_main(self):
        pass


class ChildWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.text_to_display = None

    def shutdown_window(self, text_to_show):
        self.text_to_display = text_to_show

        self.root.title("helpAssistant")
        self.root["bg"] = "black"
        self.root.resizable(False, False)
        lbl = tk.Label(text=self.text_to_display, bg="black", foreground="white", fg="lightgrey")
        btn_ignore = tk.Button(text="Проигнорировать",
                               activebackground="white",
                               bg="black",
                               foreground="white",
                               command=lambda: self.root.destroy()
                               )
        btn_poweroff = tk.Button(text="Выключить компьютер",
                                 activebackground="white",
                                 bg="black",
                                 foreground="white",
                                 command=lambda: os.system("poweroff"),
                                 # bd=2
                                 )

        lbl.pack(side=tk.TOP)
        btn_ignore.pack()
        btn_poweroff.pack()

        self.root.update_idletasks()
        self.root.overrideredirect(1)
        self.root.wm_attributes("-topmost", 1)
