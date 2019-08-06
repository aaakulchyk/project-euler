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


def non_negative_int_domain(f, *args, **kwargs):
    """Restrict funcion's domain to Z+."""
    @functools.wraps(f)
    def _func(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError(f'Function {f.__name__} only works with non-negative values. Got {arg}.')
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
def is_relatively_prime(n, m):
    """Returns whether or not `n` is relatively prime to `m`."""
    min_ = min(n, m)
    i = 2
    while i <= min_:
        if (not n % i) and (not m % i):
            return False
        i += 1
    return True


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


@non_negative_int_domain
def get_rank(n):
    """How many digits a number has in decimal notation."""
    rank = 0
    while n:
        rank += 1
        n //= 10
    return rank


@non_negative_int_domain
def is_palindromic_dummy(n):
    """Figure out whether `n` is palindromic in decimal system using strings."""
    if n < 10:
        return True
    string_repr = str(n)
    rank = len(string_repr)
    if not rank % 2:
        return string_repr[:rank//2] == string_repr[-1:-rank//2-1:-1]
    else:
        return string_repr[:rank//2] == string_repr[-1:-rank//2:-1]


@non_negative_int_domain
def is_palindromic(n):
    """Figure out whether `n` is palindromic in decimal system."""

    # Treating one-digit numbers as base case.
    if n < 10:
        return True
    
    rank = get_rank(n)
    if n // pow(10, rank-1) != n % 10:
        return False
    else:
        next_n = (n % pow(10, rank-1)) // 10
        next_rank = get_rank(next_n)
        #print(f'n = {n}, rank={rank}, next_n = {next_n}, next_rank = {next_rank}')
        if rank - next_rank == 2:
            return is_palindromic(next_n)
        else:
            if not next_n % 10:
                return is_palindromic(next_n // 10)
            else:
                return False
            

def is_integer(n):
    """Returns whether `n` is an integer."""
    return not n % 1


def digits_product(digits):
    """Find the product of all digits in `digits: iterable`."""
    prod = 1
    for d in digits:
        prod *= int(d)
    return prod
