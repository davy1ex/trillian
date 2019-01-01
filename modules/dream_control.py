from datetime import datetime, timedelta
from threading import Thread
from time import sleep

from modules.voice import Voice
from modules.terminal_methods import Terminal
# НадоСделать список:
# -- оповещение, когда пора спать
# -- если время больше того, когда я должен лечь
#    спать - вывести напоминание, которое предложит выключить пекарню
# -- убарть отсюда голос
# -- переписать это говно

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
            minute=00,
            second=00
        )

        hour_for_day_when_must_wake_up = time_now.hour

        # увеличивает день на +1, ЕСЛИ время больше 12 ночи, но меньше 6 утра

        self.default_time_when_must_wake_up = datetime(
            year=time_now.year,
            month=time_now.month,
            day=hour_for_day_when_must_wake_up,
            hour=6,
            minute=00,
            second=00
        )

        if not (00 <= time_now.hour <= 6):
            self.default_time_when_must_wake_up += timedelta(days=1)

        # блок, связанный с созданием потока и его первоначальной настройки
        self.running = False
        self.Thread = Thread(target=self.run)
        # self.start()

    def go_to_sleep(self):
        time_now = datetime.now()
        if self.default_time_when_must_go_sleep < time_now < self.default_time_when_must_wake_up:
            return True

    def start(self):
        if not self.running:
            self.running = True
            self.Thread.start()

    def get_time_for_delay(self):
        return (self.default_time_when_must_go_sleep - datetime.now()).seconds

    def run(self):
        time_for_sleep = self.get_time_for_delay()
        # time_for_sleep = 5
        sleep(time_for_sleep)
        while True:
            Voice().talk_to_me('Сер, кажется вам пора спать')

            # и заснуть на 30 минут, чтобы напомнить снова
            sleep(1800)

    def get_time_for_awareness(self):
        return round((self.default_time_when_must_go_sleep - datetime.now()).seconds / 3600, 1)


if __name__ == '__main__':
    dream_control = DreamController()
    dream_control.start()
