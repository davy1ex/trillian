import pyttsx3
from threading import Thread

# СделатьЛист: :
# -- Реализовать рабочий код как для линукса, так и для винды

if '__main__' != __name__:
    print('Модуль \"Voice\" активирован')


class Voice:
    def __init__(self):
        pass

    def say_to_me(self, text_to_speech):
        engine = pyttsx3.init()
        engine.say(text_to_speech)
        Thread(target=engine.runAndWait).start()
