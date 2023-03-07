from dataclasses import dataclass


# making class struct type
@dataclass
class V2D:
    x: int
    y: int

    def __add__(self, value):
        if type(value) == int:
            return V2D(self.x + value, self.y + value)
        elif type(value) == V2D:
            return V2D(self.x + value.x, self.y + value.y)
        raise TypeError("incorrect add value")

    def __iter__(self):
        yield self.x
        yield self.y
    
    def __eq__(self, __o: object) -> bool:
        if type(__o) is V2D:
            return self.x == __o.x and self.y == __o.y
        return False

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"