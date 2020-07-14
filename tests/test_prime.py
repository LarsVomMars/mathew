from mathew import prime

def test_primegen():
    assert list(prime.primegen(10)) == [2,3,5,7]


def test_is_prime():
    assert prime.is_prime(4567) == True
