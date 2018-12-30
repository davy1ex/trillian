from constants.phrases import phrases
from test.executer import Executer


class Trillian:
    def __init__(self):
        print(phrases['hello_from_symbols'])
        Executer()


if __name__ == "__main__":
    app = Trillian()
