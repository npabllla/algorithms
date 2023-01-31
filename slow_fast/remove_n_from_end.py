from typing import Optional

from linked_list.list_node import ListNode


def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = head
    fast = head
    i = 1

    while i <= n:
        fast = fast.next
        i += 1

    if not fast:
        return head.next

    while fast and fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return head
