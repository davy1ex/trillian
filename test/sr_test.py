import os

import speech_recognition as sr
from time import sleep
from modules.voice import Voice


def what_iam_say():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('say anything')
		r.adjust_for_ambient_noise(source, duration=1)
		text_speech = r.listen(source)
		print('text recognition...')

	try:
		command = r.recognize_google(text_speech, language='ru').lower()
		print('you said:', command)
	except sr.UnknownValueError:
		command = what_iam_say()

	return command


def execute_command(command):
	if 'заблоки' in command:
		os.system('xflock4')

	elif 'сверни всё' in command or 'рабочий стол' in command:
		os.system('wmctrl -k on')

	elif 'обратно' in command:
		os.system('wmctrl -k off')

	elif 'привет' in command:
		Voice().say_to_me('Приветствую')

	elif 'терминал' in command:
		os.system('exo-open --launch TerminalEmulator')

	elif 'браузер' in command:
		os.system('exo-open --launch WebBrowser')

	elif 'убейся' in command:
		exit()


while True:
	execute_command(what_iam_say())
	sleep(0.1)



# if __name__ == '__main__':
# 	while True:
# 		execute_command(what_iam_say())
# 		sleep(0.1)
#
