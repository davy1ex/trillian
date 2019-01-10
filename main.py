# просто красивый конец (начало?)
# а также главный файл, который запускает всю программу

import sys

from constants.phrases import phrases

if len(sys.argv) > 1:
    if 'test' in sys.argv[1]:
        from modules.test.executer import Executer
else:
    from modules.executer import Executer


class Trillian:
    def __init__(self):
        print(phrases['hello_from_symbols'])
        Executer()


if __name__ == '__main__':
    app = Trillian()
