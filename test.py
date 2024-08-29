from decorator import check_key_down


class Test:
    def __init__(self):
        pass

    @check_key_down
    def say_test(self):
        print('hello test')
