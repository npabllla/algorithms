from typing import Optional

from linked_list.list_node import ListNode


def is_palindrome(self, head: Optional[ListNode]) -> bool:
    numbers = []
    cur = head

    while cur:
        numbers.append(cur.val)
        cur = cur.next

    left = 0
    right = len(numbers) - 1

    while left <= right:
        if numbers[left] != numbers[right]:
            return False
        left += 1
        right -= 1

    return True


