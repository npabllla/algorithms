from typing import List


def sorted_squares(self, nums: List[int]) -> List[int]:
    res = []
    left = 0
    right = len(nums) - 1

    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            res.append(nums[right] ** 2)
            right = right - 1
        else:
            res.append(nums[left] ** 2)
            left = left + 1

    return res[::-1]
