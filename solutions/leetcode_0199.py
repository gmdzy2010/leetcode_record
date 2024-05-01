from collections import deque
from typing import Deque, List, Self


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


def right_view_of_binary_tree(root: TreeNode | None) -> List[int]:
    """二叉树的右视图

    使用二叉树层序遍历改造一下即可

    Args:
        - root (TreeNode | None): 二叉树根节点

    Returns:
        - List[int]: 层序遍历最右边的值列表
    """
    ans: List[int] = []
    if not root:
        return ans

    nodes: Deque[TreeNode] = deque()
    nodes.appendleft(root)
    while nodes:
        size = len(nodes)
        node_values: List[int] = []

        for _ in range(size):
            node = nodes.pop()
            node_values.append(node.val)
            if node.left:
                nodes.appendleft(node.left)
            if node.right:
                nodes.appendleft(node.right)

        ans.append(node_values[-1])

    return ans
