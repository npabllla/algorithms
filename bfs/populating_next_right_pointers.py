from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def connect(self, root: Optional[Node]) -> Optional[Node]:
    queue = [root]

    while queue:
        for i in range(len(queue) - 1):
            queue[i].next = queue[i + 1]

        for _ in range(len(queue)):
            current = queue.pop(0)
            if current and current.left:
                queue.append(current.left)
                queue.append(current.right)

    return root
