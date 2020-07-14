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

    yields = [2, 3, 5, 7, 11, 13]
    for y in yields:
        if max_prime is None or y < max_prime:
            yield y
        else:
            return 

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
