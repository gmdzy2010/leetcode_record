from collections import deque
from typing import Deque, Self


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


def main(root: TreeNode | None):
    """判断二叉树是否对称

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - bool: 是否对称的结果
    """
    ans1 = get_max_depth_recur(root)
    print(ans1)

    ans2 = get_max_depth_queue(root)
    print(ans2)


def get_max_depth_recur(node: TreeNode | None) -> int:
    """二叉树的最大深度

    Args:
        node (TreeNode | None): _description_

    Returns:
        int: _description_
    """
    if not node:
        return 0

    left_depth = get_max_depth_recur(node.left)
    right_depth = get_max_depth_recur(node.right)

    return 1 + max(left_depth, right_depth)


def get_max_depth_queue(root: TreeNode | None) -> int:
    """二叉树的最大深度

    使用二叉树层序遍历的方法，层数就是最大深度

    Args:
        root (TreeNode | None): 根节点

    Returns:
        int: 二叉树最大深度
    """
    if not root:
        return 0

    ans = 0
    nodes: Deque[TreeNode] = deque()
    nodes.appendleft(root)

    while nodes:
        ans += 1
        for _ in range(len(nodes)):
            node = nodes.pop()
            if node.left:
                nodes.appendleft(node.left)
            if node.right:
                nodes.appendleft(node.right)

    return ans


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(2)
    test_root.left.left = TreeNode(3)
    test_root.left.right = TreeNode(4)
    test_root.right.left = TreeNode(4)
    test_root.right.right = TreeNode(3)
    main(test_root)
