from bfs.merge_binary_trees import TreeNode


def get_target_copy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    def inorder(o: TreeNode, c: TreeNode):
        if o:
            inorder(o.left, c.left)
            if o is target:
                self.ans = c
            inorder(o.right, c.right)

    inorder(original, cloned)
    return self.ans
