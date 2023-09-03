def bitget(n: int, k: int) -> bool:
    return ((n >> k) & 0x1) == 1


def bitset(n: int, k: int) -> int:
    return n | (0x1 << k)


def bitclr(n: int, k: int) -> int:
    return n & ~(1 << k)
