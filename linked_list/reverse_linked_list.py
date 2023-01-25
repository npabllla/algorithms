from typing import Optional

from linked_list.list_node import ListNode


def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
