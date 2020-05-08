from math import sqrt


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, other.z)
        else:
            raise NotImplementedError()

    def __iadd__(self, other):
        if isinstance(other, Vector2):
            self.x += other.x
            self.y += other.y
            return self

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, other.z)
        else:
            raise NotImplementedError()

    def __isub__(self, other):
        if isinstance(other, Vector2):
            self.x -= other.x
            self.y -= other.y
            return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        else:
            raise NotImplementedError()

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            return self
        else:
            raise NotImplementedError()

    def __copy__(self):
        return self

    def __eq__(self, other) -> bool:
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y
        else:
            raise NotImplementedError()


class Vector3:
    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, Vector2):
            return Vector3(self.x + other.x, self.y + other.y, self.z)
        else:
            raise NotImplementedError()

    def __iadd__(self, other):
        if isinstance(other, Vector3):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        else:
            raise NotImplementedError()

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vector2):
            return Vector3(self.x - other.x, self.y - other.y, self.z)
        else:
            raise NotImplementedError()

    def __isub__(self, other):
        if isinstance(other, Vector3):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        else:
            raise NotImplementedError()

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
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
        if isinstance(other, Vector3):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            raise NotImplementedError()
