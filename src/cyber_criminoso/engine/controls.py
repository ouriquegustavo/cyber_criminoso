import pygame


class Controls:
    def __init__(self, game):
        self.game = game

    def start(self):
        self.c = {
            'up': 0,
            'down': 0,
            'left': 0,
            'right': 0,
            'fire': 0,
        }

    def update(self):
        keys = pygame.key.get_pressed()
        self.c = {
            'up': int(keys[pygame.K_w] or keys[pygame.K_UP]),
            'down': int(keys[pygame.K_s] or keys[pygame.K_DOWN]),
            'left': int(keys[pygame.K_a] or keys[pygame.K_LEFT]),
            'right': int(keys[pygame.K_d] or keys[pygame.K_RIGHT]),
            'fire': int(keys[pygame.K_SPACE]),
        }
