# вообще не продумано

# СделатьЛист:
# -- Переписать это в кроссплатформ

from os import system, listdir, remove
import platform
from gtts import gTTS
from playsound import playsound

# просто свистоперделка, выводящая при иморптировании что-то типа "{название модуля} импортирован"
if '__main__' != __name__:
	print('{0}: активирован'.format(__name__))


class Voice:
	""" класс, который реализует синтез, воспроизведение, сохранение и удаление голоса """
	def __init__(self):
		""" создаёт необходимые переменные """
		self.sound_file_name = None

	def create_sound(self, text_to_speech, lang):
		""" создаёт аудиофайл sound.mp3, при условии наличия интернета """
		# (надо будет реалезовать оффлайн синтез (через pyttsx?)
		if self.sound_file_name not in listdir():
			self.sound_file_name = 'sound.mp3'
			tts = gTTS(text=text_to_speech, lang=lang)
			tts.save(self.sound_file_name)

	def play_sound(self, sound_file_name):
		""" проигрывает аудиофайл """
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
