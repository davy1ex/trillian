import tkinter as tk
import os
from constants.phrases import phrases


class MainWindow(tk.Frame):
    def __init__(self):#, title, width=None, height=None):
        self.root = tk.Tk()
        super().__init__(self.root)
        # self.root = root
        # self.init_main(title, width, height)

        self.command_after_press_on_enter = ''

    def init_main(self,title, width=None, height=None):
        if width!=None and height != None:
            self.root.geometry('{0}x{1}'.format(width, height))
        self.root.title(title)

        self.output_window = tk.Text(
            bg='black',
            highlightthickness=0,
            height=20,
            foreground='white'
        )
        self.input_line = tk.Entry(
            bg='black',
            highlightthickness=0,
            foreground='white'
        )

        # packing
        self.root.bind('<Return>', self.return_key)

        self.output_window.pack(side=tk.TOP, fill=tk.X)
        self.input_line.pack(side=tk.BOTTOM, fill=tk.X)

    def output_text(self, text):
        self.output_window.config(state=tk.NORMAL)
        self.output_window.insert(tk.END, '[BOT]: {}'.format(text))
        self.output_window.config(state=tk.DISABLED)

    def return_key(self, event):
        self.input_line.delete(0, tk.END)
        eval(self.command_after_press_on_enter)

    def run(self):
        # self.root = tk.Tk()
        self.init_main(title='helpAssistant', width=800, height=340)
        self.output_text(phrases['hello'])
        self.root.mainloop()



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


if __name__ in '__main__':
    root = tk.Tk()
    app = MainWindow(root,  title='test', width=800, height=340)
    app.command_after_press_on_enter = 'print(\'хуй\')'
    # app.bind_keys('Return', app.output_text('dggsd'))
    app.output_text('здрасьте')
    root.mainloop()
