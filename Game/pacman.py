import pygame
from Game.map import Map

YELLOW = (250, 253, 15)


class PacMan:

    def __init__(self, x, y, map: Map) -> None:
        self.px, self.py = x, y   # Position
        self.dx, self.dy = 1, 0   # Directrion
        self.ndx, self.ndy = 1, 0 # Next direction

        self._points = 0
        self._map = map

    def turn(self, x, y):
        if self._map[self.px + x, self.py + y] == Map.Wall:
            self.ndx = x; self.ndy = y
        else:
            self.dx = x; self.dy = y
            self.ndx = x; self.ndy = y

    def move(self):
        x, y = self.px + self.dx, self.py + self.dy 
        square = self._map[x, y]
        
        if square == Map.Wall:
            return

        if square == Map.Point:
            self._map[x, y] = ' '
            self._points += (square == Map.Point)

        self.px = x; self.py = y
        
    def draw(self, screen: pygame.Surface, s: int):
        pygame.draw.rect(screen, YELLOW, (self.px * s, self.py * s, s, s))

    def check_dir(self):
        if self._map[self.px + self.ndx, self.py + self.ndy] != Map.Wall:
            self.dx = self.ndx; self.dy = self.ndy

