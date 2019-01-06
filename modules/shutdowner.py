import os
import platform

from threading import Thread
from datetime import datetime
from time import sleep


# НадоСделать:
# -- определить что это за система и какой к ней нужен подход
# -- вывести уведомление об отключении за 5 минут
# -- добавить обработчик исключений на случай того, если руки начнут расти из жопы


if '__main__' != __name__:
    print('{0}: активирован'.format(__name__))


class ShutdownByTime:
    def __init__(self, time_when_power_off):
        self.time_when_poweroff = datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            hour=int(time_when_power_off[0:2]),
            minute=int(time_when_power_off[3:5]),
        )
        Thread(target=self.run).start()

    def run(self):
        while True:
            # не будет работать до момента когда надо выключить пекарню
            sleep((self.time_when_poweroff - datetime.now()).seconds)

            # проверяет тип системы и выключает её
            name_os = platform.system()  # возвращает что-то типа -> "Windows"
            if name_os == 'Linux':          # linux
                os.system('poweroff')                
            else:
                os.system('shutdown -s')    # windows
