from Game.ChaseStrategies.strategy import Map, PacMan, ChaseStrategy, V2D


class Blinky(ChaseStrategy):

    def __init__(self, map: Map, pacman: PacMan) -> None:
        super().__init__(map, pacman)

    def chase(self, pos: V2D):
        pass
        # dx = self._pacman.px - x 
        # dy = self._pacman.py - y

        # # distx = abs(dx)
        # # disty = abs(dy)
        
        # dirx = 1 if dx > 0 else -1
        # diry = 1 if dy > 0 else -1


        # next_x = x + dirx
        # next_y = y + diry


        # square_x = self._map[next_x, y]
        # # square_y = self._map[x, next_y]

        # x = dirx if square_x in [Map.Void, Map.Point] else 0
        # y = diry if x == 0 else 0

        # # y = diry if square_y in [Map.Void, Map.Point] else 0

        # # print(x, y)
        # # print("-----------------------")

        # return x, y


        