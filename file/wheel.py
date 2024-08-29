import pygame
import robomaster
import config
from config import W_WIDTH, W_HEIGHT, keys
from decorator import check_key_down
from pygame import key


class Wheel:
    """
    机甲大师 轮子
    """

    def __init__(self, robot):
        self.wheel = robomaster.chassis.Chassis(robot)
        self.wheel_speed = config.WHEEL_SPEED
        self.wheel_speed_scale = 100

    def move_wheel(self):
        func_name = 'move_wheel'
        bt_list = [config.keys[key.key_code(i)] for i in config.keyword_bind[func_name]]
        if bt_list[0]:
            w_1 = self.one_wheel()
            w_2 = self.one_wheel()
            w_3 = self.one_wheel()
            w_4 = self.one_wheel()
        elif bt_list[1]:
            w_1 = self.one_wheel(True)
            w_2 = self.one_wheel(True)
            w_3 = self.one_wheel(True)
            w_4 = self.one_wheel(True)
        elif bt_list[2]:

            w_1 = self.one_wheel(True)
            w_2 = self.one_wheel()
            w_3 = self.one_wheel(True)
            w_4 = self.one_wheel()
        elif bt_list[3]:
            w_1 = self.one_wheel()
            w_2 = self.one_wheel(True)
            w_3 = self.one_wheel()
            w_4 = self.one_wheel(True)

        else:
            w_1, w_2, w_3, w_4 = 0, 0, 0, 0

        self.wheel.drive_wheels(w_1, w_2, w_3, w_4)

    def one_wheel(self, reverse=False):
        n = self.wheel_speed * self.wheel_speed_scale / 100
        if reverse:
            return n * -1
        else:
            return n

    # @check_key_down
    # def more_camera_speed(self):
    #     if self.camera_speed_scale < 100:
    #         self.camera_speed_scale += 1
    #
    # @check_key_down
    # def less_camera_speed(self):
    #     if self.camera_speed_scale > 1:
    #         self.camera_speed_scale -= 1
