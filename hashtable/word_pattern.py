def word_pattern(self, pattern: str, s: str) -> bool:
    words = s.split()
    pattern = list(pattern)
    n = len(words)
    k = len(pattern)
    if n != k:
        return False

    dic = {}
    words_set = set()
    for i in range(n):
        if pattern[i] not in dic.keys() and words[i] not in words_set:
            words_set.add(words[i])
            dic[pattern[i]] = words[i]

    for i in range(n):
        if pattern[i] not in dic.keys():
            return False
        shouldBeWord = dic[pattern[i]]
        if shouldBeWord != words[i]:
            return False

    return True
