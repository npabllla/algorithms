from typing import List


def find_the_distance_value(self, arr1: List[int], arr2: List[int], d: int) -> int:
    n = len(arr1)
    k = len(arr2)
    res = 0
    for i in range(n):
        counter = 0
        for j in range(k):
            if abs(arr1[i] - arr2[j]) <= d:
                counter += 1
        if counter == 0:
            res += 1

    return res


def find_the_distance_value_2(self, arr1: List[int], arr2: List[int], d: int) -> int:
    n = len(arr1)
    counter = 0
    arr2.sort()
    for i in range(n):
        left = 0
        right = len(arr2) - 1

        while left <= right:
            mid = (left + right) // 2

            if abs(arr1[i] - arr2[mid]) <= d:
                counter += 1
                break
            if arr2[mid] > arr1[i]:
                right = mid - 1
            else:
                left = mid + 1

    return n - counter
