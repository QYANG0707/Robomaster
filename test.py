import pygame, config
from sys import exit

from decorator import check_key

pygame.init()
screen = pygame.display.set_mode((100, 100))


@check_key
def test_a():
    print('A')


@check_key
def test_b():
    print('B')


# if __name__ == '__main__':
while True:
    config.keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # test_a()
    test_b()
    pygame.display.update()
