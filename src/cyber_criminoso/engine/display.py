import pygame

def sort_zorder(v):
    return v.zorder


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
        
    def get_zorder(self, obj):
        return obj.zorder

    def update(self):
        self.display.fill((0, 0, 0))


        keys = [
            v.gid
            for v in sorted(
                self.game.entity_manager.entities.values(),
                key=sort_zorder
            )
        ]
        for k in keys:
            self.game.entity_manager.entities[k].draw()

        pygame.display.flip()
        pass
