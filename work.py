'''
机甲大师 ep 所要执行的全部任务
'''
from bot_module.camera import Camera
from bot_module.info import Info
from bot_module.wheel import Wheel
from test import Test


class Work:

    def __init__(self, robot, screen, *kwargs):
        self.robot = robot
        self.screen = screen

        self.camera = Camera(robot, screen)
        self.test = Test()

        self.info = Info(robot, self.camera, screen)

        self.wheel = Wheel(robot)

    def run(self):
        '''
        机甲大师 ep 所要运行的所有功能
        '''
        self.camera.show()
        self.camera.reset_camera()
        self.camera.move_camera()
        self.camera.more_camera_speed()
        self.camera.less_camera_speed()
        self.camera.switch_gesture_recogntion()

        self.info.info_blit()

        self.wheel.move_wheel()
        self.wheel.rotation()


    def test(self):
        print('hello')