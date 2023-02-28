class Path:
    
    def __init__(self) -> None:
        self._n = 0
        self._path = []

    def add(self, value: tuple[int, int]):
        if type(value) != tuple or len(value) != 2:
            raise ValueError("must be tuple with 2 values (x, y)")
        
        self._path.append(value)

    def __iter__(self):
        for xy in self._path:
            yield xy
