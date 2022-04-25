import pygame
import math


class Projectile:
    def __init__(self, game, gid, x, y):
        self.game = game
        self.gid = gid
        self.x = x
        self.y = y

        self.w = 15
        self.h = 15

        self.speed = 30

        self.sprite = pygame.Surface((self.w, self.h)).convert_alpha()
        pygame.draw.ellipse(self.sprite, (255, 255, 0, 255), (5, 0, 5, 15), 0)

    def update(self):
        dy = -self.speed
        self.y += dy

    def draw(self):
        self.game.display.blit(
            self.sprite, (self.x - self.w / 2, self.y - self.h / 2)
        )
