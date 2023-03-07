import pygame
from Game.map import Map
from Game.vector import V2D

YELLOW = (250, 253, 15)


class PacMan:

    def __init__(self, position: V2D, map: Map) -> None:
        self.pos = position   # Position
        self.dir = V2D(1, 0)  # Directrion
        self.ndir = V2D(1, 0) # Next direction

        self._points = 0
        self._map = map

        self._is_dead = False

    
    def die(self):
        self._is_dead = True

    def turn(self, x, y):
        direction = V2D(x, y)
        if self._map[self.pos + direction] == Map.Wall:
            self.ndir = direction
        else:
            self.dir = direction
            self.ndir = direction

    def move(self):
        next_pos = self.pos + self.dir
        next_pos.x %= Map.Width
        square = self._map[next_pos]
        
        if square == Map.Wall:
            return

        if square == Map.Point:
            self._map[next_pos] = ' '
            self._points += (square == Map.Point)

        self.pos = next_pos
        
    def draw(self, screen: pygame.Surface, s: int):
        pygame.draw.rect(screen, YELLOW, (self.pos.x * s, self.pos.y * s, s, s))

    def check_dir(self):
        if self._map[self.pos + self.ndir] != Map.Wall:
            self.dir = self.ndir

