import pygame as pg
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

width = 1600
height = 900
fps = 30

pg.init()
#звук
pg.mixer.init()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Football House")
clock = pg.time.Clock()


# цикл игры


fon = (230, 101, 208)
running = True



# цикл игры
while running:
    # держим цикл на правильной скорости
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill((255, 255, 255))

    # Create a surface and pass in a tuple containing its length and width
    surf = pg.Surface((50, 50))

    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    rect = surf.get_rect()
    surf_center = (
        (width - surf.get_width()) / 2,
        (height - surf.get_height()) / 2
    )
    screen.blit(surf, surf_center)
    pg.display.flip()



pg.quit()
