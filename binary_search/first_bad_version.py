def first_bad_version(n: int) -> int:
    left = 1
    right = n

    while left < right:
        mid = (right + left) // 2

        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1

    return left


def is_bad_version(version: int) -> bool:
    return version == 2
