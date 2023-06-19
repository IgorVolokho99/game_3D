import math

import pygame

from settings import *
from map import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Or we can use exit()

    player.move()
    screen.fill(BG_COLOR)

    pygame.draw.circle(screen, PERSON_COLOR, player.get_pos(), 12)
    pygame.draw.line(screen, PERSON_COLOR, player.get_pos(), (player.x + SCREEN_WIDTH * math.cos(player.angle),
                                                              player.y + SCREEN_WIDTH * math.sin(player.angle)))

    for x, y in coor_s:  # {(2, 2), (5, 3)}
        pygame.draw.rect(screen, (50, 50, 50), (x, y, TILE1, TILE2), 2)

    pygame.display.flip()  # Or we can use pygame.display.update()
    clock.tick(FPS)
