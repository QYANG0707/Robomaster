import pygame
import robomaster
import cv2
import config
from config import W_WIDTH, W_HEIGHT, keys
from decorator import check_key_down
from pygame import key


class Camera:
    """
    机甲大师 ep 摄像头
    """

    def __init__(self, robot, screen):
        self.ca = robomaster.camera.EPCamera(robot)
        self.ca.start_video_stream(display=False, resolution="720p")

        self.gi = robomaster.gimbal.Gimbal(robot)

        self.screen = screen
        self.camera_speed = config.CAMERA_SPEED
        self.camera_speed_scale = 100

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

    @check_key_down
    def reset_camera(self):
        '''重置云台摄像头至车体中心位置'''
        if not self.gi._action_dispatcher.has_in_progress_actions:
            self.gi.recenter()

    def move_camera(self):
        func_name = 'move_camera'
        bt_list = [config.keys[key.key_code(i)] for i in config.keyword_bind[func_name]]
        if bt_list[0]:
            up_down = self.camera_speed * self.camera_speed_scale / 100
        elif bt_list[1]:
            up_down = self.camera_speed * -1 * self.camera_speed_scale / 100
        else:
            up_down = 0

        if bt_list[2]:
            left_right = self.camera_speed * -1 * self.camera_speed_scale / 100
        elif bt_list[3]:
            left_right = self.camera_speed * self.camera_speed_scale / 100
        else:
            left_right = 0
        self.gi.drive_speed(up_down, left_right)

    @check_key_down
    def more_camera_speed(self):
        if self.camera_speed_scale < 100:
            self.camera_speed_scale += 1

    @check_key_down
    def less_camera_speed(self):
        if self.camera_speed_scale > 1:
            self.camera_speed_scale -= 1
