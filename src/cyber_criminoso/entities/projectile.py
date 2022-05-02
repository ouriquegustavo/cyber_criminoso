import pygame
import math
from ..engine.entity import Entity


class Projectile(Entity):
    def __init__(self, game, gid, x, y):
        super().__init__(game, gid)
        self.game = game
        self.gid = gid
        self.x = x
        self.y = y
        self.kind = 'character_projectile'

        self.w = 15
        self.h = 15

        self.speed = 15

        self.sprite = pygame.Surface((self.w, self.h)).convert_alpha()
        self.sprite.fill((0, 0, 0, 0))
        pygame.draw.ellipse(self.sprite, (255, 255, 0, 255), (5, 0, 5, 15), 0)

        self.t = 0

    def update(self):
        self.t += 1
        dy = -self.speed
        self.y += dy
        if self.t >= 80:
            self.game.entity_manager.destroy(self.gid)

    def draw(self):
        self.game.display.blit(
            self.sprite, (self.x - self.w / 2, self.y - self.h / 2)
        )
