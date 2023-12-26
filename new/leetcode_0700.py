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


def search_tree_recur(root: TreeNode | None, val: int) -> TreeNode | None:
    """二叉搜索树，递归版本

    Args:
        root (TreeNode | None): 根节点
        val (int): 待搜索值

    Returns:
        TreeNode | None: 搜索到的节点
    """
    if not root:
        return None
    if root.val == val:
        return root
    if root.val > val:
        return search_tree_recur(root.left, val)
    if root.val < val:
        return search_tree_recur(root.right, val)

    return None


def search_tree(root: TreeNode | None, val: int) -> TreeNode | None:
    """二叉搜索树，迭代版本

    Args:
        root (TreeNode | None): 根节点
        val (int): 待搜索值

    Returns:
        TreeNode | None: 搜索到的节点
    """
    while root:
        if root.val > val:
            root = root.left
        elif root.val < val:
            root = root.right
        else:
            return root

    return None
