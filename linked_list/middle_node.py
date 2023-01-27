from typing import Optional

from linked_list.list_node import ListNode


def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
