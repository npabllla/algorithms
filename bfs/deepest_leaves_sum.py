from typing import Optional

from bfs.merge_binary_trees import TreeNode


def deepest_leaves_sum(self, root: Optional[TreeNode]) -> int:
    res = 0
    queue = [root]

    while len(queue):
        res = 0
        for _ in range(len(queue)):
            curr = queue.pop(0)
            res += curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    return res
