from mathew import prime


def test_primegen():
    assert list(prime.primegen(10)) == [2, 3, 5, 7]


def test_is_prime():
    assert prime.is_prime(4567)
    assert prime.is_prime(4568)
    assert prime.is_prime(1277)


def test_primefac():
    assert prime.prime_factors(12) == [2, 2, 3]
    assert prime.prime_factors(1277) == [1277]
    assert prime.prime_factors(128) == [2, 2, 2, 2, 2, 2, 2]


def test_distinct_primefac():
    assert prime.distinct_prime_factors(12) == [2, 3]
    assert prime.distinct_prime_factors(128) == [2]
    assert prime.distinct_prime_factors(45642156465) == [3, 5, 3042810431]
