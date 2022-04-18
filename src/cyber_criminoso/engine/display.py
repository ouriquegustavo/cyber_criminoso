import pygame


class Display:
    def __init__(self, game):
        self.game = game

    def start(self, width, height):
        pygame.init()
        self.w = width
        self.h = height
        self.display = pygame.display.set_mode([self.w, self.h])
        self.r = 0
        self.g = 0
        self.b = 0

    def update(self):
        self.r += (
            self.game.controls.c['up'] - self.game.controls.c['down']
        ) * 5
        self.b += (
            self.game.controls.c['right'] - self.game.controls.c['left']
        ) * 5
        if self.r > 255:
            self.r = 255
        if self.r < 0:
            self.r = 0
        if self.b > 255:
            self.b = 255
        if self.b < 0:
            self.b = 0
        self.display.fill((self.r, 0, self.b))

        ### DESENHAR TUDO

        pygame.display.flip()
        pass
