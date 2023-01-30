def reverse_words(self, s: str) -> str:
    words = s.split()
    res = ""
    n = len(words) - 1
    for word in words:
        res += self.reverse(word) + (" " if n != 0 else "")
        n -= 1

    return res


def reverse(self, s: str) -> str:
    n = len(s) - 1
    res = ""
    while 0 <= n:
        res += s[n]
        n -= 1

    return res
