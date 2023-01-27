from typing import Optional

from linked_list.list_node import ListNode


def detect_cycle(head: Optional[ListNode]):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
