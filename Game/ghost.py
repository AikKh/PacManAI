import pygame
from Game.vector import V2D
from Game.pacman import PacMan
from Game.ChaseStrategies.strategy import ChaseStrategy


class Ghost:

    def __init__(self, position: V2D, target: PacMan, color: tuple, T: type[ChaseStrategy]) -> None:
        super().__init__()
        self._pos = position
        self._target = target
        self._color = color
        self._stategy = T(10)

    def move(self):
        if self._pos == self._target.pos:
            return self._target.die()
        self._pos = self._stategy.chase(self._pos, self._target.pos)

    def draw(self, screen: pygame.Surface, s: int):
        pygame.draw.rect(screen, self._color, (self._pos.x * s, self._pos.y * s, s, s))
