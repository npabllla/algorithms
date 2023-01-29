from typing import List


def two_sum(self, numbers: List[int], target: int) -> List[int]:
    map = {}
    res = []

    for i in range(len(numbers)):
        target_in_map = target - numbers[i]
        if target_in_map in map.keys():
            return [map[target_in_map] + 1, i + 1]
        map[numbers[i]] = i

    return res


def find_sum_of_two(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]

        if numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1

    return []
