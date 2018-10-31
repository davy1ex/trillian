import os
from threading import Thread
from datetime import datetime


class TurnOff_By_Time:
    def __init__(self):
        self.running = False
        self.thread = Thread(target=self.run)
        self.time_when_power_off = None

    def set_data(self, time_when_power_off):
        self.time_when_power_off = datetime(year=datetime.now().year,
                                            month=datetime.now().month,
                                            day=datetime.now().day,
                                            hour=int(time_when_power_off[0:2]),
                                            minute=int(time_when_power_off[3:5]),
                                            )
        print("Хорошо, я выключу в ", self.time_when_power_off)
        if not self.running:
            self.running = True
            self.thread.start()

    def check(self):
        if self.time_when_power_off == datetime.now():
            print("*Выключил*")
            # os.system("poweroff")

    def run(self):
        while self.running:
            self.check()
