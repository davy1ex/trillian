# import os

import pyttsx3
# from gtts import gTTS


def talk_to_me(audio):
    print(audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

    # tts = gTTS(text=audio, lang='en')
    # tts.save('audio.mp3')
    # os.system('mp3 audio.mp3')


if __name__ == '__main__':
    talk_to_me('Здравствуйте, сер.')