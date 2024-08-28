import pygame, config
from config import TITLE, W_WIDTH, W_HEIGHT, CONNECT_TYPE
from sys import exit

from test import Test

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))

    t = Test()

    while True:
        config.keys = pygame.key.get_pressed()
        t.say_test()
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        pygame.display.flip()
