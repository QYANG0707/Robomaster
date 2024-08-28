import pygame
import robomaster
import cv2
from config import W_WIDTH, W_HEIGHT
from decorator import check_key


class Camera:
    """
    机甲大师 ep 摄像头
    """

    def __init__(self, robot, screen):
        self.ca = robomaster.camera.EPCamera(robot)
        self.ca.start_video_stream(display=False, resolution="720p")

        self.gi = robomaster.gimbal.Gimbal(robot)

        self.screen = screen

    def show(self):
        """
        pygame中显示摄像头内容
        """
        img = self.ca.read_cv2_image()  # 读取视频帧
        # 将BGR格式转RGB格式,pygame使用RGB格式
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        surface = pygame.image.frombuffer(frame.tobytes(), (1280, 720), "RGB")
        surface = pygame.transform.scale(surface, (W_WIDTH, W_HEIGHT))
        self.screen.blit(surface, (0, 0))
        return True

    @check_key
    def reset_camera(self):
        '''重置云台摄像头至车体中心位置'''
        self.gi.recenter()

    @check_key
    def move_camera_up(self):
        self.gi.drive_speed(5, 0)
