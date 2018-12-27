import os
import platform

from threading import Thread
from datetime import datetime
from time import sleep


#
# ToDO:
# -- определить что это за система и какой к ней нужен подход
# -- вывести уведомление об отключении за 5 минут
#

if '__main__' != __name__:
    print('Модуль \"Shutdowner\" активирован')


class ShutdownByTime:
    def __init__(self, time_when_power_off):

        self.running = False
        self.thread = Thread(target=self.run)

        self.time_when_poweroff = datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            hour=int(time_when_power_off[0:2]),
            minute=int(time_when_power_off[3:5]),
        )

    def time_to_shutdown(self):
        delta = self.time_when_poweroff - datetime.now()

        if not self.running:
            self.running = True
            self.thread.start()

        return delta.seconds

    def check(self):
        sleep(int(self.time_to_shutdown()))
        # print('*выключил*')
        # if os.name() == 'Linux':
        #     os.system('poweroff')
        # else:
        #     os.system("shutdown -l")
        name_os = platform.system()         # возвращает что-то типа -> "Windows"
        if name_os == 'Linux':
            os.system('poweroff')
        else:
            os.system('shutdown -l')

    def run(self):
        self.check()
