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
    """二叉树的最小深度

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - bool: 是否对称的结果
    """
    ans1 = get_min_depth_recur(root)
    print(ans1)

    ans2 = get_min_depth_queue(root)
    print(ans2)


def get_min_depth_recur(node: TreeNode | None) -> int:
    """二叉树的最小深度

    Args:
        node (TreeNode | None): 当前节点

    Returns:
        int: 当前最小深度
    """
    if not node:
        return 0

    # * 分别从左右子树拿到最小深度
    left_min_depth = get_min_depth_recur(node.left)
    right_min_depth = get_min_depth_recur(node.right)

    # * 只要不是左右节点都为空，那么就不是最小深度
    if not node.left and node.right:
        return 1 + right_min_depth
    if node.left and not node.right:
        return 1 + left_min_depth

    return 1 + min(left_min_depth, right_min_depth)


def get_min_depth_queue(root: TreeNode | None) -> int:
    """二叉树的最大深度

    使用二叉树层序遍历的方法
    - 当当前节点左右节点都为空，即到达第一个深度计算点，返回即可

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

    # * 对二叉树进行层序遍历
    while nodes:
        ans += 1
        for _ in range(len(nodes)):
            node = nodes.pop()
            if node.left:
                nodes.appendleft(node.left)
            if node.right:
                nodes.appendleft(node.right)

            # * 当左右节点均为空，则说明到了第一个深度计算点
            if not node.left and not node.right:
                return ans

    return ans


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(2)
    test_root.left.left = TreeNode(3)
    test_root.left.right = TreeNode(4)
    main(test_root)
