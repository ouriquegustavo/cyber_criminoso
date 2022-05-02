import random


class EntityManager:
    def __init__(self, game):
        self.game = game
        self.entities = {}
        self.max_id = 65536

    def create(self, obj, *args, **kwargs):
        gid = random.randint(0, self.max_id)
        while gid in self.entities:
            gid = random.randint(0, self.max_id)
        o = obj(self.game, gid, *args, **kwargs)
        self.entities[gid] = o
        return o

    def destroy(self, gid):
        o = self.entities.pop(gid)
        del o

    def update(self):
        keys = list(self.entities.keys())
        for k in keys:
            self.entities[k].update()
