from datetime import datetime, timedelta
from threading import Thread
from time import sleep

from modules.voice import Voice


# Сделать:
# -- реализовать напоминание, которое предложит выключить пекарню

# просто для красоты
if '__main__' != __name__:
    print('{0}: активирован'.format(__name__))


class DreamController:
    def __init__(self):
        """ устанавливает необходимые переменные """
        # переменные, отвечающие за распорядок дня (время)
        time_now = datetime.now()
        self.default_time_when_must_go_to_sleep = datetime(            # отбой
            year=time_now.year,
            month=time_now.month,
            day=time_now.day,
            hour=22,
            minute=0,
            second=0
        )

        self.default_time_when_must_wake_up = datetime(             # подъём
            year=time_now.year,
            month=time_now.month,
            day=time_now.day,
            hour=6,
            minute=0,
            second=0
        )

        # увеличивает день на +1, ЕСЛИ время больше 6 утра (когда просыпаться пора)
        if 0 < time_now.hour <= self.default_time_when_must_wake_up.hour:
            self.default_time_when_must_go_to_sleep -= timedelta(days=1)

        # блок, связанный с созданием потока и его первоначальной настройкой и запуском
        self.running = False
        Thread(target=self.run).start()

    def get_time_for_delay(self):
        """ вычисляет количество секунд для задержки:
            ЕСЛИ не сплю, когда уже надо - оповещает об этом сразу
            ИНАЧЕ время до того, пока не надо будет спать"""
        if self.default_time_when_must_go_to_sleep <= datetime.now():
            delay = 0
        else:
            delay = (self.default_time_when_must_go_to_sleep - datetime.now()).seconds
        return delay

    def run(self):
        """ останавливает выполнение (time.sleep() до нужного момента,
            далее уведомляет, что пора спать и засыпает снова на 30 минут """
        time_for_sleep = self.get_time_for_delay()
        sleep(time_for_sleep)
        while True:
            Voice().say_to_me('Сер, кажется вам пора спать')

            # и заснуть на 10 минут, чтобы напомнить снова
            sleep(600)

    def get_time_for_awareness(self):
        """ возвращает время через сколько пора спать. Хз на кой мне это, но пусть будет """
        return self.default_time_when_must_go_to_sleep - datetime.now()
