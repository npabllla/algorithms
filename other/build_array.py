from typing import List


def build_array(self, nums: List[int]) -> List[int]:
    res = []
    n = len(nums)

    for i in range(0, n):
        res.append(nums[nums[i]])

    return res
