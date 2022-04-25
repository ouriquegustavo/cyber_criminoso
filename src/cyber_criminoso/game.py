import pygame
from .engine.clock import Clock
from .engine.display import Display
from .engine.controls import Controls
from .entities.character import Character


class Game:
    def __init__(self):
        self.is_running = False
        self.clock = Clock(self)
        self.display = Display(self)
        self.controls = Controls(self)

    def start(self):
        self.display.start(1366, 768)
        self.clock.start(60)
        self.is_running = True

        self.entities = {}

        self.character = Character(self, 0, 100, 100)
        self.entities[0] = self.character

        while self.is_running:
            self.clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.controls.update()

            keys = list(self.entities.keys())
            print(len(keys))
            for k in keys:
                self.entities[k].update()

            self.display.update()
            print(self.controls.c)
