from typing import List


def summary_ranges(self, nums: List[int]) -> List[str]:
    nums.sort()
    res = list()
    n = len(nums)
    interval_start_index = 0

    for i in range(n):
        if n - i == 1:
            if i == interval_start_index:
                insert_string = str(nums[i])
            else:
                insert_string = str(nums[interval_start_index]) + "->" + str(nums[i])

            res.append(insert_string)
            break

        if nums[i + 1] - nums[i] != 1:
            if i == interval_start_index:
                insert_string = str(nums[i])
            else:
                insert_string = str(nums[interval_start_index]) + "->" + str(nums[i])
            res.append(insert_string)
            interval_start_index = i + 1

    return res
