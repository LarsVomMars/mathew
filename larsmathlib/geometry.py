from math import sqrt, acos, degrees


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
        else:
            raise NotImplementedError()

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
        else:
            raise NotImplementedError

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
        if isinstance(v3, Vector):
            x = self.y * v3.z - self.z * v3.y
            y = self.z * v3.x - self.x * v3.z
            z = self.x * v3.y - self.y * v3.x
            return Vector(x, y, z)
        else:
            raise NotImplementedError()

    def dot(self, v3) -> float:
        if isinstance(v3, Vector):
            x = self.x * v3.x
            y = self.y * v3.y
            z = self.z * v3.z
            return x + y + z
        else:
            raise NotImplementedError()

    def angle(self, v3) -> float:
        if isinstance(v3, Vector):
            return degrees(acos(self.dot(v3) / (abs(self) * abs(v3))))
        else:
            raise NotImplementedError()

    @staticmethod
    def from_points(p1, p2):
        if isinstance(p1, Point) and isinstance(p2, Point):
            return p1.difference_vector(p2)
        else:
            raise NotImplementedError()
