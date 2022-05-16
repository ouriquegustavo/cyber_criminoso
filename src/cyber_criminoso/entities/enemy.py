import pygame
import math
from os.path import join
from .projectile import Projectile
from ..engine.entity import Entity
import random


class Enemy(Entity):
    def __init__(self, game, gid, x, y):
        super().__init__(game, gid)
        self.x = x
        self.y = y

        self.w = 32
        self.h = 32
        self.radius = 15
        
        self.kind = 'enemy'

        self.sprite = pygame.Surface((self.w, self.h)).convert_alpha()
        self.sprite.fill((0, 0, 0, 0))
        pygame.draw.circle(
            self.sprite, (255, 0, 0, 255), (15.5, 15.5), self.radius
        )

        self.rsq = self.radius * self.radius

        self.should_destroy = False

        self.proj_delay_max = 20
        self.proj_delay_cur = 0

    def update(self):
        self.y -= -3
        if not self.should_destroy:
            if not self.proj_delay_cur:
                self.proj_delay_cur = self.proj_delay_max
                self.game.clock.create_task(
                    'gen_proj',
                    0,
                    self.game.entity_manager.create,
                    (Projectile, self.x, self.y, 0, 15, ['character']),
                )
            if self.proj_delay_cur:
                self.proj_delay_cur -= 1
            projs = [
                e
                for e in self.game.entity_manager.entities.values()
                if e.kind == 'character_projectile'
            ]
            if self.y > 768:
                self.should_destroy = True
                self.game.clock.create_task(
                    f'destroi_{self.gid}',
                    0,
                    self.game.entity_manager.destroy,
                    (self.gid,)
                )
                xr = random.randint(100, 1266)
                yr = random.randint(10, 650)
                self.game.entity_manager.create(Enemy, xr, yr)


    def draw(self):
        self.game.display.blit(
            self.sprite, (self.x - self.w / 2, self.y - self.h / 2)
        )
