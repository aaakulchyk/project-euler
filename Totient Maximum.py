import sys
from _helpers import is_relatively_prime


def totient(n):
    """Return relatively prime numbers for `n`."""
    result = set([1])
    for i in range(2, n):
        if is_relatively_prime(i, n):
            result.add(i)
    return result


def main():
    try:
        limit = int(input('\nEnter a limit: '))
    except ValueError:
        sys.exit()
    
    max_frac = 0
    ans = 0

    # n/totient(n) is always greater for even successors.
    for n in range(2, limit+1, 2):
        frac = n / len(totient(n))
        if frac > max_frac:
            max_frac = frac
            ans = n
        print(n)
    
    print(f'Maximum ratio = {max_frac} for {ans}')



if __name__ == "__main__":
    main()
    #print(is_relatively_prime(5, 10))
    #print(f'Totients of 10 = {totient(10)}')
