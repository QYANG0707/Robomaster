import pygame
from pygame import key
import config


def check_key_down(func):
    '''
    当函数调用时会去到config.py中的keyword_bind字典中进行比对
    若在配置文件中指定的的按钮按压,则执行该函数
    '''
    def wrapper(self, *args, **kwargs):
        func_name = func.__name__
        bt = config.keyword_bind[func_name]
        bt_id = key.key_code(bt)
        # print(bt,bt_id)
        if config.keys[bt_id]:
            return func(self, *args, **kwargs)

    return wrapper
