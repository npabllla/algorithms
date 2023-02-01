def check_inclusion(self, s1: str, s2: str) -> bool:
    n = len(s1)
    k = len(s2)
    if k < n:
        return False

    dic_s1 = {}
    dic_s2 = {}
    for char in set(s1 + s2):
        dic_s1[char] = 0
        dic_s2[char] = 0

    for char in s1:
        dic_s1[char] += 1

    for i in range(n):
        dic_s2[s2[i]] += 1

    if dic_s2 == dic_s1:
        return True

    start_pointer = 0
    for i in range(n, k):
        dic_s2[s2[start_pointer]] -= 1
        start_pointer += 1
        dic_s2[s2[i]] += 1
        if dic_s2 == dic_s1:
            return True

    return False
