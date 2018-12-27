import pyttsx3

# СделатьЛист: :
# -- Реализовать рабочий код как для линукса, так и для винды

if '__main__' != __name__:
    print('Модуль \"Voice\" активирован')


class Voice:
    def talk_to_me(self, text_to_speech):
        print('[только что было сказано]: "{}"'.format(text_to_speech))

        engine = pyttsx3.init()
        engine.say(text_to_speech)
        engine.runAndWait()
