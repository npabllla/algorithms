from typing import List

def search_range(self, nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] == target:
            r = mid
        else:
            r = mid - 1
    start = l
    if nums[l] != target:
        return [-1, -1]
    else:
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                l = mid + 1
            else:
                r = mid - 1
        end = r
        return [start, end]
