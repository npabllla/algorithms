from typing import List


def rotate(self, nums: List[int], k: int) -> None:
    k = k % len(nums)
    if k < 0:
        k += len(nums)

    self.reverse_between(nums, 0, len(nums) - k - 1)
    self.reverse_between(nums, len(nums) - k, len(nums) - 1)
    self.reverse_between(nums, 0, len(nums) - 1)


def reverse_between(self, nums: List[int], start: int, end: int):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
