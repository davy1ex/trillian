import os
import threading
from datetime import datetime


class TurnOff_By_Time(threading.Thread):
    def __init__(self, time_when_power_off):
        super().__init__()
        self.time_when_power_off = datetime(year=datetime.now().year,
                                            month=datetime.now().month,
                                            day=datetime.now().day,
                                            hour=int(time_when_power_off[0:2]),
                                            minute=int(time_when_power_off[3:5]),
                                            )
        # print("Хорошо, я выключу в ", self.time_when_power_off)
        # while True:
        #     self.check()

    def check(self):
        if self.time_when_power_off == datetime.now():
            print("*Выключил*")
            # os.system("poweroff")

    def run(self):
        print("Хорошо, я выключу в ", self.time_when_power_off)     # вывод исправлю
        while True:
            self.check()