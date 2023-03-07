from Game.map import Map
from Game.vector import V2D
from abc import ABC, abstractmethod
from Game.A_star.finder import Finder



class ChaseStrategy(ABC):

    def __init__(self, max_dist: int) -> None:
        super().__init__()
        self._n = 0
        self._max_dist = max_dist

        self._finder = Finder(Map())
    
    @abstractmethod
    def chase(self, pos: V2D) -> tuple[int, int]: pass
