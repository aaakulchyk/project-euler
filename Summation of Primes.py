from _helpers import is_prime


def main():
    limit = int(input('\nEnter a limiting prime number: '))
    result = 2
    n = 3
    while n < limit:
        if is_prime(n):
            result += n
        n += 2
    print(result)


if __name__ == '__main__':
    main()
