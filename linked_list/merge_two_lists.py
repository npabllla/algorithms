from typing import Optional

from linked_list.list_node import ListNode


def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    res = ListNode()
    pointer = res

    while list1 and list2:
        if list1.val < list2.val:
            pointer.next = list1
            list1 = list1.next
        else:
            pointer.next = list2
            list2 = list2.next
        pointer = pointer.next

    if list1:
        pointer.next = list1

    if list2:
        pointer.next = list2

    return res.next
