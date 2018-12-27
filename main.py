from threading import Thread
from random import choice

from modules.shutdowner import ShutdownByTime
from test.dream_control import DreamController
# from modules.dream_control import DreamControl            # правка от 24.12.18
from modules.voice import Voice

from constants.phrases import phrases

# СделатьЛист
# --  контроль сна (в лучшем случае - ложиться до 12 ночи, вставать в 6 - 7 утра, взависимости от пар
#     или личных предпочтнеий / запланированных дел
# -- ГУИ
# -- реализовать лог программы
# -- напсаить обработчик команд


class Bot(Thread):
    def __init__(self):
        super().__init__()
        self.shutdown = ShutdownByTime

        self.dream_controller = DreamController()
        self.dream_controller.start()

        self.voice = Voice()

        self.say_on_screen(phrases['hello_from_symbols'], voice=False)
        self.voice.talk_to_me(choice(phrases['hellos']))

        # self.dream_control = DreamControl()           # правка от 24.12.18

    def say_on_screen(self, text, voice=True):
        print('[Bot]: {}'.format(text))
        if voice:
            self.voice.talk_to_me(text)

    def user_input_check(self):
        while True:
            user_input = input(">: ").lower()
            if 'выкл' in user_input:
                self.say_on_screen('Хорошо, я выключу в {}'.format(user_input.split()[2]))
                # print('[Bot]: Лады')
                user_input_time = user_input.split()[2]
                # пофиксить и создать экземпрял в конструкторе сего класса
                ShutdownByTime(user_input_time).time_to_shutdown()

            elif 'или' in user_input:
                was_choiced = choice(user_input.split('или'))
                # print("[Bot]: {}".format(was_choiced))
                self.say_on_screen('Я думаю вариант \"{}\" верный.'.format(was_choiced))
            elif 'сколько' in user_input or 'до сна' in user_input:
                self.say_on_screen('осталось {} ч'.format(self.dream_controller.get_time_for_awareness()))

    def run(self):
        self.user_input_check()


if __name__ == '__main__':
    app = Bot()#.user_input_check()
    app.start()
