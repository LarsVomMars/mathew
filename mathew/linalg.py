from enum import IntEnum
from math import sqrt, acos, degrees
from typing import Union, Tuple, List


class Positions(IntEnum):
    INTERSECT = 0
    TRUE_PARALLEL = 1
    CO_LINEAR = CONGRUENT = 2
    SKEW = 3
    NON_INTERSECT = 4
    IN_PLANE = 5


class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, others):
        if isinstance(others, Vector):
            return Point(self.x + others.x, self.y + others.y, self.z + others.z)
        elif isinstance(others, Point):
            return Vector(self.x + others.x, self.y + others.y, self.z + others.z)
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
        elif isinstance(others, Point):
            return Vector(self.x - others.x, self.y - others.y, self.z - others.z)
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

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __len__(self):
        return self.__abs__()

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
        elif isinstance(other, Vector):
            return self.dot(other)
        else:
            raise NotImplementedError()

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.dot(other)
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


class Matrix:
    def __init__(self, matrix: List[List[float]]):
        self.m = matrix
        if any(len(matrix[i]) != len(matrix[i - 1]) for i in range(1, len(matrix))):
            raise TypeError("All rows must me the same length")

    def __getitem__(self, item):
        return self.get_row(item)

    def size(self) -> Tuple[int, int]:
        return len(self.m), len(self.m[0])

    def arith_add_rows(self, row: int, add: int, mul: float = 1):
        add_row = self.m[add]
        base_row = self.m[row]
        for i in range(len(add_row)):
            add_row[i] += base_row[i] * mul
        self.m[add] = add_row

    def get_row(self, row: int) -> List[float]:
        return self.m[row]

    def get_col(self, col: int) -> List[float]:
        return [row[col] for row in self.m]


class Line:
    def __init__(self, a: Point, b: Vector):
        self.p = a
        self.v = b

    def __str__(self):
        return f"{self.p} + r * {self.v}"

    def __repr__(self):
        return f"Line({repr(self.p)}, {repr(self.v)})"

    def has(self, point) -> bool:
        """
        Checks if point is on the line
        """
        if isinstance(point, Point):
            r1 = (point.x - self.p.x) / self.v.x
            r2 = (point.y - self.p.y) / self.v.y
            r3 = (point.z - self.p.z) / self.v.z
            return r1 == r2 == r3
        else:
            raise NotImplementedError()

    def value(self, r: float) -> Point:
        """
        Returns point for a certain value of r
        """
        return self.p + r * self.v

    def intersects(self, line) -> Union[Positions, Tuple[Positions, Union[Point, float]]]:
        """
        Checks if lines intersect and returns PoI or the minimal distance between the lines
        """
        if isinstance(line, Line):
            if self.v.co_linear(line.v):
                if self.has(line.p):
                    return Positions.CONGRUENT
                else:
                    t = - line.v.dot(line.p - self.p) / line.v.dot(line.v)
                    p = line.value(t)
                    return Positions.TRUE_PARALLEL, self.p.distance(p)
            else:
                # Too lazy to solve SoLE
                r = (self.p.y - line.p.y + ((line.p.x - self.p.x) / self.v.x) * self.v.y) / (
                        line.v.y - (line.v.x * self.v.y / self.v.x))
                t = (line.p.x - self.p.x + r * line.v.x) / self.v.x

                if self.p.z + t * self.v.z == line.p.z + r * line.v.z:
                    return Positions.INTERSECT, self.p + t * self.v
                else:
                    n = self.v.cross(line.v)
                    dist = (n.dot(line.p - self.p)) / abs(n)
                    return Positions.SKEW, abs(dist)
        else:
            raise NotImplementedError()

    def angle(self, line):
        """
        Computes the angle between two lines
        """
        if isinstance(line, Line):
            return acos(abs(self.v * line.v) / (abs(self.v) * abs(line.v)))
        else:
            raise NotImplementedError()

    @staticmethod
    def from_points(p1: Point, p2: Point):
        """
        Creates the line between two points
        """
        if isinstance(p1, Point) and isinstance(p2, Point):
            v2 = Vector.from_points(p1, p2)
            return Line(p1, v2)
        else:
            raise NotImplementedError()


class Plane:
    def __init__(self, a: float, b: float, c: float, d: float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def has_point(self, p: Point):
        return self.a * p.x + self.b * p.y + self.c * p.z == self.d

    def intersects_line(self, line: Line) -> Union[Positions, Tuple[Positions, Point]]:
        v = Vector(self.a, self.b, self.c)
        denom = v.dot(line.v)
        # TODO: Check if in plane
        if denom != 0:
            r = (self.d - (v.dot(line.p))) / denom
            return Positions.INTERSECT, line.p + r * line.v
        else:
            return Positions.TRUE_PARALLEL

    def intersects_plane(self, plane):
        pass

    @staticmethod
    def from_points(p1: Point, p2: Point, p3: Point):
        """
        Creates a plane from the three points
        Converts from parametric to cartesian
        """
        if isinstance(p1, Point) and isinstance(p2, Point) and isinstance(p3, Point):
            v1 = Vector.from_origin(p1)
            v2 = Vector.from_points(p1, p2)
            v3 = Vector.from_points(p1, p3)
            n = v2.cross(v3)
            d = n.dot(v1)
            return Plane(n.x, n.y, n.z, d)
        else:
            raise NotImplementedError()

    @staticmethod
    def from_normal(p: Point, n: Vector):
        if isinstance(p, Point) and isinstance(n, Vector):
            v = Vector.from_origin(p)
            d = n.dot(v)
            return Plane(n.x, n.y, n.z, d)
        else:
            raise NotImplementedError()


def solve(eq: Matrix, res: List[float]) -> List[float]:
    """
    Inefficient solver for systems of linear equations using gaussian elimination
    """
    rows, cols = eq.size()

    assert (rows == len(res)) and "Sizes should be the same"
    assert (rows == cols) and "Matrix should be a square matrix"

    for i in range(rows - 1):
        row = eq.get_row(i)
        for j in range(i + 1, rows):
            mul = -row[j] / row[i]
            eq.arith_add_rows(i, j, mul)
            res[j] += mul * res[i]

    solved = []
    for i in range(rows - 1, -1, -1):
        r = res[i]
        for ci in range(cols):
            if len(solved) > ci:
                r -= eq[i][cols - ci - 1] * solved[ci]
            else:
                solved.append(r / eq[i][cols - ci - 1])
                break
    return solved[::-1]
