from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    prefix = 1
    postfix = 1
    for i in range(n):
        res[i] *= prefix
        prefix *= nums[i]

        res[n-i-1] *= postfix
        postfix *= nums[n-i-1]

    return res


test = [1, 2, 3, 4]
product_except_self(test)