import pygame
from .engine.clock import Clock
from .engine.display import Display
from .engine.controls import Controls
from .engine.entity_manager import EntityManager
from .entities.character import Character
from .entities.enemy import Enemy


class Game:
    def __init__(self):
        self.is_running = False
        self.entity_manager = EntityManager(self)
        self.clock = Clock(self)
        self.display = Display(self)
        self.controls = Controls(self)

    def start(self):
        self.display.start(1366, 768)
        self.clock.start(60)
        self.is_running = True

        self.character = self.entity_manager.create(Character, 633, 700)

        self.entity_manager.create(Enemy, 500, 100)

        while self.is_running:
            self.clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.controls.update()
            self.entity_manager.update()

            self.display.update()
