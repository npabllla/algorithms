def climb_stairs(self, n: int) -> int:
    if n == 1 or n == 0:
        return n
    # n-1 + n - 2
    n1 = 1
    n2 = 2
    for _ in range(3, n + 1):
        n1, n2 = n2, n2 + n1

    return n2
