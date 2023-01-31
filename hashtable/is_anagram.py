def is_anagram(self, s: str, t: str) -> bool:
    n = len(s)
    k = len(t)
    if n != k:
        return False

    charToInt: dict[str, int] = {}

    for i in range(n):
        char = s[i]
        if char in charToInt.keys():
            charToInt[char] += 1
        else:
            charToInt[char] = 1

    for i in range(k):
        char = t[i]
        if char in charToInt.keys():
            charToInt[char] -= 1
            if charToInt[char] == 0:
                charToInt.pop(char)
        else:
            print(charToInt)
            return False

    return len(charToInt) == 0
