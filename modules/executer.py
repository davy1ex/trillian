# берёт на себя приём и выполнение команд пользователя
# пихая первое и второе в отдельные потоки
# (тестовая версия)

from threading import Thread
from random import choice

from modules.shutdowner import ShutdownByTime
from modules.dream_control import DreamController
from modules.terminal_methods import Terminal


class Executer:
    def __init__(self):
        user_input = None
        
        # self.listen_thread = Thread(target=self.listen).start()
        # self.do_thread = Thread(target=self.do).start()


        self.dream_control = DreamController()
        self.shutdown_by_time = ShutdownByTime        
        self.terminal = Terminal()

        while True:
            self.do(self.listen())

    def listen(self):
        return input('>: ')

    def do(self, user_input):
        if 'выкл' in user_input:
            self.shutdown_by_time(user_input.split()[2])
            self.terminal.print('Хорошо. Выключу в {}'.format(user_input.split()[2]))

        elif 'или' in user_input:
            was_choiced = choice(user_input.split('или'))

            if was_choiced[0] == ' ':
                was_choiced = was_choiced.replace(' ', '', 1)

            self.terminal.print(was_choiced)

        elif 'сколько' in user_input or 'до сна' in user_input:
            time = self.dream_control.get_time_for_awareness()
            self.terminal.print('{0} ч'.format(round(time.seconds / 3600, 1)))

        elif 'test' in user_input or 'тест' in user_input:
            self.terminal.print('I\'m ok')

        user_input = None


if __name__ == '__main__':
    executer = Executer()
