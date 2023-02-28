import pygame
from Game.map import Map
from Game.vector import V2D
from threading import Thread
from Game.pacman import PacMan
from Game.ChaseStrategies.strategy import ChaseStrategy


class Ghost():

    def __init__(self, position: V2D, color: tuple, stategy: ChaseStrategy) -> None:
        super().__init__()
        self.pos = position
        self._color = color
        self._stategy = stategy

    def move(self):
        pass
        # self._stategy.chase(self.pos)
        # # print(dx, dy)
        # self.pos

    def draw(self, screen: pygame.Surface, s: int):
        pygame.draw.rect(screen, self._color, (self.pos.x * s, self.pos.y * s, s, s))
