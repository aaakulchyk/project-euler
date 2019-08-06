import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if not n % i:
            return False
    return True


def main():
    i = 10001
    num = 3
    while i > 1:
        if is_prime(num):
            latest_prime = num
            i -= 1
        num += 2
    print(latest_prime)


if __name__ == "__main__":
    main()
