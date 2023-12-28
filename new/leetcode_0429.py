from collections import deque
from typing import Deque, List, Self


class TreeNode:
    """多叉树节点"""

    def __init__(self, val=0, children=None):
        self.val: int = val
        self.children: List[Self] | None = children

    def __str__(self) -> str:
        return f"{self.val}"

    def __repr__(self) -> str:
        if self.children:
            children = ",".join(str(c) for c in self.children)
        else:
            children = "_"
        return f"node: {self.val} -> {children}"


def tranversal_with_levelorder(root: TreeNode | None) -> List[List[int]]:
    """多叉树的层序遍历

    Args:
        root (TreeNode | None): 根节点

    Returns:
        List[List[int]]: 层序遍历结果
    """
    ans: List[List[int]] = []
    if not root:
        return ans

    nodes: Deque[TreeNode] = deque()
    nodes.appendleft(root)
    while nodes:
        size = len(nodes)
        vals: List[int] = []
        for _ in range(size):
            node = nodes.pop()
            vals.append(node.val)

            if not node.children:
                continue

            for node in node.children:
                nodes.appendleft(node)

        ans.append(vals)

    return ans
