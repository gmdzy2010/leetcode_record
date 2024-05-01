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

    def __str__(self) -> str:
        return f"{self.val}"

    def __repr__(self) -> str:
        if self.left and self.right:
            return f"{self.left} <- node: {self.val} -> {self.right}"
        if self.left and not self.right:
            return f"{self.left} <- node: {self.val} -> _"
        if not self.left and self.right:
            return f"_ <- node: {self.val} -> {self.right}"
        return f"_ <- node: {self.val} -> _"


class Solution:
    """_summary_"""

    def __init__(self):
        self.prev: TreeNode | None = None
        self.head: TreeNode | None = None

    def treeToDoublyList(self, root: TreeNode | None) -> TreeNode | None:
        """BST转循环双链表

        Args:
            root (TreeNode | None): BST根节点

        Returns:
            TreeNode | None: 转换后的头节点
        """
        if not root:
            return None

        self.inorder_transvesal(root)

        # * 最后将头尾绑定，构成循环链表
        if self.head:
            self.head.left = self.prev
        if self.prev:
            self.prev.right = self.head

        return self.head

    def inorder_transvesal(self, curr: TreeNode | None):
        """中序遍历过程中完成链表的创建

        Args:
            curr (_type_): 当前节点
        """
        if not curr:
            return

        self.inorder_transvesal(curr.left)

        # * prev 存在就利用left和right属性模仿双向链表建立关联
        if self.prev:
            self.prev.right = curr
            curr.left = self.prev

        # * prev 为空，说明转换还未开始，此时记录头节点
        else:
            self.head = curr

        # * prev 来到node位置，
        self.prev = curr

        self.inorder_transvesal(curr.right)
