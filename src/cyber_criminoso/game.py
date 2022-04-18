import pygame
from .engine.clock import Clock
from .engine.display import Display
from .engine.controls import Controls


class Game:
    def __init__(self):
        self.is_running = False
        self.clock = Clock(self)
        self.display = Display(self)
        self.controls = Controls(self)

    def start(self):
        self.display.start(500, 500)
        self.clock.start(30)
        self.is_running = True

        while self.is_running:
            self.clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.controls.update()

            self.display.update()
            print(self.controls.c)
