# import os

import pyttsx3
# from gtts import gTTS


# СделатьЛист: :
# -- Реализовать рабочий код как для линукса, так и для винды

if '__main__' != __name__:
    print('Модуль \"Voice\" активирован')


class Voice:
    def __init__(self):
        self.run = False

    def talk_to_me(self, audio):
        print('[только что было сказано]: "{}"'.format(audio))

        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()

    def run(self):
        if self.run:
            self.talk_to_me()


# def talk_to_me(audio):
#     print('[только что было сказано]: "{}"'.format(audio))
#
#     # кажись, код ниже спешл фор винда, надо будет пофиксить
#     engine = pyttsx3.init()
#     engine.say(audio)
#     engine.runAndWait()
#
#     # на винде не работате, на линуксе пока что не пробовал
#     # tts = gTTS(text=audio, lang='en')
#     # tts.save('audio.mp3')
#     # os.system('mp3 audio.mp3')
#
#
# if __name__ == '__main__':
#     talk_to_me('Здравствуйте, сер.')