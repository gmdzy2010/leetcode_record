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


def main(nums: List[int]) -> TreeNode | None:
    """有序数组构造BST

    Args:
        nums (List[int]): 有序数组

    Returns:
        TreeNode | None: 根节点
    """
    return inorder_transversal(nums, 0, len(nums) - 1)


def inorder_transversal(nums: List[int], L: int, R: int) -> TreeNode | None:
    """中序遍历构造BST

    Args:
        nums (List[int]): 有序数组
        left (int): 左边界
        right (int): 右边界

    Returns:
        TreeNode | None: 根节点
    """
    if L > R:
        return None

    M = (L + R) // 2

    root = TreeNode(nums[M])
    root.left = inorder_transversal(nums, L, M - 1)
    root.right = inorder_transversal(nums, M + 1, R)

    return root


if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6, 7]
    main(test_nums)
