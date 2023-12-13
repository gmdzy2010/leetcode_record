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


def tranverse_in_zigzag_levelorder(root: TreeNode | None) -> List[List[int]]:
    """二叉树的zigzag层序遍历

    从二叉树的层序遍历修改即可

    Args:
        - root (TreeNode | None): 二叉树根节点

    Returns:
        - List[List[int]]: zigzag层序遍历的结果
    """
    ans: List[List[int]] = []
    if not root:
        return ans

    level: int = 0
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

        ans.append(node_values if level % 2 == 0 else node_values[::-1])
        level += 1

    return ans
