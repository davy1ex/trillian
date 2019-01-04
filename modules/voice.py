# # вообще не продумано

# import pyttsx3
# from threading import Thread

# # СделатьЛист: :
# # -- Реализовать рабочий код как для линукса, так и для винды
# # -- Пихнуть это в поток (попытки предпринимаются, но пока лень)
# # -- Переписать это говно

# if '__main__' != __name__:
#     print('{0}: активирован'.format(__name__))


# class Voice:
#     def __init__(self):
#         pass

#     def say_to_me(self, text_to_speech):
#         engine = pyttsx3.init()
#         engine.say(text_to_speech)
#         Thread(target=engine.runAndWait).start()

from os import system, listdir, remove
import platform
from gtts import gTTS
from playsound import playsound


if '__main__' != __name__:
	print('{0}: активирован'.format(__name__))


class Voice:
	def __init__(self):
		self.sound_file_name = None
		self.text_to_speech = None

	def create_sound(self, text_to_speech, lang):
		self.text_to_speech = text_to_speech	
		if self.sound_file_name not in listdir():
			self.sound_file_name = '{}.mp3'.format('sound')
			tts=gTTS(text=text_to_speech, lang=lang)
			tts.save(self.sound_file_name)

	def play_sound(self, sound_file_name):
		if platform.system() == 'Linux':
			system('mpg123 -q {0}'.format(sound_file_name))
		else:
			playsound(sound_file_name)

	def delete_sound(self, sound_file_name):
		if self.sound_file_name != None:
			remove(sound_file_name)

	def say_to_me(self, text, lang='ru'):
		self.create_sound(text, lang)
		self.play_sound(self.sound_file_name)
		self.delete_sound(self.sound_file_name)


if __name__ == '__main__':
	Voice().say_to_me('Привет мир')
