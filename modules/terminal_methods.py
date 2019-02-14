# просто для красоты пихнул это в отдельный файл
# в будущем (может быть) будет расширен

if '__main__' != __name__:
    print('{0}: активирован'.format(__name__))


class Terminal:
    def print(self, output_text):
        """ красиво выводит то, что надо вывести """
        # а я круто комментирую свой код...
        print('[Trillian]: {}'.format(output_text))
