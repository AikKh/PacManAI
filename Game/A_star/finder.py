from Game.map import Map


class Finder:

    def __init__(self, map: Map) -> None:
        self._map = map
        self._visited = []
        self._unvisited = []

    