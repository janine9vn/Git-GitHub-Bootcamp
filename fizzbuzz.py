def main() -> None:
    for i in range(1,101):
        if not i % 3 + i % 5:
            print("FizzBuzz")
        elif not i % 3:
            print("Fizz")
        elif not i % 5:
            print("Buzz")

if __name__ == '__main__':
    main()