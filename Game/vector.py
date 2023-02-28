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
    

