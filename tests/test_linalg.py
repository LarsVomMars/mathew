from mathew.linalg import *


def test_line():
    p1 = Point(1, 2, 3)
    p2 = Point(3, 4, 5)
    l1 = Line(p1, Vector(2, 3, 4))
    l2 = Line(p2, Vector(4, 5, 6))
    l3 = Line(Point(0, 0, 0), Vector(1, 0, 0))
    assert l1.has(p1)
    assert not l1.has(p2)
    assert l1.intersects(l2) == l2.intersects(l1) == (Positions.INTERSECT, Point(-1, -1, -1))
    assert l1.intersects(l3) == l3.intersects(l1) == (Positions.SKEW, 0.2)
    p3 = Point(1, 0, 0)
    p4 = Point(3, 2, 6)
    v1 = Vector(2, 1, 1)
    l4 = Line(p3, v1)
    l5 = Line(p4, v1)
    assert l4.intersects(l5)


def test_vector():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 8, 12)
    assert v1 + v2 == Vector(5, 10, 15)
    assert v2 - v1 == Vector(3, 6, 9)
    assert 4 * v1 == v2
    assert v1.co_linear(v2)


def test_point():
    p1 = Point(1, 1, 1)
    p2 = Point(3, 3, 3)
    v1 = Vector(2, 2, 2)
    assert p1 + v1 == p2
    assert not p1 == p2


def test_matrix():
    m = Matrix([
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 6],
    ])
    res = [4, 5, 6]
    facs = solve(m, res)
    assert facs == [-2, 3, 0]
