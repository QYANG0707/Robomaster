import pygame
import robomaster
import config
from config import W_WIDTH, W_HEIGHT, keys
from decorator import check_key_down
from pygame import key


class Wheel:
    """
    机甲大师 ep 麦克纳姆轮
    """

    def __init__(self, robot):
        self.wheel = robomaster.chassis.Chassis(robot)
        self.wheel_speed = config.WHEEL_SPEED
        self.wheel_speed_scale = 100

    def move_wheel(self):
        '''
        移动
        '''
        func_name = 'move_wheel'
        bt_list = [config.keys[key.key_code(i)] for i in config.keyword_bind[func_name]]
        if bt_list[0]:# 前进
            w_1 = self.one_wheel()
            w_2 = self.one_wheel()
            w_3 = self.one_wheel()
            w_4 = self.one_wheel()
        elif bt_list[1]:# 后退
            w_1 = self.one_wheel(True)
            w_2 = self.one_wheel(True)
            w_3 = self.one_wheel(True)
            w_4 = self.one_wheel(True)
        elif bt_list[2]:# 左移

            w_1 = self.one_wheel(True)
            w_2 = self.one_wheel()
            w_3 = self.one_wheel(True)
            w_4 = self.one_wheel()
        elif bt_list[3]:# 右移
            w_1 = self.one_wheel()
            w_2 = self.one_wheel(True)
            w_3 = self.one_wheel()
            w_4 = self.one_wheel(True)

        else:# 停止
            w_1, w_2, w_3, w_4 = 0, 0, 0, 0

        self.wheel.drive_wheels(w_1, w_2, w_3, w_4)

    def one_wheel(self, reverse=False):
        '''
        reverse = True:   轮子正转
        reverse = False:  轮子反转

        return:单个轮子的旋转速度
        '''
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



    
