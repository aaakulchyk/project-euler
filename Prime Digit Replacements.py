from _helpers import is_prime
from itertools import permutations


def replacements(pattern):
    """Yield candidate numbers after replacements."""
    pattern = ''.join(pattern)
    if pattern.find('*') == 0:
        start = 1
    else:
        start = 0
    
    for i in range(start, 10):
        yield int(pattern.replace('*', str(i)))


def num_primes(array):
    """Count prime numbers in a given sequence."""
    count = 0
    for num in array:
        if is_prime(num):
            count += 1
    return count


def patterns_generator(max_pattern_len=None):
    """Generate not permuted patterns."""
    if max_pattern_len is None:
        max_pattern_len = float('inf')
    pattern_len = 1
    while pattern_len <= max_pattern_len:
        for num_asterisks in range(1, pattern_len+1):
            #print(f'{num_asterisks} out of {pattern_len} symbols')
            start = int(pow(10, pattern_len-num_asterisks-1))
            stop = 10 * start
            for num in range(start, stop):
                yield '{}{}'.format(num, '*' * num_asterisks)
        pattern_len += 1


def main():
    for pattern in patterns_generator(3):
        for perm in permutations(pattern, len(pattern)):
            print(''.join(perm), end='; ')
            #print(f'\nLooking for replacements in pattern {"".join(perm)}')
            if num_primes([repl for repl in replacements(perm)]) == 8:
                print(''.join(perm).replace('0'))


if __name__ == "__main__":
    assert num_primes(list(range(2, 1000))) == 168, 'num_primes function'
    main()
