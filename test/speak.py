import os
import time
from threading import Thread

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


class Threader(Thread):
    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.daemon = True
        self.start()

    def run(self):
        tts_engine = pyttsx3.init()
        tts_engine.say(self._args)
        tts_engine.runAndWait()

def say(phrase):
    my_test = phrase
    my_thread = Threader(args=my_test)



# for phrase in ['dude', 'hello', 'man']:
#     print('говорю')
#     say(phrase)
#     time.sleep(0.1)