from _helpers import is_prime


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


def main():
    limit = int(input('\nEnter a limit: '))
    
    primes = []
    for n in range(2, limit+1):
        p = factorize(n)
        for i in p:
            p_count = p.count(i)
            primes_count = primes.count(i)
            
            # Only append numbers if their count increases.
            for _ in range(p_count-primes_count):
                primes.append(i)

    print(f'The answer is {product(primes)}')


if __name__ == "__main__":
    main()
