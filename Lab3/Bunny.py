import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))


def draw_body(surface, x, y, width, height, color):
    """
    Функция рисует тело зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_hand(surface, x, y, width, height, angle, color):
    """
    Функция рисует лапу зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    angel - угол поворота лапы в градусах 
    """
    hand = pygame.Surface((width, height))
    ellipse(hand, color, (0, 0, width, height))
    rotated_hand = pygame.transform.rotate(hand, angle)
    surface.blit(rotated_hand, (x, y))


def draw_head(surface, x, y, size, color):
    """
    Функция рисует голову зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - диаметр головы
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    circle(surface, color, (x, y), size // 2)
    # Глаза
    outside_eyecolor = (0, 255, 253)
    inside_eyecolor = (1, 1, 1)
    circle(surface, outside_eyecolor, (x - size // 5, y - size // 5), size // 10)
    circle(surface, outside_eyecolor, (x + size // 5, y - size // 5), size // 10)
    circle(surface, inside_eyecolor, (x - size // 5, y - size // 5), size // 30)
    circle(surface, inside_eyecolor, (x + size // 5, y - size // 5), size // 30)
    # Нос
    nouse_color = (1, 1, 1)
    polygon(surface, nouse_color, [(x - size // 20, y + size // 10),
                                   (x, y + size * 3 // 20), (x + size // 20, y + size // 10)])
    arc(surface, nouse_color, (x - size // 10, y + size // 10, size // 10, size // 10), 3.15, 6.3, 2)
    arc(surface, nouse_color, (x, y + size // 10, size // 10, size // 10), 3.15, 6.3, 2)


def draw_ear(surface, x, y, width, height, color):
    """
    Функция рисует ухо зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    # Цвет внутренности уха
    inside_color = (255, 177, 232)
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))
    ellipse(surface, inside_color, (x - width // 4, y - height // 4, width // 2, height // 2))


def draw_leg(surface, x, y, width, height, color):
    """
    Функция рисует ногу зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_hare(surface, x, y, width, height, color):
    """
    Функция рисует зайца на экране.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """

    angle = 45
    hands_width = width // 5
    hands_height = height // 3

    draw_hand(surface, x, y, hands_width, hands_height, angle, color)
    draw_hand(surface, x - width * 10 // 17, y, hands_width, hands_height, -angle, color)

    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2

    draw_body(surface, x, body_y, body_width, body_height, color)

    head_size = height // 4

    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    for ear_x in (x - head_size // 4, x + head_size // 4):
        draw_ear(surface, ear_x, ear_y, width // 8, ear_height, color)

    draw_head(surface, x, y - head_size // 2, head_size, color)

    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    for leg_x in (x - width // 4, x + width // 4):
        draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)


draw_hare(screen, 400, 400, 400, 800, (200, 200, 200))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
