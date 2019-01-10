# берёт на себя приём и выполнение команд пользователя

import os, sys
from random import choice

from modules.shutdowner import ShutdownByTime
from modules.dream_control import DreamController
from modules.terminal_methods import Terminal
from modules.test.mic import Mic
from modules.voice import Voice
from modules.test import sr_test


# НадоСделать:
# -- обработчик исключений (для выключения, например)


class Executer:
    def __init__(self):
        self.dream_control = DreamController()
        self.shutdown_by_time = ShutdownByTime
        self.terminal = Terminal()

        self.voice = Voice()
        self.mic = Mic()

        while True:

            self.do(self.mic.what_iam_say())

    def listen(self):
        return input('>: ')

    def do(self, user_input):
        if 'выкл' in user_input:
            """ выключает пекарню в заданное пользователем время """
            # образец команды - "выключи в 00:00"
            if len(user_input.split(' ')) >= 3:
                time = user_input.split()[2]
            else:
                time = user_input.split(' ')[1]
            if len(time) >  4:
                time = time[0:2] + ':' + time[3:]
            else:
                time = time[0:2] + ':' + time[2:]
            self.shutdown_by_time(time)
            self.terminal.print('Хорошо. Выключу в {}'.format(time))
            self.voice.say_to_me('Хорошо. Выключу.')

        elif 'или' in user_input:
            """ помогает юзеру сделать сложный выбор """
            # делит строку и рандомно выбирает то или это
            was_choiced = choice(user_input.split('или'))

            # чтобы пробелов не было
            if was_choiced[0] == ' ':
                was_choiced = was_choiced.replace(' ', '', 1)

            self.terminal.print(was_choiced)
            self.voice.say_to_me(was_choiced)

        elif 'сколько' in user_input or 'до сна' in user_input:
            """ выводит время на бодрствование """                              # формат: "4,5 ч"
            # та самая непонятно зачем функция, даже то, что ниже полезнее
            time = self.dream_control.get_time_for_awareness()
            self.terminal.print('{0} ч'.format(round(time.seconds / 3600, 1)))

        elif 'test' in user_input or 'тест' in user_input or 'триллиан' in user_input or 'ты здесь' in user_input:
            """ если всё работает, выводит, что работает """
            # просто узнать, что ничего не сломал
            self.terminal.print('Работаю')
            self.voice.say_to_me('Да, я вас слушаю')

        elif 'рабочий стол' in user_input:
            os.system('wmctrl -k on')

        elif 'обратно' in user_input or 'верни' in user_input or 'разверни' in user_input:
            os.system('wmctrl -k off')

        elif 'заблокируй' in user_input:
            os.system('xflock4')


if __name__ == '__main__':
    executer = Executer()
