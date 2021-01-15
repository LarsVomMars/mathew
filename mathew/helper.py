from math import sqrt

from .constants import GOLDEN_RATIO


def fibonacci(n: complex) -> complex:
    """
    Calculating fibonacci numbers using the binet formula
    """
    return (pow(GOLDEN_RATIO, n) - pow(-GOLDEN_RATIO, -n)) / (sqrt(5))


def fibonacci_limit(cap: int) -> list:
    """
    Yields all fibonacci numbers up to a certain limit
    """
    i = 0
    fib_val = fibonacci(i)
    while fib_val <= cap:
        yield fib_val
        i += 1
        fib_val = fibonacci(i)


def factorial(n: int) -> int:
    """
    Returns the factorial of n
    """
    if n < 0:
        raise ValueError("n must be greater then or equal to 0")
    elif n == 0:
        return 0
    else:
        f = 1
        for i in range(2, n + 1):
            f *= i
        return f
