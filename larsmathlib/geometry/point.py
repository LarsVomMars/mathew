from larsmathlib.geometry.vector import *


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, others):
        if isinstance(others, Vector):
            return Point(self.x + others.x, self.y + others.y, self.z + others.z)
        else:
            raise NotImplementedError()

    def __iadd__(self, others):
        if isinstance(others, Vector):
            self.x += others.x
            self.y += others.y
            self.z += others.z
            return self
        else:
            raise NotImplementedError()

    def __eq__(self, others) -> bool:
        if isinstance(others, Point):
            return self.x == others.x and self.y == others.y and self.z == others.z
        else:
            raise NotImplementedError()

    def __str__(self) -> str:
        return str({'x': self.x, 'y': self.y, 'z': self.z})

    def difference_vector(self, point):
        if isinstance(point, Point):
            return Vector(point.x - self.x, point.y - self.y, point.z - self.z)
        else:
            raise NotImplementedError()

    def distance(self, point) -> float:
        if isinstance(point, Point):
            return abs(self.difference_vector(point))
        else:
            raise NotImplementedError()
