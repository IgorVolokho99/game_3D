from settings import *
import pygame


class Player:
    def __init__(self):
        self.x, self.y = start_pos
        self.angle = start_angle

    def get_pos(self):
        return self.x, self.y

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= start_speed
        if keys[pygame.K_s]:
            self.y += start_speed
        if keys[pygame.K_a]:
            self.x -= start_speed
        if keys[pygame.K_d]:
            self.x += start_speed

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
