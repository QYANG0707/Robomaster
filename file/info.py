import pygame, robomaster
from decorator import check_key_down


class Info:
    def __init__(self, robot, camera, screen):
        self.robot = robot
        self.font = pygame.font.SysFont('simHei', 20)
        self.camera = camera
        self.screen = screen

    @check_key_down
    def info_blit(self):
        text_1 = self.font.render('摄像头降速比例:' + str(self.camera.camera_speed_scale), True, 'red')
        self.screen.blit(text_1, (0, 0))
