from decorator import check_key


class Test:
    def __init__(self):
        pass

    @check_key
    def say_test(self):
        print('hello test')
