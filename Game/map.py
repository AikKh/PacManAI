import pygame


class Map:

    Width = 28
    Height = 31

    Void = ' '
    Point = '.'
    Wall = '#'


    def __init__(self) -> None:
        self._grid = Map.get_grid()

    def __getitem__(self, pos) -> str: # char
        if type(pos) != tuple or len(pos) != 2:
            raise IndexError('Index must be a tuple of length 2')

        x, y = pos
        index = y * Map.Width + x

        return self._grid[index]

    def __setitem__(self, pos, value):
        if type(pos) != tuple or len(pos) != 2:
            raise IndexError('Index must be a tuple of length 2')

        x, y = pos
        index = y * Map.Width + x

        self._grid[index] = value

    def draw(self, square: str, draw_fn):
        for x in range(0, Map.Width):
            for y in range(0, Map.Height):
                if self[x, y] == square:
                    draw_fn(x, y)


    @staticmethod
    def get_grid():
        with open("Game/grid.txt", 'r') as f:
            map = list(f.read().replace("\n", ''))
        return map