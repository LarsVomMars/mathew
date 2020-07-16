import pytest
from mathew import helper


def test_gcd():
    assert helper.gcd(3, 6) == 3
    assert helper.gcd(7, 5) == 1


def test_lcm():
    assert helper.lcm(5, 9) == 45


def test_fib():
    assert helper.fibonacci(3) == 2
    assert helper.fibonacci(-3) == 2


def test_factorial():
    assert helper.factorial(12) == 479001600
    with pytest.raises(ValueError):
        helper.factorial(-5)
