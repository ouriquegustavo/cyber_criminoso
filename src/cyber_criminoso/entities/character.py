import pygame
import math
from os.path import join
from .projectile import Projectile
from ..engine.entity import Entity


class Character(Entity):
    def __init__(self, game, gid, x, y):
        super().__init__(game, gid)
        self.x = x
        self.y = y

        self.w = 32
        self.h = 32

        self.speed = 5

        self.sprite = pygame.image.load(
            join('src', 'cyber_criminoso', 'sprites', 'ship.png')
        ).convert_alpha()

        self.proj_delay_max = 15
        self.proj_delay_cur = 0

    def update(self):
        dx = -self.game.controls.c['left'] + self.game.controls.c['right']
        dy = -self.game.controls.c['up'] + self.game.controls.c['down']
        dr = dx * dx + dy * dy
        if dr > 0:
            drsq = math.sqrt(dr)
            dx /= drsq
            dy /= drsq
        self.x += self.speed * dx
        self.y += self.speed * dy

        if self.game.controls.c['fire'] and not self.proj_delay_cur:
            self.proj_delay_cur = self.proj_delay_max
            self.game.clock.create_task(
                'gen_proj',
                0,
                self.game.entity_manager.create,
                (Projectile, self.x, self.y)
            )
            

        if self.proj_delay_cur:
            self.proj_delay_cur -= 1

    def draw(self):
        self.game.display.blit(
            self.sprite, (self.x - self.w / 2, self.y - self.h / 2)
        )
