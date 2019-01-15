# import tkinter as tk

from datetime import datetime, timedelta
from threading import Thread
from time import sleep

# from modules.gui import ChildWindow
from test.true_parser import Parser


#
# ToDo:
# -- если запуск просиходит позже времени когда должен ложиться спать - сообщить об этом
#


class DreamControl:
    def __init__(self):
        print('Модуль \'Dream_control\' активирован')
        self.time_when_wake_up = datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=(datetime.now() + timedelta(days=1)).day,
            hour=6,
            minute=00,
            second=00
        )

        # self.time_when_must_go_to_sleep = datetime(
        #     year=datetime.now().year,
        #     month=datetime.now().month,
        #     day=datetime.now().day,
        #     hour=22,
        #     minute=00,
        #     second=00
        # )


        self.running = False
        self.tomorrow_learn = True

        self.time_now = None
        self.time_to_sleep = 0
        self.time_when_must_go_to_sleep = self.calculate_time_when_must_go_to_sleep()
        self.Thread = Thread(target=self.run)

        self.start()

    def strfdelta(self, tdelta, fmt):
        # взято со stackowerflow
        d = {'days': tdelta.days}
        d['hours'], rem = divmod(tdelta.seconds, 3600)
        d['minutes'], d['seconds'] = divmod(rem, 60)
        return fmt.format(**d)

    def start(self):
        delta = self.time_when_must_go_to_sleep - datetime.now()
        self.time_to_sleep = delta.seconds
        if not self.running:
            self.running = True
            print('(модуль контроля сна активирован)')
            self.Thread.start()

    def calculate_time_to_wake_up(self):
        self.time_now = datetime.now()
        return self.strfdelta(
                    self.time_when_wake_up - self.time_now,
                    fmt='{hours} часа(ов) и {minutes} минут(ы)'
                )

    def calculate_time_to_go_to_sleep(self):
        self.time_now = datetime.now()
        return self.strfdelta(
                    self.time_when_must_go_to_sleep - self.time_now,
                    fmt='{hours} часа(ов) и {minutes} минут(ы)'
                )

    def calculate_time_when_must_go_to_sleep(self):
        day_today = datetime.today().weekday()
        # day_today = 1
        time = Parser().get_rasp()[int(day_today)]['start']
        if len(time) == 0:
            self.tomorrow_learn = False
            time = '08:00'

        if time.split(':')[0][0] == '0':
            time = time.replace('0', '', 2)

        delta = 1
        if 0 <= datetime.now().hour <= 6:
            delta = 0
        time_when_start_first_lesson = datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day + delta,
            hour=int(time.split(':')[0]),
            minute=int(time.split(':')[1]),
            second=00
        )

        time_when_must_wake_up = time_when_start_first_lesson - timedelta(hours=2)
        time_when_must_go_to_sleep = time_when_must_wake_up - timedelta(hours=8, minutes=15)
        if not self.tomorrow_learn:
            print('Завтра пар нет. Я посчитаю, что вы будете соблюдать режим и ляжете в 10 вечера.')
        return time_when_must_go_to_sleep

    def run(self):
        print('[Bot]: Напомню вам в {}, что пора ложиться спать'.format(self.time_when_must_go_to_sleep.strftime('%H:%M')))
        while True:
            sleep(self.time_to_sleep)
            self.time_to_wake_up = self.calculate_time_to_wake_up()
            print('Сер, спать осталось всего лишь', self.time_to_wake_up)
            self.time_to_sleep = 1800


if __name__ == '__main__':
    DreamControl()
