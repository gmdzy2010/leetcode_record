from typing import List, Self


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


def flatten_tree_stack(root: TreeNode | None):
    """二叉树转换为单链表

    使用二叉树的前序遍历

    Args:
        root (TreeNode | None): 根节点

    Returns:
        TreeNode | None: 转换后的根节点
    """
    if not root:
        return None

    # * 需要一个前序节点，初始为None
    prev: TreeNode | None = None

    # * 使用前序遍历
    stack: List[TreeNode] = []
    stack.append(root)
    while stack:
        node = stack.pop()

        # * 从 prev 出发构造单链表二叉树，左节点置空，右节点为当前节点
        if prev:
            prev.left = None
            prev.right = node

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        # * 下一轮 prev 从 node 继续
        prev = node

    return None
