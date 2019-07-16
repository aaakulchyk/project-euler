import math


def largest_prime_factor(n):
    max_prime = -1
    
    while not n % 2:
        max_prime = 2
        n >>= 1

    for i in range(3, int(math.sqrt(n))+1, 2):
        while not n % i:
            max_prime = i
            n /= i
        
    if n > 2:
        max_prime = n

    return max_prime


if __name__ == "__main__":
    print(largest_prime_factor(int(input('Number: '))))