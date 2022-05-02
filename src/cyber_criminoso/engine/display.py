import pygame


class Display:
    def __init__(self, game):
        self.game = game

    def start(self, width, height):
        pygame.init()
        self.w = width
        self.h = height
        self.display = pygame.display.set_mode([self.w, self.h])

    def blit(self, *args, **kwargs):
        self.display.blit(*args, **kwargs)

    def update(self):
        self.display.fill((0, 0, 0))

        ### DESENHAR TUDO
        for k, v in self.game.entity_manager.entities.items():
            v.draw()

        pygame.display.flip()
        pass
