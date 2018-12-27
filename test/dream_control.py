from datetime import datetime, timedelta
from threading import Thread
from time import sleep

# НадоСделать список:
# -- оповещение, когда пора спать
# -- если время больше того, когда я должен лечь спать - вывести напоминание, которое предложит выключить пекарню

if '__main__' != __name__:
    print('Тестовый модуль контроля сна активирован.')


class DreamControl:
    def __init__(self):
        super().__init__()
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

        day_when_must_wake_up = time_now.hour

        # увеличивает день на +1, ЕСЛИ время больше 12 ночи, но меньше 6 утра
        if not 00 <= time_now.hour <= 6:
            day_when_must_go_on = time_now.day + 1

        self.default_time_when_must_wake_up = datetime(
            year=time_now.year,
            month=time_now.month,
            day=day_when_must_wake_up,
            hour=6,
            minute=00,
            second=00
        )

        # блок, связанный с созданием потока и его первоначальной настройки
        self.running = True
        self.Thread = Thread(target=self.run)
        self.start()

    def time_to_sleep(self):
        time_now = datetime.now()
        if self.default_time_when_must_go_sleep < time_now < self.default_time_when_must_wake_up:
            return True

    def start(self):
        self.running = True
        pass

    def get_time_for_sleep(self):
        return (self.default_time_when_must_go_sleep - datetime.now()).seconds

    def run(self):
        time_for_sleep = self.get_time_for_sleep()
        print('Напомню тебе о сне через {} секунд.'.format(time_for_sleep))
        while True:
            sleep(time_for_sleep)
            print('Типа спать пора')
        # if self.time_to_sleep == True:


if __name__ == '__main__':
    dream_control = DreamControl()
    print(dream_control.get_time_for_sleep())
