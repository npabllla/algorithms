def is_happy_number(n: int):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_digits(n)

    return n == 1


def sum_digits(number: int) -> int:
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum
