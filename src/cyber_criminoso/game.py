import pygame
import time


class Game:
    def __init__(self):
        self.is_running = False

    def start_display(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([self.width, self.height])

    def start_clock(self, tps):
        self.tps = tps
        self.clock = pygame.time.Clock()

    def start(self):
        self.start_display(500, 500)
        self.start_clock(1)
        self.is_running = True

        while self.is_running:
            self.clock.tick(self.tps)
            print('teste', time.time())
