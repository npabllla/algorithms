def is_palindrome(self, s: str) -> bool:
    string = ""
    for c in s:
        if c.isalnum():
            string += c.lower()

    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True
