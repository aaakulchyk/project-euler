def squared_sum(n):
    """Find squared sum of natural numbers up to n."""
    result = 0
    for num in range(1, n+1):
        result += num ** 2
    return result


def sum_of_squares(n):
    """Find sum of squares of natural numbers up to n."""
    result = 0
    for num in range(1, n+1):
        result += num
    return result * result


def main():
    n = int(input('\nEnter a number: '))
    print(sum_of_squares(n) - squared_sum(n))


if __name__ == "__main__":
    main()
