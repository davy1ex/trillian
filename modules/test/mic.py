# здесь готовится голосовое управление
# хорошо всё готовится

from threading import Thread

import speech_recognition as sr


class Mic:
    def __init__(self):
        self.r = sr.Recognizer()

    def what_iam_say(self):
        with sr.Microphone() as source:
            print('say anything')
            self.r.adjust_for_ambient_noise(source, duration=1)
            text_speech = self.r.listen(source)
            print('text recognition...')

        try:
            command = self.r.recognize_google(text_speech, language='ru').lower()
            print('you said:', command)
        except sr.UnknownValueError:
            command = self.what_iam_say()

        return command

    # def run(self):
    #     while True:
    #         self.what_iam_say()

    # def execute_command(command):
    #     if 'заблоки' in command:
    #         os.system('xflock4')
    #
    #     elif 'сверни всё' in command or 'рабочий стол' in command or 'сверни всё' in command:
    #         os.system('wmctrl -k on')
    #
    #     elif 'обратно' in command:
    #         os.system('wmctrl -k off')
    #
    #     elif 'привет' in command:
    #         Voice().say_to_me('Приветствую')
    #
    #     elif 'терминал' in command:
    #         os.system('exo-open --launch TerminalEmulator')
    #
    #     elif 'браузер' in command:
    #         os.system('exo-open --launch WebBrowser')
    #
    #     elif 'убейся' in command:
    #         exit()#
