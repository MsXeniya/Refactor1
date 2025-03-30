import pytest


class MathOperations:
    def factorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def is_prime(self, num):
        if not isinstance(num, int) or num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def gcd(self, a, b):
        if not all(isinstance(i, int) for i in (a, b)):
            raise ValueError("GCD is only defined for integers")
        while b:
            a, b = b, a % b
        return abs(a) #число без знака


@pytest.fixture
def math_ops():
    return MathOperations()


def test_factorial(math_ops):
    assert math_ops.factorial(0) == 1
    assert math_ops.factorial(5) == 120
    with pytest.raises(ValueError):
        math_ops.factorial(-3)
    with pytest.raises(ValueError):
        math_ops.factorial(3.5)


def test_is_prime(math_ops):
    assert not math_ops.is_prime(1)
    assert math_ops.is_prime(2)
    assert not math_ops.is_prime(10)
    assert math_ops.is_prime(17) #17 простое
    assert not math_ops.is_prime(18) #18 не простое


def test_gcd(math_ops):
    assert math_ops.gcd(48, 18) == 6
    assert math_ops.gcd(5, 0) == 5 #Если одно число = 0, то вернет второе
    assert math_ops.gcd(-48, -18) == 6 #Всегда положительное
    with pytest.raises(ValueError):
        math_ops.gcd(48.5, 18)
