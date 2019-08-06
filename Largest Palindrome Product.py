from _helpers import is_palindromic


def main():
    largest_palindrome = 0
    for i in range(110, 991, 11):
        for j in range(100, 1001):
            product = i * j
            if is_palindromic(product) and product > largest_palindrome:
                largest_palindrome = product
    print(largest_palindrome)


if __name__ == "__main__":
    main()
