from math import sqrt, acos, degrees

from larsmathlib.geometry.point import *


class Vector:
    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise NotImplementedError()

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise NotImplementedError()

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            self.z -= self.z
            return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise NotImplementedError()

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise NotImplementedError()

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            self.z *= other
            return self
        else:
            raise NotImplementedError()

    def __copy__(self):
        return self

    def __eq__(self, other) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            raise NotImplementedError()

    def __str__(self):
        return str({'x': self.x, 'y': self.y, 'z': self.z})

    def cross(self, v3):
        x = self.y * v3.z - self.z * v3.y
        y = self.z * v3.x - self.x * v3.z
        z = self.x * v3.y - self.y * v3.x
        return Vector(x, y, z)

    def dot(self, v3) -> float:
        x = self.x * v3.x
        y = self.y * v3.y
        z = self.z * v3.z
        return x + y + z

    def angle(self, v3) -> float:
        return degrees(acos(self.dot(v3)/(abs(self)*abs(v3))))

    @staticmethod
    def from_points(p1, p2):
        return p1.difference_vector(p2)
