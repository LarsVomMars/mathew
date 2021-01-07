from enum import IntEnum
from math import sqrt, acos, degrees
from typing import Union, Tuple


class Positions(IntEnum):
    INTERSECT = 0
    TRUE_PARALLEL = 1
    CO_LINEAR = CONGRUENT = 2
    SKEW = 3
    NON_INTERSECT = 4


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

    def __sub__(self, others):
        if isinstance(others, Vector):
            return Point(self.x - others.x, self.y - others.y, self.z - others.z)
        else:
            raise NotImplementedError()

    def __isub__(self, others):
        if isinstance(others, Vector):
            self.x -= others.x
            self.y -= others.y
            self.z -= others.z
            return self
        else:
            raise NotImplementedError()

    def __eq__(self, others) -> bool:
        if isinstance(others, Point):
            return self.x == others.x and self.y == others.y and self.z == others.z
        else:
            raise NotImplementedError()

    def __str__(self):
        return f"({self.x}|{self.y}|{self.z})"

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def difference_vector(self, point):
        """
        Returns the vector between self and another point
        """
        if isinstance(point, Point):
            return Vector(point.x - self.x, point.y - self.y, point.z - self.z)
        else:
            raise NotImplementedError()

    def distance(self, point) -> float:
        """
        Returns the length of the vector between self and another point
        """
        if isinstance(point, Point):
            return abs(self.difference_vector(point))
        else:
            raise NotImplementedError()

    def on_line(self, line) -> bool:
        if isinstance(line, Line):
            return line.has(self)
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
        return f"({self.x}|{self.y}|{self.z})"  # Hmm

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def cross(self, v3):
        """
        Calculates the cross product of self and another vector
        """
        if isinstance(v3, Vector):
            x = self.y * v3.z - self.z * v3.y
            y = self.z * v3.x - self.x * v3.z
            z = self.x * v3.y - self.y * v3.x
            return Vector(x, y, z)
        else:
            raise NotImplementedError()

    def dot(self, v3) -> float:
        """
        Calculates the dot product of self and another vector
        """
        if isinstance(v3, Vector):
            x = self.x * v3.x
            y = self.y * v3.y
            z = self.z * v3.z
            return x + y + z
        else:
            raise NotImplementedError()

    def angle(self, v3) -> float:
        """
        Calculates the angle between self and another vector
        """
        if isinstance(v3, Vector):
            return degrees(acos(self.dot(v3) / (abs(self) * abs(v3))))
        else:
            raise NotImplementedError()

    def co_linear(self, vector):
        """
        Checks if vectors are co-linear (multiples of each other)
        """
        if isinstance(vector, Vector):
            if vector.x == 0 or vector.y == 0 or vector.z == 0:
                return False
            r1 = self.x / vector.x
            r2 = self.y / vector.y
            r3 = self.z / vector.z
            return r1 == r2 == r3
        else:
            raise NotImplementedError()

    @staticmethod
    def from_points(p1: Point, p2: Point):
        """
        Creates the vector between two points
        """
        if isinstance(p1, Point) and isinstance(p2, Point):
            return p1.difference_vector(p2)
        else:
            raise NotImplementedError()

    @staticmethod
    def from_origin(p: Point):
        """
        Creates the vector between the origin and p
        """
        if isinstance(p, Point):
            o = Point(0, 0, 0)
            return Vector.from_points(o, p)
        else:
            raise NotImplementedError()


class Line:
    def __init__(self, a: Point, b: Vector):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + r * {self.b}"

    def __repr__(self):
        return f"Line({repr(self.a)}, {repr(self.b)})"

    def has(self, point) -> bool:
        """
        Checks if point is on the line
        """
        if isinstance(point, Point):
            r1 = (point.x - self.a.x) / self.b.x
            r2 = (point.y - self.a.y) / self.b.y
            r3 = (point.z - self.a.z) / self.b.z
            return r1 == r2 == r3
        else:
            raise NotImplementedError()

    def value(self, r: float) -> Point:
        """
        Returns point for a certain value of r
        """
        return self.a + r * self.b

    def intersects(self, line) -> Union[Positions, Tuple[Positions, Point]]:
        """
        Checks if lines intersect and returns PoI
        """
        if isinstance(line, Line):
            if self.b.co_linear(line.b):
                if self.has(line.a):
                    return Positions.CONGRUENT
                else:
                    return Positions.TRUE_PARALLEL
            else:
                # Too lazy to solve SoLE
                r = (self.a.y - line.a.y + ((line.a.x - self.a.x) / self.b.x) * self.b.y) / (
                        line.b.y - (line.b.x * self.b.y / self.b.x))
                t = (line.a.x - self.a.x + r * line.b.x) / self.b.x

                if self.a.z + t * self.b.z == line.a.z + r * line.b.z:
                    return Positions.INTERSECT, self.a + t * self.b
                else:
                    return Positions.SKEW
        else:
            raise NotImplementedError()

    @staticmethod
    def from_points(p1: Point, p2: Point):
        """
        Creates the line between two points
        """
        if isinstance(p1, Point) and isinstance(p2, Point):
            v1 = p1
            v2 = Vector.from_points(p1, p2)
            return Line(v1, v2)
        else:
            raise NotImplementedError()
