from threading import Thread
from random import choice

from test.shutdowner import ShutdownByTime
# from modules.dream_control import DreamControl
from constants.phrases import phrases
from test.gui import MainWindow


class Bot(Thread):
    def __init__(self):
        super().__init__()
        print(phrases["hello"])
        # self.dream_control = DreamControl()

        self.main_window = MainWindow()

    def user_input_check(self):
        while True:
            user_input = self.main_window.input_line.get()
            print(user_input)
            if "выкл" in user_input:
                print('[Bot]: Лады')
                user_input_time = user_input.split()[2]
                ShutdownByTime(user_input_time).time_to_shutdown()

            elif "когда" in user_input and "вставать" in user_input:
                print("Через", self.dream_control.calculate_time_to_wake_up())

            elif "когда" in user_input and ("ложиться" in user_input or "спать" in user_input):
                # print("Через {0}ч {1}м.".format(self.dream_control.time_when_must_go_to_sleep.hour,
                #                                 self.dream_control.time_when_must_go_to_sleep.minute))
                print("Через", self.dream_control.calculate_time_to_go_to_sleep())

            elif 'или' in user_input:
                print(choice(user_input.split('или')))

    def start_gui(self):
        self.main_window.run()

    def run(self):
        self.start_gui()
        self.user_input_check()


if __name__ == "__main__":
    app = Bot()#.user_input_check()
    app.start()
