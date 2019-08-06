import math


def get_rank(n):
    """How many digits a number has in decimal notation."""
    rank = 0
    while n:
        rank += 1
        n //= 10
    return rank


def is_palindromic(n):
    """Figure out whether a number is palindromic in decimal system."""
    rank = get_rank(n)
    if n < 10:
        return True
    
    power = pow(10, rank-1)
    if n % 10 == n // power:
        next_number = (n // 10) % (power // 10)
        return is_palindromic((n // 10) % pow(10, rank-2)) if next_number > 0 else True
    return False


def add_reversed(n):
    """Add the reversed n to n. E.g. 394 + 493"""
    result = n
    rank = get_rank(n)
    for i in range(1, rank+1):
        summand = (n % 10) * pow(10, rank-i)
        result += summand
        n //= 10
    return result


def is_lychrel_number(n):
    """Figure out whether a number form a palindrome in max. 50 iterations."""
    for _ in range(50):
        n = add_reversed(n)
        if is_palindromic(n):
            return False
    return True



def main():
    limit = int(input('\nEnter a limit for counting Lychel numbers: '))
    count = 0
    lychrel_nums = []
    for num in range(12, limit):
        if is_lychrel_number(num):
            lychrel_nums.append(num)
            count += 1
    #print(*lychrel_nums)
    print('\n', count)


if __name__ == "__main__":
    main()
