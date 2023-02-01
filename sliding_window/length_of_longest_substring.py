def length_of_longest_substring(self, s: str) -> int:
    memo = set()
    left = 0
    res = 0
    for right, char in enumerate(s):
        while char in memo:
            left_char = s[left]
            memo.remove(left_char)
            left += 1

        memo.add(char)
        res = max(right - left + 1, res)
    return res
