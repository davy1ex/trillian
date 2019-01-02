from datetime import datetime, timedelta
from threading import Thread
from time import sleep

from modules.voice import Voice
from modules.terminal_methods import Terminal


# НадоСделать список:
# -- если время больше того, когда я должен лечь
#    спать - вывести напоминание, которое предложит выключить пекарню
# -- убарть отсюда голос


if '__main__' != __name__:
    print('{0}: активирован'.format(__name__))


class DreamController:
    def __init__(self):
        # задаёт переменные, отвечающие за распорядок дня (время)

        time_now = datetime.now()
        self.default_time_when_must_go_sleep = datetime(
            year=time_now.year,
            month=time_now.month,
            day=time_now.day,
            hour=22,
            minute=0,
            second=0
        )

        self.default_time_when_must_wake_up = datetime(
            year=time_now.year,
            month=time_now.month,
            day=time_now.hour,
            hour=6,
            minute=0,
            second=0
        )

        # увеличивает день на +1, ЕСЛИ время больше 6 утра (когда просыпаться пора)
        if not (6 < time_now.hour):
            self.default_time_when_must_wake_up += timedelta(days=1)

        # блок, связанный с созданием потока и его первоначальной настройкой и запуском
        self.running = False
        Thread(target=self.run).start()

    def get_time_for_delay(self):
        if datetime.now().hour < 0:
            delay = (self.default_time_when_must_go_sleep - datetime.now()).seconds
        else:
            delay = 0
        return delay

    def run(self):
        time_for_sleep = self.get_time_for_delay()
        sleep(time_for_sleep)
        while True:
            Voice().say_to_me('Сер, кажется вам пора спать')

            # и заснуть на 10 минут, чтобы напомнить снова
            sleep(600)

    def get_time_for_awareness(self):
        # возвращает время через сколько пора спать. Хз на кой я это реализовал, но пусть будет.
        # return round((self.default_time_when_must_go_sleep - datetime.now()).seconds / 3600, 1)
        return self.default_time_when_must_go_sleep - datetime.now()
