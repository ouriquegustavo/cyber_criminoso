from pygame.time import Clock as PyGameClock


class Clock:
    def __init__(self, game):
        self.game = game

    def start(self, tps):
        self.tps = tps
        self.clock = PyGameClock()

    def tick(self):
        self.clock.tick(self.tps)
