from typing import Optional

from bfs.merge_binary_trees import TreeNode


def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
    queue = [root]
    res = 0
    while len(queue):
        for _ in range(len(queue)):
            curr = queue.pop(0)
            if low <= curr.val <= high:
                res += curr.val

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    return res
