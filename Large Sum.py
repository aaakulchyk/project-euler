def main():
    result = 0

    with open('./large_numbers.txt') as f:
        for i, num in enumerate(f.readlines()):
            result += int(num)
        print(i)

    print(result)


if __name__ == "__main__":
    main()
