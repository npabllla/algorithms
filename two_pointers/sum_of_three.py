def find_sum_of_two(nums, target, start_index):
    left = start_index
    right = len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return True
        if s < target:
            left += 1
        else:
            right -= 1

    return False


def sum_of_three(nums, target):
    nums.sort()
    for i in range(0, len(nums) - 2):
        remaining_sum = target - nums[i]
        if find_sum_of_two(nums, remaining_sum, i + 1):
            return True

    return False


sum_of_three([15, 123, 25], 10)


def test():
    arr = [-25, -10, -7, -3, 2, 4, 8, 10]
    print(sum_of_three(arr, -8))
    print(sum_of_three(arr, -25))
    print(sum_of_three(arr, 0))
    print(sum_of_three(arr, -42))
    print(sum_of_three(arr, 22))
    print(sum_of_three(arr, -7))
    print(sum_of_three(arr, -3))
    print(sum_of_three(arr, 2))
    print(sum_of_three(arr, 4))
    print(sum_of_three(arr, 8))
    print(sum_of_three(arr, 7))
    print(sum_of_three(arr, 1))

test()