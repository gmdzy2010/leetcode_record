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


def path_sum_recur(root: TreeNode | None, target: int) -> int:
    """路径总和，递归法

    Args:
        - root (TreeNode | None): 根节点
        - target (int): 目标和

    Returns:
        - int: 总和为 target 的路径数量
    """
    if not root:
        return 0

    ans = root_sum(root, target)
    ans += path_sum_recur(root.left, target)
    ans += path_sum_recur(root.right, target)

    return ans


def root_sum(root: TreeNode | None, target: int) -> int:
    if not root:
        return 0

    ans = 0
    if root.val == target:
        ans += 1

    ans += root_sum(root.left, target - root.val)
    ans += root_sum(root.right, target - root.val)

    return ans
