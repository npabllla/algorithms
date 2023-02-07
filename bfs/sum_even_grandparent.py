from bfs.merge_binary_trees import TreeNode


class Solution:
    res = 0

    def sum_even_grandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.val % 2 == 0:
            if root.left and root.left.left:
                self.res += root.left.left.val
            if root.left and root.left.right:
                self.res += root.left.right.val
            if root.right and root.right.left:
                self.res += root.right.left.val
            if root.right and root.right.right:
                self.res += root.right.right.val

        self.sum_even_grandparent(root.left)
        self.sum_even_grandparent(root.right)

        return self.res
