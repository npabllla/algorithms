def is_palindrome(s: str):
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return is_palindrome_between(s, left + 1, right) or is_palindrome_between(s, left, right - 1)

    return True


def is_palindrome_between(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("abc"))
