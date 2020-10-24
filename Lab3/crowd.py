import pygame
import random
from pygame.draw import *
import math

pygame.init()


def body(scr, x, skin_color, body_color):
    """
    draws a body
    :param scr: surface of display on which the picture is
    :param x: x-coord of the performance' center
    :return: none
    """
    ellipse(scr, body_color, (x - 150, 400, 300, 200))
    # hands
    polygon(scr, skin_color, [(x - 159, 435), (x - 295, 158), (x - 267, 155), (x - 134, 404)])
    polygon(scr, skin_color, [(115 + x, 400), (197 + x, 150), (223 + x, 154), (149 + x, 412)])
    # sleeves
    polygon(scr, body_color, [(x - 115, 468), (x - 167, 463), (x - 182, 422), (x - 125, 393), (x - 94, 425)])
    polygon(scr, body_color, [(x + 108, 455), (x + 153, 451), (x + 161, 409), (x + 111, 382), (x + 86, 420)])
    polygon(scr, (0, 0, 0), [(x - 115, 468), (x - 167, 463), (x - 182, 422), (x - 125, 393), (x - 94, 425)], 1)
    polygon(scr, (0, 0, 0), [(x + 108, 455), (x + 153, 451), (x + 161, 409), (x + 111, 382), (x + 86, 420)], 1)
    # wrists
    ellipse(scr, skin_color, (x - 305, 98, 46, 78))
    ellipse(scr, skin_color, (x + 185, 98, 46, 78))


def face(scr, x, eye_color, skin_color, hair_color):
    """
    draws a face
    :param scr: surface of display on which the picture is
    :param x: x-coord of the performance' center
    """
    circle(scr, skin_color, (x, 300), 125)
    # mouth
    polygon(scr, (255, 0, 0, alpha), [(x, 300 + 75), (x - 50, 300 + 40), (x + 50, 300 + 40)])
    # nose
    polygon(scr, (100, 70, 40, alpha), [(x, 300 + 30), (x - 15, 300 + 10), (x + 15, 300 + 10)])
    # eyes
    ellipse(scr, eye_color, (x - 67, 300 - 40, 50, 40))
    ellipse(scr, eye_color, (x + 17, 300 - 40, 50, 40))
    ellipse(scr, (0, 0, 0), (x - 67, 300 - 40, 50, 40), 2)
    ellipse(scr, (0, 0, 0), (x + 17, 300 - 40, 50, 40), 2)
    circle(scr, (0, 0, 0), (x - 42, 300 - 20), 7)
    circle(scr, (0, 0, 0), (x + 42, 300 - 20), 7)
    # hair
    for i in range(5, 27):
        alpha_0 = i / 10
        polygon(scr, hair_color,
                [(x - (125 + 30) * math.cos(alpha_0), 300 - (125 + 30) * math.sin(alpha_0)),
                 (x - (125 - 7) * math.cos(alpha_0) + 10 * math.sin(alpha_0),
                  300 - (125 - 7) * math.sin(alpha_0) - 10 * math.cos(alpha_0)),
                 (x - (125 - 7) * math.cos(alpha_0) - 10 * math.sin(alpha_0),
                  300 - (125 - 7) * math.sin(alpha_0) + 10 * math.cos(alpha_0))])


def boy(scr, x, body_color, hair_color, eye_color, skin_color):
    """
    draws a face
    :param scr: surface of display on which the picture is
    :param x: x-coord of the performance' center
    """
    body(scr, x, skin_color, body_color)
    face(scr, x, eye_color, skin_color, hair_color)


width = 1000
num_people = 10
start = 400
end = 100
screen = pygame.display.set_mode((width, 500))
boy_surf = pygame.Surface((650, 500), pygame.SRCALPHA)
perspective = width // (num_people + num_people**2)
poz1 = 0
poz2 = width


for j in range(num_people):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    alpha = 255 * (1 - j / num_people)
    boy(boy_surf, 325, (r, b, g, alpha), (r, g, b, alpha), (143, 255, 228, alpha), (255, 246, 207, alpha))
    poz2 -= perspective * (num_people - j)
    screen.blit(pygame.transform.smoothscale(boy_surf, (perspective * (num_people - j), perspective * (num_people - j))),
                (poz1, 100 + perspective * j))
    boy(boy_surf, 325, (g, r, b, alpha), (g, b, r, alpha), (143, 255, 228, alpha), (255, 246, 207, alpha))
    screen.blit(pygame.transform.smoothscale(boy_surf, (perspective * (num_people - j), perspective * (num_people - j))),
                (poz2, 100 + perspective * j))
    poz1 += perspective * (num_people - j)

pygame.display.update()
clock = pygame.time.Clock()

finished = False
while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
