import functools
import math


def positive_int_domain(f, *args, **kwargs):
    """Restrict funcion's domain to Z+."""
    @functools.wraps(f)
    def _func(*args, **kwargs):
        for arg in args:
            if arg < 1:
                raise ValueError(f'Function {f.__name__} only works with positive values. Got {arg}.')
            if type(arg) != int:
                raise TypeError(f'Function {f.__name__} only works with integers. Got a(n) {type(arg)} value.')
        return f(*args, **kwargs)
    return _func


class primes(object):
    def __init__(self, start, stop):
        self.start = start if start >= 2 else 2
        self.stop = stop
        self.current = self.start

    def __iter__(self):
        return self

    def __increment__(self):
        # Two is the only even prime number.
        if self.current == 2:
            self.current += 1
        else:
            self.current += 2

    def __next__(self):
        if self.current < self.stop:
            while not self.is_prime(self.current):
                self.__increment__()
            tmp = self.current
            self.__increment__()
            return tmp
        else:
            raise StopIteration

    @staticmethod
    def is_prime(n):
        return is_prime(n)


@positive_int_domain
def is_prime(n):
    """Whether or not a number is prime."""
    for i in range(2, int(math.sqrt(n))+1):
        if not n % i:
            return False
    return True


@positive_int_domain
def is_relatively_prime(n, to):
    """Returns whether or not `n` is relatively prime to `to`."""
    if n == 1 or to % n:
        return True
    return False


@positive_int_domain
def factorize(n):
    """Return a list of prime numbers composing given number."""
    primes = []
    
    i = 1
    while n > 1 and i <= n:
        if i < 3:
            i += 1
        else:
            i += 2

        if not n % i and is_prime(i):
            primes.append(i)
            n //= i
            i = 1

    return primes


def product(arr):
    """Multiply all numbers in an array."""
    result = 1
    for i in arr:
        result *= i
    return result


if __name__ == "__main__":
    print([i for i in iter(primes(2, 50))])
