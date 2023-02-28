from Game.map import Map
from Game.vector import V2D
from Game.pacman import PacMan
from abc import ABC, abstractmethod



class ChaseStrategy(ABC):

    def __init__(self, map: Map, pacman: PacMan) -> None:
        super().__init__()
        self._map = map
        self._pacman = pacman
    
    @abstractmethod
    def chase(self, pos: V2D) -> tuple[int, int]: pass
