def is_power_of_two(self, n):
    if n <= 0:
        return False
    if n == 1:
        return True

    while n % 2 == 0:
        n /= 2

    return n == 1
