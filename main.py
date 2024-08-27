import pygame
from config import TITLE, W_WIDTH, W_HEIGHT, CONNECT_TYPE
from robomaster import robot
from sys import exit
from work import Work

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))

    rbt = robot.Robot()
    rbt.initialize(conn_type=CONNECT_TYPE)

    work = Work(rbt, screen)

    while True:
        work.run()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    rbt.close()
                    exit()

        pygame.display.flip()
