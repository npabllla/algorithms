from typing import List


def remove_duplicates(self, nums: List[int]) -> int:
    size = len(nums)
    insert_index = 1
    for i in range(1, size):
        if nums[i - 1] != nums[i]:
            nums[insert_index] = nums[i]
            insert_index = insert_index + 1

    return insert_index
