import pyttsx3

# СделатьЛист: :
# -- Реализовать рабочий код как для линукса, так и для винды

if '__main__' != __name__:
    print('Модуль \"Voice\" активирован')


class Voice:
    def talk_to_me(self, audio):
        print('[только что было сказано]: "{}"'.format(audio))

        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()
