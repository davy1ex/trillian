from threading import Thread

from modules.shutdowner import ShutdownByTime
from modules.dream_control import DreamControl
from constants.phrases import phrases


class Bot(Thread):
    def __init__(self):
        super().__init__()
        print(phrases["hello"])
        self.dread_control = DreamControl()

    def user_input_check(self):
        while True:
            user_input = input(">: ").lower()
            if "выкл" in user_input:
                print('[Bot]: Лады')
                user_input_time = user_input.split()[2]
                ShutdownByTime(user_input_time).time_to_shutdown()

            elif "когда" in user_input and "вставать" in user_input:
                print("Через", self.dread_control.calculate_time_to_wake_up())

            elif 'test' in user_input:
                print(user_input)
                user_input_time = user_input.split()[1]
                print(ShutdownByTime(user_input_time).time_to_shutdown())

    def run(self):
        self.user_input_check()


if __name__ == "__main__":
    app = Bot()
    app.start()
