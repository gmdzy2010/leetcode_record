from collections import deque
from math import inf
from typing import Deque, Self, Tuple


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


def get_max_width(root: TreeNode | None) -> int | float:
    """二叉树的最大宽度

    使用二叉树层序遍历模版，计算每一层最右侧索引和最左侧索引的差值，再加一即可

    Args:
        - root (TreeNode | None): 二叉树根节点

    Returns:
        - int: 最大距离
    """
    ans = 0
    if not root:
        return ans

    nodes: Deque[Tuple[TreeNode, int]] = deque()
    nodes.appendleft((root, 1))
    while nodes:
        # * 初始化每一层的最小/最大节点索引
        min_index, max_index = inf, 0

        # * 处理当前层
        for _ in range(len(nodes)):
            node, index = nodes.pop()
            # * node 节点索引为 index ，那么其左节点索引为 2 * index
            if node.left:
                nodes.appendleft((node.left, 2 * index))

            # * 右节点索引为 2 * index + 1
            if node.right:
                nodes.appendleft((node.right, 2 * index + 1))

            min_index = min(min_index, index)
            max_index = max(max_index, index)

        ans = max(ans, max_index - min_index + 1)

    return ans
