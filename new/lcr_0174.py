from typing import Self


class TreeNode:
    """二叉树节点"""

    def __init__(
        self,
        val: int = 0,
        left: Self | None = None,
        right: Self | None = None,
    ):
        self.val = val
        self.left: Self | None = left
        self.right: Self | None = right


class Solution:
    """_summary_"""

    def __init__(self):
        self.ans = -1
        self.curr_cnt = 0

    def find_target_node(self, root: TreeNode | None, cnt: int) -> int:
        """BST找目标节点，中序遍历（逆）

        Args:
            root (TreeNode | None): 根节点
            cnt (int): 目标值

        Returns:
            int: 找到的节点值
        """
        self.ans = -1
        self.curr_cnt = cnt

        self.reverse_inorder_transvesal(root)

        return self.ans

    def reverse_inorder_transvesal(self, node: TreeNode | None):
        """逆中序遍历

        Args:
            node (TreeNode | None): 当前节点
        """
        if not node:
            return

        if self.curr_cnt == 0:
            return

        # * 先右节点递归
        self.reverse_inorder_transvesal(node.right)

        # * 每次减一
        self.curr_cnt -= 1

        # * 如果自减之后的 curr_cnt 为零，此时即为第 cnt 个最大值
        if self.curr_cnt == 0:
            self.ans = node.val
            return

        self.reverse_inorder_transvesal(node.left)
