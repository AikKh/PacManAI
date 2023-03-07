from Game.ChaseStrategies.strategy import ChaseStrategy, V2D


class Blinky(ChaseStrategy):

    def __init__(self, max_dist: int) -> None:
        super().__init__(max_dist)
        self._path = iter([])

    def chase(self, start: V2D, end: V2D):
        if self._n < 1:
            self.update_path(start, end)
        self._n -= 1
        
        return next(self._path)
    

    def update_path(self, start, end):
        path = self._finder.find_path(start, end) 
        self._n += (self._max_dist % len(path))
        self._path = iter(path)
        next(self._path)
        