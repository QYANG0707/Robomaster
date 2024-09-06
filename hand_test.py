import pygame
import cv2
import mediapipe as mp
from time import sleep


class Camera:
    def __init__(self, screen):
        self.camera = cv2.VideoCapture(0)
        self.screen = screen
        self.count = 0

        self.mp_hand = mp.solutions.hands
        self.hands = self.mp_hand.Hands(static_image_mode=False, max_num_hands=4, model_complexity=1,
                                        min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.mpDraw = mp.solutions.drawing_utils  # 初始化Mediapipe库绘图工具
        self.handLmsStyle = self.mpDraw.DrawingSpec(
            color=(51, 204, 255), thickness=5)
        self.handConStyle = self.mpDraw.DrawingSpec(
            color=(0, 255, 0), thickness=5)

        self.p_time = 0
        self.c_time = 0

    def get_frame(self):
        res, frame = self.camera.read()
        frame = cv2.flip(frame, 1)  # 图像反转
        self.save_frame = frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.get_hand(frame)

        self.surface = pygame.image.frombuffer(
            frame.tobytes(), frame.shape[1::-1], 'RGB')

    def blit(self):
        self.get_frame()
        self.screen.blit(self.surface, (0, 0))

    def take_photo(self):
        cv2.imwrite(f'{self.count}.png', self.save_frame)
        self.count += 1
        sleep(1)

    def get_hand(self, frame):
        result = self.hands.process(frame)
        imgHeight = frame.shape[0]
        imgWidth = frame.shape[1]
        if result.multi_hand_landmarks:  # 检查是否检测到手部
            for handLms in result.multi_hand_landmarks:  # 遍历检测到的手部
                self.mpDraw.draw_landmarks(
                    frame, handLms, self.mp_hand.HAND_CONNECTIONS, self.handLmsStyle, self.handConStyle)  # 绘制手部关键点和连接线
                for i, lm in enumerate(handLms.landmark):  # 遍历每个关键点
                    xPos = int(lm.x * imgWidth)  # 计算关键点在图像中的x坐标
                    yPos = int(lm.y * imgHeight)  # 计算关键点在图像中的y坐标
                    # cv2.putText(img, str(i), (xPos-25, yPos+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), )
                    if i in [4, 8, 12, 16, 20]:  # 绘制特定关键点的标记,如果是特定的关键点（在代码中是第5个关键点）
                        cv2.circle(frame, (xPos, yPos), 7,
                                   (255, 51, 102), cv2.FILLED)


pygame.init()  # 初始化pygame
pygame.display.set_caption('我是标题')
screen = pygame.display.set_mode((640, 480))  # 设置窗口尺寸

camera = Camera(screen)

while True:

    camera.blit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('喀嚓..')
                camera.take_photo()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('喀嚓喀嚓')
                camera.take_photo()

    pygame.display.flip()
