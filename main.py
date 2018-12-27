from threading import Thread
from random import choice

from modules.shutdowner import ShutdownByTime
# from modules.dream_control import DreamControl            # правка от 24.12.18
from modules.voice import Voice

from constants.phrases import phrases

# СделатьЛист
# --  контроль сна (в лучшем случае - ложиться до 12 ночи, вставать в 6 - 7 утра, взависимости от пар
#     или личных предпочтнеий / запланированных дел
# -- ГУИ
# -- реализовать лог программы


class Bot(Thread):
    def __init__(self):
        super().__init__()
        # print(phrases["hello_from_symbols"])
        self.say_on_screen(phrases['hello_from_symbols'])
        # talk_to_me(choice(phrases['hellos']))
        self.shutodwn = ShutdownByTime
        Voice().talk_to_me(choice(phrases['hellos']))

        # self.dream_control = DreamControl()           # правка от 24.12.18

    def say_on_screen(self, text):
        print('[Bot]: {}'.format(text))

    def user_input_check(self):
        while True:
            user_input = input(">: ").lower()
            if 'выкл' in user_input:
                Voice().talk_to_me('Хорошо, я выключу в {}'.format(user_input.split()[2]))
                # print('[Bot]: Лады')
                self.say_on_screen('Хорошо')
                user_input_time = user_input.split()[2]
                ShutdownByTime(user_input_time).time_to_shutdown()
            # код ниже немного сломался. Починю позже.
            # elif "когда" in user_input and "вставать" in user_input:          # правка от 24.12.18
            #     print("Через", self.dream_control.calculate_time_to_wake_up())            # правка от 24.12.18

            # elif "когда" in user_input and ("ложиться" in user_input or "спать" in user_input):           # правка от 24.12.18
                # print("Через", self.dream_control.calculate_time_to_go_to_sleep())            # правка от 24.12.18

            elif 'или' in user_input:
                was_choiced = choice(user_input.split('или'))
                # print("[Bot]: {}".format(was_choiced))
                self.say_on_screen('Я думаю вариант \"{}\" верный.'.format(was_choiced))
                Voice().talk_to_me('Я думаю вариант \"{}\" верный.'.format(was_choiced))

    def run(self):
        self.user_input_check()


if __name__ == '__main__':
    app = Bot()#.user_input_check()
    app.start()
