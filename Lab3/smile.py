import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))


def drawface(a):
    circle(screen, (225, 225, 0), (a, a - 25), 150)
    circle(screen, (100, 250, 0), (a - 80, a - 50), 40)
    circle(screen, (100, 250, 0), (a + 80, a - 50), 40)
    circle(screen, (0, 0, 0), (a + 80, a - 50), 20)
    circle(screen, (0, 0, 0), (a - 80, a - 50), 20)
    rect(screen, (255, 0, 0), (a - 80, a + 30, 150, 30))
    polygon(screen, (0, 0, 0,), [[a + 40, a - 60], [a + 20, a - 80], [a + 110, a - 120], [a + 100, a - 100]])
    polygon(screen, (0, 0, 0,), [[a - 40, a - 60], [a - 20, a - 80], [a - 110, a - 120], [a - 100, a - 100]])


drawface(200)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()