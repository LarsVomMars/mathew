def is_prime(n: int) -> bool:
    """
    Checks if n is a prime number
    """
    if n < 1:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def primegen(max_prime: int = None):
    """
    Yields primes to max_prime if defined
    """
    yield 2
    yield 3
    yield 5
    yield 7
    yield 11
    yield 13
    pg = primegen()
    p = next(pg) and next(pg)
    q = p ** 2
    sieve = {}
    n = 13

    while True:
        if n not in sieve:
            if n < q:
                if max_prime is None or n < max_prime:
                    yield n
                else:
                    return
            else:
                nxt = q + 2 * p
                step = 2 * p
                while nxt in sieve:
                    nxt += step
                sieve[nxt] = step
                p = next(pg)
                q = p ** 2

        else:
            step = sieve.pop(n)
            nxt = n + step
            while nxt in sieve:
                nxt += step
            sieve[nxt] = step

        n += 2
