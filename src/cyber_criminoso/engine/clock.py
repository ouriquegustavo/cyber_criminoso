from pygame.time import Clock as PyGameClock


class Clock:
    def __init__(self, game):
        self.game = game
        self.t = 0
        self.task_dict = {}

    def start(self, tps):
        self.tps = tps
        self.clock = PyGameClock()

    def tick(self):
        self.clock.tick(self.tps)
        
    def create_task(self, key, delay, function, fargs=(), fkwargs={}):
        self.task_dict[key] = {
            'key': key,
            'instant': self.t + delay,
            'function': function,
            'args': fargs,
            'kwargs': fkwargs
            
        }
    
    def destroy_task(self, key):
        if key in self.task_dict:
            self.task_dict.pop(key)
            
    def execute_task(self, key):
        self.task_dict[key]['function'](
            *self.task_dict[key]['args'],
            **self.task_dict[key]['kwargs']
        )
        self.destroy_task(key)
        
    def update(self):
        self.t += 1
        # Evitar que o dicionário mude de tamanho durante a execução
        tasks = list(self.task_dict.keys())
        for key in tasks:
            if self.t >= self.task_dict[key]['instant']:
                self.execute_task(key)
                
        self.tick()
