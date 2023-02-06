from typing import List


def three_sum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = set()
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return list(res)
