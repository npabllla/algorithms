from typing import List


def longest_consecutive(self, nums: List[int]) -> int:
    res = 0
    set_nums = set(nums)

    for num in set_nums:
        if num - 1 not in set_nums:
            curr = num
            curr_streak = 1

            while curr + 1 in set_nums:
                curr += 1
                curr_streak += 1

            res = max(res, curr_streak)

    return res
