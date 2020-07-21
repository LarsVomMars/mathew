from itertools import islice

def factor(num):
    """
    find a number factor
    """
    result_list = [i for i in range(num+1) if num%i == 0]
    return result_list
def is_prime(n: int) -> bool:
    """
    Checks if n is a prime number
    """
    result = True if len(factor(n)) == 2 else False
    return result


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


def nth_prime(n: int) -> int:
    """
    Returns the nth prime
    """
    return next(islice(primegen(), n, n + 1))


def largest_prime_factor(n: int) -> int:
    """
    Returns the largest prime factor of n
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


def prime_factors(n: int) -> list:
    """
    Returns all prime factors of n
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    return factors


def distinct_prime_factors(n: int) -> list:
    """
    Returns all distinct prime factors of n
    """
    factors = prime_factors(n)
    return list(dict.fromkeys(factors))
