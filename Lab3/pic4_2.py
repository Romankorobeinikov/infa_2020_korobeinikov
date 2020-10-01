import pygame
from pygame.draw import *
import math

pygame.init()


def body(x, skin_color, body_color):
    ellipse(screen, body_color, (x - 150, 400, 300, 200))
    # hands
    polygon(screen, skin_color, [(x - 159, 435), (x - 295, 158), (x - 267, 155), (x - 134, 404)])
    polygon(screen, skin_color, [(115 + x, 400), (197 + x, 150), (223 + x, 154), (149 + x, 412)])
    # sleeves
    polygon(screen, body_color, [(x - 115, 468), (x - 167, 463), (x - 182, 422), (x - 125, 393), (x - 94, 425)])
    polygon(screen, body_color, [(x + 108, 455), (x + 153, 451), (x + 161, 409), (x + 111, 382), (x + 86, 420)])
    polygon(screen, (0, 0, 0), [(x - 115, 468), (x - 167, 463), (x - 182, 422), (x - 125, 393), (x - 94, 425)], 1)
    polygon(screen, (0, 0, 0), [(x + 108, 455), (x + 153, 451), (x + 161, 409), (x + 111, 382), (x + 86, 420)], 1)
    # wrists
    ellipse(screen, skin_color, (x - 305, 98, 46, 78))
    ellipse(screen, skin_color, (x + 185, 98, 46, 78))


def face(x, eye_color, skin_color, hair_color):
    circle(screen, skin_color, (x, 300), 125)
    # mouth
    polygon(screen, (255, 0, 0), [(x, 300 + 75), (x - 50, 300 + 40), (x + 50, 300 + 40)])
    # nose
    polygon(screen, (100, 70, 40), [(x, 300 + 30), (x - 15, 300 + 10), (x + 15, 300 + 10)])
    # eyes
    ellipse(screen, eye_color, (x - 67, 300 - 40, 50, 40))
    ellipse(screen, eye_color, (x + 17, 300 - 40, 50, 40))
    ellipse(screen, (0, 0, 0), (x - 67, 300 - 40, 50, 40), 2)
    ellipse(screen, (0, 0, 0), (x + 17, 300 - 40, 50, 40), 2)
    circle(screen, (0, 0, 0), (x - 42, 300 - 20), 7)
    circle(screen, (0, 0, 0), (x + 42, 300 - 20), 7)
    # hair
    for alpha in range(5, 27):
        alpha_0 = alpha / 10
        polygon(screen, hair_color,
                [(x - (125 + 30) * math.cos(alpha_0), 300 - (125 + 30) * math.sin(alpha_0)),
                 (x - (125 - 7) * math.cos(alpha_0) + 10 * math.sin(alpha_0),
                  300 - (125 - 7) * math.sin(alpha_0) - 10 * math.cos(alpha_0)),
                 (x - (125 - 7) * math.cos(alpha_0) - 10 * math.sin(alpha_0),
                  300 - (125 - 7) * math.sin(alpha_0) + 10 * math.cos(alpha_0))])


def message(x):
    rect(screen, (0, 200, 0), (x - 330, 60, 600, 70))
    font = pygame.font.SysFont('serif', 48)
    text = font.render("PYTHON is AMAZING", 1, (0, 0, 0))
    screen.blit(text, (x - 250, 70))


def boy(x, body_color, hair_color, eye_color, skin_color):
    body(x, skin_color, body_color)
    face(x, eye_color, skin_color, hair_color)


screen = pygame.display.set_mode((800, 500))
boy(450, (255, 151, 95), (255, 80, 255), (0, 178, 255), (255, 246, 207))
message(450)
pygame.display.update()
clock = pygame.time.Clock()

finished = False
while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
