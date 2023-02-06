from typing import List


def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
    memo = {}

    for num in nums:
        if num in memo.keys():
            memo[num] += 1
        else:
            memo[num] = 1

    memo_list = sorted(memo.items(), key=lambda x:x[1], reverse=True)
    res = list()
    for i in range(k):
        res.append(memo_list[i][0])

    return res
