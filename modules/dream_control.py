import tkinter as tk

from datetime import datetime, timedelta
from threading import Thread, Timer
from time import sleep

from modules.gui import ChildWindow


class DreamControl:
    def __init__(self):
        self.time_when_wake_up = datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=(datetime.now() + timedelta(days=1)).day,
            hour=6,
            minute=00,
            second=00
        )

        self.time_when_must_go_to_sleep = datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            hour=22,
            minute=00,
            second=00
        )
        self.Thread = Thread(target=self.run)
        self.running = False

        self.time_now = None

        self.start()

    def start(self):
        if not self.running:
            self.running = True
            print("(модуль контроля сна активирован)")
            Timer(4, self.run).start()
            self.Thread.start()

    def check(self):
        if self.running:
            self.time_now = datetime.now()
            # if self.time_when_must_go_to_sleep <= self.time_now <= self.time_when_wake_up:
            if datetime.strftime(self.time_now, "%H:%M") == "21:00":
                    print("хуй")
                    time_to_wake_up = self.calculate_time_to_wake_up()
                    root = tk.Tk()
                    poweroff_window = ChildWindow(root).shutdown_window("Спать пора. Блядь.")
                    root.mainloop()
                    # print("Сер, спать осталось всего лишь", time_to_wake_up)
                    # sleep(1800)
                    # sleep(4)

    def calculate_time_to_wake_up(self):
        self.time_now = datetime.now()
        return self.strfdelta(
                    self.time_when_wake_up - self.time_now,
                    fmt="{hours} часа(ов) и {minutes} минут(ы)"
                )

    def strfdelta(self, tdelta, fmt):
        d = {"days": tdelta.days}
        d["hours"], rem = divmod(tdelta.seconds, 3600)
        d["minutes"], d["seconds"] = divmod(rem, 60)
        return fmt.format(**d)

    def run(self):
        while True:
            self.check()
