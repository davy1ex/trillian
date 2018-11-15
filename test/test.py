from threading import Thread

a = input('')
# if a == '42':
#     print('ok')
# else:
#     print('ok\'t')


class Test(Thread):
    def __init__(self):
        super().__init__()
        self.var = ''

    def test(self):
        print('test')

Test().test()