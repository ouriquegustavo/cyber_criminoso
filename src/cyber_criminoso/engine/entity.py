class Entity:
    def __init__(self, game, gid):
        self.game = game
        self.gid = gid
        self.kind = 'kind'
        self.targets = []
        self.zorder = 0
        self.radius = 0

    def update(self):
        pass
        
    def check_for_collision(self):
        for k, v in self.game.entity_manager.entities.items():
            if v.kind in self.targets:
                dx = v.x - self.x
                dy = v.y - self.y
                drsq = dx * dx + dy * dy
                drr = self.radius + v.radius
                drrsq = drr * drr
                if drsq <= drrsq:
                    return v
        return False

    def draw(self):
        pass
