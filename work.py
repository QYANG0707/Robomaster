from file.camera import Camera
from test import Test


class Work:

    def __init__(self, robot, screen, *kwargs):
        self.robot = robot
        self.screen = screen

        self.create_camera()
        self.test = Test()

    def create_camera(self):
        self.camera = Camera(self.robot, self.screen)

    def run(self):
        '''
        机甲大师 ep 所要运行的所有功能
        '''
        self.camera.show()
        self.camera.reset_camera()
        self.camera.move_camera_up()
