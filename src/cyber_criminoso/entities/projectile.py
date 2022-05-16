import pygame
import math
import random
from ..engine.entity import Entity

class Projectile(Entity):
    def __init__(self, game, gid, x, y, vx=0, vy=0, targets=[]):
        super().__init__(game, gid)
        self.game = game
        self.gid = gid
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.kind = 'projectile'
        self.targets = targets

        self.w = 15
        self.h = 15
        
        self.radius = 7

        self.sprite = pygame.Surface((self.w, self.h)).convert_alpha()
        self.sprite.fill((0, 0, 0, 0))
        pygame.draw.ellipse(self.sprite, (255, 255, 0, 255), (5, 0, 5, 15), 0)
        
        self.t = 0

    def update(self):
        self.t += 1
        self.x += self.vx
        self.y += self.vy
        if self.t >= 80:
            self.game.clock.create_task(
                f'destroi_{self.gid}',
                0,
                self.game.entity_manager.destroy,
                (self.gid,)
            )
        target = self.check_for_collision()
        if target:
            self.collide(target)
            
    def collide(self, target):
        target.x = random.randint(10, 1300)

    def draw(self):
        self.game.display.blit(
            self.sprite, (self.x - self.w / 2, self.y - self.h / 2)
        )
