from typing import List


def valid_mountain_array(self, arr: List[int]) -> bool:
    if len(arr) < 3:
        return False
    i = 1
    n = len(arr) - 1
    sp = 0
    while i <= n:
        if arr[i - 1] < arr[i]:
            sp += 1
        i += 1

    if sp == n or sp == 0:
        return False

    tp = sp
    while (sp + 1) <= n:
        if arr[sp] > arr[sp + 1]:
            tp += 1
        sp += 1

    if tp != n:
        return False

    return True


def valid_mountain_array_2(self, arr: List[int]):
    n = len(arr)
    i = 0

    # walk up
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # peak can't be first or last
    if i == 0 or i == n - 1:
        return False

    # walk down
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1
