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
        self.user_input = None
        
        self.listen_thread = Thread(target=self.listen).start()
        self.do_thread = Thread(target=self.do).start()

        self.dream_control = DreamController()
        self.shutdown_by_time = ShutdownByTime        
        self.terminal = Terminal()

    def listen(self):
        while True:
            if not self.user_input:
                self.user_input = input('>: ')

    def do(self):
        while True:
            if self.user_input is not None:
                if 'выкл' in self.user_input:
                    self.shutdown_by_time(self.user_input.split()[2]).thread.start()
                    self.terminal.print('Хорошо. Выключу в {}'.format(self.user_input.split()[2]))

                elif 'или' in self.user_input:
                    was_choiced = choice(self.user_input.split('или'))

                    if was_choiced[0] == ' ':
                        was_choiced = was_choiced.replace(' ', '', 1)

                    self.terminal.print(was_choiced)

                elif 'сколько' in self.user_input or 'до сна' in self.user_input:
                    self.terminal.print(self.dream_control.get_time_for_awareness())

                elif 'test' in self.user_input or 'тест' in self.user_input:
                    self.terminal.print('I\'m ok')

                self.user_input = None


if __name__ == '__main__':
    executer = Executer()
