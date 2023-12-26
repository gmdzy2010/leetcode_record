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


def merge_tree_recur(
    root1: TreeNode | None,
    root2: TreeNode | None,
) -> TreeNode | None:
    """合并二叉树，递归版本

    Args:
        root1 (TreeNode | None): 根节点1
        root2 (TreeNode | None): 根节点2

    Returns:
        TreeNode | None: _description_
    """
    if not root1:
        return root2
    if not root2:
        return root1

    root1.val += root2.val
    root1.left = merge_tree_recur(root1.left, root2.left)
    root1.right = merge_tree_recur(root1.right, root2.right)

    return root1


def merge_tree_queue(
    root1: TreeNode | None,
    root2: TreeNode | None,
) -> TreeNode | None:
    """合并二叉树，队列版本

    Args:
        root1 (TreeNode | None): 根节点1
        root2 (TreeNode | None): 根节点2

    Returns:
        TreeNode | None: _description_
    """
    if not root1:
        return root2
    if not root2:
        return root1

    nodes: Deque[TreeNode] = deque()
    nodes.appendleft(root1)
    nodes.appendleft(root2)
    while nodes:
        node1 = nodes.pop()
        node2 = nodes.pop()
        node1.val += node2.val

        # * 左右节点都不为空的情况
        if node1.left and node2.left:
            nodes.appendleft(node1.left)
            nodes.appendleft(node2.left)
        if node1.right and node2.right:
            nodes.appendleft(node1.right)
            nodes.appendleft(node2.right)

        # * node1 的左节点为空就直接用 node2 的左节点
        if not node1.left and node2.left:
            node1.left = node2.left

        # * node1 的左节点为空就直接用 node2 的左节点
        if not node1.right and node2.right:
            node1.right = node2.right

    return root1
