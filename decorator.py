import pygame
from pygame import key
import config


def check_key(func):
    def wrapper(self, *args, **kwargs):
        func_name = func.__name__
        bt = config.keyword_bind[func_name]
        bt_id = key.key_code(bt)
        if config.keys[bt_id]:
            return func(self, *args, **kwargs)

    return wrapper
