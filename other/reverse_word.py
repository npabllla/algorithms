def reverse_words(s: str) -> str:
    words = s.split()
    n = len(words) - 1
    res = ""

    while n >= 0:
        res += words[n] + (" " if n != 0 else "")
        n -= 1

    return res


print(reverse_words("a good   example"))
