import sys
from Game.A_star.path import Path
from Game.map import Map
from Game.vector import V2D
from dataclasses import dataclass
from math import sqrt

# sys.setrecursionlimit(10000)


class Finder:

    @dataclass
    class Square:
        _position: V2D
        _previous: object = None
        _visited: bool = False

        G: int = 0
        '''Distance from A to square'''
        H: int = 0
        '''Distance from B to square'''

        @property
        def F(self):
            '''Sum of G and H'''
            return self.G + self.H


    def __init__(self, map: Map) -> None:
        self._map = map

        self._squares: list[list[Finder.Square]] = None
        self._start: Finder.Square
        self._end: Finder.Square


    def find_path(self, a: V2D, b: V2D) -> Path:
        self._squares = [[self.__get_square(V2D(x, y), b)   
                          for x in range(Map.Width)] 
                          for y in range(Map.Height)]
         
        self._start = self._squares[a.y][a.x]
        self._end = self._squares[b.y][b.x]

        return self.__finding(self._start)
        

    def __finding(self, *to_visit: list[Square]):
        for square in to_visit:
            square._visited = True
            px, py = square._position
            
            if square is self._end:
                path = Path()
                return self.__create_path(square, path)

            
            neighbours = [self._squares[py + y][(px + x) % Map.Width]
                          for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
                    
            for neighbour in neighbours:
                if not neighbour or neighbour._visited:
                    continue
                
                neighbour._previous = square
                g = square.G + 1

                if neighbour.G == 0 or g < neighbour.G:
                    neighbour.G = g

        return self.__finding(*self.for_visiting())


    def __create_path(self, square, path) -> Path:
        path.add(square._position)
        if square._previous:
            return self.__create_path(square._previous, path)
        return path


    def for_visiting(self) -> list[Square]:
        to_visit = [s for row in self._squares for s in row if s and s.G > 0 and not s._visited]
        min_value = min(to_visit, key = lambda sq: sq.F).F

        return [n for n in to_visit if n.F == min_value]


    def __get_square(self, position: V2D, target: V2D):
        if self._map[position] == Map.Wall or position.x // Map.Width != 0 or position.y // Map.Height != 0:
            return None

        square = Finder.Square(position, _visited = False)
        h = round(sqrt((target.x - position.x) ** 2 + (target.y - position.y) ** 2))
        square.H = h

        return square 

        