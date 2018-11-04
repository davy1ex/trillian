from threading import Thread
from datetime import datetime


class ShutdownByTime:
    def __init__(self):
        self.running = False
        self.thread = Thread(target=self.run)

        self.time_when_poweroff = None

    def get_data(self, time_when_power_off):
        self.time_when_poweroff = datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            hour=int(time_when_power_off[0:2]),
            minute=int(time_when_power_off[3:5]),
        )
        print("Хорошо. Я выключу в ", time_when_power_off)

        if not self.running:
            self.running = True
            self.thread.start()

    def check(self):
        if self.time_when_poweroff == datetime.now():
            print("*выключил*")

    def run(self):
        while True:
            self.check()