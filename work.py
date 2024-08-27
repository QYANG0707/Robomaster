from file.camera import Camera
from decorator import check_key


class Work:

    def __init__(self, robot, screen, *kwargs):
        self.robot = robot
        self.screen = screen

        self.create_camera()
        self.key = Key()

    def create_camera(self):
        self.camera = Camera(self.robot, self.screen)

    def run(self):
        '''
        机甲大师 ep 所要运行的所有功能
        '''
        self.camera.show()
