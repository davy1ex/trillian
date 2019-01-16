# Запоминает и напоминает
from os import listdir, getcwd
from datetime import datetime


if '__main__' != __name__:
    print('{0}: активирован'.format(__name__))


class Minder:
    def __init__(self):
        self.filename = 'memorized.txt'
        if self.filename not in listdir(getcwd()):
            with open(self.filename, 'w'):
                pass
            print('Файла не было, но я создала')

    def remember(self, data_to_remember):
        text_to_write = '[' + datetime.now().strftime('%H:%M:%S') + ']: ' + data_to_remember + '\n'
        with open(self.filename, 'a+') as file:
            file.write(text_to_write)

    def remind(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def clear(self):
        with open(self.filename, 'w') as file:
            file.write('')

