from random import randint


def random_hex() -> int:
    """randomly generates a hexadecimal value

    :return: returns hex of interger from random.randint
    :rtype: int
    """
    num = randint(1000, 10000)
    return hex(num)


def main() -> None:
    rand_hex = random_hex()
    print(f"This is a random hexadecimal value: {rand_hex}")


if __name__ == "__main__":
    main()
