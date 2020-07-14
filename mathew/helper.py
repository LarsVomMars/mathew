def gcd(a: int, b: int) -> int:
    """
    Calculate greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """
    Calculate the lowest common multiply of a and b
    """
    return int(abs(a * b) / gcd(a, b))  # Will always be of type int
