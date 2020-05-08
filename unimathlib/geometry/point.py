from .vector import Vector2, Vector3

class Point2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, others):
        if isinstance(others, Vector2):
            return Point2(self.x + others.x, self.y + others.y)
        else:
            raise NotImplementedError()

    def __iadd__(self, others):
        if isinstance(others, Vector2):
            self.x += others.x
            self.y += others.y
            return self
        else:
            raise NotImplementedError()

    def __eq__(self, others):
        if isinstance(others, Point2):
            return self.x == others.x and self.y == others.y
        else:
            raise NotImplementedError()

    def difference_vector(self, point: Point2) -> Vector2:
        return Vector2(point.x - self.x, point.y - self.y)

    def distance(self, point: Point2) -> float:
        return abs(self.difference_vector(point))


class Point3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, others):
        if isinstance(others, Vector3):
            return Point3(self.x + others.x, self.y + others.y, self.z + others.z)
        else:
            raise NotImplementedError()

    def __iadd__(self, others):
        if isinstance(others, Vector3):
            self.x += others.x
            self.y += others.y
            self.z += others.z
            return self
        else:
            raise NotImplementedError()

    def __eq__(self, others):
        if isinstance(others, Point3):
            return self.x == others.x and self.y == others.y and self.z == others.z
        else:
            raise NotImplementedError()

    def difference_vector(self, point: Point3) -> Vector3:
        return Vector3(point.x - self.x, point.y - self.y, point.z - self.z)

    def distance(self, point: Point3) -> float:
        return abs(self.difference_vector(point))
