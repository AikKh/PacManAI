from Game.vector import V2D
from Game.map import Map


class Path:
    
    def __init__(self) -> None:
        self._path: list[V2D] = []

    def add(self, value: V2D):
        if type(value) != V2D:
            raise ValueError("must be a vector")
        self._path.append(value)

    def __iter__(self):
        for xy in self._path[::-1]:
            yield xy

    def __len__(self) -> int:
        return len(self._path)

    def __repr__(self) -> str:
        map = Map.get_grid()

        direct = lambda vector: {
            vector.x < 0 and vector.y == 0: '→',
            vector.x > 0 and vector.y == 0: '←',
            vector.x == 0 and vector.y > 0: '↑',
            vector.x == 0 and vector.y < 0: '↓'
        }.get(True, "F")
        
        if len(self._path):
            for i, (x, y) in enumerate(self._path[1:]):
                prev = self._path[i]
                dir = V2D(x - prev.x, y - prev.y)

                map[y * Map.Width + x] = direct(dir)

        map = [[map[i] for i in range(j, j + Map.Width)] for j in range(0, Map.Height * Map.Width, Map.Width)]
        str_map = '\n'.join([''.join(m) for m in map])
        return str_map



        
