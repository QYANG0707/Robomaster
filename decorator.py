import pygame
from pygame import key
import config


def check_key(func):
    def warpper(*args, **kwargs):
        func_name = func.__name__
        bt = config.keyword_bind[func_name]
        bt_id = key.key_code(bt)
        if config.keys[bt_id]:
            print(func_name, bt, bt_id)
            return func()
        return None

    return warpper
