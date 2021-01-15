import pytest

from mathew import helper


def test_fib():
    assert helper.fibonacci(3) == 2
    assert helper.fibonacci(-3) == 2


def test_factorial():
    assert helper.factorial(12) == 479001600
    with pytest.raises(ValueError):
        helper.factorial(-5)
