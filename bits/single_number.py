def single_number(self, nums):
    mask = 0
    for i in nums:
        mask ^= i
    return mask
