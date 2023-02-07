from bfs.merge_binary_trees import TreeNode


def get_target_copy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    q_o = [original]
    q_c = [cloned]

    while len(q_o) and len(q_c):
        for _ in range(len(q_o)):
            curr_o = q_o.pop(0)
            curr_c = q_c.pop(0)
            if curr_o is target:
                return curr_c

            if curr_o.left:
                q_o.append(curr_o.left)
                q_c.append(curr_c.left)
            if curr_o.right:
                q_o.append(curr_o.right)
                q_c.append(curr_c.right)

    return TreeNode()
